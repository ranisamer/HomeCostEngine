# HomeCostEngine — Static MVP

A fast, dependency-free home improvement calculator site designed for GitHub + Cloudflare Pages.

## Included
- Responsive homepage
- Calculators index
- Roof replacement calculator
- Concrete calculator
- HVAC replacement calculator
- Paint calculator
- Flooring calculator
- Mulch calculator
- Cost guide index + roof cost guide
- About, privacy, disclaimer, contact placeholder
- robots.txt, sitemap.xml, Cloudflare `_headers`
- No npm/build step required

## Deploy to GitHub
1. Create a new GitHub repository.
2. Upload everything inside this folder to the repository root.
3. Commit the files.

## Deploy to Cloudflare Pages
1. Cloudflare Dashboard → Workers & Pages → Create → Pages → Connect to Git.
2. Select the GitHub repository.
3. Framework preset: **None**.
4. Build command: **leave blank**.
5. Build output directory: **/** (repository root). If Cloudflare requests a value, use `.`.
6. Deploy.
7. In Custom Domains, connect your final domain.

## Before public launch
- Confirm the final domain and replace `homecostengine.com` in:
  - sitemap.xml
  - robots.txt
  - canonical tags / schema in HTML
- Replace placeholder contact details.
- Add GA4 / Search Console.
- Add a cookie/consent solution if required by your analytics/advertising setup.
- Do not add AdSense until privacy/disclosure setup is finalized.
- Review calculator assumptions and expand methodology/source documentation before marketing values as region-specific.
- Add email reports only after a real email backend is configured (e.g. Resend / Cloudflare Worker).

## Calculator philosophy
The MVP deliberately exposes assumptions instead of claiming false precision. Roof/HVAC calculators are budgeting ranges. Concrete, paint, flooring and mulch are arithmetic planning tools.

## Brand
Current working brand: **HomeCostEngine**
Working domain assumption: **homecostengine.com**
