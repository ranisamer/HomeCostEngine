"""Original landscape owner planning and cost cases, with established owner-budget methods."""
from pathlib import Path
import runpy,copy
base=runpy.run_path(str(Path(__file__).with_name('renovation-blueprint.py')))
CHAPTERS=[]
def chapter(title,deck,paragraphs,example,rows,conclusion,prompts,checks,task):
    CHAPTERS.append(dict(title=title,deck=deck,paragraphs=paragraphs,example=example,rows=rows,conclusion=conclusion,prompts=prompts,checks=checks,task=task))
def method(index,title):
    c=copy.deepcopy(base['CHAPTERS'][index]);c['title']=title
    replacements={'renovation':'landscaping project','Make the kitchen usable for two cooks':'Create a usable landscape for the household','buy new cabinets':'buy landscape materials','A bathroom project in a one-bath home has a different temporary-use problem from the same work in an empty property.':'Changing the only yard access creates different temporary-use needs from work in a separate planting bed.','fixture allowance':'finish-selection allowance'}
    def adapt(s):
        for a,b in replacements.items():s=s.replace(a,b)
        return s
    for k in ['deck','example','conclusion','task']:c[k]=adapt(c[k])
    for k in ['paragraphs','prompts','checks']:c[k]=[adapt(x) for x in c[k]]
    CHAPTERS.append(c)

method(0,'Define the landscaping project brief')
chapter('Map outdoor zones and retained features','A yard total does not describe every area of work.',[
'Create a dated site sketch with unique IDs for planting, lawn, paths, seating, service and retained areas. Record intended activities, household routes and features to remain. A sketch organizes discussion but does not establish boundaries, grades or technical design.',
'Collect existing reports and accessible observations about sunlight, water-related concerns, access and prior work. Ask appropriate qualified providers to assess relevant questions. Do not dig or disturb utilities, structures or unknown materials to improve the owner record.',
'Keep new work, removal and protection boundaries explicit. Shared site access and project-wide services should have their own IDs so they are not added separately to every planting-zone budget.',
'Use the same zone plan for measurement, design, procurement, quotations and handover. If a zone changes, revise dependent quantities and care assumptions. Record unverified dimensions as approximate until the responsible provider confirms them.'
], 'A fictional yard plan has three planting zones, one path zone, one seating zone and two retained areas.', [('Planting zones','3'),('Path and seating zones','2'),('Retained areas','2'),('Total indexed zones','7')],
'The seven zones are an index, not a design approval or verified area schedule.',
['Zone IDs / intended activities / dated sketch','Retained features / protection / removal boundaries','Accessible observations / existing reports','Shared access and project-wide service IDs','Verified measurements / open assessments / current version'],
['Retained areas are explicit.','Shared work is indexed once.','The sketch is not treated as technical design.'], 'Prepare one current zone plan and give it to every provider preparing scope or prices.')

chapter('Assess soil questions before choosing amendments','A bag count cannot determine what the soil needs.',[
'Ask the relevant horticultural adviser, qualified provider or local extension service what soil information is useful for the proposed planting. Penn State Extension provides soil-testing resources as one university example [2]. Use a suitable local source and the actual intended use.',
'Retain the report, its scope and the responsible interpretation. A fertility report does not automatically answer every drainage, contamination, structural or site-suitability question. Keep other concerns with the appropriate assessor rather than assuming one test resolves all conditions.',
'Price assessed preparation and selected amendments using the actual recommendation and product basis. This book supplies no sampling depth, fertilizer rate, chemical treatment or universal soil recipe. Avoid buying material merely to fill an unexplained allowance.',
'Connect findings to the plant selection and preparation scope. If a report changes the proposed work, revise quantities and complete cost before ordering. Retain the evidence and next review requirements with the care record.'
], 'A fictional assessed preparation scope has $180 testing/advice and $420 defined preparation, with no other site work included.', [('Testing and advice','$180'),('Defined preparation','$420'),('Stated preparation scenario','$600'),('Other site conditions','Not established')],
'The $600 is invented scope, not a standard test or soil-improvement price. Actual findings determine appropriate work.',
['Proposed planting / soil questions / local source','Actual report / scope / qualified interpretation','Separate drainage or other assessment questions','Recommended work / selected products / quantity basis','Approved preparation / revised plan / retained evidence'],
['One report is not treated as every site assessment.','Amendments have an actual recommendation basis.','No universal treatment rate is supplied.'], 'Obtain the relevant soil advice before finalizing preparation and amendment purchases.')

