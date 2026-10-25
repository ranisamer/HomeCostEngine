"""Original electrical upgrade owner planning cases, with established owner-budget methods."""
from pathlib import Path
import runpy,copy
base=runpy.run_path(str(Path(__file__).with_name('renovation-blueprint.py')))
CHAPTERS=[]
def chapter(title,deck,paragraphs,example,rows,conclusion,prompts,checks,task):
    CHAPTERS.append(dict(title=title,deck=deck,paragraphs=paragraphs,example=example,rows=rows,conclusion=conclusion,prompts=prompts,checks=checks,task=task))
def method(index,title):
    c=copy.deepcopy(base['CHAPTERS'][index]);c['title']=title
    replacements={'renovation':'electrical upgrade','Make the kitchen usable for two cooks':'Support the assessed electrical needs of the household','buy new cabinets':'buy electrical equipment','A bathroom project in a one-bath home has a different temporary-use problem from the same work in an empty property.':'Work interrupting household electrical service creates different temporary-use needs from work in an unoccupied area.','fixture allowance':'finish-selection allowance'}
    def adapt(s):
        for a,b in replacements.items():s=s.replace(a,b)
        return s
    for k in ['deck','example','conclusion','task']:c[k]=adapt(c[k])
    for k in ['paragraphs','prompts','checks']:c[k]=[adapt(x) for x in c[k]]
    CHAPTERS.append(c)

method(0,'Define the electrical upgrade brief')
chapter('Record needs and observations from safe information','The owner brief is not an electrical inspection.',[
'List the household outcomes and planned equipment affecting the project. Record accessible existing documents, service reports and prior proposals. Ask a qualified electrician to supply technical equipment details where needed rather than opening or investigating equipment yourself.',
'Describe observed issues by location and timing without assigning a diagnosis. Keep actual professional findings separate from owner reports. CPSC provides home electrical-safety resources [2]; use appropriate qualified or emergency response for actual urgent concerns.',
'Do not remove covers, touch internal components, perform electrical tests or attempt repair for this workbook. It is a purchasing and cost-planning record. The electrician must assess condition, urgency and the relevant technical requirements.',
'Give the same current brief and known records to providers asked to prepare proposals. Label unknown information clearly. A complete-looking owner inventory built from guesses can misdirect the assessment and comparison.'
], 'A fictional brief contains five requested outcomes, three existing document references and two observations awaiting professional assessment.', [('Requested outcomes','5'),('Document references','3'),('Unassessed observations','2'),('Owner diagnosis supplied','None')],
'The counts organize the brief and do not determine system condition, capacity or urgency.',
['Household outcomes / planned equipment / locations','Existing documents / reports / exact sources','Observed issue / time / location / no diagnosis','Qualified assessment questions / appropriate urgency response','Unknown details / provider / next action'],
['No owner equipment opening or testing is required.','Observations are distinct from findings.','Urgent concerns are not delayed for price ranking.'], 'Provide the needs record and request a qualified assessment before choosing electrical equipment.')

chapter('Separate panel, service and circuit scope','Similar sales labels can describe different work.',[
'Ask the electrician to identify the actual scope in plain language, including what equipment and parts of the electrical system are retained or changed. Panel-related work, utility-service-related work and new circuit work need explicit boundaries in the proposal.',
'Record who assesses each requirement and who performs or coordinates the relevant tasks. A panel replacement price should not be assumed to include a utility service change or every new equipment connection. Keep the actual design and provider findings with the scope.',
'Use the same desired outcomes when comparing offers. A less expensive proposal may solve a narrower need rather than supply the same complete project. Identify that difference before interpreting the totals as equivalent alternatives.',
'This handbook gives no electrical design, connection, replacement or sizing instruction. It organizes the owner questions and responsibilities so the actual qualified professionals can define the work and evidence.'
], 'A fictional proposal has three categories: $2,000 panel-related work, $1,500 separately assessed service-related work and $800 defined new circuit work.', [('Panel-related scope','$2,000'),('Service-related scope','$1,500'),('Circuit scope','$800'),('Complete stated scenario','$4,300')],
'The $2,000 headline is not the $4,300 complete scenario. Technical need and scope are determined by actual providers.',
['Desired outcomes / current assessment references','Panel / service / circuit boundaries','Retained equipment / excluded supporting tasks','Electrician / utility / other-provider responsibilities','Complete price / scope differences / unresolved questions'],
['Sales labels are translated into actual tasks.','Utility and circuit work are not assumed included.','Comparable scope precedes total ranking.'], 'Ask bidders to identify exactly which panel, service and circuit work their offer includes.')

