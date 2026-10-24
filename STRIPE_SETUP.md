# Stripe setup for HomeCostEngine digital books

The storefront and Stripe Checkout code are already in the repository. The site intentionally does not contain a Stripe secret key.

## 1. Add the Stripe secret in Cloudflare Pages

In Cloudflare Dashboard, open the HomeCostEngine Pages project and add an encrypted environment secret:

- `STRIPE_SECRET_KEY` = your Stripe secret API key
- `SITE_HOST` = `homecostengine.com`

Production uses the owner-configured Stripe live secret key. Use a separate non-production environment for sandbox testing. Do not commit the secret key to GitHub and do not place it in client-side JavaScript.

The checkout endpoint is:

`/api/create-checkout-session`

The purchase verification endpoint is:

`/api/verify-purchase`

## 2. Optional automatic tax

Only after Stripe Tax is configured for the account, add:

`STRIPE_AUTOMATIC_TAX` = `true`

If this variable is missing or false, Checkout leaves automatic tax disabled.

## 3. Deploy and test

Redeploy the Cloudflare Pages project after adding the secret.

Open any page under `/ebooks/`, click **Buy securely with Stripe**, complete a test-mode Checkout payment, and confirm that Stripe returns to:

`/ebooks/success.html?session_id={CHECKOUT_SESSION_ID}`

The success page verifies the Checkout Session server-side before revealing the PDF download.

## 4. Go live

When test purchases work:

1. Switch the Stripe account to live mode.
2. Replace `STRIPE_SECRET_KEY` in the Production environment with the live secret key.
3. Confirm the business name, support email, statement descriptor, payment methods, receipts, tax settings and refund policy in Stripe.
4. Make one low-risk live purchase and confirm the complete payment-to-download flow.

## Store configuration

- 10 digital books
- USD 9.00 each
- One-time payment
- Hosted Stripe Checkout
- Promotion-code support enabled
- Customer email collected by Checkout
- Download is shown only after server-side verification reports `payment_status=paid` and `status=complete`

## Paid-file note

The current PDFs use non-obvious URLs and noindex/private-cache headers, but they still live in the public website repository. For stronger paid-file protection, move the PDFs to a private Cloudflare R2 bucket and issue time-limited signed downloads after Stripe verification.



## GBP-only storefront - October 24, 2026

All 20 full-length books retain their existing numeric selling prices, now denominated in GBP (for example $9 becomes £9; no FX conversion). Visible prices and Offer structured data match server-authoritative amounts. Existing U.S. project-budget examples remain in their original currency.

Checkout creates GBP sessions with Adaptive Pricing explicitly disabled, so the checkout does not offer a locally converted selling currency. Prices are tax-inclusive if automatic tax is enabled. The new `project-quote-mini-workbook` is a genuine three-page PDF priced at 50 pence. Its PDF is bundled in the server endpoint and requires a complete, paid Stripe session for that product; no public PDF is deployed.

Buyer return: `/ebooks/success.html?session_id=…` verifies Stripe payment, shows “Thank you for your order” and “Download your PDF”. Unpaid, invalid and different-product sessions cannot retrieve the mini workbook. Keep confirmation links private. Existing paid orders continue to verify regardless of their original currency.

Transactional fulfillment is implemented at `/api/stripe-webhook`, but requires the endpoint registration and secrets described below. The thank-you email links to the verified purchase download; it does not attach a large PDF. Stripe customer receipts require Dashboard → Settings → Business → Customer emails → Successful payments. Owner email/push notifications depend on the owner's Stripe notification settings; the paid transaction appears in Stripe Payments. Do not claim either email was delivered without a completed payment and verified inbox result. Never add a purchaser to marketing without separate consent.

Validation: mock all 21 checkout amounts/currencies, disabled Adaptive Pricing, product identity and paid/unpaid PDF guards; visually inspect all three PDF pages; open live Checkout without completing a charge. A paid end-to-end delivery and inbox test remains owner-operated.


## Activate transactional book delivery (owner setup required)

1. In Stripe live Dashboard → Workbench → Webhooks, add destination `https://homecostengine.com/api/stripe-webhook` for **your account**, with `checkout.session.completed` and `checkout.session.async_payment_succeeded`. Use the snapshot event payload, not thin events.
2. Copy that destination's signing secret into Cloudflare Pages Production encrypted secret `STRIPE_WEBHOOK_SECRET` (starts `whsec_`). This differs from the API secret key. Never put it in GitHub, client code or chat.
3. Production needs `BREVO_API_KEY` plus an authenticated sender matching `BREVO_SENDER_EMAIL` (default `reports@mail.homecostengine.com`). Optional `BREVO_REPLY_TO` defaults to `reports@homecostengine.com`. Preserve suppression/unsubscribe settings; this handler never creates or resubscribes contacts.
4. Redeploy after saving secrets. GET `/api/stripe-webhook` reports only missing variable names, never values. Configured variables alone do not prove a registered Stripe destination, authenticated sender or inbox delivery.
5. Owner completes the £0.50 real order with their own card and email. Confirm paid transaction in Stripe, webhook 2xx, Brevo transactional logs and actual inbox, correct book-download link and valid PDF. No owner-authorized live charge or outbound message was executed during implementation.

The handler validates the raw-body HMAC and 5-minute signature timestamp, re-fetches the session from Stripe, fulfills only complete/paid catalog purchases, and ignores test events when using a live API key. Brevo acceptance is recorded in Stripe session metadata to suppress future repeats; a stable provider idempotency key reduces duplicates during overlapping/retried events. Brevo's deduplication window is limited: a provider-accepted send followed by a prolonged metadata-write failure needs operator reconciliation before replaying old events. Failures return 5xx for Stripe retries; no unverified browser action can trigger a send. No automatic marketing enrollment, owner notification email or campaign is added. The buyer's verified download remains available even if email delivery is delayed.

Email example: subject `Thank you - your Project Quote Mini Workbook is ready`; body thanks the buyer, names the purchased book, shows the paid amount, and provides a private `Download your book` button and reply-for-help instructions. A Stripe receipt is separate and depends on Stripe receipt settings.