chapter('Resolve drainage, grading and boundary decisions','Changing the surface can affect more than its appearance.',[
'Record observed water-related issues and the proposed changes by zone. Ask qualified providers and the actual local authority about relevant site, drainage, grading and boundary requirements. This guide gives no excavation, drainage-system or slope design.',
'Identify how proposed work interfaces with the home, retained surfaces, shared property and utilities. A decorative surface price may exclude supporting site work. Keep the affected location and accountable professional with each unresolved question.',
'Compare complete assessed alternatives rather than a material-only fix. A symptom such as pooled water does not identify the required remedy. Retain the actual findings, design and applicable decisions before committing to dependent finishes.',
'Price access, disposal and restoration where the assessed work requires them. Keep unresolved conditions as gates instead of assuming a reserve amount approves a solution. Revisit the plan when professional or authority findings change the scope.'
], 'A fictional site decision record has four questions: two resolved by current reports, one awaiting design and one awaiting a boundary clarification.', [('Resolved questions','2'),('Design pending','1'),('Boundary clarification pending','1'),('Open decisions','2')],
'The two open decisions limit dependent work. A planned finish date does not close them.',
['Dated observations / proposed changes / affected zones','Qualified site design / actual local questions','Home / shared property / utility interfaces','Assessment / design / clarification status and owners','Dependent finish limits / cost / approval evidence'],
['Symptoms are not owner diagnoses.','Site design has a qualified owner.','Open boundaries remain explicit.'], 'Resolve the drainage and boundary questions before approving the dependent hardscape or planting layout.')

chapter('Measure area and divide irregular zones','A quantity needs a clear shape and unit.',[
'Use verified dimensions and a current zone plan. For rectangles, multiply length by width in matching units. Split irregular areas into non-overlapping shapes and retain the original measurements so another person can check the calculation.',
'For a triangle, multiply base by perpendicular height and divide by two. Do not use a sloped edge as the height. Keep excluded retained surfaces and overlapping zones explicit instead of deducting an unexplained percentage.',
'Separate square-foot areas, linear-foot edges and counted plants or features. They describe different dimensions and cannot be added into one quantity. Ask providers to confirm the actual takeoff and relevant technical basis.',
'Retain the area definition with material and labor rates. A purchased material allowance does not automatically increase installed area. If a layout changes, update all affected quantities and costs rather than preserving an old total.'
], 'A fictional zone combines a 12 × 8 ft rectangle and a non-overlapping triangle with base 6 ft and perpendicular height 4 ft.', [('Rectangle: 12 × 8','96 sq ft'),('Triangle: 0.5 × 6 × 4','12 sq ft'),('Combined zone','108 sq ft'),('Material allowance','Not yet added')],
'The 108 sq ft is geometric area only. It does not approve layout, planting suitability or a final order.',
['Zone / shape IDs / verified dimensions / units','Non-overlapping sections / excluded retained surfaces','Area / edge length / counts kept separate','Provider-confirmed takeoff / price quantity basis','Revisions / material allowances / dependent costs'],
['Shapes do not overlap.','Perpendicular height is used for triangles.','Area arithmetic is separate from technical suitability.'], 'Check one irregular zone independently and reconcile it with the provider takeoff.')