chapter('Request the professional capacity assessment','Visible empty spaces do not answer every capacity question.',[
'Give the electrician current household use and planned equipment information. Ask for the assessment supporting the proposed option and an explanation of relevant assumptions. The owner should be able to identify the report and outcome without performing a technical calculation.',
'Distinguish physical equipment space from the professional assessment of electrical capacity and suitability. An unused position or a familiar rating on a document does not by itself approve a proposed new load. Keep the actual provider conclusion and supporting record.',
'Ask what alternatives were considered and what information could change the recommendation. A later equipment selection may require reassessment. Record the selected models and planned uses with the assessment version.',
'This guide performs no load calculation and provides no circuit, conductor, breaker or service-size selection. Do not use its cost examples to decide whether an existing system can support additional equipment.'
], 'A fictional decision record has four required inputs. Three are supplied to the electrician and one planned equipment specification is still missing.', [('Required input records','4'),('Supplied','3'),('Equipment specification pending','1'),('Final selection approved by this record','No')],
'The missing specification is a decision gate. Counting input records does not calculate capacity.',
['Assessment provider / method reference / date','Current and planned equipment / actual specifications','Relevant assumptions / professional conclusion / alternatives','Missing inputs / changed selections / reassessment triggers','Report version / proposal link / technical decision owner'],
['Space and assessed capacity remain distinct.','No owner load shortcut is used.','Actual equipment changes trigger relevant review.'], 'Ask the electrician to explain the assessment basis and identify any input still needed.')

chapter('Build the future equipment schedule','Plan the real options without assuming all must be installed now.',[
'List possible future appliances, heating and cooling equipment, vehicle charging or other planned uses with their status. Separate committed selections, likely future options and vague possibilities. ENERGY STAR home-upgrade resources include planning for additional electric equipment [3].',
'Give qualified providers actual product information where selected and ask how uncertain future choices should be handled. Do not invent loads or purchase a larger system solely because a list contains many possible devices.',
'Compare stages with complete supporting scope and repeated-service assumptions visible. Doing some coordinated work now may differ from repeating access or visits later, but the technical feasibility and actual tradeoff require professional review.',
'Keep future options outside current committed cost until approved. A readiness decision should state what it provides and what remains conditional. The schedule supports the design conversation rather than prescribing electrification or capacity.'
], 'A fictional equipment plan has two committed selections, two possible later choices and one undefined idea.', [('Committed selections','2'),('Later options','2'),('Undefined idea','1'),('All five treated as approved work','No')],
'An option count does not establish electrical demand or require an upgrade. Use actual professional assessment.',
['Current / committed / later / undefined equipment status','Exact selected models / provider inputs','Professional readiness alternatives / limitations','Staged work / repeated services / complete cost tradeoff','Current approval / future decision / review trigger'],
['Possible equipment is not counted as committed scope.','No demand is inferred from device counts.','Readiness has an explicit boundary.'], 'Share the equipment schedule with the electrician and label every unselected future option.')

