"""Original home addition planning and cost cases, with established owner-budget methods."""
from pathlib import Path
import runpy,copy
base=runpy.run_path(str(Path(__file__).with_name('renovation-blueprint.py')))
CHAPTERS=[]
def chapter(title,deck,paragraphs,example,rows,conclusion,prompts,checks,task):
    CHAPTERS.append(dict(title=title,deck=deck,paragraphs=paragraphs,example=example,rows=rows,conclusion=conclusion,prompts=prompts,checks=checks,task=task))
def method(index,title):
    c=copy.deepcopy(base['CHAPTERS'][index]);c['title']=title
    replacements={'renovation':'home addition project','Make the kitchen usable for two cooks':'Create usable additional space for the household','buy new cabinets':'choose an addition layout','A bathroom project in a one-bath home has a different temporary-use problem from the same work in an empty property.':'Opening a connection to the occupied home creates different temporary-use needs from work in a detached area.','fixture allowance':'finish-selection allowance'}
    def adapt(s):
        for a,b in replacements.items():s=s.replace(a,b)
        return s
    for k in ['deck','example','conclusion','task']:c[k]=adapt(c[k])
    for k in ['paragraphs','prompts','checks']:c[k]=[adapt(x) for x in c[k]]
    CHAPTERS.append(c)

method(0,'Define the home addition brief')
chapter('Compare the space alternatives first','An addition is one possible response to a household need.',[
'Describe the space problem in functional terms: room use, access, privacy, storage or another outcome. Compare the proposed addition with feasible alternatives such as changing the existing layout or reducing the desired scope. Qualified providers must establish which alternatives are suitable for the actual property.',
'Keep the same required outcome when comparing options, and identify genuine differences. A smaller room with different access may not provide the same function. Record tradeoffs rather than treating every extra square foot as equally useful.',
'Use complete scenario costs including relevant design, supporting work, owner costs and temporary arrangements. A lower building-package price may exclude substantial existing-home changes. Keep future sale value outside the funding plan unless supported and appropriately reviewed; this book makes no resale-return prediction.',
'Retain the reasons for the chosen alternative and the assessments still needed. An early preference is not design approval or permission to build. If professional findings change feasibility, reopen the alternatives rather than forcing the original concept into an unsupported budget.'
], 'A fictional layout change costs $45,000 and an addition scenario costs $90,000 on a stated complete scope. Both are assumed to meet the same basic room-use requirement for this comparison.', [('Existing-layout scenario','$45,000'),('Addition scenario','$90,000'),('Immediate cost difference','$45,000'),('Suitability and other outcomes','Require actual review')],
'The lower cost does not prove equal privacy, access or long-term usefulness. Compare the actual outcomes and feasibility.',
['Space problem / desired room function','Alternative layouts / scope / professional feasibility','Matched outcomes / meaningful differences','Complete scenario cost / excluded effects','Preferred option / rationale / open assessments'],
['Options are compared against the same need.','Resale value is not promised.','Preference is distinct from approved design.'], 'Ask the design provider to compare feasible ways to achieve the same household outcome.')

chapter('Check local feasibility and property constraints','A proposed footprint needs local evidence.',[
'Collect the property information the responsible designer and local authority need to review the addition. Identify boundaries, existing approvals, relevant records and known shared-property constraints. An owner sketch or real-estate listing is not a substitute for the required project information.',
'Ask which planning, building, access, site or other requirements apply to the actual proposal. Seattle publishes a house-addition resource as one local example [2]. Its rules are not nationwide standards and cannot determine the permissible size or location of an addition elsewhere.',
'Record each feasibility question with the appropriate source, responsible provider and next decision. Keep preliminary discussion, formal application and issued approval separate. A fee paid or a submission accepted does not mean the addition has been approved.',
'Price the relevant assessment and design work before committing to downstream orders. If a constraint changes the proposed footprint or function, revise the concept and complete scenario. Do not hide an unresolved feasibility issue inside a generic construction reserve.'
], 'A fictional feasibility register has five questions. Two have written answers, two await professional information and one awaits the authority response.', [('Written answers','2'),('Professional information pending','2'),('Authority response pending','1'),('Questions still open','3')],
'Three open questions mean the concept remains conditional. They are not assumed to have favorable answers.',
['Property records / boundaries / current concept','Relevant local authority / professional sources','Feasibility questions / written status / dates','Design or application prerequisites / responsible owner','Concept changes / assessment costs / downstream limits'],
['Local examples are not used as national rules.','Submission and approval remain distinct.','Open feasibility affects the budget status.'], 'Resolve the property-specific feasibility questions with the actual authority and design team.')