chapter('Convert bulk volume and bag quantities','Depth is an input to verify, not a recommendation.',[
'Use the professionally or horticulturally established material and depth for the actual purpose. Record the source and area before calculating volume. This guide does not prescribe mulch, soil or gravel depth for any application.',
'For length and width in feet and depth in inches, cubic yards equal length times width times depth divided by 324. The divisor combines twelve inches per foot and twenty-seven cubic feet per cubic yard. Keep the units visible.',
'Convert to bags using the actual net volume printed for the selected product. Round whole-bag orders upward when required and retain any separately approved allowance. A bag described by weight cannot automatically be converted using a volume example.',
'Compare delivered bulk and bag alternatives on complete scope, including transport, handling and placement where relevant. A geometric volume does not establish compaction, settlement, loss or actual supplier ordering requirements. Have the responsible provider confirm the final quantity.'
], 'For arithmetic only, an assumed 12 × 8 ft area at 3 in depth contains 24 cu ft, or 0.88889 cu yd. Fictional bags contain 2 cu ft each, with no allowance.', [('12 × 8 × 3 / 12','24 cu ft'),('24 / 27','0.88889 cu yd'),('24 / 2','12 bags'),('Appropriate actual depth','Not determined here')],
'The depth and bag size are teaching inputs. They are not application instructions or a supplier order confirmation.',
['Material / purpose / source-approved depth','Verified area / units / geometric volume','Actual bag volume / whole-unit rounding','Allowance / supplier terms / final quantity verifier','Bulk versus bags / complete delivery and handling cost'],
['Depth is not taken from the example as a recommendation.','Weight and volume units are distinguished.','The actual label determines bag conversion.'], 'Confirm the actual depth, product volume and complete delivered quantity with the responsible provider.')

chapter('Build the plant schedule with local suitability','A count and a retail tag do not establish a planting design.',[
'Record exact plant references, selected sizes, counts and zones from the actual planting plan. Ask the relevant qualified adviser to confirm suitability for local conditions, intended use and site constraints. This guide recommends no species, spacing or chemical treatment.',
'EPA WaterSense landscape resources support considering the complete design and ongoing care [3]. Keep actual water, light, soil and maintenance questions with the local provider. A broad label such as low maintenance does not describe every duty for every site.',
'Compare plant supply separately from preparation, installation, support, delivery and establishment care. Different selected sizes can change both the product and labor scope. Keep approved substitutions and their complete cost effect visible.',
'Retain nursery or supplier terms, actual labels and care guidance at handover. Record plant condition observations and the process for replacement or warranty questions. No planting choice here guarantees survival, future appearance or a bill saving.'
], 'An invented plan orders 48 plants at $12 each and four larger selected plants at $150 each. All prices are supply only.', [('48 × $12','$576'),('4 × $150','$600'),('Plant supply total','$1,176'),('Installation and care','Separate scope')],
'The quantities and prices do not prescribe a planting layout or suitable species.',
['Exact plant references / sizes / counts / zones','Local suitability reviewer / actual site information','Supply / preparation / install / establishment boundaries','Substitution approval / complete incremental price','Labels / care / supplier terms / replacement process'],
['Counts come from the actual plan.','Local suitability is reviewed.','Supply-only prices are labeled.'], 'Confirm the complete plant and establishment schedule before accepting substitutions or ordering.')

chapter('Price irrigation as a complete assessed system','A controller price is not the installed watering plan.',[
'Ask an appropriate qualified irrigation provider to assess the actual landscape and relevant water-service and local requirements. Record the design basis, zones and retained equipment. This planner gives no hydraulic, backflow, controller, trenching or connection procedure.',
'Keep the selected planting and other landscape zones linked to the irrigation plan. Changes to the plant schedule or surface layout may affect the assessed system. Do not assume a prior generic watering schedule suits new selections.',
'Compare supply, installation, relevant supporting work, setup, checks and operating handover. A product-only total can omit access, restoration or other required services. Assign each interface to a responsible provider.',
'Use actual provider care and operation guidance for the site. Keep seasonal and establishment-related instructions sourced and review them when conditions change. No example schedule here establishes water needs or a guaranteed saving.'
], 'A fictional assessed irrigation package has $800 equipment, $1,000 installation and $200 setup/handover, confirmed non-overlapping.', [('Equipment','$800'),('Installation','$1,000'),('Setup and handover','$200'),('Defined system scope','$2,000')],
'The example does not size or specify an irrigation system. Actual design and local requirements remain with qualified sources.',
['Current landscape / water-service / local questions','Qualified design / zones / retained equipment','Equipment / install / support / restoration inclusions','Setup / checking / operating handover / provider','Sourced care / changed planting / review triggers'],
['Product cost is separate from a complete system.','Landscape changes trigger relevant review.','Watering needs are not invented.'], 'Request the complete assessed irrigation scope and actual operating handover before comparing controllers.')

