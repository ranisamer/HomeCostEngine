"""Original basement remodeling planning and cost cases, with established owner-budget methods."""
from pathlib import Path
import runpy,copy
base=runpy.run_path(str(Path(__file__).with_name('renovation-blueprint.py')))
CHAPTERS=[]
def chapter(title,deck,paragraphs,example,rows,conclusion,prompts,checks,task):
    CHAPTERS.append(dict(title=title,deck=deck,paragraphs=paragraphs,example=example,rows=rows,conclusion=conclusion,prompts=prompts,checks=checks,task=task))
def method(index,title):
    c=copy.deepcopy(base['CHAPTERS'][index]);c['title']=title
    replacements={'renovation':'basement remodel','Make the kitchen usable for two cooks':'Make the basement usable for the intended activities','buy new cabinets':'buy basement finishes','A bathroom project in a one-bath home has a different temporary-use problem from the same work in an empty property.':'Work affecting the only basement access creates different temporary-use needs from work in an isolated unused area.','fixture allowance':'finish-selection allowance'}
    def adapt(s):
        for a,b in replacements.items():s=s.replace(a,b)
        return s
    for k in ['deck','example','conclusion','task']:c[k]=adapt(c[k])
    for k in ['paragraphs','prompts','checks']:c[k]=[adapt(x) for x in c[k]]
    CHAPTERS.append(c)

method(0,'Define the basement remodeling brief')
chapter('Connect intended use to feasibility questions','A storage refresh and a sleeping room are different proposals.',[
'Describe how the household wants to use the basement and identify the actual areas included. Keep storage, recreation, sleeping, work, bathing and other uses distinct. A room label on an owner sketch does not establish that the space is suitable or approved for that use.',
'Ask qualified providers and the appropriate local authority which design, access, service and approval questions apply. Record existing conditions and limitations without assuming that previously finished space meets current project requirements. Keep the relevant findings with the proposed layout.',
'Compare feasible alternatives against the same household need. Reducing the scope may change both cost and usefulness. Record the tradeoff instead of treating every finished square foot as equivalent.',
'Use the brief to identify decision gates before purchasing finishes. If a room use is not yet confirmed feasible, retain its price as a conditional scenario. This planner provides no code determination, occupancy approval or design specification.'
], 'A fictional brief identifies four zones: recreation, storage, bathroom and a proposed sleeping room. The sleeping-room use awaits professional and local review.', [('Defined activity zones','3'),('Proposed use awaiting review','1'),('Total layout zones','4'),('All uses approved','Not established')],
'A complete zone list is not an approval. Resolve the relevant use questions before treating every zone as ready to finish.',
['Intended uses / zones / household outcomes','Existing-use records / known limitations','Qualified and local feasibility questions','Feasible alternatives / function and scope tradeoffs','Open gates / conditional costs / decision owners'],
['Room labels are not approval evidence.','Different uses receive relevant review.','Conditional scope stays visible.'], 'Confirm the proposed uses with the relevant qualified providers and local authority.')

chapter('Build a measured basement baseline','Footprint area is only one of the needed records.',[
'Create a dated plan of the basement footprint, proposed rooms, retained equipment, columns, stairs and accessible service routes. Label verified dimensions and owner approximations separately. Ask the responsible provider to confirm the takeoff and technical constraints for the actual proposal.',
'Record clear dimensions and relevant overhead or access restrictions as questions for professional review. A geometric area calculation cannot determine whether the ceiling, stair, room or route is suitable. Do not alter structural or service elements to obtain more space without appropriate design.',
'Keep total footprint, finished zones and retained utility areas distinct. A contractor price based on total footprint may not describe the same work as another price based only on selected finished rooms. Save the area definition beside each ratio.',
'Give each zone a stable ID for quotes, selections, changes and handover. Revise dependent quantities when the layout changes. Photographs and drawings should support the record without requiring hazardous access or disturbance.'
], 'A fictional 30 × 20 ft basement has 600 sq ft of footprint. A confirmed 100 sq ft utility zone remains unfinished, leaving 500 sq ft in the proposed finish scope.', [('Footprint','600 sq ft'),('Retained utility zone','−100 sq ft'),('Proposed finish area','500 sq ft'),('Suitability of proposed use','Requires separate review')],
'The 500 sq ft is an arithmetic scope boundary, not a determination of legal living area.',
['Dated plan / zone IDs / verified dimensions','Retained equipment / columns / stairs / access','Footprint / finish area / excluded utility zones','Professional dimension and suitability questions','Layout revisions / dependent quantities / evidence'],
['Finish area and footprint remain distinct.','Dimensions do not become code approvals.','Retained utility space is explicit.'], 'Ask bidders to acknowledge the same finish-area definition and current plan.')

