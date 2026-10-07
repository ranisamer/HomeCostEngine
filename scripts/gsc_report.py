"""Read-only U.S. Web Search Console reporting. Credentials never enter output files."""
import csv
import datetime as dt
import json
import os
from pathlib import Path
import sys
import time
from urllib.parse import quote, urlparse
from zoneinfo import ZoneInfo

API = 'https://www.googleapis.com/webmasters/v3'
SCOPE = 'https://www.googleapis.com/auth/webmasters.readonly'
PAGE_SIZE = 25000
MAX_ROWS = 100000


class ReportError(Exception):
    pass


def select_property(entries, domain, override=''):
    permitted = [e['siteUrl'] for e in entries if e.get('permissionLevel') in
                 ('siteOwner', 'siteFullUser', 'siteRestrictedUser')]
    if override:
        if override not in permitted:
            raise ReportError('Configured GSC_PROPERTY is not accessible to this service account.')
        host = override.removeprefix('sc-domain:') if override.startswith('sc-domain:') else urlparse(override).hostname
        if host not in (domain, 'www.' + domain):
            raise ReportError('GSC_PROPERTY does not match the configured website.')
        return override
    for candidate in ('sc-domain:' + domain, 'https://' + domain + '/', 'https://www.' + domain + '/'):
        if candidate in permitted:
            return candidate
    raise ReportError('No matching property access. Add the service-account email to this site in Search Console; use GSC_PROPERTY for a nonstandard URL-prefix property.')


def period_windows(end):
    current_start = end - dt.timedelta(days=27)
    previous_end = current_start - dt.timedelta(days=1)
    return (current_start, end), (previous_end - dt.timedelta(days=27), previous_end)


class Client:
    def __init__(self, credential_info):
        try:
            from google.oauth2 import service_account
            from google.auth.transport.requests import AuthorizedSession
            credentials = service_account.Credentials.from_service_account_info(credential_info, scopes=[SCOPE])
            self.session = AuthorizedSession(credentials)
        except Exception:
            raise ReportError('Unable to initialize credentials. Check GSC_SERVICE_ACCOUNT_JSON contains the complete service-account JSON.') from None

    def request(self, method, path, body=None):
        for attempt in range(4):
            try:
                response = self.session.request(method, API + path, json=body, timeout=45)
            except Exception:
                if attempt < 3:
                    time.sleep(2 ** attempt)
                    continue
                raise ReportError('Google authentication or network request failed. Check the key is active and retry.') from None
            if response.status_code in (429, 500, 502, 503, 504) and attempt < 3:
                time.sleep(2 ** attempt)
                continue
            if response.status_code != 200:
                messages = {401: 'Authentication failed; check the service-account key.',
                            403: 'Access denied; enable Search Console API and add the service account to this property.',
                            404: 'Property not found; check its exact Search Console identifier.'}
                raise ReportError(messages.get(response.status_code, 'Search Console API returned HTTP ' + str(response.status_code)))
            try:
                return response.json()
            except ValueError:
                raise ReportError('Google returned an invalid JSON response.') from None

    def query(self, site, start, end, dimensions, usa=True):
        body = {'startDate': str(start), 'endDate': str(end), 'dimensions': dimensions,
                'type': 'web', 'dataState': 'final', 'aggregationType': 'auto', 'rowLimit': PAGE_SIZE}
        if usa:
            body['dimensionFilterGroups'] = [{'groupType': 'and', 'filters': [
                {'dimension': 'country', 'operator': 'equals', 'expression': 'usa'}]}]
        rows = []
        while len(rows) < MAX_ROWS:
            body['startRow'] = len(rows)
            result = self.request('POST', '/sites/' + quote(site, safe='') + '/searchAnalytics/query', body)
            batch = result.get('rows', [])
            rows.extend(batch)
            if len(batch) < PAGE_SIZE:
                return {'rows': rows, 'pagination_cap_reached': False}
        return {'rows': rows, 'pagination_cap_reached': True}


def collect(client, domain, override='', now=None):
    now = now or dt.datetime.now(dt.timezone.utc)
    today_pt = now.astimezone(ZoneInfo('America/Los_Angeles')).date()
    requested_end = today_pt - dt.timedelta(days=3)
    site = select_property(client.request('GET', '/sites').get('siteEntry', []), domain, override)
    # Discover dated finalized activity separately; no U.S. metrics are derived from this probe.
    probe = client.query(site, requested_end - dt.timedelta(days=89), requested_end, ['date'], usa=False)
    dates = sorted(row['keys'][0] for row in probe['rows'])
    end = min(requested_end, dt.date.fromisoformat(dates[-1])) if dates else requested_end
    windows = period_windows(end)
    report = {'generated_at_utc': now.isoformat(), 'domain': domain, 'property': site,
              'country': 'usa', 'search_type': 'web', 'data_state': 'final',
              'date_timezone': 'America/Los_Angeles', 'latest_observed_finalized_date': dates[-1] if dates else None,
              'first_observed_date_in_90_day_probe': dates[0] if dates else None,
              'limitations': ['API returns available top rows, not a guaranteed exhaustive keyword inventory.',
                             'Anonymized queries are omitted. Query/page row totals may differ from property totals.',
                             'No activity on a date does not distinguish zero traffic from unavailable history.',
                             'This report does not measure calculator engagement or diagnose indexing coverage.'],
              'periods': {}}
    for label, (start, stop) in zip(('current', 'previous'), windows):
        period = {'start': str(start), 'end': str(stop)}
        for name, dimensions in [('totals', []), ('daily', ['date']), ('queries', ['query']),
                                 ('pages', ['page']), ('query_pages', ['query', 'page'])]:
            period[name] = client.query(site, start, stop, dimensions)
        report['periods'][label] = period
    report['history_caution'] = not dates or dates[0] > str(windows[1][0])
    return report


