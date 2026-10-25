"""Original window and door replacement planning cases, with established owner-budget methods."""
from pathlib import Path
import runpy,copy
base=runpy.run_path(str(Path(__file__).with_name('renovation-blueprint.py')))
CHAPTERS=[]
def chapter(title,deck,paragraphs,example,rows,conclusion,prompts,checks,task):
    CHAPTERS.append(dict(title=title,deck=deck,paragraphs=paragraphs,example=example,rows=rows,conclusion=conclusion,prompts=prompts,checks=checks,task=task))
def method(index,title):
    c=copy.deepcopy(base['CHAPTERS'][index]);c['title']=title
    replacements={'renovation':'window and door project','Make the kitchen usable for two cooks':'Improve the selected openings for household use','buy new cabinets':'order replacement windows','A bathroom project in a one-bath home has a different temporary-use problem from the same work in an empty property.':'Replacing the only entrance creates different temporary-use needs from replacing a window in an unused room.','fixture allowance':'finish-selection allowance'}
    def adapt(s):
        for a,b in replacements.items():s=s.replace(a,b)
        return s
    for k in ['deck','example','conclusion','task']:c[k]=adapt(c[k])
    for k in ['paragraphs','prompts','checks']:c[k]=[adapt(x) for x in c[k]]
    CHAPTERS.append(c)

method(0,'Define the window and door replacement brief')
chapter('Create an opening-by-opening inventory','A window count does not describe the complete order.',[
'Assign an ID to every selected opening and record its room, location and current type from accessible observations. Keep windows, exterior doors, grouped units and retained openings distinct. A three-part assembly may not be priced as three independently installed openings.',
'Record the observed concern and desired result: operation, comfort, water-related symptoms, appearance, access or another household need. An observation does not diagnose the frame, glass, wall or installation. Ask qualified providers to assess relevant causes.',
'Link photographs, prior invoices, warranty records and existing product labels where safely available. Mark unknown details rather than guessing. Do not remove trim, glass or hardware or use hazardous access to complete the inventory.',
'Use the same IDs for assessment, measurements, selections, quotations, delivery and handover. If an opening is added or removed, update every dependent record. A count-only total can hide differences in size, operation and installation scope.'
], 'A fictional inventory has eight window openings, one exterior door and one grouped assembly retained unchanged.', [('Window openings selected','8'),('Exterior door selected','1'),('Retained grouped assembly','1'),('Selected opening count','9')],
'The retained assembly is not part of the selected order. Product units and installation openings still need their own definitions.',
['Opening ID / room / current type / retained status','Observed concern / desired outcome / date','Accessible photos / labels / prior records','Assessment questions / qualified reviewer','Common IDs for measure / quote / delivery / closeout'],
['Openings and product units are distinguished.','Observations are not diagnoses.','Retained items are excluded explicitly.'], 'Prepare one opening schedule and use it for every bidder and supplier.')

chapter('Compare repair and replacement alternatives','The right scope depends on assessed condition.',[
'Ask the responsible provider to explain the condition and feasible options for each opening. Keep a defined repair, limited component replacement and complete replacement separate. A glass-only price may not address frame condition or a wall-interface concern.',
'State what each alternative changes and retains. Record any unresolved cause, limitation or further assessment. Do not assign an invented future life to the repaired opening or assume a new product automatically resolves the observed symptom.',
'Compare the same desired outcome and complete supporting work. Access, protection, decoration and any relevant assessment can affect both options. A lower immediate total is one part of the decision, not proof of suitability.',
'Retain professional guidance about operation, condition or urgency. This planner provides no glazing, hardware repair, diagnostic or removal procedure. Use qualified findings and the actual scope before deciding what to purchase.'
], 'A fictional assessed repair is $250. A complete replacement alternative is $900 including the defined supporting work. Future energy, repairs and useful life are not modeled.', [('Defined repair','$250'),('Complete replacement','$900'),('Immediate difference','$650'),('Future lifetime cost','Not established')],
'The $650 gap does not establish which option is appropriate. Compare the actual findings and outcomes.',
['Opening / condition finding / provider / evidence','Repair / limited component / full replacement scope','Retained elements / unresolved cause / limitations','Matched supporting work / complete immediate costs','Urgent guidance / decision rationale / approved option'],
['Glass-only scope is not assumed complete.','Useful life and savings are not invented.','Provider findings remain attached to the choice.'], 'Request a written explanation of what each assessed option fixes and leaves unchanged.')

