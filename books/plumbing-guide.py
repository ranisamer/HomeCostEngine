"""Original plumbing owner planning and cost cases, with established owner-budget methods."""
from pathlib import Path
import runpy,copy
base=runpy.run_path(str(Path(__file__).with_name('renovation-blueprint.py')))
CHAPTERS=[]
def chapter(title,deck,paragraphs,example,rows,conclusion,prompts,checks,task):
    CHAPTERS.append(dict(title=title,deck=deck,paragraphs=paragraphs,example=example,rows=rows,conclusion=conclusion,prompts=prompts,checks=checks,task=task))
def method(index,title):
    c=copy.deepcopy(base['CHAPTERS'][index]);c['title']=title
    replacements={'renovation':'plumbing project','Make the kitchen usable for two cooks':'Restore the defined plumbing function for the household','buy new cabinets':'choose plumbing fixtures','A bathroom project in a one-bath home has a different temporary-use problem from the same work in an empty property.':'Work affecting the only bathroom creates different temporary-use needs from work in a spare room.','fixture allowance':'finish-selection allowance'}
    def adapt(s):
        for a,b in replacements.items():s=s.replace(a,b)
        return s
    for k in ['deck','example','conclusion','task']:c[k]=adapt(c[k])
    for k in ['paragraphs','prompts','checks']:c[k]=[adapt(x) for x in c[k]]
    CHAPTERS.append(c)

method(0,'Define the plumbing project brief')
chapter('Create a fixture and service inventory','Give the concern an exact location and reference.',[
'List the fixtures, equipment and relevant service areas included in the proposed work. Assign an ID and location to each. Use existing documents and accessible labels to record exact products where available, leaving uncertain information unknown rather than guessing.',
'Record observed symptoms with dates, timing and affected locations. Keep a provider diagnosis separate from the owner description. A wet area, slow drain or changed bill can raise a question without identifying the cause or appropriate remedy.',
'Link prior service reports, invoices and warranty records to the relevant item. EPA WaterSense provides home-maintenance resources for water-related questions [2]. Use actual qualified findings to establish work for the current concern.',
'Do not disturb materials, open equipment or attempt technical tests to complete the schedule. The owner inventory is a communication tool, not an assessment or authorization to repair. Retain the same IDs for proposals, changes and handover.'
], 'A fictional work list contains two faucets, one toilet and one water-heating item. A separate retained fixture is recorded but excluded from the proposed scope.', [('Faucets selected','2'),('Toilet selected','1'),('Water-heating item','1'),('Selected items','4')],
'The count does not establish repair scope or technical requirements. Each item still needs the relevant assessment.',
['Item ID / room / exact product if known','Observed symptom / date / timing / location','Prior reports / invoices / warranty references','Selected or retained status / scope boundary','Qualified assessment questions / provider / next action'],
['Symptoms are separate from diagnoses.','Unknown product details remain labeled.','No owner technical testing is needed.'], 'Send the dated item schedule and relevant prior records when booking the assessment.')

chapter('Separate assessment from the repair proposal','A service visit may answer a question before it prices a solution.',[
'Ask what the diagnostic or assessment visit includes and what remains outside its fee. Record the provider, defined task and expected report or explanation. A call-out charge does not automatically include a complete repair.',
'Request the assessed finding and proposed scope in understandable language. Identify any uncertainty, limitation or further investigation needed. Keep the owner observation, professional finding and priced remedy as separate records.',
'Clarify whether additional assessment requires approval and whether any fee is credited against accepted work. Use the actual written terms rather than assuming an industry-wide credit rule. A quoted option is not yet an approved obligation.',
'If findings require urgent attention, follow appropriate qualified or emergency guidance rather than waiting for a normal comparison exercise. This book supplies no diagnostic, isolation or repair procedure. Its purpose is to preserve the evidence behind the cost decision.'
], 'A fictional visit costs $150 and identifies a proposed $400 repair. The owner has approved only the visit; no fee credit has been offered.', [('Approved assessment','$150'),('Unapproved repair proposal','$400'),('Current committed cost','$150'),('If repair is later approved','$550 combined scope')],
'Do not describe the repair as committed or paid before approval. Actual terms determine any credit or additional assessment cost.',
['Assessment fee / exact scope / expected evidence','Observed issue / professional finding / limitations','Proposed remedy / exclusions / further questions','Approval status / fee-credit terms / extra-visit process','Urgent guidance / responsible provider / next decision'],
['A visit fee is not assumed to include the repair.','Options remain separate from commitments.','Actual terms determine fee treatment.'], 'Ask for the assessment scope and written additional-work approval process before the visit.')