chapter('Resolve water and moisture questions before finishes','Covering a symptom does not establish that its cause is resolved.',[
'Record observed damp areas, staining, odors and prior water events with dates and locations. Keep accessible evidence and previous reports without diagnosing the cause. Ask qualified providers to assess the relevant source and the scope needed before enclosing or covering affected areas.',
'EPA mold guidance explains the importance of moisture control [2]. Use the actual professional assessment and applicable product requirements to establish readiness. This book provides no mold diagnosis, cleanup method, waterproofing detail or universal moisture threshold.',
'Separate assessment, source-related work, interior repair and finish restoration in the proposal where those services differ. A decorative finish package may exclude the work that makes the area ready. Retain the responsible provider and evidence required to close the issue.',
'Keep unresolved conditions as gates affecting selections, dates and budget. A contingency amount does not approve work or guarantee that every water-related problem is covered. Review the forecast after actual findings rather than assuming the first allowance is complete.'
], 'An invented assessed scenario has $300 investigation, $2,500 defined source-related work and $700 finish restoration. All categories are confirmed non-overlapping.', [('Assessment','$300'),('Defined source-related work','$2,500'),('Restoration','$700'),('Defined scenario','$3,500')],
'The example is not a remediation recommendation or a typical price. Actual findings determine the scope and readiness.',
['Dated observations / prior water records / locations','Qualified assessment / source questions / findings','Readiness requirements / responsible verifier','Assessment / remedy / restoration inclusions','Open gate / evidence / revised cost and timing'],
['Symptoms are distinct from diagnosed causes.','Finish readiness has supporting evidence.','Restoration is not assumed inside source work.'], 'Resolve the relevant moisture findings before authorizing dependent finish purchases or enclosure.')

chapter('Include a radon decision record','Appearance and odor cannot establish the radon condition.',[
'Use current EPA radon resources and an appropriate qualified source to determine the testing and follow-up approach for the actual home [3]. EPA explains that testing is needed to know radon levels. A dry-looking or newly finished basement is not evidence of a particular result.',
'Keep the test report, method context, provider or responsible source and date with the project record. Have the appropriate professional explain the result and any needed next steps. This planner gives no test placement, duration, interpretation threshold or mitigation-system design.',
'If further work is recommended, obtain a defined proposal and coordinate its interfaces before finishing affected areas. Clarify responsibilities for access, power, restoration, follow-up and retained documentation as relevant to the actual system.',
'Separate an unresolved radon question from approved cost. A budget line or a purchased test kit does not establish an acceptable result. Keep the decision gate open until the relevant evidence and follow-up requirements are documented.'
], 'A fictional owner file needs three records: the applicable test result, the qualified explanation of next steps and evidence of any required follow-up. Two are available and one remains pending.', [('Expected decision records','3'),('Available records','2'),('Pending follow-up evidence','1'),('Gate closed','No')],
'This count does not describe radon levels or recommend a technical response. Use actual current guidance and qualified advice.',
['Current guidance / responsible testing source','Actual report / date / context / provider','Qualified explanation / required next steps','Defined work / access / restoration / follow-up scope','Evidence pending / decision owner / finish dependencies'],
['Appearance is not treated as a test result.','Technical interpretation stays with the appropriate source.','Follow-up remains part of the scope.'], 'Resolve the radon evidence and any relevant follow-up before closing dependent finish decisions.')

