# Kitchen Remodel Cost Planner - third completed book

2026-10-24 original edition. Existing product slug and £9 GBP price preserved.

{
  "pages": 64,
  "fillable_fields": 95,
  "chapters": 21,
  "word_count": 9180,
  "sha256": "66504782f854d9a0d24c0cf4e837e5d3061ad2c1c7138ea4b0ee1be730ac6ed7",
  "preview_physical_pages": [
    7,
    8,
    9
  ],
  "edition": "2026-10-24"
}

19 working chapters each contain explanation, a hypothetical example and a five-field reusable worksheet. Seven general owner budgeting methods intentionally reuse the original HomeCostEngine renovation manuscript; twelve kitchen chapters address existing conditions, layout, cabinets, hardware, counters, plumbing, appliances, electrical endpoints, ventilation, flooring, finishes and temporary arrangements. The source dependency is books/renovation-blueprint.py. Public copy explains the overlap. Project rates are invented USD inputs, not market benchmarks or guaranteed savings.

Rebuild with `python3 scripts/build_kitchen_planner.py`. All pages reviewed on the contact sheet, with full-size text, hardware and closeout pages checked. Bounds and outlines checked by generator. 95 canonical fields and 95 widgets have appearances; saved QA values agree after reopening. Samples are physical pages 7-9 of this exact PDF.

Tests passed: `node scripts/test_kitchen_delivery.mjs`, `node scripts/test_book_webhook.mjs`, `node scripts/test_gbp_store.mjs`. Complete paid/right-product mock receives exactly the reviewed PDF bytes. Missing, unpaid, incomplete and wrong-product requests are rejected. All 21 catalog products use the existing signed-webhook thank-you flow with correct product title, actual amount and private order URL; no live purchase or external email was sent during these checks.

Publication updates only this product's PDF route, catalog entries, product page, cover, samples and library card. First and second completed books and transactional mail behavior are preserved. The full PDF is bundled in the server route rather than a static asset; the GitHub repository is public, so this is site checkout gating, not DRM.

Supporting primary sources: FTC contractor guidance, EPA RRP guidance and ENERGY STAR dishwasher buying information. The book links to them and does not imply their endorsement.

Progress: renovation blueprint, roofing handbook and kitchen planner complete. Bathroom book is next; 17 other full-book editions remain to be rewritten and reviewed individually.