chapter('Compare assessed repair and upgrade alternatives','Different approaches can meet different boundaries.',[
'Ask the electrician to describe viable alternatives for the actual findings and household goals. Keep condition-related work, added functionality and optional readiness changes distinct. A proposed panel upgrade is not automatically the remedy for every observed issue.',
'Record what each alternative retains and changes, its technical basis and relevant limitations. Keep utility or authority dependencies attached. Do not use a low-price alternative if the responsible provider has found it unsuitable.',
'Compare complete installed costs, supporting work, disruption and future assumptions. The least immediate spending may involve a narrower outcome or later work. Avoid assigning a guaranteed useful life or future saving to justify one option.',
'Retain the chosen scope and professional explanation. This workbook does not determine technical viability or contract rights. Its function is to preserve a fair comparison of actual assessed alternatives.'
], 'A fictional assessed option is $2,600 now. A broader future-readiness option is $3,400 on a defined complete scope. Future spending is not modeled.', [('Assessed current-scope option','$2,600'),('Broader readiness option','$3,400'),('Initial difference','$800'),('Guaranteed later saving','Not established')],
'The $800 difference buys the stated scope only. Actual suitability and future requirements remain part of the decision.',
['Actual findings / viable options / technical provider','Retained and changed elements / limitations','Same household outcomes / meaningful differences','Complete installed prices / disruption / future assumptions','Selected option / rationale / accepted evidence'],
['Condition and optional readiness are separate.','Unsuitable options are not ranked as cheapest.','Future benefits are not promised.'], 'Ask the electrician to explain the complete scope and limitations of each viable alternative.')

chapter('Coordinate the utility boundary and lead time','The electrician may not control every prerequisite.',[
'Ask the electrician and actual utility to establish responsibilities for relevant service coordination. Record contacts, required information, current decisions and who submits or books each task. A contractor estimate does not necessarily include every utility-related service or charge.',
'Distinguish preliminary discussion, submitted request, confirmed arrangement and completed prerequisite. Keep the actual evidence and date for each. A tentative utility date should not be treated as a guaranteed construction or return-to-service time.',
'Price confirmed separate charges and retain unresolved fees visibly. Do not replace an unknown utility obligation with zero to make the project appear funded. Ask the responsible source for the scope and terms.',
'Connect utility dependencies to household arrangements and other providers. This handbook supplies no meter, service, disconnection or reconnection procedure. Actual qualified providers and the utility must determine the work and readiness.'
], 'A fictional coordination record has three prerequisites: one confirmed, one submitted and one awaiting required information.', [('Confirmed','1'),('Submitted only','1'),('Information pending','1'),('All prerequisites complete','No')],
'A submitted request is not a confirmed service appointment or approval.',
['Actual utility / electrician contacts / responsibility','Required information / submission owner / record IDs','Discussion / submitted / confirmed / completed status','Separate charges / unresolved fees / actual terms','Household timing / other providers / readiness evidence'],
['Utility scope is not assumed inside the bid.','Dates retain their actual status.','No technical service procedure is provided.'], 'Confirm the utility responsibilities and actual prerequisite status before accepting a fixed work date.')

chapter('Track local approvals and final evidence','A permit allowance is not the issued record.',[
'Ask the relevant local authority and qualified project team what approvals, submissions, visits and final records apply to the actual scope. Record the current requirements and responsible provider. This guide gives no nationwide permit exemption, code edition or approval rule.',
'Keep fee estimates, submitted applications, issued approvals and completed required checks separate. A contractor may include only some administrative or review services. Clarify the accepted boundary and any owner responsibility.',
'Link actual technical documents and selected equipment to the current submission or approved scope. If work changes, ask the appropriate parties whether reassessment or updated documents are needed. Do not assume an earlier record covers every revision.',
'Retain the final evidence required for the actual work with the owner file. An owner visual review or completed payment does not replace relevant professional or authority checks. The workbook organizes status without certifying compliance.'
], 'A fictional local-review register has four items: two issued records, one application still submitted and one final check not yet completed.', [('Issued records','2'),('Submitted application','1'),('Final check pending','1'),('Remaining open items','2')],
'The count is not a compliance finding. Actual authority and professional records determine completion.',
['Relevant authority / actual requirements / responsible party','Fee / application / issued / final status','Current scope / technical documents / equipment references','Changes / reassessment questions / revised records','Required final evidence / retention / unresolved items'],
['Fee payment and issued approval are distinct.','Actual requirements have a verified source.','Visual review does not replace required checks.'], 'Ask who obtains and retains every relevant final record before the work begins.')

