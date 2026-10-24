"""Original painting budget and quote cases, with established owner-budget methods."""
from pathlib import Path
import runpy,copy
base=runpy.run_path(str(Path(__file__).with_name('renovation-blueprint.py')))
CHAPTERS=[]
def chapter(title,deck,paragraphs,example,rows,conclusion,prompts,checks,task):
    CHAPTERS.append(dict(title=title,deck=deck,paragraphs=paragraphs,example=example,rows=rows,conclusion=conclusion,prompts=prompts,checks=checks,task=task))
def method(index,title):
    c=copy.deepcopy(base['CHAPTERS'][index]);c['title']=title
    replacements={'renovation':'painting project','Make the kitchen usable for two cooks':'Refresh the occupied rooms with an agreed finish','buy new cabinets':'buy paint','A bathroom project in a one-bath home has a different temporary-use problem from the same work in an empty property.':'Painting every occupied bedroom creates different temporary-use needs from painting a vacant room.','fixture allowance':'finish-selection allowance'}
    def adapt(s):
        for a,b in replacements.items():s=s.replace(a,b)
        return s
    for k in ['deck','example','conclusion','task']:c[k]=adapt(c[k])
    for k in ['paragraphs','prompts','checks']:c[k]=[adapt(x) for x in c[k]]
    CHAPTERS.append(c)

method(0,'Define the painting project brief')
chapter('Create a room and surface schedule','A room name does not describe everything to be painted.',[
'Assign an ID to each room or exterior area and list the surfaces included: walls, ceilings, trim, doors or other agreed elements. Record both sides of a door where relevant and state whether closets and inside cupboard surfaces are included. Mark the boundaries of retained finishes rather than relying on an informal whole-room description.',
'Separate existing condition, selected appearance and contracted preparation. A photograph can record an observation but does not establish the cause of staining, cracking or peeling. Refer condition questions to the responsible provider and retain any assessment before agreeing how the affected surface enters the scope.',
'Connect every surface to its proposed product, color, finish and extent of work. A ceiling-only refresh and a full room with trim are different projects even when they share the same floor area. Use the schedule to make inclusions visible before asking for a total price.',
'Revise the schedule when a color, boundary or room changes. Give the updated version to everyone pricing or supplying the work. Keep furniture moving, protection, return-to-use and owner tasks with the room record so the desired result and household needs remain connected.'
], 'A fictional room has four wall IDs, one ceiling ID, one trim group and one door group. A closet is explicitly excluded rather than silently assumed included.', [('Walls','4 surface IDs'),('Ceiling','1 surface ID'),('Trim and door groups','2 IDs'),('Included schedule','7 IDs')],
'A surface count is a scope index. It does not establish paint quantity, preparation need or labor time.',
['Room or area IDs / dated photos / boundaries','Walls / ceilings / trim / doors / explicit exclusions','Condition observations / assessment references','Color / finish / product selection status','Protection / furniture / occupied-use requirements'],
['Closets and doors have explicit scope.','Condition observations are not diagnoses.','All bidders receive the same schedule.'], 'Create one surface schedule and resolve unclear inclusions before comparing painting totals.')

chapter('Calculate wall area and opening deductions','Floor area is not the area of the walls.',[
'For a simple rectangular room of uniform height, add the wall lengths to obtain the perimeter, then multiply by the wall height. A room floor measuring twelve by ten feet has a perimeter of forty-four feet, not an area of forty-four square feet. Label every dimension and result with its unit.',
'For sloped ceilings, varying heights or irregular walls, calculate separately measured sections. Do not use an average height without recording how it was established. Ask the painter to verify the actual takeoff and confirm the boundary between walls, trim and other surfaces.',
'Deduct openings only on a clearly stated basis. If a door or window area is removed from wall paint quantity, any painting of that element belongs on a separate surface line. A painter may use a different labor-pricing convention because cutting-in work remains; quantity arithmetic and labor rates need not share the same basis.',
'Keep gross area, opening deductions and net paintable area visible. Rounding a room dimension early can create a larger quantity error across multiple coats. Save the original measurements and the approved version rather than hiding deductions inside a single total.'
], 'A hypothetical 12 × 10 ft rectangular room has 8 ft-high walls. One opening is 3 × 7 ft and another is 4 × 3 ft, both excluded from wall coating area.', [('Perimeter: 2 × (12 + 10)','44 ft'),('Gross wall area: 44 × 8','352 sq ft'),('Openings: 21 + 12','33 sq ft'),('Net wall area','319 sq ft')],
'The 319 sq ft is the wall area for one coat. The ceiling, trim and opening surfaces are not included in it.',
['Room geometry / verified wall lengths / heights','Gross wall area / sections / units','Measured opening deductions / agreed basis','Separate door / trim / window scope','Net wall area / revision / painter confirmation'],
['Wall area is distinct from floor area.','Deductions do not erase separate painted surfaces.','Labor quantity conventions are recorded.'], 'Check one room by individual wall areas and reconcile it with the perimeter method.')

