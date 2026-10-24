# Renovation Budget Blueprint — first real book release

Edition: 2026-10-24. Existing product, £9 GBP. Original editorial content; reference used only for broad sequence and restrained book typography.

## Artifact

```json
{
  "pages": 64,
  "fillable_fields": 95,
  "chapters": 21,
  "word_count": 9257,
  "sha256": "d6aa02886a7f20f61e3a6022b2916eae20f990d54c88ec5cb902b4ea88d49803",
  "preview_physical_pages": [
    7,
    8,
    9
  ],
  "edition": "2026-10-24"
}
```

64 physical pages at 6 × 9 inches; 21 numbered chapters; chapters 2–20 each contain explanation, a hypothetical worked case and a planning sheet. 95 multiline fields (2,000 characters each), designed for compatible PDF readers and printing. Fields do not calculate automatically. All project examples use hypothetical USD, not market benchmarks; selling price remains GBP.

## Build and inspect

Requires Python 3 with reportlab, Pillow and PyMuPDF; DejaVu Serif/Sans TTF fonts at the standard Linux path used in the script. From the repository root:

- `python3 scripts/build_renovation_blueprint.py`
- `node scripts/test_blueprint_delivery.mjs`
- `node scripts/test_book_webhook.mjs`

The generator rebuilds the owner review PDF under output/, cover and three sample-page WebP images, contact sheet, validation JSON, and server-bundled paid route. Do not publish the full PDF under a static asset URL. Only pages 7–9 are public sample images.

## Checks and limits

All 64 rendered pages inspected on a contact sheet, plus full-size cover, contents, worksheet, dense chapter, example and source pages. Text bounds, page count, outline count and field count checked automatically. Field save/reopen confirmed with local QA values. Worked arithmetic checked independently. The paid route returns exactly the reviewed bytes in mock tests and rejects missing, unpaid, incomplete and wrong-product sessions. Legacy mini download regression covered. First-book checkout remains server-priced at 900 pence GBP with adaptive pricing disabled. JSON-LD and changed JavaScript parse.

The existing webhook's valid-signature, paid-status, book-title, £9 amount, private order-page URL, missing config, delivery failure and retry deduplication tests use mock Stripe/Brevo responses. No new real charge or email was sent. Earlier owner-confirmed live mini purchase is separate evidence; it does not establish inbox placement or a paid purchase of this book.

## Primary supporting resources

FTC Home Repair Scams; EPA Renovation, Repair and Painting Program; EPA Mold, Moisture and Your Home; ENERGY STAR contractor guidance; NFRC performance labels. Direct links are included in the actual PDF source notes. These organizations do not endorse the book.

## Publishing

One atomic default-branch commit contains the artifact source, exact server bytes, real samples, first product/catalog updates, scoped preview guard, tests and this record. Final deployment and live £9 checkout observation are reported with that commit; no customer payment is performed by the agent.