chapter('Confirm access, stairs and proposed escape arrangements','The floor plan must work under the actual requirements.',[
'Mark existing stairs, doors, windows, routes and proposed room uses on the current plan. Ask qualified providers and the actual local authority to establish the applicable access and emergency escape requirements. This guide supplies no universal opening size, stair dimension or legal-bedroom rule.',
'Keep existing conditions separate from the proposed design. A window used for light is not automatically evidence that a sleeping-room proposal meets the relevant requirements. Record the assessment and approved solution from the responsible parties.',
'Price complete changes including structural questions, exterior work, access, protection and restoration as assessed. A window supply price can omit substantial work at the opening and outside the wall. Assign every required interface a provider.',
'Connect approvals and installation evidence to the room-use decision. Do not market or label a space as approved merely because a finish contractor completed its decorative work. Retain the actual documentation needed for the proposed use.'
], 'A fictional assessed opening scenario has $900 selected product, $2,100 defined installation and external work, and $400 restoration.', [('Product supply','$900'),('Installation and external scope','$2,100'),('Restoration','$400'),('Defined scenario','$3,400')],
'The example does not specify a compliant opening or authorize a use. Actual requirements and design must be established locally.',
['Current stairs / openings / routes / room uses','Qualified and local requirement questions','Approved design / assessment / document versions','Product / external work / restoration / interfaces','Required completion evidence / use status / records'],
['Requirements come from actual local review.','Product-only prices are not complete scope.','Decorative completion is not use approval.'], 'Ask the design team and relevant authority to resolve access and escape questions for the intended use.')

chapter('Coordinate wall, floor and ceiling assemblies','Usable area depends on the actual approved build-up.',[
'Ask the qualified provider to define proposed floor, wall and ceiling assemblies for the actual conditions and use. Record the product and design references, retained elements and unresolved questions. This book gives no insulation, vapor-control, fire, structural or fastening specification.',
'Identify interfaces with moisture-related work, services, openings and retained equipment. A finish layer is only part of an assembly. Ask who confirms compatibility and who retains the supporting documents before comparing supply prices.',
'Use professionally established dimensions to review the resulting room and access layout. Additional layers can affect usable space and connections, but owner arithmetic cannot determine technical suitability. Update the scope when the assembly changes.',
'Reconcile supply, installation, preparation and protection across proposals. A complete package may already include some accessories. Keep them visible so the comparison neither omits necessary scope nor adds the same component twice.'
], 'A fictional assembly proposal has $2,000 supply, $1,400 installation and $600 defined preparation. The installer confirms that accessories are already in supply.', [('Supply including accessories','$2,000'),('Installation','$1,400'),('Preparation','$600'),('Defined assembly scope','$4,000')],
'No separate accessory allowance is added. The example does not prescribe a basement assembly.',
['Approved assembly / product / design references','Condition and compatibility reviewers / open questions','Interfaces / retained equipment / service access','Resulting dimensions / professionally confirmed layout','Supply / labor / preparation / included accessories'],
['Assembly choices have qualified responsibility.','Interfaces are reviewed together.','Included accessories are counted once.'], 'Obtain the complete assembly schedule and scope before comparing finish-layer prices.')