chapter('Record the existing home and site','The addition must connect to a real property, not a blank plot.',[
'Create a dated record of existing rooms, site access, adjoining elements and areas to remain. Link prior drawings, reports and relevant service records. Mark unverified dimensions and concealed conditions so they are not treated as confirmed construction information.',
'Ask qualified providers to identify needed site and existing-building assessments. Structural, soil, drainage, utility or material questions may affect the scope. This book gives no investigation, excavation, sampling or technical diagnosis procedure.',
'For relevant older-home disturbance, refer actual material and paint questions to appropriate professionals using current requirements. EPA provides renovation guidance for lead-related concerns [3]. A budget worksheet does not establish that a material is safe to disturb.',
'Keep each finding linked to the affected design and cost package. An addition may require work inside the existing home as well as the new footprint. Retain those interfaces rather than describing the entire project as new square footage only.'
], 'A fictional site record has three new-work zones, two retained zones and one existing-home connection zone awaiting assessment.', [('New-work zones','3'),('Retained zones','2'),('Connection assessment zone','1'),('Total indexed zones','6')],
'Zone counts organize the record but do not verify site suitability, dimensions or a safe work method.',
['Existing-home and site zones / dated records','Prior plans / reports / verified and unknown inputs','Professional assessments / utility and material questions','Retained areas / access / protection / connection scope','Findings / affected design / cost / decision dates'],
['Concealed conditions remain explicit.','Assessments have qualified owners.','The existing-home interface is part of scope.'], 'Provide bidders with the same current site and existing-home information.')

chapter('Assign the design and coordination team','Every critical decision needs a responsible author.',[
'List the professional roles needed for the actual addition and ask how they coordinate. Identify responsibility for project design, structural questions, services, approvals and construction review where applicable. This planner does not decide required professional qualifications or legal appointments.',
'Record who prepares each document, who reviews it and which version becomes the basis for pricing. A contractor should not need to choose between contradictory drawings without a clear decision owner. Keep unresolved design interfaces in a question register.',
'Clarify which professional services are included, optional, staged or excluded in each appointment. A concept design fee may not include detailed documents, submissions or later review. Ask for written scope and payment stages rather than assuming one fee covers the whole project.',
'Use the responsibility record when a design change affects the addition. Coordinate revised quantities, services, approvals and cost before procurement. An owner approval of appearance does not replace the appropriate professional review.'
], 'A fictional professional-services scenario has $4,000 concept work, $5,000 detailed documents and $2,000 defined review services, with no overlap.', [('Concept service','$4,000'),('Detailed documents','$5,000'),('Defined later review','$2,000'),('Professional-services scenario','$11,000')],
'The figures are invented. They illustrate why a concept fee alone is not the complete professional budget.',
['Required roles / qualified providers / appointment scope','Document author / reviewer / version / pricing basis','Concept / detail / submission / review inclusions','Fees / staged payments / exclusions / owner decisions','Change coordination / affected documents / approval record'],
['Each technical document has a responsible author.','Professional-service boundaries are written.','Appearance approval is separate from technical review.'], 'Confirm the complete professional scope before using an early design fee in the funding plan.')

