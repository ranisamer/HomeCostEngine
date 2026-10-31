# Insulation workbook — DRAFT, October 31, 2026

Not released for sale. Queue day 6 is a resumable draft, not completed publication. Prior garage release remains live-verification pending.

## Deliverables
- books/daily/insulation-scope.json: original manuscript, four hypothetical cases, six worksheets, two completed records, twelve provider questions.
- scripts/build_insulation_workbook.py: creates actual 25-page/30-field PDF, real cover and previews, and books/drafts/insulation-download.js with exact PDF bytes. Staged route is not a live function.
- scripts/build_insulation_drafts.py: creates clearly marked/noindex review product and distinct companion at books/drafts/insulation-product.html and insulation-article.html; no sales button/Offer.
- books/drafts/insulation-integration.json: proposed title, 799 pence GBP, 25 pages and matching route fixture. Not registered in live catalogs.
- scripts/qa_insulation_draft.py, test_insulation_stage.mjs and test_insulation_webhook_stage.mjs: reproducible artifact and isolated integration tests.

Proposed £7.99 GBP is justified as a conservative test of the zone-to-completion workflow, coverage/minimum-price/allowance checks and reusable records. Implemented price: none. No existing price or currency changed.

Intended final product: https://homecostengine.com/ebooks/insulation-quote-scope-workbook

Intended final article: https://homecostengine.com/blog/compare-insulation-quotes-without-unlike-work

These are intended URLs, not verified published pages. Neither index nor sitemap nor live checkout was changed.

## Sources checked October 31
FTC consumer page https://consumer.ftc.gov/articles/what-know-when-youre-buying-home-insulation (May 2021) and rule overview https://www.ftc.gov/legal-library/browse/rules/r-value-rule — limited R-value/product-information context, no legal interpretation or recommended R-value.
ENERGY STAR https://www.energystar.gov/saveathome/seal_insulate — air-sealing/insulation and location suitability context; no savings percentage used.
EPA https://www.epa.gov/mold/brief-guide-mold-moisture-and-your-home — moisture-control context, no cleanup/design steps.
An attempted DOE /energysaver/insulation page returned 404 and was excluded. Companion contains three contextual primary links plus a free six-row checklist and area illustration.

All 36 substantive method paragraphs are newly authored and have no exact match in existing manuscripts. Editorial assessment meets the 80% original-content target; exact matching is not semantic proof. General envelope concepts from the energy guide and comparison techniques are related and disclosed; layout/delivery code is reused.

## Passed checks
Four cases independently recomputed with Decimal: excluded union 210 and treatment 1,040 sq ft; fictional 34 x 28 = 952 coverage leaves 48 gap and ceiling quantity 36 gives 1,008; $462 unit multiplication is overridden by $600 minimum, versus $575 fixed; $2,860 versus $2,750 and +$120 allowance delta yields $2,980/$2,870. All inputs are fictional, not installation instructions or market prices.

30 canonical/widget values save/reopen with nonempty appearances; 1,000-character limits and 25 outline entries verified. Entire contact sheet and full-size case, completed record and saved form inspected without observed defects. PDF SHA256 88e9f3b9ae5b05a51a8cb81ecd0f6082b4f9a044c372b3d809311c22a8bdf6da.

Isolated fixture passed fixed-GBP price/ignored client-price attack, paid+complete matching entitlement, exact-byte private PDF and denial checks. Mocked signed webhook passed matching draft title/£7.99/private-order link and deduplication. No real API calls, payment, mail or spending.

All 26 existing products' GBP/webhook regressions and 25 book routes passed; analytics privacy/private-build guards passed. Live catalogs and site indexes remain byte-identical.

## QA maintenance
Fixed qa_solar_workbook.py, qa_battery_workbook.py, qa_ev_workbook.py and qa_garage_workbook.py to check immutable prior amounts while allowing later products. Solar uses the existing release-era battery-price baseline, which includes solar. Earlier equality-of-key-set tests failed as the catalog grew. All four now pass. No production checkout, entitlement or analytics code changed. Existing historical validation documents retained.

## Access blocker and recovery
Browser could not navigate: bwrap cannot create /home/agent/.codex/sessions on read-only filesystem. Public retrieval of garage product and companion failed too. This does not establish site downtime or a site-served bot block. Live UI/image/responsive checks are unperformed.

First verify the existing garage release, then resume this exact insulation draft. Move/review staged route, register matching server checkout/verify entry, generate real sale page and article, update relevant category/index/reciprocal links/sitemap, re-run mocks, use fresh-main expected-head commit, wait for Cloudflare and verify live URLs. Remove DRAFT labels only at successful release, regenerating PDF and previews. Do not create another title for the same queue entry.

## Acquisition and uncertainty
Latest available successful USA Web GSC run 41013698041 / artifact 12958407480, generated October 30: finalized September 29–October 26, 2,862 property impressions, 1 click, average position 51.09. No returned insulation query rows; top/anonymization limits apply. Not evidence of no global market. The window predates this draft; no conversion/growth inference.

GA4 U.S. product/article/preview/checkout activity, live Stripe orders/refunds/net revenue and actual reader feedback unavailable. Missing does not mean zero. Technical tests do not validate demand/usefulness. No customer contacted or additional automation created; ongoing publishing retained. Public source PDF availability remains an inherited limit; draft is explicitly not sold.