chapter('Separate owner dimensions from the final order','A geometric area check is not an ordering measurement.',[
'Record owner dimensions only as clearly labeled discussion inputs, using consistent units and the opening IDs. Ask the installer or supplier to define and verify the actual ordering dimensions and responsibility. Do not infer a product order size from an approximate visible opening.',
'Keep different measurement references distinct, including product size, opening size and any professional installation allowance. This handbook supplies no measurement procedure or universal adjustment. Use the exact selected product and responsible provider confirmation.',
'For arithmetic, inches can be converted to feet before multiplying area. The result can help compare a quantity record, but it cannot establish fit, suitability or installation requirements. Retain the original units and source.',
'Require a written final measure and order approval process, including how errors and substitutions are handled. Connect the confirmed dimensions to the exact selected model, operation and opening ID. A paid deposit is not evidence that the measurement is correct.'
], 'A fictional rectangle of 36 × 60 inches has geometric area 15 sq ft: 36 × 60 / 144. The dimensions are not an order specification.', [('36 × 60','2,160 square inches'),('2,160 / 144','15 sq ft'),('Final order dimensions','Provider verification required'),('Fit established by arithmetic','No')],
'The area calculation cannot tell the supplier which product size to manufacture.',
['Opening ID / owner dimension / unit / source','Provider-defined measurement reference','Exact product / operation / confirmed order dimensions','Geometric area check / limitations','Final measure approval / error and substitution process'],
['Approximate dimensions remain labeled.','Area arithmetic is separate from ordering.','Final measurement has an accountable provider.'], 'Obtain the written final measure and product match before approving a custom order.')

chapter('Compare retained-frame and full-frame scope','Installation approaches can have different boundaries.',[
'Ask the installer to explain the proposed replacement approach and which existing frame or surrounding elements remain. Terms used in sales material may not fully describe the actual work. Keep the assessed condition and proposed boundary with the opening schedule.',
'Record the consequences for visible opening, adjacent finishes, wall interfaces and restoration as determined by the provider. This book gives no frame removal, flashing, anchoring or installation procedure. A choice should follow the actual assessed opening and product requirements.',
'Compare complete installed alternatives with the same selected outcome. A product-only difference can omit work that changes the final total. Identify retained elements, exclusions and unresolved condition questions before ranking prices.',
'Assign responsibility for any additional findings after removal and the approval process for changed scope. An approach that retains components should not be described as correcting unknown concealed conditions. Keep those limits explicit in the accepted proposal.'
], 'A fictional limited-boundary option is $700 per opening, with $150 separately required restoration. A matched broader-boundary option is $950 installed.', [('Limited option','$700'),('Required restoration','$150'),('Complete limited scenario','$850'),('Broader installed option','$950'),('Scenario difference','$100')],
'Neither approach is recommended by this arithmetic. Actual condition and professional scope establish suitability.',
['Assessed opening / proposed approach / retained elements','Product requirements / qualified responsibility','Visible result / wall interfaces / restoration','Matched installed alternatives / exclusions / totals','Concealed-condition review / change approval terms'],
['Sales terms are translated into actual boundaries.','Retained components have explicit limits.','Supporting restoration is included.'], 'Ask the installer to show the complete boundary and exclusions for each proposed approach.')