chapter('Reconcile call-out, labor and fixed-price terms','The pricing model needs a complete inclusion check.',[
'Identify whether the proposal uses a fixed defined price, hourly work, a minimum charge or another arrangement. Record included labor, materials, travel and other fixed fees. Similar headline prices can have different boundaries.',
'For hourly terms, clarify the unit, minimum, estimated time and approval process for additional work. Distinguish worker-hours from elapsed time and separate material or equipment charges where relevant. This guide supplies no universal labor rate or job duration.',
'For fixed-price work, ask which conditions and exclusions can change the final amount. A fixed total for one assessed repair is not a promise to correct every related concealed issue. Keep the accepted scope and actual terms together.',
'Apply confirmed credits once and retain their evidence. A call-out credit can replace part of the combined charge, but it should not be assumed or deducted twice. Reconcile the complete total before choosing an option.'
], 'An invented offer has a $200 call-out charge and $400 defined repair, with a written $100 credit if that repair is accepted.', [('Call-out','$200'),('Defined repair','$400'),('Confirmed conditional credit','−$100'),('Combined accepted scope','$500')],
'The credit applies only under the stated fictional terms. The example is not a standard pricing practice.',
['Fixed / hourly / minimum / travel pricing basis','Labor / material / equipment / fee inclusions','Estimate limits / concealed conditions / approval process','Actual fee-credit evidence / applicable conditions','Complete total / no duplication / accepted terms'],
['Pricing units and minimums are visible.','Fixed scope has explicit exclusions.','Credits are applied once under actual terms.'], 'Request one written total showing all fees and credits for the scope you intend to accept.')

chapter('Compare repair, component replacement and upgrade','A new product can solve a different problem from a repair.',[
'Ask the qualified provider to identify feasible alternatives based on actual condition. Describe which component is repaired or replaced and which connected elements remain. A product upgrade may change appearance or function without resolving an unrelated source of the concern.',
'Compare the desired outcome, immediate cost, disruption and ongoing obligations for each alternative. Do not assign an invented remaining life or assume every new product reduces water or energy use in the actual household.',
'Include access, supporting services and restoration where they differ. An option with a lower fixture price can require additional work. Keep the actual assessment and selection compatibility with the comparison.',
'Record the chosen scope and reasons separately from optional preferences. If qualified guidance limits viable options, retain that evidence instead of ranking an unsuitable alternative as cheapest. This chapter supplies no repair or installation instruction.'
], 'A fictional assessed component repair is $180. A different upgrade option is $450 supply plus $250 installation and $100 restoration.', [('Defined repair','$180'),('Upgrade complete scope','$800'),('Immediate difference','$620'),('Future reliability or savings','Not established')],
'The alternatives must actually address the required outcome before the $620 difference is useful.',
['Assessed condition / feasible alternatives / retained items','Required outcome / optional function or appearance','Supply / install / support / restoration differences','Ongoing care / warranty / unresolved assumptions','Chosen scope / evidence / rationale / provider guidance'],
['Options address the stated need.','Future life and savings are not invented.','The upgrade uses its complete installed price.'], 'Ask the provider to explain what each option changes and what it leaves unresolved.')

