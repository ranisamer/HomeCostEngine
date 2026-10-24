# Bathroom Remodel Budget Guide - fourth completed edition

Original 2026-10-25 bathroom planning edition. Existing slug and £9 GBP price retained.

{
  "pages": 64,
  "fillable_fields": 95,
  "chapters": 21,
  "word_count": 9198,
  "sha256": "2b0990af5f816d2c28110c6dc42b0206911c553f838e347150835c278e394a39",
  "preview_physical_pages": [
    7,
    8,
    9
  ],
  "edition": "2026-10-25"
}

19 working chapters contain decision explanations, hypothetical examples and five-field worksheets. Seven chapters intentionally reuse HomeCostEngine owner-budget methods with bathroom adaptation; twelve are bathroom-specific. The manuscript depends on books/renovation-blueprint.py, which is already tracked. Public copy explains the overlap. All example rates are invented USD, with no market-price or savings claims. No construction, cleanup or hazardous-material procedure is provided.

Rebuild: `python3 scripts/build_bathroom_guide.py`. All 64 pages reviewed on a contact sheet; full-size moisture, assembly, first chapter, worksheet and source pages checked. Bounds, outlines and field count validated by generator. The canonical 95 AcroForm fields and 95 widgets have appearances; a saved QA value agrees in field tree and widget after reopening. Public samples are physical PDF pages 7-9 of the delivered edition.

Tests: `node scripts/test_bathroom_delivery.mjs`, previous three book delivery tests, `node scripts/test_book_webhook.mjs`, `node scripts/test_gbp_store.mjs`. Right-product/paid/complete sessions receive exactly the reviewed bytes; missing, unpaid, incomplete and wrong-product sessions are rejected. All 21 catalog products use the same verified transactional thank-you flow with correct title, paid amount and private order URL; retries deduplicate. No external buyer message or payment was triggered.

Store changes: new server-bundled PDF route, product catalog and verification entries, original cover, three real sample images, chapter list, benefits and intended-reader copy. Actual-edition library guards now accept later edition dates and retain accurate 64-page notes instead of relying on one hardcoded date. Library script cache versions updated.

The site gates PDF delivery on purchase verification; the repository is public, so this is not DRM. Primary sources are FTC contractor guidance, EPA moisture/RRP/WaterSense guidance and ENERGY STAR ventilation-fan information. No endorsement is claimed.

Completed full-book editions: renovation budget, roof replacement, kitchen remodel, bathroom remodel. Sixteen remaining full-book editions retain their earlier content pending individual rewrite and review; HVAC is next in catalog order.