chapter('Specify operation, frame and exact product options','A brand name is not the complete selection.',[
'Record exact manufacturer, series, product code, operating type, color, dimensions and relevant options for each opening. Link the approved selection to the final provider measure. A similar appearance can conceal different construction, operation or included accessories.',
'Discuss household use, cleaning access, screens, privacy and hardware needs with the provider. Keep technical suitability, local requirements and any special use condition under qualified review. The owner should understand the selected features without using the book as a design approval.',
'Compare proposals using the same current specification or mark alternatives explicitly. An upgrade should state the incremental complete installed cost over the accepted baseline, including any supporting changes. Do not accept a cheaper unspecified substitute as equivalent.',
'Set a selection deadline and written substitution process. Review the product and opening schedule together before the order is confirmed. Save actual labels and order details for warranty and handover.'
], 'A fictional order has six standard selections at $500 each and two different-operation selections at $650 each, all supply only.', [('6 × $500','$3,000'),('2 × $650','$1,300'),('Product supply total','$4,300'),('Installation and supporting work','Excluded')],
'The $4,300 is not the installed project price. Exact selections and supply terms are teaching assumptions.',
['Opening / exact series / code / operation / options','Final measure / approved appearance / technical reviewer','Screens / hardware / household-use requirements','Matched specification / alternatives / incremental cost','Selection deadline / substitution approval / retained labels'],
['The exact selected product is identified.','Supply-only totals remain labeled.','Substitutions require review.'], 'Approve one exact product schedule covering every selected opening before procurement.')

chapter('Read energy ratings as separate measures','One low number does not describe every performance question.',[
'NFRC consumer information distinguishes whole-product energy ratings such as U-factor, solar heat gain coefficient and visible transmittance [2]. Record the actual rated product and options rather than relying on a generic glass description.',
'Lower U-factor indicates lower rated heat transfer. Solar heat gain coefficient describes admitted solar heat, while visible transmittance describes admitted visible light. These measures answer different questions; a lower value is not a universal best choice for every metric and location.',
'Ask the qualified provider to explain suitability for the actual climate, orientation and household goals, using current relevant requirements. A label comparison does not assess the entire installed opening or predict the household energy bill.',
'Keep ratings, complete installed price and other outcomes separate in the decision record. Do not average unlike ratings into an invented performance score or convert a rating difference directly into a guaranteed percentage saving.'
], 'Two fictional products have U-factors 0.30 and 0.25, with SHGC values 0.20 and 0.35 respectively. No household energy model has been performed.', [('Product A: U / SHGC','0.30 / 0.20'),('Product B: U / SHGC','0.25 / 0.35'),('Lower rated heat transfer','B on U-factor alone'),('Lower admitted solar heat','A on SHGC alone'),('Better actual selection','Requires project-specific review')],
'The example shows a tradeoff between different measures. It does not rank actual products or calculate savings.',
['Exact rated product / options / label reference','U-factor / SHGC / VT / relevant other data','Climate / orientation / household goals / reviewer','Installed scope / price / other outcome tradeoffs','No direct rating-to-bill saving assumption'],
['Ratings describe the actual selected product.','Unlike measures are not combined into a score.','Bill savings are not inferred from a label difference.'], 'Ask the provider to explain the actual label tradeoffs for each proposed product and opening.')

chapter('Review glass and special-use requirements','Appearance choices can carry technical questions.',[
'List proposed glazing options and the reason for each, including privacy, light, acoustic or other household goals. Ask qualified providers and the relevant authority to establish any safety, escape, impact or other requirements for the actual location and use.',
'Keep exact product references and evidence separate from broad marketing terms. A glazing option with a stated benefit does not automatically satisfy every relevant requirement. This book supplies no glass specification, rating threshold or compliant opening dimension.',
'Compare the complete incremental installed cost and any effect on operation, weight, hardware or other supporting scope as assessed by the provider. Do not assume that changing glass leaves every other product or installation decision unchanged.',
'Retain the approved selection and relevant technical documents with the opening schedule. If an option changes before manufacture, obtain the updated provider review and price before confirming the order.'
], 'A fictional privacy option adds $80 per selected unit across three units, with a separately confirmed $60 supporting change.', [('3 × $80','$240'),('Supporting change','$60'),('Complete incremental option','$300'),('Technical suitability','Requires actual review')],
'The $300 is an invented change scenario, not a specification or standard upgrade price.',
['Glazing goal / opening / exact option reference','Qualified and local special-use questions','Supporting technical evidence / approved selection','Incremental product / install / support cost','Order revision / provider review / retained documents'],
['Marketing terms are not approval evidence.','Special requirements use actual qualified review.','Complete option cost includes dependent work.'], 'Resolve location-specific glazing questions before approving a final custom product specification.')