chapter('Check measured quantities and fixed charges','A linear-foot number does not define the technical work.',[
'Record the professionally defined work boundary and quantity basis for measured scope. Keep length, counts, visits and fixed services distinct. An owner measurement is a discussion input until the responsible provider confirms it.',
'For arithmetic, multiply a verified quantity by its matching quoted rate. State what that rate includes and whether access, fittings, labor, testing, disposal or restoration are separate. This handbook provides no pipe sizing, material selection, routing or pressure design.',
'Retain the actual endpoint and area references so quantity changes can be traced. A revised length can affect supporting work and dates as well as material. Ask the provider to explain the complete effect before approving it.',
'Do not treat a rate per foot as a complete project quotation when required work remains undefined. Keep conditional quantities and their approval terms visible. A correct multiplication cannot verify technical suitability or site conditions.'
], 'A fictional professionally defined measured scope is 35 linear ft at $25 per linear ft, plus a separate agreed $150 fixed service. Technical specifications are intentionally absent.', [('35 × $25','$875'),('Separate fixed service','$150'),('Defined measured subtotal','$1,025'),('Technical suitability','Not determined by arithmetic')],
'The rate and quantity are invented and include only their stated scope. They are not a pipe specification or market benchmark.',
['Work boundary / endpoints / provider-confirmed quantity','Units / rate / included tasks and materials','Fixed services / access / restoration exclusions','Quantity revision / dependent scope / approval terms','Technical design references / open findings'],
['Unlike units remain separate.','A rate has explicit inclusions.','Quantity arithmetic does not establish design.'], 'Ask for the measured-scope basis and complete fixed-fee inclusions before comparing unit rates.')

chapter('Include access, openings and restoration','Reaching the work can be a separate cost.',[
'Ask the qualified providers to identify the access needed for the assessed work and which surfaces or areas are affected. Keep the actual scope, protection and relevant material-assessment questions with the proposal. This book supplies no cutting, excavation or opening procedure.',
'Assign who creates access, performs the plumbing work and restores the affected finish or site. A plumbing repair price may exclude those supporting services. An unassigned restoration task is a scope gap even when the repair total is fixed.',
'Define the restoration outcome and exclusions. Patch, paint, trim, paving or landscape work can involve different boundaries and providers. Avoid assuming a general make-good phrase means complete matching of every finish.',
'Reconcile supporting work across contractors and keep concealed-condition terms explicit. When an assessment changes the access plan, revise the complete cost and sequence before authorizing extra work. Retain photographs and completion evidence where appropriate.'
], 'An invented assessed repair has $500 plumbing work, $200 defined access and $350 agreed finish restoration, confirmed non-overlapping.', [('Plumbing repair','$500'),('Access service','$200'),('Finish restoration','$350'),('Defined complete scenario','$1,050')],
'The $500 repair line is less than the complete scenario. Actual surfaces and provider scope determine the additional work.',
['Assessed access / affected areas / current records','Open / repair / restore providers and boundaries','Protection / material questions / relevant review','Restoration outcome / exclusions / matching limits','Concealed conditions / approved revisions / completion evidence'],
['Access and restoration have owners.','Broad phrases are clarified.','Required supporting services enter the total once.'], 'Obtain the complete access and restoration scope with the repair proposal.')

chapter('Specify fixtures and owner-supplied products','The exact selection affects the installation boundary.',[
'Record the selected fixture or equipment reference, included accessories and supply owner. Ask the installer to confirm compatibility and actual site requirements before purchase. A product selected for appearance may need supporting components or a different scope.',
'Clarify what an owner-supplied item changes in receiving, installation, fault handling and warranty responsibilities. Use the actual provider and supplier terms. Do not assume a contractor must install every product supplied by the owner at an unchanged price.',
'Compare the complete installed alternatives including delivery, accessories and restoration. A cheaper retail price can be offset by extra services or unsuitable inclusions. Keep the exact baseline and confirmed credits when replacing an allowance.',
'Retain labels, order records and product documents with the item schedule. Review substitutions before procurement and record who approves them. This book does not determine product fit, water quality suitability or installation requirements.'
], 'A fictional owner-supplied fixture is $220 with $30 accessories and $250 agreed installation. A matched complete supplied-and-installed offer is $520.', [('Owner product and accessories','$250'),('Agreed installation','$250'),('Owner-supply scenario','$500'),('Matched supplied/installed offer','$520'),('Narrow price difference','$20')],
'The $20 gap ignores any unmodeled delivery or term differences. Confirm suitability and responsibility before treating the options as equivalent.',
['Exact product / accessories / supply owner','Installer compatibility and site confirmation','Receiving / faults / warranty / actual terms','Complete price / allowance replacement / confirmed credit','Order / labels / substitutions / approval evidence'],
['Owner supply has explicit responsibilities.','Retail price is not the complete comparison.','Suitability is checked before purchase.'], 'Get installer acceptance of the exact owner-supplied item and its complete terms before ordering.')