chapter('Separate ceilings, doors and trim quantities','Different surfaces need different measurement records.',[
'Measure ceiling area separately from wall area. A level rectangular ceiling uses length times width; a sloping or irregular ceiling needs its own confirmed measurement basis. State whether beams, soffits and other features belong in the same scope or require separate surface IDs.',
'Count doors and identify which faces and edges are included. Record trim in a clearly defined unit, such as a measured length or a counted component group, matching the quote. Do not multiply a trim length by an unrelated wall-paint coverage rate and assume the result prices the work.',
'Keep products and finishes distinct where they differ. A wall coating may not be the specified product for a door or other surface. Ask the painter to identify the applicable preparation and coating system for each group rather than buying one quantity of an unspecified paint.',
'Normalize bids only after their units and scope are understood. An each-door rate cannot be compared directly with a square-foot wall rate. A package price is still useful when its included surfaces, preparation and finish criteria are clear.'
], 'An invented room schedule has a 12 × 10 ft level ceiling, two doors painted on both faces and 44 linear ft of separately priced base trim.', [('Ceiling area','120 sq ft'),('Door count','2 doors'),('Included door faces','4 faces'),('Base trim length','44 linear ft')],
'These are different units and cannot be added into one paintable-area total without additional defined surface measurements.',
['Ceiling geometry / beams / separate features','Door count / included faces and edges','Trim lengths or groups / matching quote units','Product and finish per surface group','Separate labor bases / package inclusions'],
['Unlike units have not been added.','Door-face scope is explicit.','Each surface has its own product basis.'], 'Ask bidders to state the units and inclusions behind ceiling, door and trim prices.')

chapter('Connect coverage and coat count to quantity','A theoretical gallon result is not a complete purchasing order.',[
'Use the selected product documentation and painter assessment to establish the coverage assumption and intended coats. Coverage depends on the actual product and surface. The manufacturer calculator resource is a planning aid [2]; a default input does not verify the coverage of your room.',
'Multiply net paintable area by the stated coat count, then divide by the assumed coverage per gallon for one coat. Keep the coat count and coverage basis visible so they are not applied twice. Distinguish U.S. liquid gallons from other volume units when comparing labels or supplier quotes.',
'Calculate different products and colors separately. A small remainder of ceiling paint cannot automatically finish a wall of another color or finish. Any selected allowance for application losses or touch-up stock should be explicit rather than quietly hidden inside an altered room measurement.',
'Have the painter confirm the order and container sizes. A mathematical result may need whole-container rounding and a different quantity if the substrate, color change or agreed finish requires it. Record who approves the final quantity and how unused tinted material is handled.'
], 'For teaching only, 319 sq ft of net wall area receives two assumed coats at an invented coverage of 350 sq ft per U.S. gallon per coat. No loss allowance has been added.', [('319 × 2','638 coat-sq ft'),('638 / 350','1.82286 U.S. gal'),('If sold only in 1 gal cans','2 cans'),('Coverage assumption','Verify for selected product')],
'Two gallons is only the whole-can result under these assumptions. It does not guarantee coverage or prescribe a coat count.',
['Surface area / product / color / finish','Agreed coat count / coverage assumption / evidence','Area × coats / coverage / unrounded gallons','Explicit loss or touch-up allowance / owner approval','Container sizes / rounded order / painter confirmation'],
['Coverage is stated per coat.','Colors and products are calculated separately.','Theoretical quantity is distinct from final order.'], 'Confirm coat count and expected coverage with the painter and exact product documents.')

