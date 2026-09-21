# Stripe setup for HomeCostEngine digital books

The storefront and Stripe Checkout code are already in the repository. The site intentionally does not contain a Stripe secret key.

## 1. Add the Stripe secret in Cloudflare Pages

In Cloudflare Dashboard, open the HomeCostEngine Pages project and add an encrypted environment secret:

- `STRIPE_SECRET_KEY` = your Stripe secret API key
- `SITE_HOST` = `homecostengine.com`

Start with a Stripe **test** secret key. Do not commit the secret key to GitHub and do not place it in client-side JavaScript.

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
