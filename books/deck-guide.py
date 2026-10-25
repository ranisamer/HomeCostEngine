"""Original deck owner planning and cost cases, with established owner-budget methods."""
from pathlib import Path
import runpy,copy
base=runpy.run_path(str(Path(__file__).with_name('renovation-blueprint.py')))
CHAPTERS=[]
def chapter(title,deck,paragraphs,example,rows,conclusion,prompts,checks,task):
    CHAPTERS.append(dict(title=title,deck=deck,paragraphs=paragraphs,example=example,rows=rows,conclusion=conclusion,prompts=prompts,checks=checks,task=task))
def method(index,title):
    c=copy.deepcopy(base['CHAPTERS'][index]);c['title']=title
    replacements={'renovation':'deck project','Make the kitchen usable for two cooks':'Create a usable outdoor area for the household','buy new cabinets':'buy deck boards','A bathroom project in a one-bath home has a different temporary-use problem from the same work in an empty property.':'Replacing the only outdoor access creates different temporary-use needs from work on a separate unused deck.','fixture allowance':'finish-selection allowance'}
    def adapt(s):
        for a,b in replacements.items():s=s.replace(a,b)
        return s
    for k in ['deck','example','conclusion','task']:c[k]=adapt(c[k])
    for k in ['paragraphs','prompts','checks']:c[k]=[adapt(x) for x in c[k]]
    CHAPTERS.append(c)

method(0,'Define the deck and outdoor-living brief')
chapter('Map use, layout and the existing site','A useful deck begins with the household outcome.',[
'Describe the intended activities and how people move between the home, deck and yard. Record furniture, access and retained outdoor uses without treating a furniture sketch as a structural design. Assign an ID to each proposed platform, stair, landing or other area.',
'Collect existing property records and accessible observations about the site. Ask qualified providers to assess relevant ground, drainage, structural, utility and boundary questions. Do not dig, climb or disturb components to complete the owner record.',
'Compare feasible layouts against the same outcomes. A smaller platform with different stairs may have a different total and usefulness even when the decking material is unchanged. Keep the tradeoffs visible beside the concept.',
'Identify local approvals and technical decisions needing confirmation before procurement. A plan drawn to scale can support discussion but does not itself authorize construction. Retain the professionally confirmed version used for pricing.'
], 'A fictional layout has one platform, one stair group and one landing, with the access route retained as a separate site record.', [('Platform','1 area ID'),('Stair group','1 scope ID'),('Landing','1 area ID'),('Retained access','Separate record')],
'The component list organizes scope. It does not establish design, dimensions or approval requirements.',
['Activities / household routes / retained uses','Platform / stair / landing IDs / current sketch','Property records / accessible site observations','Qualified site and design questions / local review','Feasible layouts / tradeoffs / pricing version'],
['The owner sketch is not a structural instruction.','Site questions have appropriate reviewers.','Access is included in the concept record.'], 'Agree on the intended use and ask the qualified provider to confirm feasible layouts.')

chapter('Compare repair, resurfacing and replacement scope','New boards do not establish the condition of the retained structure.',[
'Describe the observed issues and ask a qualified provider to assess the existing deck and relevant connections. Keep the findings and limitations with the proposal. This book supplies no structural inspection, probing, loading or repair procedure.',
'Separate a defined repair, surface replacement and complete replacement as different alternatives. State which structure, connections, guards, stairs and other elements remain. A resurfacing quote cannot be assumed to include assessment or correction of all retained components.',
'Compare complete assessed alternatives with the same intended use and relevant requirements. Record supporting work, removal, disposal and restoration. Avoid assigning an invented remaining life to the retained deck to make a price comparison appear precise.',
'Keep professional use restrictions or urgent findings outside a simple price ranking. The owner should obtain the appropriate response rather than continue use because an option is cheaper. The worksheet supports the decision record without certifying serviceability.'
], 'A fictional assessed surface option is $5,000 with $2,000 separately required retained-component work. A matched complete replacement offer is $9,000.', [('Surface package','$5,000'),('Required retained-component scope','$2,000'),('Complete limited-work option','$7,000'),('Matched replacement','$9,000'),('Immediate difference','$2,000')],
'The example does not recommend retention or predict useful life. Actual findings and complete scope determine viable options.',
['Observed issues / qualified assessment / limitations','Repair / surface / replacement alternatives','Retained elements / required supporting scope','Complete prices / exclusions / no life assumption','Use guidance / decision rationale / accepted option'],
['New surface boards do not certify retained structure.','Required repairs enter the limited-work price.','Urgent qualified findings are not averaged into a score.'], 'Request the retained-component assessment and complete scope before choosing resurfacing.')