chapter('Define the area behind a cost-per-foot number','A rate needs both a cost boundary and an area definition.',[
'Record whether an area refers to the addition footprint, gross floor area, usable internal area or another defined measure. Use the professional drawing and measurement basis for the actual project. Two different denominators can produce different rates from the same total.',
'For a simple rectangle, length times width provides geometric area. It does not determine how local authorities, designers or appraisers measure regulated or marketable space. Keep the arithmetic distinct from those actual definitions.',
'State what the numerator includes: building package, installed work, professional costs, owner costs, tax or reserve. A package-only rate cannot be compared directly with an all-in rate. Always retain the complete dollar amount beside the ratio.',
'Use a ratio as a summary of a defined scenario, not a universal prediction for a different addition. Size, interfaces, site conditions, selected rooms and fixed costs can change the relationship. Ask for project-specific scope and proposals before relying on a multiplication.'
], 'A fictional 20 × 15 ft footprint is 300 sq ft. A $90,000 building package equals $300 per footprint sq ft. A $105,000 broader scenario equals $350 on the same denominator.', [('20 × 15','300 sq ft footprint'),('$90,000 / 300','$300 per footprint sq ft'),('$105,000 / 300','$350 per footprint sq ft'),('Difference in included cost','$15,000')],
'Neither rate is a local benchmark. The difference comes from the scenario cost boundary, not a changed footprint.',
['Drawing / area definition / verified dimensions','Geometric area / exclusions / professional basis','Cost numerator / included and excluded categories','Total cost / matching denominator / resulting ratio','Comparable scenario limits / actual proposal questions'],
['Area definition is stated.','Package and all-in ratios are distinguished.','A ratio is not used as a project quote.'], 'Ask every rate-based estimate to state its exact area and cost inclusions.')

chapter('Budget foundation and structural scope','Quantity checking cannot establish structural design.',[
'Ask the responsible design professionals to establish the foundation, structural and existing-building requirements. Record the current documents and relevant assessment findings. This book provides no footing, beam, reinforcement, load or connection specification.',
'Define the work packages needed to deliver the approved structural scope, including relevant site preparation, access, inspection and restoration. Clarify what is included in a contractor offer and which tasks depend on unresolved conditions.',
'Use conditional quantities and rates only where the scope, measurement and approval process are written. A provisional excavation amount is not a guarantee that all ground-related work is covered. Retain the trigger and responsible assessor for any revision.',
'Reconcile new-work and existing-home costs so support, protection and connection scope are counted once. If an assessment changes the design, revise all dependent quantities and dates before treating an earlier price as final.'
], 'A fictional professionally defined structural package contains $18,000 new-work scope and $4,000 existing-home supporting work. Both expressly exclude an unresolved site item.', [('Defined new-work package','$18,000'),('Existing-home support scope','$4,000'),('Defined subtotal','$22,000'),('Unresolved site item','Separate decision gate')],
'The $22,000 is not a complete structural prediction until excluded required work is resolved.',
['Professional design / assessments / document versions','New and existing structural package boundaries','Site / access / review / restoration inclusions','Conditional quantities / rates / approval triggers','Unresolved findings / revised design / forecast effects'],
['Design belongs to qualified professionals.','Existing-home support is visible.','Unresolved scope remains outside the defined subtotal.'], 'Obtain the current professionally defined structural scope before comparing its prices.')