chapter('Review water-heating alternatives as installed systems','The heater price does not establish the whole project.',[
'Ask qualified providers to assess household demand, actual site conditions and feasible water-heating options. Department of Energy selection resources discuss system types, sizing and fuel considerations [3]. Use the actual professional assessment rather than a universal shortcut.',
'Record retained services and supporting work for each option, including relevant connections, access, approvals and restoration. This planner supplies no fuel, electrical, venting, temperature, pressure or water-heater installation procedure.',
'Compare complete installed cost, care obligations and explicitly assumed operating scenarios. A product efficiency label or equipment price alone does not predict household savings. Keep actual tariffs, use and other assumptions visible where a provider offers a cost model.',
'Ask who provides required checks, operating guidance, product records and warranty support. Review any conversion or substitution with all affected qualified providers before procurement. A new product choice can affect more than the plumbing line.'
], 'A fictional assessed water-heating option includes $950 equipment, $800 installation/supporting scope and $250 restoration, with no overlap.', [('Equipment','$950'),('Installation and support','$800'),('Restoration','$250'),('Defined installed option','$2,000')],
'The numbers are invented and prescribe neither capacity nor configuration. Actual feasibility and complete scope require assessment.',
['Household needs / current equipment / site information','Qualified assessment / feasible options / actual models','Supporting services / access / approvals / restoration','Complete cost / operating assumptions / ongoing duties','Checking / operating / warranty / cross-trade coordination'],
['Sizing and configuration remain professionally assessed.','Equipment is separate from installed scope.','No guaranteed operating saving is assumed.'], 'Request complete assessed water-heating options rather than comparing bare equipment prices.')

chapter('Define drain and sewer assessment scope','A camera record and a repair proposal answer different questions.',[
'Describe the reported concern and give the provider relevant prior reports and location information. Ask what the proposed assessment covers and what limitations remain. A single image or a brief verbal description may not define a complete repair scope.',
'Retain the actual findings, location references and qualified explanation before comparing remedies. This handbook provides no drain-clearing, chemical, camera-operation, excavation, pipe-repair or confined-space procedure.',
'Separate investigation, proposed repair, access and site restoration costs. Ask how each alternative addresses the assessed issue and which components remain. A limited intervention should not be assumed to renew the entire service or guarantee future performance.',
'Record relevant responsibility and approval questions with the actual utility, authority or provider. Shared or off-property work may need clarification. Do not treat a private-property repair price as covering an unresolved service boundary.'
], 'A fictional assessed scenario has $250 investigation, $1,800 defined repair and $700 site restoration, with no fee credit assumed.', [('Assessment','$250'),('Defined repair','$1,800'),('Restoration','$700'),('Complete stated scenario','$2,750')],
'The example does not select a repair method. Actual findings, boundaries and relevant requirements determine viable work.',
['Reported concern / prior reports / location evidence','Assessment scope / limitations / qualified findings','Defined alternatives / retained service / outcome limits','Investigation / repair / access / restoration cost','Utility or shared boundary / approvals / responsible owner'],
['Images are interpreted by the appropriate provider.','Assessment and repair have distinct scope.','Unresolved service boundaries remain visible.'], 'Request the assessment evidence and complete repair/restoration boundary before comparing remedies.')

