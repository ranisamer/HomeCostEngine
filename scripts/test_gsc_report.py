import datetime as dt
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from gsc_report import Client, ReportError, collect, markdown, period_windows, save, select_property


class FakeClient:
    def __init__(self):
        self.calls = []

    def request(self, method, path):
        return {'siteEntry': [{'siteUrl': 'sc-domain:example.com', 'permissionLevel': 'siteRestrictedUser'}]}

    def query(self, site, start, end, dimensions, usa=True):
        self.calls.append((str(start), str(end), dimensions, usa))
        if not usa:
            return {'rows': [{'keys': ['2026-09-15']}, {'keys': ['2026-10-03']}], 'pagination_cap_reached': False}
        keys = {'date': '2026-10-01', 'page': 'https://example.com/a', 'query': '=sample|query'}
        return {'rows': [{'keys': [keys[k] for k in dimensions], 'clicks': 2, 'impressions': 80,
                          'ctr': .025, 'position': 14.5}], 'pagination_cap_reached': False}


class Tests(unittest.TestCase):
    def test_access_and_exact_property(self):
        entries = [{'siteUrl': 'https://example.com/', 'permissionLevel': 'siteRestrictedUser'},
                   {'siteUrl': 'sc-domain:example.com', 'permissionLevel': 'siteFullUser'}]
        self.assertEqual(select_property(entries, 'example.com'), 'sc-domain:example.com')
        self.assertEqual(select_property(entries, 'example.com', 'https://example.com/'), 'https://example.com/')
        with self.assertRaises(ReportError):
            select_property([{'siteUrl': 'sc-domain:example.com', 'permissionLevel': 'siteUnverifiedUser'}], 'example.com')
        with self.assertRaises(ReportError):
            select_property(entries, 'another.com', 'sc-domain:example.com')

    def test_periods_and_real_query_page_dimensions(self):
        client = FakeClient()
        report = collect(client, 'example.com', now=dt.datetime(2026, 10, 7, 0, 30, tzinfo=dt.timezone.utc))
        current, previous = period_windows(dt.date(2026, 10, 3))
        self.assertEqual((current[1]-current[0]).days, 27)
        self.assertEqual((previous[1]-previous[0]).days, 27)
        self.assertEqual((current[0]-previous[1]).days, 1)
        self.assertEqual(report['periods']['current']['end'], '2026-10-03')
        self.assertTrue(report['history_caution'])
        self.assertEqual(len(client.calls), 11)
        self.assertTrue(all(call[3] for call in client.calls[1:]))
        self.assertEqual(sum(call[2]==['query', 'page'] for call in client.calls), 2)

    def test_country_filter_and_pagination(self):
        client = Client.__new__(Client)
        bodies = []
        def request(method, path, body):
            bodies.append(dict(body))
            return {'rows': [{'keys':['one']}, {'keys':['two']}]} if len(bodies)==1 else {'rows':[]}
        client.request = request
        with patch('gsc_report.PAGE_SIZE', 2):
            result = client.query('sc-domain:example.com', dt.date(2026, 9, 1), dt.date(2026, 9, 2), ['query','page'])
        self.assertEqual(len(result['rows']), 2)
        self.assertEqual(bodies[1]['startRow'], 2)
        self.assertEqual(bodies[0]['dataState'], 'final')
        self.assertEqual(bodies[0]['type'], 'web')
        self.assertEqual(bodies[0]['dimensionFilterGroups'][0]['filters'][0]['expression'], 'usa')

    def test_outputs_and_empty_metrics(self):
        report = collect(FakeClient(), 'example.com', now=dt.datetime(2026,10,7,tzinfo=dt.timezone.utc))
        with tempfile.TemporaryDirectory() as folder:
            save(report, Path(folder))
            self.assertEqual(json.loads((Path(folder)/'report.json').read_text())['country'], 'usa')
            self.assertIn("'=sample|query", (Path(folder)/'current-query_pages.csv').read_text())
            self.assertIn('sample\\|query', (Path(folder)/'report.md').read_text())
            self.assertNotIn('private_key', (Path(folder)/'report.json').read_text())
        report['periods']['previous']['totals']['rows'] = []
        self.assertIn('N/A', markdown(report))


if __name__ == '__main__':
    unittest.main()