chapter('Connect roof, walls and weather protection','The joint with the existing home needs accountable scope.',[
'Identify the new roof and wall areas, openings and interfaces with retained construction on the professional documents. Ask who designs and confirms the actual assembly and weather-protection details. This planner supplies no flashing, waterproofing, framing or roofing procedure.',
'Clarify responsibility for supply, installation, transitions, checks and restoration. A separate roof and wall offer can each omit the joint between them. Give the interface a clear owner and required completion record.',
'Ask the contractor to describe temporary protection and the sequence for opening or closing affected areas. Keep weather decisions and occupant restrictions with the provider plan. A selected finish date is not evidence that the existing home will remain usable throughout the work.',
'Price complete alternatives with compatible selected products and supporting work. A material-only upgrade may alter installation, transitions or later care. Retain the actual product references and professional confirmation with the accepted package.'
], 'An invented envelope scenario has $15,000 roof and wall work, $1,500 defined existing-home interface work and $800 temporary protection, all non-overlapping.', [('Roof and wall package','$15,000'),('Existing-home interface','$1,500'),('Temporary protection','$800'),('Defined envelope scenario','$17,300')],
'The example prices complete boundaries without prescribing an assembly or protection method.',
['Current roof / wall / opening / interface documents','Qualified assembly and detail responsibility','Supply / install / check / restore package owners','Temporary protection / weather / occupied-use plan','Complete prices / product changes / care records'],
['The existing-home joint has an owner.','Temporary protection is in the scope.','Material-only prices are not treated as complete assemblies.'], 'Review the roof-to-wall and new-to-existing interfaces with the responsible providers.')

chapter('Price openings and existing-room changes','The connection can alter more than the added area.',[
'Mark proposed openings, retained rooms and affected circulation routes on the current plans. Ask qualified providers to establish structural and other technical requirements. An owner floor-plan sketch cannot authorize removing a wall or changing a doorway.',
'List the existing-room work caused by the connection: protection, service changes, finishes, trim, access and restoration as assessed. A new addition package may exclude these tasks even though the room connection needs them.',
'Keep each affected surface or system linked to a package and price. Reconcile any work already included in structural or service offers. Similar labels need clarification before deleting or adding a line.',
'Review how the connection sequence affects household use and temporary arrangements. Record who confirms readiness for access or use and what evidence is needed. This chapter organizes the owner scope without providing demolition, support or installation instructions.'
], 'A fictional existing-room connection adds $2,500 defined opening-related work, $900 finish restoration and $600 temporary separation, with structural design outside this narrow example.', [('Opening-related scope','$2,500'),('Finish restoration','$900'),('Temporary separation','$600'),('Defined connection additions','$4,000')],
'The $4,000 includes only the stated scope and is not a design or complete price for a real opening.',
['Current connection plan / affected rooms / routes','Qualified technical decisions / prerequisite evidence','Protection / services / finishes / restoration lines','Package overlaps / confirmed exclusions / providers','Occupancy sequence / readiness / approved changes'],
['Openings use professional design.','Existing-room restoration is not omitted.','Scope overlaps are resolved with evidence.'], 'Ask for the existing-room connection scope separately from the new-floor-area package.')

chapter('Coordinate plumbing, electrical and comfort systems','More room area does not prove existing capacity is sufficient.',[
'Give qualified service providers the current addition layout, intended use and selected equipment information. Ask them to assess relevant system needs and the effect on retained services. This book performs no load, capacity, pipe, circuit or heating and cooling design.',
'Record the proposed work and supporting interfaces, including applicable utility coordination, access, approvals and restoration. A connection-only quote may not cover an assessed service upgrade. Keep the actual findings and design basis with the proposal.',
'Compare complete assessed options using the same served areas and outcomes. Different configurations may involve different supporting work. Do not rank an equipment-only price against a full installed system without making that difference visible.',
'Assign responsibility for checks, operating guidance, records and handover. If the room use or selected equipment changes, ask the providers to review the relevant design and cost again. Area arithmetic alone cannot approve a retained service.'
], 'A fictional assessed service scenario has $4,000 electrical work, $3,000 plumbing work and $5,000 comfort-system work, each with stated non-overlapping boundaries.', [('Electrical package','$4,000'),('Plumbing package','$3,000'),('Comfort-system package','$5,000'),('Defined service scenario','$12,000')],
'The figures are invented, not expected trade prices. Actual systems and selected use determine required work.',
['Current use / layout / selected equipment inputs','Qualified service assessments / design references','Utilities / access / approvals / restoration owners','Complete assessed alternatives / retained components','Checking / operating / handover evidence / change triggers'],
['Existing capacity is professionally assessed.','Equipment prices are separate from complete scope.','Changed use triggers relevant review.'], 'Request service proposals based on the same current addition layout and assessed requirements.')

