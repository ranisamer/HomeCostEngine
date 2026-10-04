# U.S. long-tail search roadmap

Reviewed 2026-09-27. These are editorial hypotheses based on existing site coverage and public result patterns, not verified search-volume or ranking-difficulty estimates. Check U.S. Search Console data before changing priority. One search intent should have one primary URL; related phrases can be answered within that page.

| Search intent / candidate query | Primary URL | Distinct answer to provide | Supporting internal link |
| --- | --- | --- | --- |
| Cost to install gutter guards on a two-story house; how many linear feet for a 2,000 sq ft house | `/blog/gutter-guard-installation-cost.html` | Separate actual upper and lower eave runs, access, preparation and verified local rates; explain why total floor area is not gutter length. | `/roofing/gutter-replacement-cost.html` |
| Cabinet refacing cost for 20 doors and 8 drawers | `/blog/kitchen-cabinet-refacing-cost.html` | Door/drawer/panel takeoff and comparable quote inclusions; do not mistake allocated total per opening for a material unit price. | `/guides/kitchen-remodel-cost.html` |
| Roof decking replacement cost per sheet during a roof replacement | `/calculators/roof-decking-replacement-cost.html` | Editable panel count, installed per-sheet rate, waste and repair allowance; article explains uncertainty after tear-off. | `/blog/roof-decking-replacement-cost.html` |
| How much extra concrete for a 20×20 slab | `/blog/how-much-extra-concrete-should-i-order.html` | Volume from measured thickness and thickened edges, then explicit waste reserve without double counting. | `/calculators/concrete.html` |
| Subfloor replacement cost after water damage | `/blog/subfloor-replacement-cost.html` | Scope of demolition, moisture correction, panel replacement and floor finish exclusions. | `/calculators/flooring.html` |

## Next intent tests — 2026-09-28

These are long-tail editorial hypotheses, not measured low-competition keywords. Review U.S. Search Console query-page pairs before assigning priority or claiming ranking opportunity. Each query maps to one existing canonical URL because a new page would overlap its core answer.

| Candidate U.S. homeowner query | Canonical answer | Distinct addition and next step |
| --- | --- | --- |
| How to size a heat pump after air sealing and insulation | `/blog/how-to-size-a-heat-pump-for-your-home.html` | Added a before/after load scenario and retrofit sequencing; connect to HVAC planning. |
| How much extra concrete for uneven subgrade and a thickened patio edge | `/blog/how-much-extra-concrete-should-i-order.html` | Added measured low spot and edge calculations before allowance or supplier rounding. |
| How to compare window replacement quotes when trim repair is excluded | `/blog/window-replacement-cost-per-window.html` | Added an opening-by-opening normalized example and an explicit change-order method. |

## Publishing rules

1. Inspect the existing URL and competing intent before commissioning another article. Add a useful section or worked example to the primary page when the intent overlaps.
2. Put the answer and calculation near the top, then include scope, exclusions, regional caveats, and a link to the relevant calculator in the body. Link back contextually from two to four related pages when publishing a genuinely new topic.
3. Do not fabricate a national or state price, search volume, customer result, or credential. An illustrative calculation must say it is hypothetical and use locally verified rates for real budgets.
4. Keep the canonical URL, title, heading, on-page FAQ and structured data consistent. Test internal links and images after publishing.
5. Review Search Console Performance for Web with Country = United States, comparing 28 and 90 days. For each query-page pair, record impressions, clicks, CTR and average position. Prioritize queries already earning impressions where a matching page answers incompletely; inspect pages receiving the same query to catch cannibalization. Measure changes after Google has had time to recrawl and accumulate data. Reassess candidates with no impressions instead of generating near-duplicate location or house-size pages.

