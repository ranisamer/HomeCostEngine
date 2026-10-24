# HVAC Replacement Buyers Guide - fifth completed edition

Original 2026-10-25 HVAC planning edition. Existing product slug, £9 GBP.

{
  "pages": 64,
  "fillable_fields": 95,
  "chapters": 21,
  "word_count": 9231,
  "sha256": "0b04965c7fcb70dabbf4037981fd922c1f409c7653bc892cbe934d3583f70d51",
  "preview_physical_pages": [
    7,
    8,
    9
  ],
  "edition": "2026-10-25"
}

19 working chapters, each with explanation, hypothetical worked case and five-field worksheet. Six general budgeting chapters use HomeCostEngine renovation methods with HVAC adaptation; thirteen are HVAC-specific. No sizing, diagnostic, installation, wiring, refrigerant or commissioning procedure is supplied. No incentive amount or eligibility is assumed. Project dollar amounts are invented USD examples, not market prices or promised energy savings.

Rebuild: `python3 scripts/build_hvac_guide.py`. Manuscript depends on the tracked books/renovation-blueprint.py. All pages reviewed on a contact sheet and full-size sizing, ownership-cost, budget and source pages checked. Generator checks page bounds, outlines and field counts. 95 canonical fields and 95 widgets have appearances; QA saved value agrees after reopening. Public cover and samples are actual pages of the reviewed PDF.

Tests passed: test_hvac_delivery.mjs, test_book_webhook.mjs and test_gbp_store.mjs. Right-product/paid/complete mock delivery equals the reviewed bytes; invalid entitlement states are denied. The existing signed-webhook flow covers all 21 products with correct name, paid amount and private order URL, with retry deduplication. No live payment or external email was sent.

Store: original cover, three actual samples, full chapter list, intended-reader and benefits copy, exact 64-page description, product-specific paid route and matching catalogs. The GitHub repository is public; site checkout gating is not DRM. Sources: FTC contractor guidance, ENERGY STAR quality-installation and heat-pump buying guidance. No endorsement is claimed.

Completed: renovation budget, roofing, kitchen, bathroom and HVAC. Concrete is next; 15 other editions remain to be rewritten and reviewed individually.