chapter('Specify equipment through qualified responsibility','A familiar brand name does not establish compatibility.',[
'Ask the electrician to identify the exact proposed equipment and components and the basis for their suitability. Keep manufacturer references, current technical documents and relevant approvals with the proposal. The owner should not select internal components from a generic shopping list.',
'Record retained equipment and who confirms its condition and compatibility with the actual design. A product that physically fits or has a similar label is not automatically an approved substitute. This book provides no component-matching or installation instruction.',
'Compare complete defined packages rather than a bare enclosure price. Supporting components, labor, checks, records and interfaces can change the total. Ask for exclusions and conditional work in writing.',
'Review substitutions through the responsible qualified provider before procurement. Update the design, price and relevant documents where needed. Save actual installed product references at handover without opening equipment to obtain them.'
], 'A fictional proposal has $700 specified equipment/components and $1,500 defined qualified installation/support work, confirmed non-overlapping.', [('Specified equipment/components','$700'),('Qualified installed scope','$1,500'),('Defined package','$2,200'),('Owner component selection','Not established by this example')],
'The figures prescribe no equipment or installation. Actual design and compatibility decisions remain with qualified providers.',
['Exact proposed equipment / manufacturer references','Qualified suitability / retained component review','Supply / install / supporting components / checks','Complete package / exclusions / conditional work','Substitution approval / revised documents / actual labels'],
['Compatibility has a qualified owner.','Bare equipment is not the complete package.','No owner equipment opening is needed.'], 'Request the exact equipment schedule and qualified suitability confirmation with the proposal.')

chapter('Define downstream circuits and equipment interfaces','A panel project can leave other required work outside scope.',[
'Map the actual equipment and areas served by proposed downstream work using the professional design. Keep the desired household function and selected product information with each scope line. This book supplies no wiring, circuit, conductor or protection specification.',
'Ask which tasks are included in the panel-related package and which belong to separate equipment installers or other trades. New appliances or service changes can involve interfaces beyond the panel. Give each required task one accountable provider.',
'Compare quantities only on their stated approved basis. A counted circuit line does not imply that all circuits have equal design or installed cost. Do not average unlike tasks into a universal unit rate.',
'Retain the relevant checks, operating information and final records for the complete accepted work. If the equipment selection changes, ask the responsible professionals to review affected design and scope before procurement.'
], 'An invented accepted scope has $800 defined downstream work and a separate $300 equipment-installer interface, expressly excluded from each other.', [('Downstream electrical scope','$800'),('Equipment-installer interface','$300'),('Complete defined addition','$1,100'),('Circuit design','Not supplied here')],
'The $1,100 includes only stated work. Technical requirements and counts must come from the actual professional design.',
['Actual equipment / served areas / design references','Panel package / downstream / other-installer boundaries','Task owners / prerequisites / supporting work','Quantity and unit basis / complete inclusion check','Changed selections / required checks / retained final evidence'],
['Circuit counts do not establish design.','Other-installer tasks are visible.','Equipment changes trigger relevant review.'], 'Ask all affected installers to confirm their interface boundaries against the same current equipment schedule.')