chapter('Separate platform area from perimeter and stairs','Different shapes create different quantity records.',[
'Calculate geometric platform area from the professionally established layout and verified dimensions. Split irregular non-overlapping sections before adding them. Keep stairs, landings and other features on their own scope lines unless the takeoff expressly includes them.',
'Record perimeter and each edge condition separately from area. A square and a long narrow rectangle can have the same surface area and different perimeter. Railing, fascia and edge-related scope need their actual location and unit basis.',
'Ask the responsible provider which portions of perimeter receive guards, stairs, connections or other details. The total perimeter is not automatically the required guard length. This guide gives no guard, stair or structural dimension requirement.',
'Retain the area, edge schedule and layout version with every quote. If the shape changes, update dependent quantities rather than preserving the old per-square-foot total. A calculator verifies arithmetic but cannot approve the layout.'
], 'Two fictional platforms have equal area: 12 × 12 ft and 6 × 24 ft. Their perimeters differ.', [('12 × 12 area / perimeter','144 sq ft / 48 ft'),('6 × 24 area / perimeter','144 sq ft / 60 ft'),('Perimeter difference','12 linear ft'),('Required guard length','Not determined here')],
'Equal area does not mean equal edge scope or complete installed cost. Use the actual professionally defined edge schedule.',
['Approved layout / verified dimensions / area sections','Platform area / separate stairs and landings','Perimeter / edge IDs / guard and opening locations','Provider-confirmed quantities / matching units','Layout revisions / dependent material and labor changes'],
['Area and perimeter are distinct.','Perimeter is not assumed required guard length.','Shape changes update the takeoff.'], 'Ask every bidder to use the same area and edge schedule rather than only a surface area.')

chapter('Establish structural and local decision gates','A material list cannot replace project-specific design.',[
'Ask qualified providers and the actual local authority to establish the relevant structural, site and approval requirements. Record who prepares and reviews the design and which documents support pricing. The owner record should identify decisions without supplying technical dimensions.',
'American Wood Council deck resources are technical references with stated scope and limitations [2]. Their existence does not establish that a particular detail applies to the actual deck or jurisdiction. This handbook does not reproduce their design tables or adopt a building-code edition.',
'Record foundation, framing, connection, guard and stair questions as applicable with responsible professionals. Keep unknown conditions and retained components explicit. A construction allowance is not approval for an unreviewed structural solution.',
'Connect gate closure to purchasing and scheduling. If the design or relevant authority decision changes, revise quantities, compatible products and complete prices before confirming the order. Retain final professional and authority records required for the actual work.'
], 'A fictional design register has five gates. Three have current written evidence, one awaits site findings and one awaits a local decision.', [('Resolved gates','3'),('Site findings pending','1'),('Local decision pending','1'),('Downstream order fully ready','No')],
'The two open gates remain conditional even if a supplier has prepared a material quotation.',
['Structural / site / local questions and responsible sources','Qualified design author / reviewer / current version','Retained components / unknowns / assessment evidence','Purchasing and schedule dependencies','Gate closure / revised quantities / retained final records'],
['Technical references are not universal approvals.','No structural specification comes from this book.','Open gates limit downstream commitments.'], 'Confirm the actual design and approval basis before buying the main structural or surface package.')