chapter('Review water-use claims and product expectations','A lower-use label does not predict the entire bill.',[
'Record the household outcome behind a proposed product change, such as function, convenience or water use. Use exact product documentation and appropriate qualified advice to establish suitability. A broad claim of efficiency is not a complete product specification.',
'Compare usage with billing units, period length and occupancy context visible. A changed bill can reflect rates, fees or household behavior as well as fixture use. Keep those differences separate rather than crediting one repair with every cost change.',
'Use a clearly labeled scenario if estimating a product-related difference. Record event count, volume per event and excluded uses without presenting those inputs as universal household behavior. The arithmetic is a question tool, not a diagnosis or promised saving.',
'Retain actual subsequent observations and provider follow-up. A completed installation does not guarantee a specific bill result. Any water-quality, pressure or health-related concern requires the appropriate qualified assessment rather than a purchase based on this workbook.'
], 'For arithmetic only, an invented usage scenario changes one assumed event from 2 gallons to 1.5 gallons, occurring ten times per day. No other use is modeled.', [('Assumed reduction per event','0.5 gallon'),('10 assumed events per day','5 gallons per day'),('30-day scenario','150 gallons'),('Actual bill saving','Not established')],
'The event volumes and frequency are invented. The result is not an actual fixture rating or household saving claim.',
['Desired outcome / exact product / suitability source','Actual bills / units / days / occupancy and rate context','Scenario event count / volumes / excluded uses','Qualified questions / pressure or quality concerns','Observed outcome / provider follow-up / claim limits'],
['Hypothetical use is not product certification.','Volume and dollar savings are distinct.','Health and technical concerns use qualified sources.'], 'Ask for exact product evidence and keep any usage scenario separate from a promised bill outcome.')

chapter('Confirm local, utility and other-trade responsibilities','A plumbing quote cannot answer every approval question.',[
'Ask the relevant authority, utility and qualified providers what applies to the actual work. Record responsibility for permits, submissions, visits and required final records where relevant. This guide provides no nationwide exemption, fee schedule or code interpretation.',
'Identify interfaces with electrical, fuel, structural, waterproofing and finish work as assessed. Give each required task a responsible provider. A plumbing-only package should not be described as complete when a required supporting trade remains unassigned.',
'Separate estimated fees, submitted requests and issued approvals. Keep current documents and decision dates with the work plan. A fee allowance does not prove that approval has been obtained.',
'Review changes with the responsible parties before relying on earlier information. If the selected product or layout changes, relevant requirements and supporting scope may need reassessment. Retain the actual decision record rather than assuming the old approval covers every revision.'
], 'A fictional coordination register has four interfaces. Three providers confirm their scopes; one utility-related responsibility remains unresolved.', [('Interfaces listed','4'),('Confirmed scopes','3'),('Unresolved utility boundary','1'),('Coordination complete','No')],
'The open boundary is a decision gate. It is not assumed included in the plumber price.',
['Actual local and utility questions / authoritative contacts','Permits / submissions / checks / records responsibilities','Supporting trades / boundaries / current documents','Fee estimate / submitted / issued status','Product or layout changes / reassessment / closure evidence'],
['Actual requirements use relevant local sources.','Supporting trades have owners.','Fee payment is distinct from approval.'], 'Resolve the authority, utility and supporting-trade boundaries before finalizing the work sequence.')