chapter('Separate hardscape surfaces from edges and preparation','Equal area can involve different supporting work.',[
'Record exact surfaces, edge locations, steps and retained features on the current plan. Ask qualified providers to establish relevant design, ground and drainage requirements. This book supplies no paving, concrete, retaining-wall, base or structural specification.',
'Keep surface area, edge length and counted features distinct. A per-square-foot product rate does not establish the installed scope for every shape. Access, preparation, supporting work and restoration may be separate.',
'Compare complete alternatives with the same use and boundaries. A cheaper surface may involve different preparation or ongoing obligations. Retain actual product requirements and professional assessment rather than assuming similar appearance means equivalent work.',
'Reconcile fixed fees and shared site services across proposals. If the shape or levels change, have the relevant design and takeoff reviewed before procurement. Owner arithmetic checks quantity but cannot approve the site solution.'
], 'A fictional 12 × 12 ft surface has 144 sq ft area and 48 ft perimeter. A separate 20 ft edge line is priced at $8 per linear ft, with its extent confirmed by the provider.', [('Surface area','144 sq ft'),('Geometric perimeter','48 ft'),('Priced selected edge','20 linear ft'),('20 × $8','$160 edge scope')],
'The priced edge is not assumed to equal the full perimeter. The example gives no construction detail.',
['Surface and edge IDs / current layout / exact products','Qualified design / ground and drainage assessments','Area / linear feet / feature counts / takeoff','Preparation / installation / support / fixed fees','Complete alternatives / shape changes / revised records'],
['Surface area and edge scope are distinct.','Preparation has actual assessed boundaries.','Quantity arithmetic is not construction approval.'], 'Ask bidders for the full surface, edge and preparation scope using the same plan.')

chapter('Include removal, clearance and retained-feature protection','A clean new plan can conceal substantial existing-site work.',[
'List the actual existing elements to remove and the retained features needing protection. Ask qualified providers to assess relevant trees, materials, utilities and site concerns. This book gives no tree removal, demolition, excavation or hazardous-material procedure.',
'Clarify access, debris handling, disposal, cleanup and restoration. A clearing rate may exclude a fixed removal service or specialist assessment. Keep the responsible provider and exact boundary with every required task.',
'Record local or shared-property questions before disturbance where relevant. Do not treat ownership of the yard as automatic permission for every proposed change. Use actual authoritative information and qualified advice.',
'Reconcile removal and preparation inclusions across the landscape, hardscape and irrigation packages. Similar line names need confirmation before they are deleted as duplicates. Unexpected findings should follow the agreed review and approval process.'
], 'A fictional ordinary-clearance package is $900 including disposal, with $200 separately agreed retained-feature protection.', [('Clearance including disposal','$900'),('Separate protection','$200'),('Defined supporting scope','$1,100'),('Specialist or unknown work','Not included')],
'No additional disposal charge is added in this scenario. Actual materials and site findings determine relevant scope.',
['Removed / retained elements / protection boundaries','Qualified assessment / local and shared questions','Clearance / disposal / access / cleanup inclusions','Specialist exclusions / fixed fees / provider roles','Package overlaps / unexpected findings / approvals'],
['Retained-feature protection is explicit.','Specialist work is not assumed ordinary clearance.','Included disposal is not added twice.'], 'Confirm existing-site removal and protection scope before finalizing the new-work total.')