chapter('Budget primer as a separate product decision','Do not count a primer coat as a finish coat.',[
'Ask the painter which surfaces require primer, which product is proposed and why. Record the assessment and the coating system for the actual substrate and condition. A marketing phrase on a finish-paint label does not settle every priming question for an unknown surface.',
'Measure the area receiving the specified primer separately from the area receiving finish coats. Localized priming and full-surface priming can have different quantities. Use the primer product coverage and approved coat assumption rather than borrowing the finish-paint calculation unchanged.',
'Keep primer supply and preparation labor visible in the proposal. A package may include primer without showing a separate supply charge. Reconcile inclusions before adding an allowance, and ask how any newly discovered condition changes the approved preparation and primer scope.',
'Record interfaces with stain treatment, repairs or other specialist work through the responsible provider. This book gives no product-compatibility judgment or application procedure. Selection should follow the actual product information and assessed surface requirements.'
], 'A fictional assessed scope requires primer on 200 sq ft with one assumed coat at 250 sq ft per U.S. gallon. Primer costs an invented $30 per one-gallon can.', [('200 × 1 / 250','0.8 U.S. gal'),('Whole one-gallon cans','1'),('Primer supply cost','$30'),('Finish paint and labor','Separate scope')],
'The assumed coverage is not a product specification. Primer and finish quantities remain separate even if both are purchased together.',
['Surfaces requiring primer / assessment basis','Selected primer / compatibility reviewer','Area / coats / coverage / container quantity','Supply and labor inclusions / package reconciliation','New-condition review / approval / updated scope'],
['Primer is not counted as a finish coat.','Coverage belongs to the selected primer.','Supply is not duplicated in package pricing.'], 'Ask for the proposed preparation and coating system in writing before ordering materials.')

chapter('Choose colors and finishes before the final quote','Selection changes can create work beyond the can price.',[
'Create a selection schedule linking each surface group to its exact color reference, product and finish. Record sample approvals with the actual room and lighting context. A phone photograph or a remembered color name is an unreliable substitute for an agreed selection record.',
'Ask the painter how the proposed color change and surface condition affect preparation and coat assumptions. Do not promise that a darker or lighter selection will always need a fixed number of coats. Agree how the desired appearance and any additional work will be assessed.',
'Compare changes using their incremental complete cost over the accepted baseline. Additional colors may involve different material quantities and work organization even when the area remains unchanged. Identify the cause of the price change rather than treating it as a mysterious premium.',
'Set a selection deadline before procurement and record who approves substitutions. If a color or finish changes later, obtain the revised scope, schedule effect and total cost before authorizing it. Keep old and new versions so the final handover identifies what was actually used.'
], 'A fictional approved selection change adds $45 in materials and $120 in defined labor compared with the same baseline scope. No other work changes.', [('Extra material cost','$45'),('Extra labor cost','$120'),('Incremental change','$165'),('Revised selection','Written approval required')],
'An incremental price is meaningful only against a defined baseline. Do not add the full replacement material price on top of material already credited or included.',
['Room and surface / exact color / finish / product','Sample approval / date / responsible owner','Baseline coat and preparation assumptions','Incremental material / labor / schedule impact','Selection deadline / change approval / final labels'],
['Selections are traceable to specific surfaces.','Appearance and coat assumptions are discussed.','Changes are priced against the accepted baseline.'], 'Approve the selection schedule before the painter confirms final procurement and timing.')