chapter('Price access, protection and restoration','Supporting surfaces and site work need a clear owner.',[
'Ask the qualified providers to define the access and supporting work needed for the actual scope. Record affected rooms, surfaces and external areas with relevant assessment questions. This book gives no opening, excavation, routing or technical work procedure.',
'Assign protection, contents moving, access creation, electrical work and restoration to the relevant providers. An electrical price may exclude wall finishes or external surfaces. Keep those exclusions visible instead of assuming the household will complete them.',
'Define the restoration outcome and actual limits. Patch, decoration and matching existing finishes can have different scopes. Request written clarity for broad phrases that could be interpreted differently.',
'Reconcile supporting work across the electrical, utility and general contractor offers. Count shared services once where confirmed and use the agreed process for unexpected conditions. Retain actual completion evidence for the supporting tasks.'
], 'A fictional scenario adds $250 access preparation, $200 protection and $550 restoration outside the electrical package.', [('Access preparation','$250'),('Protection','$200'),('Restoration','$550'),('Supporting-work addition','$1,000')],
'The addition applies only when those services are confirmed excluded elsewhere. Actual site conditions determine scope.',
['Assessed access / affected areas / material questions','Open / protect / work / restore roles','Restoration outcome / finish and matching limitations','Fixed services / overlaps / accepted exclusions','Unexpected conditions / approvals / evidence'],
['Supporting tasks have providers.','Owner technical work is not assumed.','Shared services are not duplicated.'], 'Get the complete access and restoration responsibilities in writing before comparing the project totals.')

chapter('Plan interruption and household arrangements','Outage duration and readiness must come from responsible providers.',[
'Discuss the household functions affected by the proposed work and identify any needs requiring special arrangements. Record provider communications, contacts and the actual interruption plan. Do not place sensitive personal details on a general contractor comparison sheet.',
'Ask the electrician and utility to establish the technical sequence and return-to-service responsibilities. This guide provides no switching, isolation, temporary-power, connection or restart procedure. Temporary equipment arrangements require appropriate qualified review.',
'Keep estimated duration distinct from confirmed readiness. Delays in a prerequisite can affect other trades and household costs. Ask who communicates a change and how additional services are approved under actual terms.',
'Record owner-support costs separately from electrical work and count them once. A plan should remain useful if a tentative date changes. Keep urgent professional guidance outside normal budget ranking.'
], 'A fictional household scenario has $180 temporary arrangements and $120 separate storage/moving support, neither inside the contractor package.', [('Temporary arrangements','$180'),('Storage and moving','$120'),('Separate owner-support total','$300'),('Return-to-service time','Provider confirmation required')],
'The costs do not establish a safe interruption duration or technical solution. Use actual responsible-provider guidance.',
['Affected functions / household arrangements / privacy boundary','Electrician and utility sequence / contacts','Estimated and confirmed timing / readiness owner','Delay terms / communication / approval process','Separate owner costs / supporting providers / revised plan'],
['No owner isolation or temporary-power method is supplied.','Readiness is separate from a calendar estimate.','Owner-support costs appear once.'], 'Confirm the provider interruption and communication plan before accepting the work dates.')

chapter('Compare pricing models and conditional work','A fixed panel number may not be a fixed complete project.',[
'Record fixed scope, allowances, measured work, fees and unresolved items separately. Ask for the exact inclusion boundary of each headline. A fixed price can still exclude utility, access, restoration or concealed-condition work.',
'For conditional items, identify the evidence, quantity or trigger and the actual approval process. Keep unapproved options outside committed cost. A general contingency line should not silently authorize undefined technical work.',
'Reconcile deposits and payment stages to the accepted total. Actual local rules and contract obligations need relevant review; this book supplies no universal lawful deposit or payment schedule. Keep actual invoice dates and unpaid obligations visible.',
'Compare complete matched scenarios before selecting an offer. A lower equipment or panel package can lose its advantage when required excluded tasks are added. Do not invent low allowances for unresolved required work to make the comparison appear complete.'
], 'Fictional bid A is $2,200 excluding $1,000 confirmed supporting work. Bid B is $3,000 including the same support scope. Other scope is assumed matched.', [('A with required support','$3,200'),('Matched bid B','$3,000'),('Scenario difference','$200 in B’s favor'),('Unresolved required work','Not assumed zero')],
'The headline gap reverses in the stated scenario. Actual technical scope and written terms must still match.',
['Fixed / allowance / measured / fee / unresolved lines','Actual inclusions / utility and supporting exclusions','Conditional evidence / scope / approval process','Payment total / actual dates / unpaid obligations','Matched complete scenarios / remaining gates / rationale'],
['Fixed package and complete project are distinct.','Conditional work has an approval boundary.','Unresolved required work is not priced at zero.'], 'Request complete matched offers and resolve required exclusions before comparing the headline totals.')