def cell(value):
    return str(value).replace('|', '\\|').replace('\n', ' ').replace('\r', ' ').replace('<', '&lt;').replace('>', '&gt;')


def metrics(period):
    rows = period['totals']['rows']
    return rows[0] if rows else {'clicks': 0, 'impressions': 0, 'ctr': 0, 'position': None}


def markdown(report):
    current, previous = report['periods']['current'], report['periods']['previous']
    a, b = metrics(current), metrics(previous)
    lines = ['# U.S. organic search report: ' + report['domain'], '',
             'Property: `' + report['property'] + '` • Web • United States • finalized data',
             'Generated: ' + report['generated_at_utc'], '',
             '| Metric | ' + current['start'] + ' to ' + current['end'] + ' | ' + previous['start'] + ' to ' + previous['end'] + ' | Change |',
             '|---|---:|---:|---:|']
    for key in ('clicks', 'impressions', 'ctr', 'position'):
        def fmt(v):
            if v is None:
                return 'N/A'
            return f'{v * 100:.2f}%' if key == 'ctr' else f'{v:.2f}' if key == 'position' else f'{v:,.0f}'
        delta = 'N/A' if a[key] is None or b[key] is None else (
            f'{(a[key] - b[key]) * 100:+.2f} percentage points' if key == 'ctr' else f'{a[key] - b[key]:+.2f}')
        lines.append('| ' + key + ' | ' + fmt(a[key]) + ' | ' + fmt(b[key]) + ' | ' + delta + ' |')
    if report['history_caution']:
        lines += ['', '**History caution:** the 90-day probe has no recorded activity covering the full previous window. Treat this comparison as a limited baseline, not proven growth or decline.']
    lines += ['', '## Query and page observations', '',
              'Sorted by measured impressions. These are observed U.S. query–page pairs, not search-volume or difficulty estimates.', '',
              '| Query | Page | Clicks | Impressions | CTR | Avg. position | Review action |',
              '|---|---|---:|---:|---:|---:|---|']
    pairs = sorted(current['query_pages']['rows'], key=lambda r: (-r['impressions'], -r['clicks']))
    for row in pairs[:30]:
        action = 'Collect more evidence'
        if row['impressions'] >= 20:
            action = 'Check answer and title against intent'
            if 5 <= row['position'] <= 30:
                action = 'Review existing canonical answer and internal links'
        lines.append('| ' + cell(row['keys'][0]) + ' | ' + cell(row['keys'][1]) +
                     f" | {row['clicks']:.0f} | {row['impressions']:.0f} | {row['ctr'] * 100:.2f}% | {row['position']:.2f} | {action} |")
    if not pairs:
        lines.append('| No reported U.S. query–page rows | — | — | — | — | — | No ranking conclusion |')
    lines += ['', '## Interpretation', '',
              'Clicks count clicks on search results, not impressions or analytics sessions. Average position is an aggregate, not a guaranteed rank. Review existing coverage and recent edits before choosing one primary page; do not publish variants solely from query wording.', '',
              'Finalized report dates follow Pacific Time. Empty rows are not proof of an indexing problem. Use URL Inspection separately for indexing questions.', '']
    lines += ['- ' + value for value in report['limitations']]
    for name, p in report['periods'].items():
        for dimension, result in p.items():
            if isinstance(result, dict) and result.get('pagination_cap_reached'):
                lines.append(f'- Pagination safety cap reached: {name}/{dimension}; this export is truncated.')
    return '\n'.join(lines) + '\n'


def save(report, destination):
    destination.mkdir(parents=True, exist_ok=True)
    (destination / 'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    summary = markdown(report)
    (destination / 'report.md').write_text(summary, encoding='utf-8')
    dimensions = {'totals': [], 'daily': ['date'], 'queries': ['query'], 'pages': ['page'], 'query_pages': ['query', 'page']}
    for label, period in report['periods'].items():
        for name, keys in dimensions.items():
            with (destination / f'{label}-{name}.csv').open('w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(keys + ['clicks', 'impressions', 'ctr', 'position'])
                for row in period[name]['rows']:
                    # Neutralize spreadsheet formulas in externally supplied query/page strings.
                    safe_keys = ["'" + x if x.startswith(('=', '+', '-', '@', '\t', '\r')) else x for x in row.get('keys', [])]
                    writer.writerow(safe_keys + [row[k] for k in ('clicks', 'impressions', 'ctr', 'position')])
    summary_path = os.environ.get('GITHUB_STEP_SUMMARY')
    if summary_path:
        with open(summary_path, 'a', encoding='utf-8') as f:
            f.write(summary)


def main():
    raw = os.environ.get('GSC_SERVICE_ACCOUNT_JSON', '')
    if not raw:
        raise ReportError('Missing GSC_SERVICE_ACCOUNT_JSON repository secret.')
    try:
        info = json.loads(raw)
    except ValueError:
        raise ReportError('GSC_SERVICE_ACCOUNT_JSON is not valid JSON. Paste the complete downloaded file into the repository secret.') from None
    if info.get('type') != 'service_account':
        raise ReportError('Expected a service-account JSON key, not an API key or OAuth client file.')
    domain = os.environ.get('GSC_DOMAIN', '')
    if not domain or '/' in domain:
        raise ReportError('GSC_DOMAIN must be the website hostname.')
    report = collect(Client(info), domain, os.environ.get('GSC_PROPERTY', ''))
    save(report, Path('gsc-output'))
    print('Read-only U.S. report created for ' + domain + '. See the workflow summary and report artifact.')


if __name__ == '__main__':
    try:
        main()
    except ReportError as error:
        print('::error::' + str(error), file=sys.stderr)
        sys.exit(1)