chapter('Define preparation and condition allowances','A low paint price cannot compensate for missing scope.',[
'Ask for a description of included preparation by surface and observed condition. Distinguish routine work included in the base price from repairs, specialist assessments or concealed conditions requiring review. A general promise to prepare as necessary does not reveal the budget boundary.',
'Record unresolved staining, damage or recurring moisture questions with a responsible assessor. Painting over a symptom does not establish that its cause has been resolved. Keep any required investigation or remedy separate from the decorative coating proposal until the provider confirms the scope.',
'Use conditional quantities and rates only where they have a defined basis and approval process. State the assumed quantity, matching unit, evidence for a revision and whether a cost replaces an existing allowance. Avoid a double charge when provisional preparation becomes confirmed work.',
'Retain dated observations and approved work records. This handbook provides no sanding, scraping, chemical stripping, repair or mold-treatment procedure. The planning record helps the owner ask for complete scope while qualified providers decide the actual method and suitability.'
], 'An invented preparation allowance is six hours at $40 per hour. After an assessment, the owner approves nine hours at the same rate, replacing the original allowance.', [('Original allowance: 6 × $40','$240'),('Approved revised work: 9 × $40','$360'),('Increase to forecast','$120'),('Combined charge of both amounts','Incorrect')],
'Replace $240 with $360. Do not keep the old allowance and add the complete new charge.',
['Surface conditions / photos / assessment references','Base preparation / exclusions / specialist questions','Conditional quantity / rate / approval trigger','Revised scope / evidence / schedule effect','Old allowance replacement / forecast reconciliation'],
['Condition causes are assessed separately.','Provisional work has a defined boundary.','Confirmed work replaces its original allowance.'], 'Resolve preparation inclusions and the concealed-condition process before accepting a price.')

chapter('Resolve older-paint questions before disturbance','Assessment belongs before the preparation schedule.',[
'Record the known building history and any existing paint or hazard reports. EPA explains that renovation work can create lead hazards when lead-based paint is disturbed [3]. Refer relevant older-property questions to appropriately qualified providers before planning sanding, scraping or other disturbance.',
'Ask the provider which assessments, certifications and local requirements apply to the actual work. Retain current verification and the defined scope rather than assuming an ordinary painting quote includes every required service. This handbook does not determine legal applicability, diagnose lead paint or authorize removal.',
'Separate assessment, any required specialist work and ordinary painting in the budget. Identify who coordinates them and which findings must be resolved before the next stage. If the result changes the project, revise the scope and dates before treating the earlier painting price as complete.',
'Keep occupant communication and completion records with the responsible provider plan. Do not use this book as a testing, containment, cleanup or clearance procedure. The owner decision is to obtain the right assessment and documented responsibilities before disturbance.'
], 'A fictional planning record has three gates: obtain the assessment, resolve any required specialist scope, then approve the revised painting scope. No hazard condition or specialist cost has been established.', [('Gate 1','Assessment and documented findings'),('Gate 2','Required scope and responsible provider'),('Gate 3','Approved painting scope and dates'),('Specialist cost','Not assumed zero')],
'A gate is an unresolved decision, not a prediction that work is required. Price and authorize actual assessed scope through the responsible providers.',
['Property history / existing paint reports','Assessment provider / applicable requirement review','Findings / specialist scope / coordination owner','Occupied-area plan / readiness / stage approvals','Revised budget / dates / retained completion evidence'],
['Relevant questions are resolved before disturbance.','Ordinary pricing is not assumed to include specialist work.','No owner testing or removal procedure is supplied.'], 'Have the responsible qualified provider resolve older-paint questions before preparation starts.')

chapter('Price protection, furniture and access','The painter needs a defined working environment.',[
'List what must be moved, covered, disconnected or retained in each work area. Assign responsibility for furniture, wall-mounted items, floor protection and storage. An occupied home with heavy furniture can involve scope absent from an empty-room example.',
'Ask the contractor to assess high areas, stairwells, exterior access and any equipment needs. This book gives no ladder, scaffold or access procedure. Keep the required service, provider and fixed charge visible instead of assuming every square-foot rate covers every access condition.',
'Record protection boundaries and the process for reporting damage or unexpected conditions. Clarify whether the crew removes and resets items and which tasks need another provider. Do not treat electrical fixtures or appliances as ordinary owner moving tasks without the appropriate qualified support.',
'Reconcile fixed setup charges across the full project. A contractor may mobilize once for several rooms or charge separate visits under agreed terms. Compare the same staging assumptions and do not multiply a project-wide setup fee by every room unless the quote expressly does so.'
], 'A fictional occupied-room plan adds $180 furniture moving, $120 defined protection and one $200 project-wide access-equipment charge. All are expressly excluded from base painting.', [('Furniture moving','$180'),('Protection scope','$120'),('One access charge','$200'),('Separate supporting-work total','$500')],
'The access charge is counted once. Actual equipment suitability and use remain with the contractor.',
['Furniture / contents / move and reset owners','Protection boundaries / retained finishes / damage process','Access assessment / equipment / responsible provider','Other-trade interfaces / agreed owner tasks','Fixed charges / mobilizations / no-duplication check'],
['Occupied-room services are explicitly assigned.','Access is professionally assessed.','Project-wide charges are counted once.'], 'Walk the work areas with the contractor and confirm protection and access inclusions.')

