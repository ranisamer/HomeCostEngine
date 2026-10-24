# Roof Replacement Planning Handbook - original edition

Second full book in the catalog. Existing slug, £9 GBP, 2026-10-24 edition.

{
  "pages": 64,
  "fillable_fields": 95,
  "chapters": 21,
  "word_count": 9555,
  "sha256": "b89ca77fe57edd28529d8d694ebafd1dbaa3bcc79bbca1bc558c399c10c4c3e1",
  "preview_physical_pages": [
    7,
    8,
    9
  ],
  "edition": "2026-10-24"
}

Original roofing text follows the broad reference sequence, with 19 worked decision/arithmetic cases and 19 fillable worksheets. Rates are hypothetical USD, not local market benchmarks. No owner roof access is required. Supporting references: FTC contractor guidance, NRCA contractor selection and DOE cool-roof guidance.

Rebuild: `python3 scripts/build_roof_handbook.py`. Reviewed all 64 pages on a contact sheet plus full-size text, worksheet and source pages. Verified 95 canonical AcroForm fields and widgets with appearances; QA input saved and reopened with matching values. Public cover and samples are actual PDF pages. The full PDF is served from the paid route after complete/paid/right-product Stripe verification; repository source itself is public, so this is checkout gating, not DRM.

Tests: `node scripts/test_roof_delivery.mjs`, `node scripts/test_blueprint_delivery.mjs`, `node scripts/test_book_webhook.mjs`, `node scripts/test_gbp_store.mjs`. Mock paid download equals the reviewed bytes. Missing/unpaid/incomplete/wrong-product requests are rejected. All 21 catalog products (20 full-book entries and the mini workbook) produce the correct title, paid GBP amount and private order link in the mocked thank-you email; provider retries deduplicate. Neutral feedback wording permits negative feedback and requires permission before publication. No external buyer email or real charge was triggered.

Both completed books now explain why to buy, intended reader, practical benefits, exact deliverables and the difference from free tools, with real sample pages and no guaranteed savings or customer-review claims. Other books retain their previous editions until rewritten individually. Kitchen is next in catalog order.