chapter('Check decking quantities and purchasing units','Board counts need an approved layout and coverage basis.',[
'Ask the installer and supplier for a takeoff based on the selected product, current layout and professionally established installation requirements. Record net surface area, layout allowance, selling unit and coverage basis. Nominal board dimensions alone may not describe usable coverage.',
'Use the approved allowance explicitly, then convert to the actual selling unit. If whole units are required, round the count upward and multiply back to show the purchase basis. Keep cutting allowance and separately selected future repair stock distinct.',
'For geometry-only examples, label coverage inputs as assumptions. The arithmetic cannot determine spacing, fastening, supports, suitability or a compliant installation. Use the actual product documentation and responsible installer for those decisions.',
'Reconcile board lengths, colors, profiles, accessories and return terms on the written order. A surplus coverage number is not guaranteed useful leftover material. Ask who confirms the final takeoff and how substitutions are reviewed.'
], 'For arithmetic only, a fictional 216 sq ft surface uses an assumed 10% allowance and an invented equivalent coverage of 5.5 sq ft per whole purchasing unit.', [('216 × 1.10','237.6 sq ft equivalent'),('237.6 / 5.5','43.2 units'),('Whole units','44'),('44 × 5.5','242 sq ft equivalent')],
'The allowance and coverage are invented. They do not specify a board size, spacing or installation method.',
['Approved takeoff / product / layout / verifier','Net area / allowance / stated rationale','Selling unit / actual coverage basis / rounded count','Profiles / lengths / accessories / separate repair stock','Supplier confirmation / returns / substitution process'],
['Allowance is project-specific.','Coverage arithmetic is not installation design.','Surplus is not promised usable repair stock.'], 'Have both installer and supplier confirm the exact product and purchasing units on the order.')

chapter('Price guards, stairs and landings as complete systems','A rail material rate is not the finished edge scope.',[
'Use the professionally established edge, stair and landing schedule to identify required systems. Record exact selected products and supporting components. This book supplies no required height, spacing, stair geometry or load criterion.',
'Ask who confirms compatibility between the guard, posts, structure, stairs and relevant interfaces. A matching appearance does not establish technical suitability. Keep the product documents and qualified review with the accepted design.',
'Price supply, installation, supporting work and completion evidence as a complete package. A linear-foot rate may apply to only part of the assembly. Keep counted openings, stair groups and other distinct units separate.',
'Review changed layouts or product substitutions before ordering. A different edge product can affect structural or finishing work. Retain the complete incremental cost and required review rather than approving a material-only saving.'
], 'A fictional complete-edge scenario has $2,400 guard package, $1,800 stair package and $600 landing-related scope, confirmed non-overlapping.', [('Guard package','$2,400'),('Stair package','$1,800'),('Landing scope','$600'),('Defined edge and access total','$4,800')],
'The example does not establish required systems or compliant details. Actual design and local requirements determine scope.',
['Approved edge / stair / landing schedule','Exact products / compatible components / reviewer','Supply / install / support / completion inclusions','Linear feet / counts / separate scope units','Layout or selection changes / complete revised price'],
['Requirements come from actual qualified review.','Assembly components are included once.','Different scope units are not blended.'], 'Request a complete guard, stair and landing proposal using the current design.')