chapter('Include door hardware and access scope','A door slab price is not a complete entrance.',[
'For selected doors, record the exact unit, operation, hardware, threshold and surrounding scope in the provider proposal. Clarify which existing elements remain and which are replaced. A slab-only supply price can differ substantially from a complete installed entrance.',
'Ask qualified providers to review relevant access, security, weather and local requirements. This guide does not specify locks, fire ratings, thresholds, clearances or technical installation methods. Keep the actual suitability and product documents with the selection.',
'Identify any separate finishing, electrical or control-related interface. Assign supply, installation, programming where applicable, checks and restoration. A decorative hardware allowance may exclude other parts needed for the complete accepted result.',
'Plan household access during the change and request the operating, care and warranty handover. Keep secure credentials or access codes outside a general contractor comparison sheet. The owner record needs responsibility and evidence, not sensitive entry information.'
], 'An invented entrance scenario has $700 unit supply, $180 hardware, $500 installation and $120 restoration, all non-overlapping.', [('Door unit','$700'),('Hardware','$180'),('Installation','$500'),('Restoration','$120'),('Defined entrance scope','$1,500')],
'The $700 unit is less than half of this defined installed scenario. Actual selections and requirements establish scope.',
['Exact door unit / retained frame / operating selection','Hardware / threshold / access / technical reviewer','Supply / installation / controls / finishing owners','Temporary entry / privacy and credential boundary','Operating checks / care / warranty / handover evidence'],
['Slab or unit supply is distinguished from an entrance.','Credentials stay out of shared worksheets.','Household access has a provider-confirmed plan.'], 'Ask for the complete entrance and hardware scope before comparing door-unit prices.')

chapter('Assign weather, air and finish interfaces','The wall connection belongs in the installed proposal.',[
'Ask the responsible installer to explain the complete opening-to-wall scope and relevant product requirements. Record who establishes the actual weather, air and adjacent-finish details. This handbook provides no sealing, flashing, anchoring or waterproofing procedure.',
'Assign responsibility for preparation, installation, checks, exterior and interior restoration. A window supplier and a separate finish contractor can each exclude the interface. Keep the task and accountable provider visible before accepting either price.',
'Clarify concealed-condition assessment and change terms. A quoted standard installation may not include correction of every hidden wall issue. Record what evidence triggers review and how additional work is approved.',
'Keep the accepted boundary, actual products and completion evidence in the owner file. A high product rating does not prove that every installation interface was completed correctly. Discuss any observed concern with the responsible qualified provider.'
], 'A fictional eight-opening installation has $2,400 defined base work and $600 separately agreed finish restoration. No concealed repair scope is included.', [('Base installation scope','$2,400'),('Separate finish restoration','$600'),('Defined installed-work subtotal','$3,000'),('Concealed-condition repair','Excluded / subject to assessment')],
'The example labels the boundary instead of implying that a standard install charge covers every wall condition.',
['Opening-to-wall scope / product references / designer','Preparation / install / check / restore owners','Interior and exterior finish boundaries','Concealed conditions / evidence / approval process','Actual completion record / observations / follow-up'],
['The wall interface has an accountable owner.','Hidden-condition limits are explicit.','Product ratings are not installation certificates.'], 'Ask for written interface and restoration inclusions with the installation proposal.')

