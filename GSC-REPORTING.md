# U.S. Search Console reporting

This read-only workflow supports the SEO program through December 29, 2026. It runs daily at 00:37 UTC (04:37 Dubai), on manual dispatch, and when its own code changes on main. Scheduled runs after the program end skip collection. Manual runs remain available. It does not publish site content or submit indexing requests.

## Owner setup

1. Enable Google Search Console API in the Google Cloud project.
2. Add the service-account email as a Restricted user to the site's actual Search Console property.
3. Store the complete service-account JSON in the repository Actions secret `GSC_SERVICE_ACCOUNT_JSON`. Never commit a key or paste it into an issue or log.
4. If automatic discovery cannot find the property, set Actions variable `GSC_PROPERTY` to the exact identifier: `sc-domain:example.com` for a Domain property, or `https://example.com/` for a URL-prefix property. Use the site's real hostname.

No Cloud project Editor role, Search Console ownership or read/write API scope is required for this reporting workflow. The API scope is `webmasters.readonly`.

## Where the results are

Open Actions → U.S. Search Console report → latest successful run. The Summary has the two-period totals and up to 30 query-page observations. Download the `gsc-us-web-report` artifact for JSON and CSV exports (90-day retention). Report artifacts require repository access; they are not deployed to the website. The job Summary is visible to people who can view the repository's Actions runs, so it contains measured SEO data, never credentials.

For automated SEO review, list workflow runs for `.github/workflows/gsc-report.yml`, select the newest successful run on main, fetch its `gsc-us-web-report` artifact, and read `report.json` or `report.md`. Check the generation date, exact property, country and period dates before using it. A failed or stale run is not fresh performance evidence. The existing site-editing process remains separate.

## Data interpretation

- Country equals `usa`, search type `web`, data state `final`.
- Query-page exports come from one API request grouping by both dimensions; they are not guessed joins of independent query and page CSVs.
- Report dates follow Pacific Time, as Search Console requires. Collection uses a three-day safety lag and checks the latest observed finalized activity. Current and preceding windows have 28 dates each with no overlap.
- The first observed date in a 90-day probe is activity evidence, not proof of the property's creation date or complete history. Limited history is flagged.
- Site totals are fetched separately. Anonymized queries and API top-row limits mean query-page rows should not be summed to recreate totals. A pagination safety cap is disclosed if reached.
- Priorities use measured impressions and observed position. The 20-impression review threshold is a triage heuristic, not search volume or a promise of ranking improvement.
- This export does not measure tool engagement, provide full indexing coverage, or replace URL Inspection. Clicks, impressions and analytics sessions are different measurements.

## Troubleshooting

- Missing/invalid secret: replace the Actions secret with the complete JSON document downloaded from Service Account → Keys, not an ordinary API key.
- HTTP 403: check API activation, service-account property access and the key's project. Ensure permission was added to the actual property used in Search Console.
- No matching property: use `GSC_PROPERTY` for the actual supported domain or URL-prefix property. The workflow refuses a different domain.
- Empty U.S. rows: access can be valid while there is no reportable U.S. traffic. Do not conclude an indexing failure from empty data.
- Transient quota/network errors: retry the workflow; the collector retries transient errors with bounded backoff and does not print credential-bearing exceptions.

The successful first live run, not the presence of a secret alone, establishes that the connection works.