chapter('Assign the house and site interfaces','The connection belongs in both the design and the price.',[
'Identify proposed interfaces with the home, doors, walls, roof, site and retained surfaces. Ask qualified providers to establish the actual connection approach and requirements. This guide gives no ledger, flashing, anchorage, foundation or freestanding design instructions.',
'Assign responsibility for design, supply, installation, checks, weather-related interfaces and restoration. A deck and siding quote can each omit the joint between them. Keep the interface as an explicit work package with a responsible provider.',
'Record access and household-use effects during work. Ask the contractor to confirm temporary arrangements and relevant restrictions. A new door or changed access point may involve separate work beyond the deck surface.',
'Reconcile interface costs across structural, exterior and finish packages. If design changes, update dependent products and prices before procurement. Retain the final evidence and care responsibilities for the actual installed connection.'
], 'A fictional interface scope contains $900 defined connection work, $700 adjacent-finish restoration and $400 temporary access arrangements.', [('Connection scope','$900'),('Adjacent restoration','$700'),('Temporary access','$400'),('Defined interface total','$2,000')],
'The total is a teaching scenario, not a connection specification or price for a real home.',
['Current house / site / access interface records','Qualified design / responsible provider / version','Supply / install / check / restore responsibilities','Temporary access / household guidance / fixed services','Overlap reconciliation / changes / final records'],
['The interface has an accountable provider.','No owner connection method is prescribed.','Adjacent restoration is included in the scenario.'], 'Ask the relevant providers to confirm the new-to-existing interface scope together.')

chapter('Compare materials with care obligations','An initial premium is not an automatic lifetime saving.',[
'Record the exact selected products and the complete installed baseline for each alternative. Ask the responsible provider to confirm suitability for the actual design, exposure and use. A broad material category does not identify every product requirement or accessory.',
'Use current manufacturer information for installation and care responsibilities. Trex publishes product-specific resources as one manufacturer example [3]. Follow the actual selected manufacturer documents and qualified provider decisions rather than applying one brand requirement to all products.',
'Compare initial installed cost and a clearly labeled future-care scenario. Record the number of events, price per event, horizon and excluded effects. Do not assign a guaranteed life or claim that a material needs no attention without actual supporting terms.',
'Retain warranty issuer, scope, exclusions and reporting process. A warranty duration does not establish complete installed coverage or the actual cost of ownership. Keep repair options and future assumptions visible beside the initial price.'
], 'A fictional ten-year comparison has option A at $8,000 plus five assumed $400 care events, and B at $9,500 plus two assumed $200 events. No financing or time-value effects are included.', [('A: $8,000 + 5×$400','$10,000'),('B: $9,500 + 2×$200','$9,900'),('Illustrative difference','$100'),('Future events','Assumed, not predicted')],
'The close scenario result depends on invented care events. Confirm actual product obligations and test different assumptions.',
['Exact products / complete installed alternatives','Suitability reviewer / actual manufacturer documents','Care events / costs / horizon / excluded effects','Warranty issuer / scope / exclusions / reporting','Scenario sensitivity / initial premium / decision rationale'],
['Manufacturer examples are not universal requirements.','Future care is labeled assumed.','Warranty years are not lifetime-cost proof.'], 'Compare the actual installed alternatives and documented care duties before choosing on an ownership-cost claim.')

chapter('Include removal, disposal and temporary access','The existing deck can create work outside the new package.',[
'Define the existing components to remove and the retained areas to protect. Ask the contractor to establish the appropriate removal plan and relevant assessment needs. This handbook supplies no demolition, dismantling, lifting or material-handling procedure.',
'Clarify debris routes, disposal, cleanup and restoration. An old surface area does not fully describe removal complexity. Keep fixed services and access restrictions visible alongside any unit-rate work.',
'Record temporary household routes and provider use restrictions where the deck serves a doorway or circulation route. Assign protection and communication responsibilities. Do not assume a door remains safe to use while the external access is changed.',
'Reconcile removal inclusions across the replacement and site packages. A separate disposal allowance should not be added when the quoted removal price includes it. Unexpected findings should follow the agreed assessment and change process.'
], 'An invented removal proposal is $1,200 including ordinary disposal. A separate $300 temporary-access service is confirmed excluded.', [('Removal including disposal','$1,200'),('Separate temporary access','$300'),('Defined supporting total','$1,500'),('Additional disposal line','$0 in this scenario')],
'Actual materials, site conditions and provider terms establish the appropriate work and price.',
['Removed / retained components / assessment questions','Contractor removal scope / included disposal','Debris route / protection / cleanup / restoration','Temporary access / household guidance / owner','Fixed fees / package overlaps / unexpected-condition process'],
['Removal methods remain with qualified providers.','Disposal is not charged twice.','Changed access has a defined plan.'], 'Confirm removal, disposal and temporary-access inclusions before comparing replacement totals.')