chapter('Coordinate delivery, access and placement','Bulk material cost is only part of getting it into the zone.',[
'Ask suppliers and installers to assess the actual receiving location, route and working arrangements. Record relevant restrictions and responsible providers. A delivered-to-curb price may not include handling or placement in the final zone.',
'Keep unit rates, minimum orders, delivery fees, handling and return terms separate. A small order can involve fixed charges that dominate the material price. Confirm the supplier selling unit and whether tax or other fees are included.',
'Assign who orders, receives, checks quantities and resolves shortages or wrong products. Retain delivery evidence and the actual product information. A material pile on site does not prove the correct quantity or specification has been supplied.',
'Coordinate protection, storage, cleanup and readiness with the installer. This planner provides no equipment operation, loading or placement procedure. If access changes, revise the complete cost and sequence using the agreed process.'
], 'An invented bulk supply order is $240 materials, $90 delivery and $170 separately agreed handling/placement, with no overlap.', [('Material supply','$240'),('Delivery','$90'),('Handling and placement','$170'),('Complete stated logistics scenario','$500')],
'The $240 material line is less than half the complete scenario. Actual supplier and site terms determine the charges.',
['Supplier selling units / actual receiving route','Minimums / fees / tax / returns / fixed charges','Ordering / receiving / checking / discrepancy owners','Handling / placement / storage / protection boundaries','Readiness / changed access / approved logistics cost'],
['Curb delivery is not assumed final placement.','Fixed charges appear beside unit prices.','Receiving has an accountable owner.'], 'Get the complete delivered-and-placed scope before choosing between bulk and bag supply.')

chapter('Review lighting, structures and optional features','The retail item may need qualified supporting services.',[
'List desired lighting, shade, furniture, decorative or other outdoor features with their approval status. Keep optional preferences separate from required work. A product image does not establish suitability for the actual site.',
'Ask appropriate qualified providers about relevant electrical, structural, fire-safety, access and local questions. This guide supplies no wiring, foundation, anchorage or appliance installation instructions. Record the actual design and selected product references.',
'Compare complete installed additions over the same baseline, including supporting work, restoration and ongoing care. A retail price may omit essential services. Keep confirmed credits for replaced scope and apply them once.',
'Check the funding and phase effect before approval. An optional item should not silently consume money needed for accepted site or service obligations. Update affected providers and records when a feature changes the layout.'
], 'A fictional optional feature has $400 product cost, $350 qualified supporting work and $150 restoration, all outside the baseline.', [('Product','$400'),('Supporting work','$350'),('Restoration','$150'),('Complete optional addition','$900')],
'The feature remains conditional until assessed and approved. The example is not a design or suitability recommendation.',
['Optional feature / status / actual product reference','Qualified electrical / structural / local questions','Product / support / restoration / ongoing care','Baseline / confirmed credits / complete change price','Funding / phase / approval / updated layout'],
['Retail price is not the complete addition.','Technical services have qualified owners.','Unapproved options are outside committed scope.'], 'Request the complete assessed feature cost before adding a retail purchase to the project.')