chapter('Plan household interruption and the work sequence','The provider must define shutdown and return-to-use arrangements.',[
'Discuss which household functions the assessed work affects and identify any temporary arrangements needed. Record the provider plan for interruption, communication and readiness. This handbook gives no valve, utility-isolation, restart or technical emergency procedure.',
'Connect the sequence to actual assessment, product availability, approvals, access and other-trade prerequisites. A one-day repair duration may begin after several unresolved decisions. Keep estimated dates distinct from confirmed arrangements.',
'Assign responsibility for protecting the work area, moving contents and coordinating restoration. Avoid assuming the homeowner will perform technical work to shorten the schedule. Owner tasks should be explicit, practical and agreed.',
'Record delay terms and cost effects through the accepted change process. When a prerequisite fails, update dependent providers and household arrangements. A planned finish time is not a guarantee of readiness to use the affected service.'
], 'A fictional household plan adds $120 temporary arrangements and $180 separate storage/moving services, neither included in the accepted repair package.', [('Temporary arrangements','$120'),('Storage and moving','$180'),('Separate owner-support cost','$300'),('Service return-to-use timing','Provider confirmation required')],
'The figures do not define interruption duration or technical readiness. Use actual provider guidance.',
['Affected functions / household needs / provider plan','Interruption communication / readiness / contacts','Assessment / supply / approval / access prerequisites','Protection / contents / restoration / agreed owner tasks','Delays / approved cost / revised sequence and use guidance'],
['Technical interruption remains with providers.','Owner-support costs are counted once.','Dates are distinct from use readiness.'], 'Agree on household arrangements and the provider communication plan before confirming work dates.')

chapter('Compare complete proposals and retain the handover','The final record connects the assessed issue to the accepted result.',[
'Give bidders the same item schedule, actual findings and desired outcome. Compare assessment terms, defined repair or replacement, products, access, supporting trades, restoration and relevant final evidence. Mark included, excluded, allowance and unresolved lines.',
'Keep pricing models and units explicit. A service-call headline, material rate and complete fixed repair are different records. Normalize only matched scope and retain actual terms for conditional work and fee credits.',
'Include owner and temporary costs outside contractor packages where relevant, with reserve separate. Reconcile confirmed credits and unpaid obligations without treating a requested refund as received money. No scenario here is a local price benchmark.',
'Save actual installed labels, provider findings, completion evidence, operating and care guidance and warranty contacts. Keep unresolved follow-up on a dated action list. The owner file supports later decisions without guaranteeing future condition or service performance.'
], 'A fictional accepted repair/access/restoration scope is $1,050, with $100 approved additional work and a confirmed $50 credit. Payments total $800.', [('Accepted scope plus addition','$1,150'),('Confirmed credit','−$50'),('Reconciled defined cost','$1,100'),('Paid / unpaid','$800 / $300')],
'The $300 remains a payment obligation under the stated example. Actual completion and payment terms require separate review.',
['Common findings / outcome / item schedule / complete scope','Pricing basis / inclusions / conditional work / credits','Supporting trades / owner costs / reserve / open decisions','Actual labels / reports / care / warranties / punch list','Final costs / payments / obligations / follow-up evidence'],
['Matched scope precedes price ranking.','Only confirmed credits reduce cost.','Open follow-up survives decorative completion.'], 'Retain the complete accepted scope and reconcile the final handover and unpaid obligations.')

method(2,'Build the all-in plumbing project budget')
method(5,'Normalize contractor proposals')
method(6,'Review the live cost forecast')
method(17,'Approve changes and reconcile the reserve')
method(18,'Close out and retain project records')
SOURCES=[('1','FTC: Home Repair Scams','https://consumer.ftc.gov/features/pass-it-on/home-repair-scams'),('2','EPA WaterSense: Home Maintenance','https://www.epa.gov/watersense/home-maintenance'),('3','Department of Energy: Selecting a New Water Heater','https://www.energy.gov/node/369127')]

