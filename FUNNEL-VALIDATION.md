# Roofing funnel: verification and paid-acquisition gate

Reviewed October 22, 2026. Owner priority: prove useful actions and book fulfillment before considering advertising. No campaign, budget or marketing send is authorized by this document.

## Current evidence

- Live roof-book page and purchase button tested October 22: `Checkout is not configured yet.` No checkout page, payment, receipt or paid delivery could be completed. The server source confirms a 503 response when STRIPE_SECRET_KEY is unavailable. This is an observed runtime blocker, not proof about the owner's Stripe account.
- Roof calculator and public workbook/PDF are accessible. QA interaction and a PDF request verify functionality, not real customer use or a saved/read file.
- Existing analytics property in middleware: G-T47EEK5EH0. Event instrumentation below uses that existing tag; access to the GA4 reporting interface is still needed to verify received real traffic. No historical conversion numbers are available from source code or GSC.
- No verified buyer reviews were provided; the roof-book page now states that none have been published instead of presenting an editorial star score beside a verified-review heading.
- The payment-return page now starts with neutral verification wording. It only says payment verified after the server confirms paid and complete; no payment token is sent to GA4 from that page.

## Measured actions

| Event | Exact meaning | Does not establish |
|---|---|---|
| roof_calculation | First valid user-submitted roofing calculation with a numeric result per page load | Unique person, contractor quote or purchase |
| workbook_open | User click to free workbook landing page | Download or subscription |
| workbook_download_click | User click on the free PDF link | Completed save, reading or email delivery |
| roof_book_open | User click to the roofing book page | Checkout or sale |
| checkout_attempt | User click on a roof-book purchase button | Stripe session or paid transaction |
| checkout_error | Roof-book inline checkout failure | Failed card charge |

No page-load calculation event. No input values, email, ZIP, estimate totals, session tokens or payment details in custom event parameters. A blocked/unavailable Google tag means events are not received; never infer delivery from JavaScript availability. Existing enhanced-measurement events may also exist; do not add them to these counts as if different people.

## QA and reporting

Open a page with `?hce_qa=1`. Middleware omits GA4 on that request; the funnel script writes local `[HCE funnel QA]` console messages only. Internal clicked links retain the QA marker. Do not use the marker for real traffic. Return to ordinary URLs for production use. Test purchases must remain distinguishable in Stripe's test environment; no synthetic purchase event is sent to GA4.

In GA4, verify the named events on genuinely consented/allowed real traffic; configure an exploration from roof calculation to workbook to book/checkout. Custom parameters are funnel_version and page_path only. Filter U.S. geography and organic source when answering the U.S. SEO question. Event counts are not automatically unique visitors or conversion rates; choose the same user/session basis and completed dates. Stripe completed live payments and successful file fulfillment, reconciled to unique order IDs, are the source of truth for sales.

## Release gates before any proposed paid test

1. Owner configures the encrypted Stripe test secret in Cloudflare Pages and redeploys, using STRIPE_SETUP.md. Never paste keys into chat or repository files.
2. Complete test-mode payment, unpaid/failed/cancelled cases and a repeat verification. Confirm correct product, actual PDF contents/page count and promised bonus delivery. The current return-page-only delivery also needs a recovery path for customers who close Checkout before returning; do not claim automatic email fulfillment is implemented.
3. Owner verifies business/payment settings, then separately authorizes any real small purchase with an amount limit. No charge is authorized or made during this audit.
4. Verify real GA4 actions and reporting access, free PDF and optional unchecked consent. Brevo transactional inbox delivery and suppression require an owner-authorized test address and provider access.
5. Review the actual sample: useful organic actions, completed downloads where observable, settled sales, refunds and fulfillment errors. There is no invented minimum or guaranteed conversion rate. Keep spend at zero until this evidence is reviewed and a separate budget is approved.

No claim of AdSense approval, live sales, inbox delivery or return visitors is made by implementing instrumentation.