chapter('Plan phases and establishment care together','Deferring work can repeat services and change the care plan.',[
'Ask the landscape team to establish a practical sequence for the actual local conditions, selected plants and site work. Keep technical, horticultural and local-review gates explicit. This book gives no universal planting season or watering interval.',
'Compare combined and phased work using repeated access, delivery, protection and setup costs. A lower first-stage payment does not necessarily mean a lower total. Record which outcomes each completed phase provides.',
'Retain the actual establishment and ongoing-care instructions, task owners and relevant supplier terms. A newly planted area can need a different plan from an established one. Use local qualified guidance rather than a generic maintenance slogan.',
'Include first-year care and follow-up where outside installation prices. Clarify what is included in a contractor or supplier promise and what remains the household responsibility. No plan here guarantees plant survival or a future appearance.'
], 'A fictional combined project is $8,000. Two matched phases are $4,500 and $4,000 because a repeated setup service is explicitly included.', [('Combined scope','$8,000'),('Phase 1','$4,500'),('Phase 2','$4,000'),('Phased total','$8,500'),('Phasing premium','$500')],
'The $500 premium is a teaching scenario. Actual season, suitability and care decisions require local review.',
['Actual sequence / local conditions / provider guidance','Combined and phased scope / repeated services','Phase outcomes / usable routes / retained areas','Establishment and care tasks / source / responsible owner','First-year cost / supplier terms / follow-up evidence'],
['Phasing is not labeled automatic saving.','Care tasks have actual sources.','Installation and establishment duties are distinct.'], 'Compare complete phase totals and obtain the selected-plant care handover before scheduling.')

chapter('Compare complete landscape scenarios and closeout','A plant or material subtotal is not the whole yard.',[
'Combine the current zone plan, actual assessments, selected plants, materials and supporting systems into one proposal request. Mark preparation, removal, hardscape, irrigation, delivery, handling, optional work and care included, excluded, allowance or unresolved.',
'Keep area, volume, linear feet and counts on their correct bases. A bag supply price is not placement labor, and a plant count is not establishment scope. Normalize only matched proposals and resolve required exclusions before ranking.',
'Add professional, owner and temporary costs outside contractor packages where relevant, with reserve separate. Reconcile shared access and mobilization once where confirmed. Keep unsupported future water or maintenance savings outside the funding plan.',
'At handover, retain actual plant and product references, provider records, care tasks, confirmed credits and open follow-up. The owner file supports the ongoing landscape without certifying site performance, survival or a resale return.'
], 'A fictional scenario has $1,176 plant supply, $600 preparation, $2,000 irrigation, $3,000 hardscape, $1,100 clearance/protection and $500 logistics, all non-overlapping.', [('Plant supply + preparation','$1,776'),('Irrigation','$2,000'),('Hardscape','$3,000'),('Clearance / protection','$1,100'),('Logistics','$500'),('Defined comparison scope','$8,376')],
'The $8,376 excludes unstated installation, care, tax, owner costs and reserve unless explicitly included. It is not a local landscaping-price benchmark.',
['Current zone plan / findings / selections / quantities','Included / excluded / allowance / unresolved scope','Unit bases / complete supply and labor / overlaps','Professional / owner / care / reserve / total funding','Actual labels / care / credits / final obligations / follow-up'],
['Different quantity units remain distinct.','Supply subtotals are not complete project prices.','Future savings and survival are not promised.'], 'Resolve the required scope and care responsibilities before choosing a complete landscape proposal.')

method(2,'Build the all-in landscaping project budget')
method(5,'Normalize contractor proposals')
method(6,'Review the live cost forecast')
method(17,'Approve changes and reconcile the reserve')
method(18,'Close out and retain project records')
SOURCES=[('1','FTC: Home Repair Scams','https://consumer.ftc.gov/features/pass-it-on/home-repair-scams'),('2','Penn State Extension: Soil Testing','https://extension.psu.edu/soil-testing'),('3','EPA WaterSense: Water-Smart Landscape Design','https://www.epa.gov/watersense/water-smart-landscape-design')]