chapter('Assess heating, cooling and ventilation scope','New room use needs an assessed service plan.',[
'Give the responsible HVAC provider the proposed layout, use and current system information. Ask for the assessment supporting the proposed comfort and ventilation approach. Existing equipment age or house floor area alone does not determine the correct solution for a changed basement.',
'Record served zones, retained equipment and supporting work. Ask who confirms compatibility, distribution, controls and applicable requirements. This guide performs no load, capacity, duct or ventilation calculation and gives no installation procedure.',
'Compare complete installed alternatives with the same desired outcomes. A small equipment price may exclude connections, distribution, access or restoration. Keep unresolved assumptions and professional decisions attached to the scenario.',
'Include operating guidance, relevant checks and warranty records in the accepted scope. A finished ceiling should not remove needed service access without appropriate design. Coordinate the service plan before dependent finishes are closed.'
], 'An invented assessed option includes $2,400 equipment and distribution work, $600 supporting connections and $300 restoration.', [('Equipment and distribution','$2,400'),('Supporting connections','$600'),('Restoration','$300'),('Defined service option','$3,300')],
'The numbers do not establish system suitability or expected energy savings. Use actual provider assessment and scope.',
['Current layout / intended use / existing system records','Qualified assessment / proposed service / served zones','Retained components / controls / compatibility owner','Connection / access / restoration / finish interfaces','Checking / operating guidance / warranty / handover'],
['The service option has an assessment basis.','Supporting work is included.','Finish design retains required access.'], 'Coordinate the assessed comfort and ventilation scope before final ceiling and room selections.')

chapter('Plan electrical, lighting and communication work','A room outlet count is not a capacity assessment.',[
'List the intended activities and selected equipment for the proposed rooms, then give that information to the qualified electrical provider. Ask which assessment, design and approval questions apply. This planner supplies no circuit, wiring, panel or load-calculation instructions.',
'Separate lighting, power, controls, communication and any required supporting work in the scope. Record retained components and new-work boundaries. An existing outlet location does not establish that the proposed use or equipment is adequately served.',
'Coordinate product selections and routes with the room layout and other services. Ask who handles openings, protection, checking and restoration. A decorative light allowance may exclude installation or supporting electrical work.',
'Keep actual professional records and completion evidence with the accepted proposal. If the intended equipment or room use changes, ask for a relevant reassessment before procurement. Do not make a technical decision from a low fixture price.'
], 'A fictional assessed electrical package has $1,800 defined electrical work, $400 light fixtures and $300 restoration. Fixture supply is expressly excluded from the electrical line.', [('Electrical work','$1,800'),('Fixture supply','$400'),('Restoration','$300'),('Defined package','$2,500')],
'Do not add fixture supply if the actual package already includes it. The example is not a design or local price estimate.',
['Room activities / selected equipment / current plan','Qualified assessment / retained and new boundaries','Lighting / power / controls / communication scope','Product supply / labor / access / restoration owners','Approval / checking / completion evidence / changes'],
['Capacity decisions remain with qualified providers.','Fixture supply and installed work are distinguished.','Use changes trigger relevant review.'], 'Request an electrical proposal based on the same layout and actual intended equipment.')

chapter('Price plumbing and bathroom interfaces','The fixture is one part of the complete room.',[
'Ask a qualified plumbing provider to assess the proposed fixtures, existing services and relevant requirements. Retain the design and findings for the actual layout. This planner performs no drainage, supply, venting, pumping or water-heating design.',
'Identify the supporting scope required to make the room usable, including assessed access, openings, waterproofing-related interfaces and restoration. Assign each task to the appropriate provider. A plumbing fixture allowance may cover supply only.',
'Compare alternatives using complete installed scope and ongoing obligations. A different layout or system may affect other trades and future access. Do not decide suitability by comparing only a toilet, shower or pump product price.',
'Connect the service design to finish sequencing and relevant approval records. Keep product care, operating guidance and warranty responsibilities in the handover file. Qualified providers must confirm actual readiness and completion.'
], 'A fictional bathroom scenario has $1,200 fixture supply, $3,000 assessed plumbing scope and $1,300 other defined room interfaces, confirmed non-overlapping.', [('Fixture supply','$1,200'),('Plumbing package','$3,000'),('Other room interfaces','$1,300'),('Defined bathroom scenario','$5,500')],
'The example excludes any unstated work. Actual site conditions and proposed use determine the requirements.',
['Fixture and room layout / assessed service requirements','Qualified design / existing service / approval questions','Access / opening / finish interfaces / providers','Supply / installation / supporting scope / ongoing duties','Sequencing / checks / care / completion records'],
['Fixture prices are not installed room totals.','Supporting interfaces have owners.','Technical suitability uses actual assessments.'], 'Ask for the complete bathroom and service-interface scope before choosing fixtures.')

