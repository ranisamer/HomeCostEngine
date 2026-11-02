# My roof project — first return-visit workspace

Prepared November 1, 2026. **DRAFT FOR REVIEW; NOT PUBLISHED TO MAIN OR LIVE.**

Owner-approved direction: give U.S. homeowners a useful reason to return while collecting roof proposals and updating a cash plan. No external post, email, ad budget or marketing enrollment is authorized by this implementation.

## Scope

Existing `/projects.html#my-roof-project`, connected from the existing roof calculator and quote comparison tool. One optional browser-local project, without an account, email gate or server database. Original calculator formulas, titles, canonicals, paid products, Stripe, consent and unsubscribe behavior remain untouched.

- Explicitly save the latest user-calculated roof inputs and model range. Stale input changes disable save. Restoring inputs recalculates with today's model; the dated stored estimate stays labeled. State-level inputs are stored, ZIP/live local-data values are not.
- Keep three actual proposals, priced exclusions, unresolved-work flags and scope notes. Blank slots remain empty; explicit zero required when no priced exclusions remain. No demo prices are passed off as real proposals. Existing quote-scoring tool remains available for a distinct task.
- Choose one proposal for arithmetic, not contractor recommendation. Known scope = quote + required priced exclusions. Keep included allowances inside quote total. Cash plan = known scope + separate owner reserve; remaining cash = cash plan − payments already made. Unknown required work remains provisional. Paid-above-known warnings prevent treating an overpayment as savings.
- Save checklist progress, export/import a private JSON backup, print saved records and delete only this feature's browser record after confirmation. No cloud sync or public sharing token. Storage failures do not claim success, malformed imports do not replace saved records, and concurrent-tab changes prevent silent overwrite.

## Arithmetic verified

Proposal A $15,000 + required priced exclusions $1,800 = known scope $16,800. Owner reserve $1,000 gives $17,800 cash plan. $3,000 already paid leaves $13,800 known scope unpaid and $14,800 cash including reserve. Against a $20,000 budget, headroom is $2,200. Proposal B $16,500 + $0 exclusions stays $16,500. No contractor is selected automatically; scope may differ.

## Measurement boundary

Existing GA4 only, when available under the site's existing consent/configuration. Events: `roof_project_saved`, `roof_second_quote_saved`, `roof_project_exported`, `roof_project_imported`, `roof_project_reopened`. Parameters are `funnel_version` and static `page_path`; no project name, notes, cost, ZIP, contact or backup contents. `hce_qa=1` logs locally and carries into workspace links. Reopened means a stored record at least 24 hours old was opened, not a verified retained unique user. Use GA4 user/cohort reports to measure actual 7-/28-day retention after production verification. No usage or conversion outcome is claimed.

## Validation and blocker

Run from repository root:

```
node --check assets/roof-project.js
node scripts/test_roof_project_model.cjs
node scripts/test_roof_project_dom.cjs
```

33 model assertions and 26 DOM-adapter assertions pass. The adapter executes actual feature code using IDs/defaults parsed from the changed source pages, covering persistence/reload, second quote, invalid save, JSON roundtrip, corrupt data, failure/cancel behavior, concurrent tabs, snapshot handoff, restoring inputs and QA links. Source checks also verify unique IDs and associated labels. A DOM adapter is not a browser rendering or accessibility-tree test.

**BLOCKED:** production HTTP currently returns 403 from this environment. Cloud browser fails before navigation because its sessions path is read-only. Local Chromium also fails to start because an OS socket operation is denied. These failures do not establish that visitors or Google are blocked. Real browser desktop/mobile layout, keyboard interaction, print/export download behavior, production script loading, live storage across navigation and GA4 receipt remain unverified. No default-branch update/deployment is made. Do not describe this branch as a live launch.

Before release: inspect responsive/keyboard/error states and actual saved/reloaded/imported/downloaded files in a working browser; verify the existing calculator and quote tool still work; check live destination links/PDF and unchecked email consent; review GA4 QA exclusion; then merge/release atomically and verify live content. Resume the paused daily task only after live verification is restored and the owner requests continuation. The unrelated prepared cabinet repair remains separate.

Draft acquisition scripts: `docs/ROOF-PROJECT-VIDEO-DRAFTS.md`. No external publication has occurred.