STORE=dict(slug='landscaping-backyard-budget-planner',title='Landscaping Cost Guide',category='Landscaping & Backyard Planning',amount=999,route='/api/download-landscape-guide',number=19,test='scripts/test_landscape_delivery.mjs',
description='A 64-page landscape planning guide with 19 worked examples and 19 fillable worksheets. Connect zones, site questions, material quantities, plants, irrigation, logistics, phases and care costs.',
eyebrow='Price the whole landscape, not only the materials',why_title='Why buy this landscaping planning guide?',why='A plant list or bulk-material price can miss preparation, delivery, placement, systems and first-year care. This guide helps you connect the quantities to the complete assessed scope and responsible providers.',
benefits=[('Check different quantity units.','Keep area, volume, bag counts, edge lengths and plant counts distinct.'),('Expose supporting scope.','Record soil and site questions, preparation, irrigation, access, handling and restoration.'),('Plan beyond installation day.','Compare phases, establishment duties and sourced care responsibilities.')],
reader='U.S. homeowners organizing landscape or backyard work and comparing complete proposals. Local qualified providers must establish site suitability, design, plant selection and actual care requirements.',
difference_title='What does the paid guide add to a calculator?',difference='It connects individual quantities to site, purchasing, scope, sequencing and care records, with 19 worked cases, 19 worksheets and 95 fillable fields.',
limits='One-time purchase. No subscription. Example costs, depths and quantities are hypothetical. No local price, suitable planting, water saving, survival or future appearance is promised.',
helps=['Create a zone plan with retained features and shared work','Record soil, drainage and boundary decision gates','Check geometric area, bulk volume and whole bags','Separate plants, irrigation, hardscape and logistics','Compare complete phases and care responsibilities'],
sequence='zone records, soil and site questions, area and volume calculations, plants, irrigation, supporting work, phases and care handover',
example='For arithmetic only, a fictional 12 × 8 ft area at an assumed 3 in depth contains 24 cu ft, or 0.88889 cu yd. At an invented 2 cu ft per bag, that is 12 bags before any allowance. The depth is not a recommendation for any landscape application.',
calculator_html='<p>Use the free <a href="/calculators/">HomeCostEngine calculators</a> for individual quantity checks and the <a href="/calculators/contractor-quote-comparison">quote comparison calculator</a> with matched scope. Confirm actual material and planting requirements locally.</p>',
examples='Work through zone and assessment records, irregular area, volume and bag conversion, supply-only plant counts, complete irrigation scope, edges, clearance inclusions, delivery/placement, optional features and phase premiums. Six general owner-budget chapters use the HomeCostEngine renovation method with landscape adaptation; thirteen chapters add landscape decisions. No excavation, drainage, irrigation, treatment or planting specification is supplied.')
PDF_META=dict(key='landscape',subject='Original landscape owner planning guide and 19 fillable worksheets',header='LANDSCAPE OWNER PLANNING',cover_title='Landscaping<br/>Cost Guide',cover_lines=['Check the quantities. Include the site and care.','Compare complete landscape scenarios.'],
preface=['A landscape project connects the outdoor plan to actual site conditions, selected products, plants and ongoing care. This guide helps you organize the owner scope without treating a material subtotal as the complete yard.',
'Start with the brief and zone map. Resolve soil, drainage and relevant boundary questions, then separate area, volume, length and counts. Connect plants, irrigation, hardscape, clearance, logistics, optional features and the first care plan.',
'Each working chapter contains an explanation, an original hypothetical case and a reusable sheet. Six general owner-budget chapters use the HomeCostEngine renovation method with landscape adaptation. Thirteen chapters add landscape-specific quantity and scope decisions.',
'All costs, depths and quantities are invented USD teaching inputs, not local price ranges or application instructions. A depth used to demonstrate volume is not a recommendation. Plant counts and product names do not establish local suitability or survival.',
'Use actual qualified providers, relevant local authorities and suitable extension or horticultural advice for site design, planting and care. This book gives no digging, treatment, drainage or installation procedure. Keep current plans, findings, selections, changes, delivery and care records with the sheets.'],
workflow=['Record outdoor activities, zones, retained features and the funding boundary.','Collect actual site findings, verified quantities and locally suitable selections.','Match preparation, plants, materials, systems, logistics and care responsibilities.','Track approved orders, allowances, paid costs, obligations and complete changes.','Reconcile scope and credits. Retain actual labels, sourced care and follow-up records.'],
afterword='A useful landscape plan connects the outdoor outcome to actual site findings, correct quantity units and complete responsibilities. Keep material supply separate from installation and care, resolve local and technical questions, and retain the records that support the landscape after handover.')