STORE=dict(slug='plumbing-project-cost-quote-handbook',title='Plumbing Repair Cost Guide',category='Plumbing Projects',amount=1199,route='/api/download-plumbing-guide',number=17,test='scripts/test_plumbing_delivery.mjs',
description='A 64-page plumbing planning guide with 19 worked examples and 19 fillable worksheets. Separate assessment, repair scope, products, access, restoration, service fees and complete proposals.',
eyebrow='Know what the repair price actually includes',why_title='Why buy this plumbing planning guide?',why='A service-call fee, fixture price and complete repair proposal cover different things. This guide helps you connect the assessed issue to the full work, supporting services and final cost record.',
benefits=[('Clarify assessment and pricing.','Record visit fees, approval limits, actual credits and fixed or measured scope.'),('Include the work around the repair.','Assign access, openings, restoration, supporting trades and household arrangements.'),('Compare complete choices.','Review repair, replacement, fixtures, water heating and service boundaries with actual qualified findings.')],
reader='U.S. homeowners arranging a plumbing assessment, comparing repair or replacement proposals, or checking the complete cost of fixtures and supporting work. Actual providers must assess conditions and technical requirements.',
difference_title='What does the paid guide add to a calculator?',difference='It connects individual totals to assessment, scope, approval and handover records, with 19 worked cases, 19 reusable worksheets and 95 fillable fields.',
limits='One-time purchase. No subscription. Example fees, quantities and use scenarios are hypothetical. No diagnosis, local repair price, technical suitability or bill saving is promised.',
helps=['Create a location-based fixture and concern schedule','Separate assessment, proposed work and approved obligations','Reconcile fees, credits, labor and measured quantities','Include access, products, supporting trades and restoration','Retain findings, care records, final costs and follow-up'],
sequence='item inventories, assessments, pricing terms, repair alternatives, measured scope, access, fixtures, water heating, service interfaces and handover',
example='A fictional repair is $500, with $200 required access and $350 finish restoration expressly excluded. The complete defined scenario is $1,050. The $500 headline covers less than the whole work, and none of these teaching amounts is a local price benchmark.',
calculator_html='<p>Use the free <a href="/calculators/contractor-quote-comparison">quote comparison calculator</a> with complete matched proposals. Keep assessment terms and supporting-work inclusions attached to the totals.</p>',
examples='Work through approval status, call-out credits, complete repair alternatives, measured quantities, access/restoration, owner-supplied fixtures, installed water-heating scope, drain assessment and final obligations. Six general owner-budget chapters use the HomeCostEngine renovation method with plumbing adaptation; thirteen chapters add plumbing decisions. No diagnostic, isolation, repair, testing or installation procedure is supplied.')
PDF_META=dict(key='plumbing',subject='Original plumbing owner planning guide and 19 fillable worksheets',header='PLUMBING PROJECT PLANNING',cover_title='Plumbing Repair<br/>Cost Guide',cover_lines=['Clarify the assessment. Define the whole repair.','Compare complete scope and supporting work.'],
preface=['A plumbing decision connects an observed concern to a qualified assessment, defined remedy and complete supporting work. This guide helps you organize the owner record without diagnosing the system or treating a call-out fee as the repair price.',
'Start with the brief and item inventory. Separate assessment, proposal and approval, then clarify pricing terms, measured scope, access, restoration, products, water heating, drain questions and service interfaces.',
'Each working chapter contains an explanation, an original hypothetical case and a reusable sheet. Six general owner-budget chapters use the HomeCostEngine renovation method with plumbing adaptation. Thirteen chapters add plumbing-specific scope and purchasing decisions.',
'All costs, quantities and use scenarios are invented USD teaching inputs, not local price ranges, product ratings or technical instructions. Fee credits depend on actual written terms. A proposed option is not an approved or paid obligation.',
'Qualified providers and the relevant local sources must establish assessment, urgency, design, requirements and completion. This book provides no diagnostic, isolation, testing, repair or installation procedure. Keep findings, accepted scope, actual products, changes, invoices and follow-up evidence with the sheets.'],
workflow=['Record affected items, observed concerns, desired function and funding limits.','Collect qualified findings, exact products and provider-confirmed work quantities.','Match assessment terms, repair scope, access, services, restoration and actual credits.','Track accepted work, allowance changes, paid costs and unpaid obligations.','Reconcile the handover. Retain actual product, care, warranty and follow-up records.'],
afterword='A useful plumbing plan connects the assessed concern to a complete accepted scope and clear responsibilities. Separate assessment from repair, retain supporting-work and credit evidence, and keep final costs, unpaid obligations and unresolved follow-up visible after the service visit.')