chapter('Budget outdoor features and service interfaces','An attractive extra can change the complete design.',[
'List optional features such as lighting, shade, built-in furniture or other desired outdoor equipment. Give each a separate selection and decision status. An inspiration image does not establish that a feature is suitable for the actual deck.',
'Ask the appropriate qualified providers to assess structural, electrical, fuel, fire-safety, weather and other relevant requirements. This guide provides no appliance clearances, electrical work, fuel connection or load instructions.',
'Price the complete installed addition over the baseline, including supporting work, design review, access and care obligations where relevant. A retail product price can omit the services that make the feature usable.',
'Keep unapproved options outside committed cost and test their effect on reserve and funding. If a choice changes the layout or structural design, update dependent packages before authorizing procurement. Optional work should not silently displace required obligations.'
], 'A fictional optional feature has $600 product cost, $500 qualified supporting work and $100 defined restoration, none included in the baseline.', [('Product','$600'),('Supporting work','$500'),('Restoration','$100'),('Complete optional addition','$1,200')],
'The feature remains an option until assessed and approved. This example does not determine whether any particular feature is suitable.',
['Optional feature / intended use / status','Qualified design and service questions / reviewers','Product / support / restoration / care inclusions','Baseline / complete incremental price / affected packages','Approval / reserve / funding / updated design'],
['Optional features receive relevant suitability review.','Retail price is not the installed total.','Unapproved options are separate from commitments.'], 'Ask for the complete assessed feature scope before adding an optional purchase to the order.')

chapter('Plan the sequence and local review record','Ready to build and ready to use are different decisions.',[
'Create a sequence with site assessment, current design, relevant local approvals, product orders and provider-confirmed readiness. Ask the actual authority and project team what applies. This book gives no nationwide permit exemption or occupancy rule.',
'Distinguish a fee estimate, submitted application, issued approval and required completion record. Keep the documents and responsible party for each stage. A supplier delivery date does not close design or local-review gates.',
'Record weather, access and household-use decisions with the responsible provider. Keep actual product instructions and relevant restrictions available. A visually complete surface does not establish that the whole structural and access scope has been accepted.',
'Update dates and costs when prerequisites change, using the agreed change process. Retain the evidence needed for technical checks and authority records as relevant. The owner worksheet organizes the handoffs without certifying the deck.'
], 'A fictional sequence has four pre-start gates. Three have confirmed evidence and one authority-related item remains pending.', [('Pre-start gates','4'),('Confirmed evidence','3'),('Pending item','1'),('All prerequisites complete','No')],
'The pending item requires the actual responsible-source decision. A planned start date is not approval evidence.',
['Assessment / design / local-review / supply gates','Actual authority / provider / document references','Fee / submitted / issued / completion status','Weather / access / use guidance / contacts','Revised dates / costs / final checks / retained records'],
['Local requirements are verified for the actual project.','Delivery dates do not override open gates.','Use readiness has appropriate evidence.'], 'Confirm the complete pre-start and handover record with the actual project team.')

