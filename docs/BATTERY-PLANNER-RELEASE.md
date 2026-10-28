# Home Battery Backup Budget Planner — October 28, 2026

Status: published. Release 825eca1b44279e558325f4f7afbb1898faefd145; Cloudflare Pages check 122647101807 completed successfully. Both clean live URLs verified.

The third queued title helps a U.S. homeowner prepare a selected-load outage brief, distinguish energy from output/starting power, identify conditional duration and recharge assumptions, and compare complete battery proposal scope. It does not design or size an installation. It is distinct from solar generation/ownership comparisons and the broader energy guide; that overlap is disclosed.

## Product and price

- Product: https://homecostengine.com/ebooks/home-battery-backup-budget-planner
- Companion: https://homecostengine.com/blog/what-to-ask-before-comparing-home-battery-prices
- Proposed and implemented new price: £9.99 GBP, 999 pence. All 23 pre-existing catalog amounts remain unchanged.
- Actual PDF: 26 US Letter pages; 4 original hypothetical cases; 7 reusable worksheets with 35 interactive fields; 2 completed records using the same worksheet prompts; 12 provider questions; 26 outline entries; 5 clickable source/article URLs.
- Price rationale: the original comparison workflow, checked arithmetic, completed records and reusable sheets support a conservative test price. Neither free primary sources nor page count alone justify the charge. Willingness to pay remains unvalidated.
- Editorial originality target assessed as met: the 48 substantive method paragraphs, cases, records and prompt sets were newly authored. An exact-paragraph screen found zero method paragraphs copied from legacy manuscript files. That screen does not measure semantic originality; shared planning concepts, rendering and delivery code are disclosed.

## Source checks

All four primary URLs were retrieved on October 28, 2026 and are linked near their limited claims in the article and identified beside relevant PDF modules.

1. DOE Solar-Plus-Storage 101, March 11, 2019: https://www.energy.gov/cmei/systems/articles/solar-plus-storage-101 — terminology only. Historic utility-scale prices and market figures are not used as current residential data.
2. CARB backup-power tool: https://ww2.arb.ca.gov/capp/cst/tch/welcome-to-the-zero-emissions-residential-backup-power-tool — power/energy and starting-demand context, generic-assumption and recharge limits. Not household sizing or national product selection.
3. Tesla backup scope: https://www.tesla.com/support/energy/powerwall/learn/what-can-powerwall-back-up — manufacturer-specific partial/whole-home distinction and final detailed design.
4. Tesla Backup Reserve: https://www.tesla.com/support/energy/powerwall/mobile-app/backup-reserve — reserved energy is available in outage; do not automatically subtract it as inaccessible energy. Not a settings prescription or cross-brand guarantee.

No current incentive amount, eligibility, national installed-price benchmark, savings or actual runtime is claimed. An NFPA page returned no substantive text and was excluded.

## Checks and reproducibility

- Build: python scripts/build_battery_workbook.py books/daily/home-battery-backup.json
- Product/article generation: python scripts/build_battery_store.py
- Artifact checks: python scripts/qa_battery_workbook.py
- Delivery: node scripts/test_battery_delivery.mjs; all scripts/test_*_delivery.mjs passed (23 books).
- Store and shared webhook: test_gbp_store.mjs and test_book_webhook.mjs passed for all 24 catalog products including the mini. These use mocks, not real payments or customer email.
- Privacy/private artifacts: test_book_demand.mjs and test_private_build_artifacts.mjs passed.
- All four examples were independently recomputed with Decimal, including the difference between a 2.5 kWh pre-recharge gap and a 1.0 kWh aggregate gap. Quote scope is counted once.
- All 35 fields retained canonical/widget values and saved appearances after reopening. Test input exceeds 100 characters and uses explicit newlines. Field limits are 1,000 characters; long notes scroll, and detailed schedules belong in attachments. Not every PDF viewer was tested.
- Contact sheet of all 26 pages, full-size completed examples/references and a saved filled sheet were inspected. No overlap or clipping observed in inspected renders.
- Local links, real preview files, page counts, schema, price baseline and sitemap passed. Immutable prior-price baseline is docs/battery-price-baseline.json.
- PDF SHA256: f67ef0f3477917261c8e82802297c9aee7a05bab1b1c35680024fac26b26c292. Original manuscript/build files, real WebP previews and exact PDF bytes in the established gated function route are durable release files. Do not add an ungated static copy of this new PDF.

## Acquisition and limitations

The latest available successful U.S. Search Console workflow is https://github.com/ranisamer/HomeCostEngine/actions/runs/40455797015 (artifact 12711219903, generated October 27). Finalized USA Web period September 26–October 23: 2,951 property impressions, 1 click, CTR 0.0339%, average position 50.78. Returned battery/backup query rows: none; omitted/anonymized/top-row limits mean this is not evidence of no market demand. The window predates this book. No growth inference is made.

GA4 U.S. product sessions, article-to-product activity, preview and checkout counts; live Stripe paid orders, refunds and net revenue; and actual reader feedback are unavailable through current connected tools. Missing does not mean zero. No demand or usefulness validation is claimed.

Existing server-controlled GBP checkout, paid+complete matching entitlement, private download and matching thank-you order link are reused. No actual payment, external email, customer session or spending occurred. The public repository contains embedded PDF bytes in its server routes: the live route gate is not source confidentiality or DRM. Electrical design, emergency suitability, household performance and applicable approvals require qualified providers.

## Live verification

Both exact clean product and article URLs above opened successfully in the browser after deployment. At the observed 1348 px desktop width, neither page overflowed horizontally. Both GBP price panels and Book schema show £9.99; 26 pages, 4 cases, 7 sheets, 35 fields and 2 completed demonstrations match the PDF. The actual cover and all three 796 × 1030 interior previews loaded. The article retains four contextual primary links and its reciprocal book link without generic injected source panels.

The live download route without a session returned "Invalid checkout session." Paid delivery and thank-you title/amount/link are covered by mocks; no live customer purchase or external email was performed. No mobile-device or real-reader trial occurred. The initial browser visit preceded deployment and returned a temporary 404; after the successful deployment, reload returned the intended product. No persistent live-page failure remains.

The ledger marks queue day 3 complete. The next queued topic remains EV Charger Installation Quote Planner; no additional title was created in this run.