chapter('Build the room fit-out and selection schedule','The shell does not establish the cost of the usable room.',[
'List the finishes, fixtures and equipment required for the selected room use. A bedroom, kitchen, bathroom or other addition can have different scope even with the same footprint. Keep exact selections and unresolved allowances on the room schedule.',
'Connect each product to supply, installation and supporting work. Ask the responsible provider to confirm dimensions, compatibility and technical suitability. Owner approval of appearance does not establish every installation requirement.',
'Replace allowances with actual selected scope using the agreed adjustment terms. Remove the original allowance before adding the confirmed replacement amount. Identify any other package affected by a selection change.',
'Retain delivery, storage, return and care terms for the actual products. A late substitution can alter both the total and the sequence. Keep the complete installed effect visible before approving it.'
], 'A fictional fit-out allowance is $8,000. Final matched selections total $9,200 with an additional confirmed $300 supporting-work change, and the original allowance is replaced.', [('Original allowance removed','−$8,000'),('Selected fit-out added','$9,200'),('Supporting-work addition','$300'),('Increase over original plan','$1,500')],
'Do not add all $9,200 on top of the existing allowance. The complete increase is $1,500 under these assumptions.',
['Room use / finish / fixture / equipment schedule','Exact products / technical reviewer / dimensions','Supply / installation / supporting work inclusions','Allowance replacement / selected costs / dependent changes','Lead times / delivery / returns / care requirements'],
['The room is priced beyond the shell.','Selections have relevant suitability review.','Allowance replacement is counted once.'], 'Ask for a complete fit-out schedule and the net cost of replacing provisional allowances.')

chapter('Include site work, access and restoration','The project boundary extends beyond the new room.',[
'Record assessed external work and the access needed to deliver the addition. Ask responsible providers about relevant ground, drainage, utility, landscaping and adjacent-surface questions. The planner provides no excavation, drainage, utility-location or site-work procedure.',
'Define delivery, equipment, storage, protection and cleanup responsibilities. A constrained route or occupied site may involve fixed services outside a simple area-based construction estimate. Price the actual provider-assessed arrangements.',
'Identify what will be disturbed and the restoration outcome expected. Temporary access across a retained surface can create later work that a building package excludes. Keep the restoration boundary and responsible provider explicit.',
'Reconcile shared logistics across packages and phases. A mobilization already inside one offer should not be added again without a reason. Keep delay terms and any additional visit triggers with the accepted plan.'
], 'An invented site scenario includes $2,000 assessed external work, $700 access logistics and $1,300 restoration, with no overlap.', [('External work','$2,000'),('Access logistics','$700'),('Restoration','$1,300'),('Defined site scenario','$4,000')],
'The $4,000 covers only stated work. Actual site findings and local requirements determine the scope.',
['Site and access record / assessed external questions','Delivery / equipment / storage / protection owners','Disturbed surfaces / restoration outcome / exclusions','Fixed charges / phase overlaps / mobilization terms','Open findings / provider confirmation / revised forecast'],
['External supporting work is visible.','Restoration has a defined outcome.','Shared logistics are counted once.'], 'Ask bidders to show site, access and restoration scope alongside the addition package.')