chapter('Compare a deck with another outdoor alternative','Equal area does not guarantee equal function or scope.',[
'If the household goal can be met by more than one outdoor arrangement, ask qualified providers to assess feasible options. A deck, ground-level paved area or different layout may involve different access, site and connection questions. This guide does not determine which option is technically suitable.',
'Keep the desired activities, access and retained yard uses visible in the comparison. A cheaper option may provide a different relationship to the home or require another route. Record the practical tradeoff instead of comparing only a matching surface area.',
'Use complete installed scenarios including site work, supporting services and restoration. An outdoor material price can omit the work that makes the alternative feasible. Keep professional, owner and reserve funding separate where it is outside the defined packages.',
'Retain each option as conditional until relevant site and design questions are resolved. An alternative is useful for decision-making only when its scope and limitations are understood. No cost ratio here predicts local prices or future resale value.'
], 'A fictional complete deck scope is $18,300. An alternative surface package is $13,000 but needs a separately assessed $4,000 site package. Other scope is assumed matched solely for arithmetic.', [('Deck defined scope','$18,300'),('Alternative surface','$13,000'),('Required alternative site work','$4,000'),('Complete alternative','$17,000'),('Scenario difference','$1,300')],
'The apparent $5,300 gap narrows to $1,300 after required site work. Actual usefulness and suitability still require review.',
['Household outcome / feasible alternatives / reviewers','Access / relationship to home / retained outdoor uses','Complete alternative packages / required site work','Matched scope / professional and owner additions','Conditional findings / tradeoffs / decision rationale'],
['Equal area is not assumed equal function.','Required site work enters the alternative total.','Options remain conditional until assessed.'], 'Ask for complete feasible outdoor alternatives before deciding solely on the surface package price.')

chapter('Compare complete deck and outdoor scenarios','Use the same surface, edge and access scope.',[
'Combine the current platform layout, professional decisions and selected products into a common proposal request. Include structure, surface, guards, stairs, interfaces, removal, site logistics and relevant services. Mark each required line included, excluded, allowance or unresolved.',
'Compare material, supply-only and installed prices on their stated bases. A decking-board rate does not price a complete deck. Keep surface area, edge length and counted features distinct so the comparison reflects the actual shape and scope.',
'Add professional, owner and temporary costs outside contractor prices where relevant. Reconcile overlaps and keep reserve separate from defined work. A lower headline that omits required access or guards remains incomplete until the gap is resolved.',
'Retain accepted design, actual products, changes and relevant completion evidence at handover. The planner supports owner decisions without establishing structural suitability, local compliance or a future resale return.'
], 'A fictional scenario has $10,000 structure and surface, $4,800 guards/stairs/landing, $2,000 interfaces and $1,500 removal/access, all non-overlapping.', [('Structure and surface','$10,000'),('Guards / stairs / landing','$4,800'),('Interfaces','$2,000'),('Removal and access','$1,500'),('Defined comparison scope','$18,300')],
'The $18,300 is invented defined work before any separate professional costs, owner costs, tax or reserve. It is not a deck-price benchmark.',
['Common layout / design / product / takeoff references','Structure / surface / edges / stairs / interfaces','Scope status / matching units / complete inclusions','Professional / owner / tax / reserve / overlap check','Accepted scope / care / completion records / open obligations'],
['Board prices are not labeled complete deck prices.','Area, length and counts remain distinct.','Funding additions are separate from defined work.'], 'Compare complete matched proposals before choosing by the price per square foot of decking.')

method(2,'Build the all-in deck project budget')
method(5,'Normalize contractor proposals')
method(6,'Review the live cost forecast')
method(17,'Approve changes and reconcile the reserve')
method(18,'Close out and retain project records')
SOURCES=[('1','FTC: Home Repair Scams','https://consumer.ftc.gov/features/pass-it-on/home-repair-scams'),('2','American Wood Council: Design for Code Acceptance resources','https://awc.org/collection/design-for-code-acceptance/'),('3','Trex: Product installation resources','https://www.trex.com/build-your-deck/diy/how-to/')]