chapter('Resolve removal and older-material questions','Assessment comes before disturbance.',[
'Record the existing opening materials, age-related records and prior assessments available to the owner. Ask qualified providers to identify relevant pre-disturbance questions. An appearance or a past paint color does not establish material safety.',
'EPA renovation resources address lead-related concerns in relevant older properties [3]. Have appropriately qualified providers determine the actual requirements and scope. This book provides no testing, scraping, cutting, removal or cleanup procedure.',
'Separate ordinary removal, any assessed specialist work and disposal or restoration responsibilities. A replacement price may exclude specialist services. Keep unresolved items as decision gates rather than assuming they cost zero.',
'Assign protection, household communication, waste handling and required completion records to the appropriate providers. Coordinate those responsibilities with the actual installation sequence and retain the evidence relevant to the work.'
], 'A fictional ordinary removal package is $400 with $100 separate disposal, expressly excluding any unresolved specialist scope.', [('Ordinary removal','$400'),('Separate disposal','$100'),('Defined ordinary scope','$500'),('Specialist work','Not established')],
'The $500 does not price or authorize hazardous-material work. Actual assessments determine any additional scope.',
['Existing materials / records / prior assessment','Qualified pre-disturbance questions / actual requirements','Ordinary versus specialist scope / exclusions','Protection / disposal / restoration / provider roles','Open gates / completion evidence / sequence'],
['Appearance is not treated as material clearance.','Specialist work is not assumed inside ordinary removal.','Assessment precedes relevant disturbance.'], 'Resolve older-material questions and scope responsibilities before confirming removal dates.')

chapter('Coordinate custom orders, delivery and installation','A manufacturing lead time is only part of the sequence.',[
'Record final measure, product approval, order confirmation and supplier terms as separate gates. Custom-made products may have specific change and return limitations; use the actual written terms instead of assuming a standard cancellation right.',
'Confirm who receives the units and checks opening IDs, product labels, counts and visible condition before installation. Retain the order and delivery record. An unchecked delivery should not be treated as proof that every selected unit is correct.',
'Map lead time, site readiness, household access and provider availability together. If a prerequisite changes, revise the sequence and relevant cost using agreed terms. Do not assume a new opening can be left exposed to preserve a calendar promise.',
'Assign shortage, damage and wrong-product decisions to the relevant supplier and installer. Keep the owner informed without authorizing an unreviewed substitute. Retain approved changes and the final actual product record.'
], 'A fictional delivery expects nine selected units. Eight match the order record and one has an unresolved specification discrepancy.', [('Units expected','9'),('Matched on receipt','8'),('Discrepancy pending','1'),('Full delivery acceptance','Pending review')],
'A complete count does not mean a complete specification match. Resolve the discrepancy before relying on the affected unit.',
['Final measure / product approval / order gates','Current supplier terms / changes / returns / lead time','Receiving owner / count / label / condition record','Site and household readiness / installation availability','Discrepancies / supplier decision / approved substitutions'],
['Custom-order terms are retained.','Count and specification checks are distinct.','Substitutions require appropriate review.'], 'Agree on the delivery inspection and discrepancy process before the custom order arrives.')