chapter('Protect utility and storage access','A finished layout must retain practical responsibilities.',[
'Map retained equipment, service routes, storage and access needs with the responsible providers. Ask them to establish actual clearances and requirements. This book supplies no universal service-space dimension or equipment-room design.',
'Record which areas remain unfinished and how the household can reach them. A decorative enclosure or storage decision should not assume that future service access can be sacrificed. Keep the approved layout and access obligations with the finish scope.',
'Include doors, removable components, protection, lighting and other assessed interface work where relevant. A finish area total may omit those services. Reconcile them with the electrical, HVAC, plumbing and general contractor packages.',
'At handover, confirm that the retained routes and provider-required access arrangements match the accepted design. Keep unresolved items on the punch list rather than treating a visually complete room as a complete utility interface.'
], 'A fictional layout retains an 80 sq ft utility zone and a 40 sq ft storage zone within a 600 sq ft footprint, with no overlap.', [('Footprint','600 sq ft'),('Utility zone','−80 sq ft'),('Storage zone','−40 sq ft'),('Remaining proposed room zones','480 sq ft')],
'The arithmetic does not establish adequate service space or usable living area. Qualified review determines the actual layout.',
['Retained equipment / routes / storage zones','Provider-defined access requirements / current design','Unfinished boundaries / household access / interfaces','Door / lighting / enclosure / package inclusions','Handover check / unresolved access items / records'],
['Service access is professionally established.','Retained zones are counted once.','Visual completion does not close access gaps.'], 'Review the proposed storage and utility boundaries with the service providers before enclosure.')

chapter('Select finishes against actual readiness and care needs','A product label does not resolve a site condition.',[
'List the selected floor, wall, ceiling, trim and other finishes by zone. Ask the responsible provider to confirm suitability for the assessed conditions, intended use and complete assembly. A moisture-related marketing label does not establish that a site issue has been resolved.',
'Keep preparation, accessories, installation and interfaces with each product selection. Record actual manufacturer requirements and relevant readiness evidence. This planner does not prescribe a universal moisture limit or finish installation method.',
'Compare upgrades by their incremental complete cost over the same baseline. Identify credits for replaced scope and additional supporting work. A material-only premium can understate the effect on the whole room.',
'Retain product references, care obligations, return terms and useful spare-stock decisions. Do not promise that a selected finish prevents every future water problem or guarantees an invisible repair. Use actual product and provider information.'
], 'A fictional finish upgrade adds $600 material and $250 installation, while replacing a confirmed $200 baseline accessory already in the accepted price.', [('Material premium','$600'),('Labor premium','$250'),('Confirmed omitted accessory','−$200'),('Net defined upgrade','$650')],
'The credit must be confirmed and applied once. Product suitability remains a separate qualified decision.',
['Exact finishes / zone / product references','Assessed conditions / suitability / readiness evidence','Preparation / accessories / labor / interfaces','Baseline / premiums / confirmed credits / net change','Care / returns / spare stock / final labels'],
['Labels are not treated as site clearance.','Complete upgrade cost includes interfaces.','Credits have evidence and are counted once.'], 'Confirm selected-product suitability and the complete incremental installed price before approval.')