STORE=dict(slug='deck-outdoor-living-cost-planner',title='Deck Building Cost Guide',category='Decks & Outdoor Living',amount=1099,route='/api/download-deck-guide',number=15,test='scripts/test_deck_delivery.mjs',
description='A 64-page deck planning guide with 19 worked examples and 19 fillable worksheets. Compare complete surface, structural, edge, stair, access and outdoor-alternative scenarios.',
eyebrow='A board price is only part of a deck',why_title='Why buy this deck planning guide?',why='Equal surface area can involve different edges, stairs, interfaces and supporting work. This guide helps you compare the complete assessed project rather than a decking-material headline.',
benefits=[('Check the quantity basis.','Separate platform area, perimeter, edges, stairs and actual purchasing units.'),('Expose missing systems.','Keep retained-structure assessment, guards, connections, removal and access visible.'),('Compare complete alternatives.','Use installed scope, care assumptions, optional features and feasible outdoor scenarios.')],
reader='U.S. homeowners planning a deck, assessing resurfacing versus replacement or comparing outdoor options. Qualified providers and the actual local authority must establish suitability, design and applicable requirements.',
difference_title='What does the paid guide add to a calculator?',difference='It connects area and quantity arithmetic to a complete owner scope record, with 19 worked cases, 19 reusable worksheets and 95 fillable fields.',
limits='One-time purchase. No subscription. Example costs, coverage and care events are hypothetical. No structural suitability, local approval, useful life or saving is promised.',
helps=['Map layout, site and intended outdoor use','Compare assessed repair, resurfacing and replacement options','Separate surface, edge, stair and purchasing quantities','Coordinate structure, interfaces, access and optional features','Compare complete installed and care scenarios'],
sequence='outdoor use, existing-deck alternatives, quantity records, professional gates, product purchasing, complete systems, outdoor alternatives and closeout',
example='Two fictional platforms each have 144 sq ft of surface: 12 × 12 ft has 48 ft of perimeter, while 6 × 24 ft has 60 ft. The 12 ft difference can change edge-related scope. Perimeter alone does not establish required guard length or design.',
calculator_html='<p>Use the free <a href="/calculators/">HomeCostEngine calculators</a> for individual quantity checks and the <a href="/calculators/contractor-quote-comparison">quote comparison calculator</a> with complete proposals. Retain the actual layout and edge schedule.</p>',
examples='Work through retained-component scope, equal-area different-perimeter layouts, whole-unit rounding, complete guard/stair systems, connection costs, care scenarios, removal inclusions, optional features and outdoor alternatives. Six general owner-budget chapters use the HomeCostEngine renovation method with deck adaptation; thirteen chapters add deck decisions. No structural, connection, guard, stair or installation specification is supplied.')
PDF_META=dict(key='deck',subject='Original deck owner planning guide and 19 fillable worksheets',header='DECK & OUTDOOR PLANNING',cover_title='Deck Building<br/>Cost Guide',cover_lines=['Check the surface. Include the whole system.','Compare the complete outdoor project.'],
preface=['A deck purchase connects the site, structure, surface, guards, stairs and interfaces with the home. This guide helps you check the owner quantities and complete scope without treating a board price as the whole project.',
'Start with the brief, intended use and existing site. Compare assessed repair, resurfacing and replacement alternatives, then separate area, perimeter and purchasing units. Connect professional gates, selected products, complete systems, logistics and outdoor alternatives.',
'Each working chapter contains an explanation, an original hypothetical case and a reusable sheet. Six general owner-budget chapters use the HomeCostEngine renovation method with deck adaptation. Thirteen chapters add deck and outdoor-scope decisions.',
'All costs, coverage inputs and future-care events are invented USD teaching assumptions, not local prices or product requirements. Area and perimeter describe different quantities. Purchasing arithmetic does not determine spacing, structure or installation.',
'Qualified providers and the actual authority must establish site suitability, design, relevant requirements and completion evidence. Technical and manufacturer resources retain their own scope and limitations. Keep accepted documents, actual products, changes, invoices and care records with the sheets.'],
workflow=['Record outdoor use, layouts, existing conditions and the spending boundary.','Collect qualified findings, current dimensions, edge schedules and approved takeoffs.','Match complete structure, surface, guards, stairs, interfaces and logistics.','Track accepted scope, purchasing assumptions, payments, obligations and approved changes.','Reconcile final scope and credits. Retain relevant checks, actual product and care records.'],
afterword='A useful deck plan connects the intended outdoor use to actual qualified findings, complete system scope and realistic funding. Keep surface area separate from edges and counted features, resolve retained-component and design questions, and retain the records behind the accepted project.')