Google guidance: [people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content), [crawlable links and descriptive anchors](https://developers.google.com/search/docs/crawling-indexing/links-crawlable), [Search Console Performance](https://support.google.com/webmasters/answer/7576553?hl=en).

## AdSense content-quality recovery — audit 2026-09-29

The live `ads.txt` responds 200 with the authorized publisher line. AdSense still shows an older “not found” status; do not edit the working file just to change the dashboard. Its low-value-content decision is separate.

A repository audit found 39 indexable blog articles with fewer than roughly 600 words of source article text (excluding server-added boilerplate). The Cloudflare middleware previously appended the same “Detailed planning notes” blocks across articles. That automatic depth was removed; it should not substitute for a topic-specific answer. No promise of AdSense approval follows from this cleanup.

Before adding articles, improve one existing thin, indexable canonical page per run. Start with `blog/how-much-mulch-do-i-need.html`, `blog/how-much-paint-do-i-need-for-a-room.html`, `blog/concrete-driveway-cost-per-square-foot.html`, `blog/mulch-cost-per-yard.html`, and `blog/toilet-repair-vs-replacement.html`, adjusting priority if fresh U.S. Search Console query–page data supports another page. Give each a distinct answer, calculations or quote method, scope and exclusions, local caveats, relevant primary sources, and 3–5 descriptive in-body internal links. Do not pad to a word count or create house-size variants with the same answer. Verify forms, links, canonical URLs, structured data and mobile layout before each atomic commit.

Each week compare U.S.-filtered Web Search Console query–page pairs over the latest 28 days versus the preceding 28 days: impressions, clicks, CTR, average position, index status and the page improved. The current screenshot is a page-indexing summary, not U.S. traffic evidence. Reassess whether to request AdSense review only after the indexable thin-page backlog and duplicate-content patterns have been substantively addressed.

## Daily quality update — 2026-10-01

- Primary intent: how much paint is needed for one room, including openings, finish coats and separate primer/ceiling quantities.
- Canonical: `/blog/how-much-paint-do-i-need-for-a-room`. Preserved the live extensionless URL; aligned source canonical and Article URL with it.
- Replaced the approximately 246-word source answer with a topic-specific measurement method, a 12 × 14 ft worked room, coverage sensitivity, package rounding, exclusions and five visible FAQs.
- Added five unique descriptive links within the main text and contextual inbound guidance from painting-labor and interior-painting cost pages.
- Sources checked October 1: Behr's product-specific coverage guidance and EPA's pre-1978 consumer renovation guidance. No national prices or ranking difficulty invented.
- Fresh U.S.-filtered Search Console query-page access is unavailable. The September 30 export remains a dated all-country baseline; automated live performance tracking is unavailable.
- Source audit scanned 71 blog article files. With the current method (main article text, excluding related asides), 41 were below 600 words before this update, including three noindex pages; 38 indexable articles were below 600 words and 37 remain after this update. This differs from the September 29 audit and is a count to track consistently, not evidence that new thin articles were published. Confirm indexability and actual content before selecting each next page.
- Room quantity page was listed in the September 29 recovery queue; the September 21 edit still left it without worked quantity math. This substantive recovery resolves that observed gap.
- Image: existing quantity page has no hero; this is an existing-page update, so no new-article raster image was required.
- Next queue: concrete driveway cost per square foot, mulch cost per yard, toilet repair versus replacement. Preserve recent substantive improvements; review current content and history before choosing.
- Outcome checks: formula arithmetic, source/visible FAQ alignment, extensionless canonical, internal destinations and live output required before marking publication complete.


## Daily quality update — 2026-10-02

- Primary intent: concrete driveway cost per square foot as a comparable installed-scope metric, not a national price claim.
- Canonical: `/blog/concrete-driveway-cost-per-square-foot`. Source canonical and Article URL now align with the extensionless live URL normalized by site middleware.
- Replaced the approximately 327-word source answer with a homeowner quote-normalization method, a 720 sq ft quantity example, low/typical/high-complexity scope logic, inclusions, exclusions, permit caveats and five visible FAQs.
- Added five unique descriptive links within the main text and contextual inbound links from the concrete-patio-thickness and gravel-driveway-cost pages.
- Sources checked October 2: NRMCA joint guidance, American Concrete Pavement Association subgrade/subbase guidance and ACI curing guidance. No national installed prices or ranking difficulty invented.
- Fresh U.S.-filtered Search Console query-page access is unavailable. The September 30 export remains a dated all-country baseline; automated live performance tracking is unavailable.
- The tracked indexable thin-page backlog moves from 37 to approximately 36 after this substantive update; reverify current indexability and source word count before selecting the next page.
- Image: existing page has no hero; this is an existing-page update, so no new-article raster image was required.
- Next queue: mulch cost per yard, then toilet repair versus replacement, unless verified fresh query-page evidence supports a different existing page.
- Outcome checks: quantity arithmetic, source/visible FAQ alignment, extensionless canonical, internal destinations, changed files and live output required before marking publication complete.


## Daily quality update, 2026-10-03

- Primary canonical intent: toilet repair versus replacement, diagnosed failure and complete installed scope. URL: /blog/toilet-repair-vs-replacement.
- Replaced 342 source words (excluding related aside) with 1,200 substantive words, a three-year quote comparison formula, a 2,336-gallon annual savings quantity example, scope scenarios, exclusions and five visible FAQs.
- Five unique in-body links to the installation calculator, hidden-leak article, installation scope article, quote comparison calculator and bathroom guide; contextual inbound links added in the hidden-leak article and bathroom guide.
- Source canonical and Article URL aligned with live extensionless URL; Article review date and author updated, matching FAQPage added. Existing 1200 x 675 SVG kept and linked to canonical; redundant planning graphic removed.
- Primary references verified October 3: EPA WaterSense Home Maintenance and Residential Toilets. No contractor prices, probabilities or promised payback invented.
- Current source audit: 71 articles, 36 indexable source articles below 600 words before this update; 35 remain after it. Counts exclude related asides and do not claim every longer page meets quality standards.
- No fresh U.S.-filtered Search Console access is available. September 30 export remains a dated all-country snapshot, not live query-page evidence.
- Next action: mulch pricing is still short, but its September 21 substantive update is within 14 days. Preserve it for now; select another verified thin page unless fresh evidence or a concrete bug changes priority.


## Daily quality update, 2026-10-04

- Primary canonical intent: complete installed gravel driveway cost per square foot, separating refresh, rebuild and difficult-site scopes. URL: `/blog/gravel-driveway-cost`. Existing quantity and calculator pages keep their separate tasks; no new phrase-variant page created.
- Replaced the 524-word source answer with a layer-by-layer quantity example, supplier conversion caveats, a complete budget formula, scope scenarios, exclusions, permit checks and five matching FAQs. No invented national or local prices.
- Five unique contextual internal destinations in the main text, plus a linked canonical hero. Strengthened inbound paragraphs in the driveway quantity guide and gravel calculator.
- Replaced the unstable external hero with an original text-free 1600 x 900 WebP at `assets/blog/gravel-driveway-cost.webp`; linked to the canonical and added alt text and explicit dimensions.
- Primary sources verified October 4: EPA-hosted Gravel Roads manual sections on Surface Gravel and Drainage, and MnDOT access/driveway permit forms. Road guidance is background, not a private driveway design specification.
- Additional scoped accessibility improvement: the gravel calculator's result now has a polite status announcement for assistive technology. No form logic or design changes.
- Source audit: 71 article files, 35 indexable articles below 600 source words before this update; 34 remain after it, excluding related asides. Word count alone does not establish complete quality.
- Fresh U.S.-filtered Search Console access is unavailable. The September 30 all-country export is a dated baseline, not live query-page evidence or proof of U.S. keyword positions.
- Next action: preserve mulch pricing until its 14-day window has passed; reaudit thin quantity and cost pages and select the next useful existing intent. Continue using measured U.S. query-page evidence when access becomes available.