chapter('Keep warranties, operation and care records','The actual installed labels support later service.',[
'Collect the actual product labels, supplier documents and installer warranty terms by opening ID. Distinguish product coverage from installation obligations. A long warranty period does not prove that every supporting cost or condition is included.',
'Ask the provider to demonstrate the agreed operation and explain care and reporting instructions for the actual products. Record observed concerns and relevant qualified checks. This book supplies no adjustment, repair or cleaning procedure.',
'Keep a location-based punch list with a responsible provider and follow-up date. Save completion evidence and relevant technical or authority records where required. An owner visual review does not replace those actual checks.',
'Reconcile changes, returned material and confirmed credits before archiving the final cost. A requested credit is not yet money recovered. Update the opening schedule to describe the installed products rather than the initial sales selection.'
], 'A fictional accepted scope is $8,000 with a $300 approved option and a confirmed $100 credit. Paid amounts total $7,000.', [('Accepted scope plus option','$8,300'),('Confirmed credit','−$100'),('Reconciled defined cost','$8,200'),('Paid / unpaid','$7,000 / $1,200')],
'The $1,200 remains an obligation under this narrow example. Actual payment and completion terms require their own review.',
['Actual opening labels / supplier and installer warranties','Operation / care / reporting contacts / provider evidence','Punch list / location / responsible owner / dates','Accepted scope / changes / confirmed credits / payments','Final schedule / technical records / archived owner file'],
['Product and installation warranties are separate.','The record matches actual installed units.','Only confirmed credits reduce the forecast.'], 'Save the opening-by-opening handover and reconcile all confirmed costs and obligations.')

chapter('Compare the complete opening replacement proposal','Product quality and installation scope need separate evidence.',[
'Give bidders the same current opening schedule, desired outcomes and selected specification. Compare exact products, retained elements, installation approach, removal, interfaces, restoration, access and completion records. Mark included, excluded, allowance and unresolved lines.',
'Retain each quantity and unit basis. A per-unit price can hide different openings or grouping, while a product-area rate may exclude labor. Normalize only matched scope and keep unresolved costs visible.',
'Add professional, owner and temporary costs outside contractor totals where relevant, then keep reserve separate. Compare rating tradeoffs and other household outcomes alongside complete installed prices. No label difference alone establishes a household saving.',
'Retain the accepted measure, order, scope and written change process. The guide supports owner planning without certifying fit, structural suitability, local compliance or future performance. Use actual qualified evidence for those decisions.'
], 'A fictional window project has $4,300 supply, $3,000 installation/restoration and $500 ordinary removal/disposal, confirmed non-overlapping.', [('Selected product supply','$4,300'),('Install and restoration','$3,000'),('Ordinary removal/disposal','$500'),('Defined comparison scope','$7,800')],
'The $7,800 excludes separate door scope, unresolved specialist work, owner costs, tax and reserve unless added explicitly. It is not a local price benchmark.',
['Common opening schedule / measure / exact specification','Approach / retained elements / interface and removal scope','Quantity and rate units / inclusions / unresolved lines','Complete price / ratings / owner costs / reserve','Accepted order / changes / actual handover evidence'],
['Exact products and boundaries match across bids.','Supply-only and installed totals stay distinct.','Excluded required work remains an open decision.'], 'Resolve opening-specific scope gaps before ranking the complete installed proposals.')

method(2,'Build the all-in window and door budget')
method(5,'Normalize contractor proposals')
method(6,'Review the live cost forecast')
method(17,'Approve changes and reconcile the reserve')
method(18,'Close out and retain project records')
SOURCES=[('1','FTC: Home Repair Scams','https://consumer.ftc.gov/features/pass-it-on/home-repair-scams'),('2','NFRC Consumer Guide: Window Ratings','https://efficientwindows.org/window-ratings/'),('3','EPA: Lead Renovation, Repair and Painting','https://www.epa.gov/lead/lead-renovation-repair-and-painting-program')]