chapter('Connect approvals, selections and the occupied schedule','A work duration begins after its prerequisites.',[
'Build a provider-confirmed sequence showing assessment, design, approvals, selections, procurement and site readiness before construction stages. Label estimated and confirmed dates. A short building duration may begin long after the owner initial decision.',
'Ask the actual authority and project team about required submissions, visits and completion records. Keep fee estimates, submitted applications and issued approvals distinct. No example here determines local eligibility, required timing or permission to occupy.',
'Map household access, usable rooms and temporary arrangements to the sequence. Record who communicates restrictions and confirms readiness. Price delays only according to actual agreed terms and approved scope changes.',
'Update dependent dates and costs when a prerequisite changes. An unapproved selection or pending authority response should not be hidden behind a confident completion promise. Retain the evidence and responsible owner for each gate.'
], 'A fictional sequence has 30 days of prerequisites followed by 60 days of work, with no overlap and all days treated as calendar days for arithmetic.', [('Prerequisite period','30 days'),('Work period','60 days'),('Total scenario duration','90 calendar days'),('Actual approval timing','Not predicted')],
'The 90 days is invented sequence arithmetic, not an addition timeline benchmark.',
['Prerequisite gates / current documents / owners','Selections / procurement / approvals / readiness status','Work sequence / calendar or working-day basis','Household routes / use restrictions / temporary costs','Revised dates / agreed changes / completion evidence'],
['Start conditions are shown.','Approval timing is not guaranteed.','Occupied-use guidance comes from responsible providers.'], 'Ask for the complete prerequisite-to-handover sequence rather than only an on-site duration.')

chapter('Compare complete addition scenarios','A single rate cannot replace the package and owner-cost record.',[
'Combine the current design, site, structural, envelope, connection, service, fit-out and external scopes into a common comparison. Identify included, excluded, allowance and unresolved lines for each offer. Retain the same area and design basis across scenarios.',
'Add professional services, owner costs and temporary arrangements where they fall outside contractor prices. Reconcile shared work with provider confirmation. Keep reserve separate from defined scope and unresolved assumptions visible.',
'Use the cost-per-foot ratio only after the numerator and denominator are explicit. A broader scenario may show a higher ratio while simply containing more required work. Compare the total funding need and the actual household outcome.',
'Retain the accepted scope, local decisions, design versions and change process. This guide does not provide a construction contract, structural design or actual market valuation. Its value is a clear owner record for asking better questions and checking complete arithmetic.'
], 'A fictional addition scenario contains $90,000 defined building work, $11,000 professional services, $2,200 temporary living and $10,000 reserve for a 300 sq ft footprint.', [('Building work','$90,000'),('Professional services','$11,000'),('Temporary living','$2,200'),('Reserve','$10,000'),('Funding scenario','$113,200'),('$113,200 / 300','$377.33 per footprint sq ft')],
'The rounded ratio summarizes invented all-in assumptions. It is not a local addition-cost benchmark or a contractor quotation.',
['Common current design / site / area definition','Package inclusions / exclusions / allowances / unresolved','Professional / owner / temporary costs / overlap check','Reserve / total funding / ratio calculation and limits','Accepted documents / local decisions / changes / handover'],
['Scenarios use the same area and scope basis.','Reserve is separate from defined construction.','The ratio is labeled a scenario result.'], 'Request complete project-specific proposals and retain the area definition beside every cost-per-foot figure.')

method(2,'Build the all-in home addition budget')
method(5,'Normalize contractor proposals')
method(6,'Review the live cost forecast')
method(17,'Approve changes and reconcile the reserve')
method(18,'Close out and retain project records')
SOURCES=[('1','FTC: Home Repair Scams','https://consumer.ftc.gov/features/pass-it-on/home-repair-scams'),('2','Seattle: House Additions and Remodels (local example)','https://www.seattle.gov/construction-and-inspections/permits/common-projects/house-additions-and-remodels'),('3','EPA: Lead Renovation, Repair and Painting','https://www.epa.gov/lead/lead-renovation-repair-and-painting-program')]