chapter('Retain the complete handover and final cost record','Payment and visual completion do not replace technical evidence.',[
'Request the actual equipment references, provider records and relevant authority or utility completion evidence for the accepted work. Keep document responsibility explicit. The owner file should not rely on opening equipment or performing tests.',
'Ask the qualified provider for the actual operating and care information the household needs and the process for reporting concerns. Keep warranty issuer, scope and exclusions with current contacts. This guide provides no operational troubleshooting or repair procedure.',
'Record incomplete tasks and observations with locations, responsible providers and follow-up dates. Distinguish technical findings from owner observations. A decorative patch or completed invoice does not close every outstanding system question.',
'Reconcile accepted scope, approved changes, confirmed credits, payments and unpaid obligations. Save the current equipment schedule and final documents together. A useful owner record supports later qualified decisions without certifying future performance.'
], 'An invented accepted complete scope is $4,300 with a $200 approved addition and a confirmed $100 credit. Payments total $3,500.', [('Accepted scope plus addition','$4,500'),('Confirmed credit','−$100'),('Reconciled defined cost','$4,400'),('Paid / unpaid','$3,500 / $900')],
'The $900 is an outstanding obligation in the example. Actual completion and payment requirements use the relevant agreement and evidence.',
['Actual equipment / provider / authority / utility records','Operating and care guidance / warranties / contacts','Punch list / observations / technical follow-up','Accepted scope / changes / confirmed credits','Final costs / payments / obligations / indexed owner file'],
['Technical completion has appropriate evidence.','No owner internal inspection is required.','Unpaid obligations remain visible.'], 'Collect the relevant final records and reconcile the cost and follow-up file before archiving the project.')

method(2,'Build the all-in electrical upgrade budget')
method(5,'Normalize contractor proposals')
method(6,'Review the live cost forecast')
method(17,'Approve changes and reconcile the reserve')
method(18,'Close out and retain project records')
SOURCES=[('1','FTC: Home Repair Scams','https://consumer.ftc.gov/features/pass-it-on/home-repair-scams'),('2','CPSC: Home Electrical Safety Checklist','https://www.cpsc.gov/safety-education/safety-guides/electronics-and-electrical-home/home-electrical-safety-checklist'),('3','ENERGY STAR: Home Upgrade planning resources','https://www.energystar.gov/products/energy_star_home_upgrade')]