chapter('Sequence the work around readiness gates','Finishes should follow resolved prerequisites.',[
'Create a provider-confirmed sequence covering assessments, design, approvals, relevant condition work, services and finishes. Name the owner and evidence for each gate. A scheduled date does not itself establish that the area is ready for the next stage.',
'Keep household routes, storage, noise and temporary arrangements with the sequence. Ask providers to communicate restrictions and readiness for access or use. This workbook supplies no site-safety, ventilation or occupancy procedure.',
'Connect product lead times and owner selections to the relevant stages. If a prerequisite changes, revise dependent dates and prices before procurement. A late fixture choice can affect more than the product delivery line.',
'Retain the agreed process for unexpected conditions and changes. Record the actual finding, approved scope and cost effect instead of allowing a general basement allowance to authorize undefined work.'
], 'A fictional sequence has six gates. Four are evidenced complete, one awaits a provider report and one depends on that report.', [('Evidenced complete','4'),('Report pending','1'),('Dependent gate pending','1'),('Open gates','2')],
'Five scheduled stages would not make the pending gates complete. Use actual provider evidence before proceeding.',
['Assessment / design / approval / service / finish gates','Responsible owner / required evidence / current status','Household routes / storage / provider use guidance','Selection and delivery dependencies / revised dates','Unexpected findings / approved changes / cost impact'],
['Dates are distinct from readiness.','Dependencies reach selections and orders.','Unexpected work uses a defined approval process.'], 'Ask the contractor to identify the evidence needed before each enclosure or finish stage.')

chapter('Compare the complete basement scenario','A finish-area rate is a summary of defined scope.',[
'Combine the current condition findings, intended use and approved layout with the full work packages. Identify included, excluded, allowance and unresolved lines. Do not compare a dry decorative refresh with an assessed room conversion as if the area alone makes them equivalent.',
'Include professional services, required supporting work, access, restoration and owner costs where relevant. Reconcile overlaps across providers. Keep reserve separate from defined construction and record which uncertain conditions still need assessment.',
'Retain the area definition beside any cost ratio. Total footprint, selected finish area and approved usable area can be different records. A ratio from a hypothetical scenario is not a market range or a proposal for the actual home.',
'Save the accepted scope, changes, local decisions and relevant completion evidence. The owner record supports review but does not certify moisture, radon, structural condition or occupancy. Keep actual provider findings and follow-up obligations available after handover.'
], 'A fictional scenario has $25,000 defined work, $2,000 professional services, $1,000 owner costs and $3,000 reserve, using a stated 500 sq ft finish area.', [('Defined work','$25,000'),('Professional services','$2,000'),('Owner costs','$1,000'),('Reserve','$3,000'),('Funding scenario','$31,000'),('$31,000 / 500','$62 per finish sq ft')],
'The $62 ratio summarizes invented all-in inputs. It is not a basement-cost benchmark or a guarantee of suitability.',
['Actual findings / intended use / layout / area basis','Package inclusions / exclusions / allowances / unresolved','Professional / owner / access / restoration costs','Reserve / total / ratio / excluded model effects','Accepted scope / completion evidence / care / follow-up'],
['Scenarios have matched use and condition assumptions.','The area denominator is explicit.','Technical conclusions remain with actual evidence.'], 'Request matched complete proposals and resolve condition gates before using a finish-area ratio to choose.')

method(2,'Build the all-in basement remodeling budget')
method(5,'Normalize contractor proposals')
method(6,'Review the live cost forecast')
method(17,'Approve changes and reconcile the reserve')
method(18,'Close out and retain project records')
SOURCES=[('1','FTC: Home Repair Scams','https://consumer.ftc.gov/features/pass-it-on/home-repair-scams'),('2','EPA: Mold, Moisture and Your Home','https://www.epa.gov/mold/brief-guide-mold-moisture-and-your-home'),('3','EPA: Radon','https://www.epa.gov/radon')]