chapter('Read labor rates and productivity assumptions','A unit price needs both a denominator and a scope.',[
'Identify whether a quote is a fixed total, hourly work or a unit rate tied to measured surface area. State the surface group, number of coats and included preparation. Two prices per square foot are not directly comparable when one uses floor area and the other uses painted wall area.',
'For an hourly proposal, ask for the estimated crew hours, hourly basis, included materials and process for exceeding the estimate. Distinguish elapsed days from labor hours: two people working six hours each create twelve worker-hours, even though only six hours pass.',
'Use productivity figures only as documented bid assumptions. The book provides no universal painting speed or labor benchmark. Room conditions, protection, detail and the agreed finish can alter the work. A cheaper hourly rate does not guarantee a lower final total.',
'Normalize only the portions you can justify. If a contractor offers an indivisible fixed package, compare its complete scope and terms rather than inventing a precise labor breakdown. Record unresolved differences and seek clarification before declaring one proposal cheaper.'
], 'An invented labor estimate uses two workers for six hours each at $40 per worker-hour, with materials priced separately.', [('2 workers × 6 hours','12 worker-hours'),('12 × $40','$480 labor'),('Elapsed working time','6 hours in this example'),('Materials','Excluded')],
'Do not charge only six worker-hours or multiply the twelve worker-hours by the crew count again.',
['Fixed / hourly / unit-rate basis and inclusions','Measurement denominator / surfaces / coat assumptions','Crew count / worker-hours / rate / estimate boundary','Materials / protection / preparation / excluded tasks','Unresolved differences / clarification / approval process'],
['Elapsed time and worker-hours are distinct.','The rate denominator is visible.','No universal productivity claim is assumed.'], 'Ask each bidder to explain the quantity and work scope behind its labor price.')

chapter('Plan room sequencing and schedule decisions','A calendar date does not replace product requirements.',[
'Discuss work order with the painter using the household occupancy plan and other-trade schedule. Record which rooms remain available, where belongings are held and who communicates changes. The cheapest sequence for an empty house may not meet the needs of an occupied one.',
'Request product-specific timing and environmental requirements from the responsible provider. Recoat timing, drying and readiness for ordinary use are different decisions. Do not substitute one universal number of hours from an example for the selected coating instructions and actual conditions.',
'For exterior work, ask who reviews weather and decides whether the work proceeds. Record the agreed approach to rescheduling, protection and any conditional charges. This guide provides no weather threshold, ventilation specification or application procedure.',
'Use readiness gates for selections, material availability, surface approval and access. When a gate changes, record its effect on dependent tasks before accepting new dates. A delay allowance should have an agreed trigger and evidence rather than becoming an automatic additional invoice.'
], 'A fictional revised sequence needs one extra mobilization at an agreed $100 and one $60 additional storage period. The accepted scope otherwise remains unchanged.', [('One agreed additional visit','$100'),('Extra storage','$60'),('Approved schedule change','$160'),('Product readiness timing','Provider confirmation required')],
'The cost example does not establish a drying, curing, recoat or occupancy interval.',
['Room sequence / household routes / other trades','Selected product timing / environmental decision owner','Weather review / rescheduling terms / contacts','Selection / supply / surface / access gates','Approved delay charges / evidence / revised dates'],
['Product-specific timing is retained.','Readiness is distinct from a promised finish date.','Schedule changes use agreed terms.'], 'Obtain the room sequence and provider use guidance before confirming the work dates.')