STORE=dict(slug='window-door-replacement-buyers-guide',title='Window Replacement Cost Guide',category='Windows & Doors',amount=999,route='/api/download-window-guide',number=16,test='scripts/test_window_delivery.mjs',
description='A 64-page window and door planning guide with 19 worked examples and 19 fillable worksheets. Organize openings, final measures, product ratings, installation boundaries and complete proposals.',
eyebrow='Compare the complete installed opening',why_title='Why buy this window replacement guide?',why='A product price and energy label do not describe the entire replacement project. This guide connects each opening to the final measure, selected product, installation approach and supporting work.',
benefits=[('Keep the order traceable.','Use opening IDs, exact selections and provider-confirmed final measurements.'),('Compare the real installed scope.','Record retained frames, removal, wall interfaces, restoration and door hardware.'),('Read the evidence clearly.','Keep rating tradeoffs, actual warranty terms and household outcomes separate from savings assumptions.')],
reader='U.S. homeowners planning window replacement and related door work, checking custom orders or comparing complete installation proposals. Actual providers must establish fit, product suitability and relevant requirements.',
difference_title='What does the paid guide add to a calculator?',difference='It connects quantity and cost arithmetic to opening-by-opening purchasing, scope and handover records, with 19 worked cases, 19 worksheets and 95 fillable fields.',
limits='One-time purchase. No subscription. Example prices, dimensions and ratings are hypothetical. No fit, local approval, product performance or bill saving is promised.',
helps=['Create one inventory for selected and retained openings','Compare assessed repair and replacement boundaries','Separate owner dimensions from final ordering measures','Read exact product selections and rating tradeoffs','Include removal, interfaces, installation and care records'],
sequence='opening inventories, assessed alternatives, final measurement, replacement approaches, selections, ratings, installation scope, delivery and handover',
example='A fictional product with U-factor 0.25 has lower rated heat transfer than one at 0.30. If its SHGC is 0.35 instead of 0.20, it also has higher rated solar heat admission. These separate measures need a project-specific review; they cannot be averaged into a universal score or guaranteed bill saving.',
calculator_html='<p>Use the free <a href="/calculators/contractor-quote-comparison">quote comparison calculator</a> with complete matched proposals. The guide adds final-measure, product, interface and handover records around the totals.</p>',
examples='Work through opening counts, repair options, inch-to-area conversion, complete frame-approach costs, exact product supply, rating tradeoffs, glazing options, door hardware, installation boundaries, ordinary removal and final credits. Six general owner-budget chapters use the HomeCostEngine renovation method with window/door adaptation; thirteen chapters add opening-specific decisions. No measuring, removal, glazing or installation procedure is supplied.')
PDF_META=dict(key='window',subject='Original window and door owner planning guide and 19 fillable worksheets',header='WINDOW & DOOR PLANNING',cover_title='Window Replacement<br/>Cost Guide',cover_lines=['Identify the openings. Confirm the final order.','Compare complete products and installation.'],
preface=['Window and door replacement connects each opening to a selected product and an installed scope. This guide helps you organize that record without treating a supply price, owner dimension or energy label as the whole project.',
'Start with the brief and opening inventory. Compare assessed options, clarify final measurement responsibility and replacement boundaries, then connect exact selections, rating tradeoffs, glazing questions, doors, interfaces, removal and delivery.',
'Each working chapter contains an explanation, an original hypothetical case and a reusable sheet. Six general owner-budget chapters use the HomeCostEngine renovation method with window and door adaptation. Thirteen chapters add opening-specific purchasing and scope decisions.',
'All costs, dimensions and example ratings are invented USD teaching inputs, not local prices or order specifications. U-factor, solar heat admission and light transmission answer different questions. Label differences do not directly predict household bill savings.',
'Qualified providers and the relevant authority must establish final measures, fit, suitability, actual requirements and completion evidence. This book supplies no measuring, removal, glazing or installation procedure. Keep final orders, labels, accepted scope, changes and warranty records with the sheets.'],
workflow=['Record selected openings, observed concerns, desired outcomes and funding limits.','Collect actual product information, assessed findings and provider-confirmed final measures.','Match exact products, replacement boundaries, installation and restoration scope.','Track approved orders, allowances, paid costs, unpaid obligations and written changes.','Reconcile final costs. Save actual opening labels, operation, care and warranty records.'],
afterword='A useful replacement plan connects every opening to its final verified measure, actual selected product and complete installed scope. Keep energy measures separate, retain the exact order and interface responsibilities, and use qualified evidence for fit, suitability and completion decisions.')