STORE=dict(slug='basement-remodeling-budget-planner',title='Basement Remodel Cost Guide',category='Basement Remodeling',amount=1399,route='/api/download-basement-guide',number=14,test='scripts/test_basement_delivery.mjs',
description='A 64-page basement planning guide with 19 worked examples and 19 fillable worksheets. Organize condition assessments, room-use questions, service interfaces, finishes and complete funding scenarios.',
eyebrow='Resolve the conditions before pricing the finishes',why_title='Why buy this basement planning guide?',why='A basement finish price can omit the work that makes the space ready for its intended use. This guide connects condition questions, responsible providers and the full room scope before a total is compared.',
benefits=[('Make readiness visible.','Record moisture and radon evidence, professional questions and unresolved decisions.'),('Connect the complete room scope.','Include access, assemblies, services, utility routes and restoration alongside selected finishes.'),('Check the funding comparison.','Use consistent area definitions, complete packages, owner costs and reserve scenarios.')],
reader='U.S. homeowners planning a basement remodel or reviewing complete contractor proposals. Actual providers and the relevant authority must establish condition findings, design, requirements and approved use.',
difference_title='What does the paid guide add to a calculator?',difference='It connects area and cost arithmetic to condition gates, responsible providers, sequencing and handover, with 19 worked cases, 19 worksheets and 95 fillable fields.',
limits='One-time purchase. No subscription. Example costs and dimensions are hypothetical. No local price, suitable room use, radon result or moisture condition is promised.',
helps=['Define the proposed use and actual feasibility questions','Separate footprint, finish area and retained utility zones','Keep moisture and radon evidence with readiness decisions','Coordinate access, assemblies, services and finish scope','Compare complete scenarios with explicit area definitions'],
sequence='intended use, measured baseline, condition and radon records, access, assemblies, services, finish readiness, complete scenarios and closeout',
example='A fictional 30 × 20 ft footprint is 600 sq ft. Excluding a confirmed 100 sq ft utility zone leaves 500 sq ft in the proposed finish scope. A $31,000 all-in teaching scenario would equal $62 per finish sq ft. Neither the area nor the ratio determines approved living space or a local price.',
calculator_html='<p>Use the free <a href="/calculators/">HomeCostEngine calculators</a> to check individual quantities and the <a href="/calculators/contractor-quote-comparison">quote comparison calculator</a> with complete proposals. Keep the actual use, condition and area assumptions attached.</p>',
examples='Work through finish-area boundaries, condition-related cost categories, decision records, complete opening and service scopes, utility zones, net finish changes and all-in area ratios. Six general owner-budget chapters use the HomeCostEngine renovation method with basement adaptation; thirteen chapters add basement-specific decisions. No testing, remediation, installation or occupancy-approval procedure is supplied.')
PDF_META=dict(key='basement',subject='Original basement owner planning guide and 19 fillable worksheets',header='BASEMENT REMODEL PLANNING',cover_title='Basement Remodel<br/>Cost Guide',cover_lines=['Resolve the conditions. Define the room use.','Compare the complete basement scope.'],
preface=['Basement remodeling connects the intended room use to existing conditions, services and local requirements. This guide helps you organize the owner evidence and complete scope before treating a finish price as the whole project.',
'Start with the brief, proposed use and measured baseline. Resolve condition, moisture, radon, access and relevant professional questions, then connect assemblies, comfort, electrical, plumbing, utility access and selected finishes.',
'Each working chapter contains an explanation, an original hypothetical case and a reusable sheet. Six general owner-budget chapters use the HomeCostEngine renovation method with basement adaptation. Thirteen chapters add basement condition and scope decisions.',
'All costs, quantities and ratio results are invented USD teaching inputs, not local market prices or design specifications. A proposed finish area is not automatically approved living area. Room labels and product marketing do not establish condition or suitability.',
'Qualified providers and the actual local authority must establish assessments, technical requirements, relevant testing, design and approved use. This book supplies no testing, remediation or installation procedure. Keep reports, actual results, accepted scope, changes and completion evidence with the sheets.'],
workflow=['Record proposed uses, zones, constraints and the spending boundary.','Collect verified dimensions, actual condition evidence and qualified design information.','Match room use, condition assumptions, complete service scope and selected finishes.','Track accepted work, allowance replacements, payments, obligations and approved changes.','Reconcile the final scope. Retain actual reports, care instructions and open follow-up.'],
afterword='A useful basement plan connects intended use to actual assessed conditions, appropriate design and complete funding. Keep readiness gates visible, preserve the exact area basis behind every ratio, and retain professional evidence and follow-up obligations after the decorative work is complete.')