STORE=dict(slug='electrical-upgrade-cost-planning-guide',title='Electrical Panel Replacement Cost Guide',category='Electrical Upgrade Planning',amount=1399,route='/api/download-electrical-guide',number=18,test='scripts/test_electrical_delivery.mjs',
description='A 64-page electrical upgrade owner guide with 19 worked examples and 19 fillable worksheets. Clarify assessed panel, service and circuit scope, utility responsibilities, supporting work and complete costs.',
eyebrow='Define the complete project behind the panel price',why_title='Why buy this electrical planning guide?',why='A panel-related headline may exclude service coordination, new circuits, access or restoration. This guide helps you ask for complete assessed scope and retain the evidence behind the owner decision.',
benefits=[('Clarify the work boundary.','Separate panel, service, downstream circuits and other-installer responsibilities.'),('Keep technical decisions accountable.','Record the qualified assessment, actual equipment schedule and relevant utility and local gates.'),('See complete funding and timing.','Include supporting work, household arrangements, conditional costs and unpaid obligations.')],
reader='U.S. homeowners reviewing an assessed electrical upgrade or panel-replacement proposal. Qualified electricians, the actual utility and relevant authorities must establish condition, capacity, design and requirements.',
difference_title='What does the paid guide add to a calculator?',difference='A complete owner comparison and evidence workflow around the financial totals, with 19 worked cases, 19 reusable worksheets and 95 fillable fields. It is not a DIY electrical manual.',
limits='One-time purchase. No subscription. Example prices and quantities are hypothetical. No technical capacity, suitable equipment, approval, completion date or saving is promised.',
helps=['Create a safe needs and document brief','Separate panel, service and downstream scope','Record qualified assessment and actual equipment decisions','Coordinate utility, local review, access and restoration','Compare complete offers and retain final evidence'],
sequence='household needs, qualified assessments, scope boundaries, equipment plans, utility and local decisions, supporting work, complete pricing and handover',
example='Fictional bid A is $2,200 but excludes $1,000 of confirmed required support. Bid B is $3,000 with that matched support included. The complete defined comparison is A: $3,200; B: $3,000. These amounts are invented, and actual suitability and scope require qualified review.',
calculator_html='<p>Use the free <a href="/calculators/contractor-quote-comparison">quote comparison calculator</a> with complete matched proposals. The guide adds the assessment, responsibility, prerequisite and handover records around those totals.</p>',
examples='Work through panel/service/circuit boundaries, missing assessment inputs, future equipment status, utility gates, complete equipment packages, downstream interfaces, restoration, household arrangements, excluded-work comparisons and final obligations. Six general owner-budget chapters use the HomeCostEngine renovation method with electrical adaptation; thirteen chapters add electrical owner decisions. No load calculation, equipment-opening, wiring, isolation, connection or installation procedure is supplied.')
PDF_META=dict(key='electrical',subject='Original electrical upgrade owner planning guide and 19 fillable worksheets',header='ELECTRICAL OWNER PLANNING',cover_title='Electrical Panel<br/>Replacement<br/>Cost Guide',cover_lines=['Clarify the scope. Keep qualified decisions clear.','Compare the complete project cost.'],
preface=['An electrical upgrade connects the assessed household need to actual equipment, service and supporting work. This guide helps you organize owner questions and complete funding without performing technical assessment or design.',
'Start with the brief and safe existing records. Separate panel, service and circuit scope, request the professional assessment and identify current versus future equipment. Then connect utility, local review, exact equipment, interfaces, access and household arrangements.',
'Each working chapter contains an explanation, an original hypothetical case and a reusable sheet. Six general owner-budget chapters use the HomeCostEngine renovation method with electrical adaptation. Thirteen chapters add electrical owner-scope and evidence decisions.',
'All prices, counts and timing examples are invented USD teaching inputs, not local quotes or technical requirements. Empty equipment spaces and owner observations do not establish capacity or condition. No incentive or future saving is assumed.',
'Qualified electricians, the actual utility and relevant authority must establish condition, urgency, capacity, design and required records. This book provides no load calculation, equipment opening, wiring, isolation or installation procedure. Keep actual findings, accepted scope, changes and final evidence with the sheets.'],
workflow=['Record desired household function, actual equipment plans and funding boundaries.','Collect qualified findings, current technical records and confirmed responsibility limits.','Match panel, service, circuit, utility, supporting-work and household-cost scope.','Track accepted work, conditional approvals, payments and unpaid obligations.','Reconcile final cost and retain actual equipment, qualified completion and care records.'],
afterword='A useful electrical owner record connects the qualified findings to complete scope, actual provider responsibilities and realistic funding. Keep technical capacity and equipment decisions with the responsible professionals, resolve utility and local gates, and retain completion evidence with the final cost record.')