chapter('Compare complete painting proposals','Match the finish and supporting work before ranking totals.',[
'Use one common surface schedule and selection record for every proposal. Map preparation, primer, finish paint, labor, protection, access, cleanup and owner tasks as applicable. Mark every line included, excluded, allowance or unresolved, with the relevant quantity and rate basis.',
'Check whether materials are included in labor or package prices. Confirm specified products and colors rather than treating any named premium paint as equivalent. Verify that a one-coat quote is not being compared against a differently specified finish without making that distinction visible.',
'Separate comparison totals from the all-in funding plan. The comparison can reveal matched contractor scope while unresolved work, owner purchases, tax and reserve still need a place in the budget. Identify the responsible provider for every required excluded item.',
'Keep the accepted scope, price, selection versions and written change process together. If a bidder cannot clarify a required line, retain it as an unresolved gap. Do not silently invent a low allowance to make an incomplete bid look complete.'
], 'An invented proposal has $130 finish paint, $30 primer, $360 defined preparation, $960 labor, $500 supporting work and $100 cleanup. Providers confirm no category overlaps.', [('Paint and primer','$160'),('Preparation','$360'),('Labor','$960'),('Supporting work','$500'),('Cleanup','$100'),('Defined comparison total','$2,080')],
'The $2,080 excludes tax, unresolved work, reserve and other owner spending unless expressly added. It is not a local market-price claim.',
['Common surface / selection / preparation versions','Included / excluded / allowance / unresolved lines','Material and labor units / coats / no overlap','Tax / owner tasks / warranty / payment terms','Matched total / gaps / responsible providers'],
['Products and coat assumptions are comparable.','Materials are included only once.','Comparison and all-in funding totals are distinguished.'], 'Return the scope comparison to bidders and resolve missing work before choosing a proposal.')

chapter('Close out with a finish and touch-up record','Keep the actual product details after the crew leaves.',[
'Agree how the completed scope will be reviewed and record observations by room and surface ID. Keep a punch list with a responsible provider and resolution date. An owner can document an incomplete edge or missed area without diagnosing why a coating has failed.',
'Request the final product, color and finish references, care guidance, warranty contacts and any return-to-use instructions. Save useful labels and selection records with invoices. Do not promise that touch-up paint will always produce an invisible repair after the finish has aged.',
'Count retained material and ask the provider for the selected product storage and disposal guidance. Record the location of useful leftovers without creating an automatic additional purchase. Follow actual supplier terms when evaluating whether unopened or tinted material is returnable.',
'Reconcile approved changes and confirmed credits against the accepted scope. Distinguish a promised correction from completed work and a requested refund from an actual credit. Archive the final obligation record with the care file so later questions use the same evidence.'
], 'A fictional closeout starts with $2,080 defined scope, adds a $165 approved selection change and subtracts a confirmed $40 supplier credit.', [('Accepted scope','$2,080'),('Approved change','$165'),('Confirmed credit','−$40'),('Reconciled defined scope','$2,205')],
'A requested credit is not deducted until confirmed. The final funding record must still include any separate owner costs and tax.',
['Room-based punch list / provider / completion evidence','Actual product / color / finish / warranty contacts','Care / use / retained material / storage location','Accepted scope / changes / confirmed credit evidence','Unpaid obligations / final record / archived care file'],
['Product and color details are retained.','Corrections and credits have evidence.','Touch-up results are not guaranteed.'], 'Save the completed punch list and actual paint references with the reconciled final invoice.')

method(2,'Build the all-in painting project budget')
method(5,'Normalize contractor proposals')
method(6,'Review the live cost forecast')
method(17,'Approve changes and reconcile the reserve')
method(18,'Close out and retain project records')
SOURCES=[('1','FTC: Home Repair Scams','https://consumer.ftc.gov/features/pass-it-on/home-repair-scams'),('2','Sherwin-Williams: Paint calculator','https://www.sherwin-williams.com/en-us/color/color-tools/paint-calculator'),('3','EPA: Lead Renovation, Repair and Painting','https://www.epa.gov/lead/lead-renovation-repair-and-painting-program')]