STORE=dict(slug='home-addition-cost-planning-guide',title='Home Addition Cost Per Square Foot Guide',category='Home Additions',amount=1699,route='/api/download-addition-guide',number=13,test='scripts/test_addition_delivery.mjs',
description='A 64-page addition planning guide with 19 worked examples and 19 fillable worksheets. Define the area behind a cost ratio and connect design, site, structure, services, fit-out and owner costs.',
eyebrow='Look beyond the square-foot headline',why_title='Why buy this addition planning guide?',why='A rate per square foot can hide different area definitions and missing work. This guide helps you connect the proposed room to the existing home, site, professional decisions and complete funding plan.',
benefits=[('Understand the ratio.','Keep the area definition and included cost categories visible beside every rate.'),('See the existing-home work.','Record structural questions, connections, services, access and restoration with responsible providers.'),('Compare complete scenarios.','Connect fit-out, professional fees, temporary living and reserve to defined building packages.')],
reader='U.S. homeowners assessing an addition concept or comparing complete proposals. Qualified designers, providers and local authorities must establish actual feasibility, technical requirements and approvals.',
difference_title='What does the paid guide add to a free calculator?',difference='It connects individual quantities to the addition feasibility and owner workflow, with 19 worked cases, 19 worksheets and 95 fillable fields. The exact chapter list shows the questions and records included.',
limits='One-time purchase. No subscription. Example rates, areas, dates and amounts are hypothetical. No local cost benchmark, permitted size or timeline is promised.',
helps=['Compare space alternatives against the same need','Record local feasibility and professional design gates','Define area and cost boundaries behind a square-foot ratio','Include structure, envelope, connections, services and fit-out','Compare complete funding, sequence and owner costs'],
sequence='space alternatives, property feasibility, existing-home records, design roles, area definitions, addition scope, complete scenarios and closeout',
example='A fictional 20 × 15 ft footprint is 300 sq ft. A $90,000 building package gives $300 per footprint sq ft, while a broader $105,000 scenario gives $350 using the same area. The difference is included scope, not a new footprint. Neither figure is a local price benchmark.',
calculator_html='<p>Use the free <a href="/calculators/">HomeCostEngine calculators</a> for individual arithmetic and the <a href="/calculators/contractor-quote-comparison">quote comparison calculator</a> with complete proposals. Retain the actual area and cost definitions.</p>',
examples='Work through matched space alternatives, professional fees, cost-per-foot denominators, complete structure and envelope scopes, existing-room connections, service packages, allowance replacement, site logistics and all-in ratios. Six general owner-budget chapters use the HomeCostEngine renovation method with addition adaptation; thirteen chapters add addition decisions. No construction design or local permit rule is supplied.')
PDF_META=dict(key='addition',subject='Original home addition owner planning guide and 19 fillable worksheets',header='HOME ADDITION PLANNING',cover_title='Home Addition<br/>Cost Per Square<br/>Foot Guide',cover_lines=['Define the area. Connect the whole scope.','Compare the complete addition scenario.'],
preface=['A home addition connects new space to an existing property, services and household. This guide helps you organize the owner questions and complete scope without treating a square-foot rate as a design or contractor quotation.',
'Start with the brief and space alternatives. Resolve local feasibility, existing-home information and professional roles before relying on the area and cost ratios. Then connect structure, envelope, openings, services, fit-out, site logistics and the occupied sequence.',
'Each working chapter contains an explanation, an original hypothetical case and a reusable sheet. Six general owner-budget chapters use the HomeCostEngine renovation method with addition adaptation. Thirteen addition chapters supply project-specific questions and scenarios.',
'All costs, areas and dates are invented USD teaching inputs. Ratio results depend on their exact numerator and denominator. They are not local price ranges, construction specifications, permitted-area determinations or promised completion dates.',
'Qualified providers and the actual local authority must establish feasibility, assessments, design, approvals and work requirements. Seattle guidance appears only as a local example. Keep the approved plans, current scope, orders, changes, invoices and handover records with the sheets.'],
workflow=['Record household needs, space alternatives, constraints and the funding boundary.','Collect current site records, professional findings, approved dimensions and area definitions.','Match complete addition packages and owner costs before comparing totals or ratios.','Track accepted scope, allowances, payments, unpaid obligations and approved changes.','Reconcile final work and credits. Retain approvals, care instructions and the owner file.'],
afterword='A useful addition plan connects the desired space to actual feasibility, professional design, complete existing-home interfaces and funding. Keep every rate beside its area and cost definitions, resolve gates before dependent commitments, and retain the records that explain the accepted scope.')

