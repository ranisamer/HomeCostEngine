"""Original home energy assessment and upgrade planning cases, with established owner-budget methods."""
from pathlib import Path
import runpy,copy
base=runpy.run_path(str(Path(__file__).with_name('renovation-blueprint.py')))
CHAPTERS=[]
def chapter(title,deck,paragraphs,example,rows,conclusion,prompts,checks,task):
    CHAPTERS.append(dict(title=title,deck=deck,paragraphs=paragraphs,example=example,rows=rows,conclusion=conclusion,prompts=prompts,checks=checks,task=task))
def method(index,title):
    c=copy.deepcopy(base['CHAPTERS'][index]);c['title']=title
    replacements={'renovation':'home energy upgrade','Make the kitchen usable for two cooks':'Improve the assessed comfort and energy outcome','buy new cabinets':'buy energy equipment','A bathroom project in a one-bath home has a different temporary-use problem from the same work in an empty property.':'Changing the only heating or cooling system creates different temporary-use needs from work on an unused room.','fixture allowance':'finish-selection allowance'}
    def adapt(s):
        for a,b in replacements.items():s=s.replace(a,b)
        return s
    for k in ['deck','example','conclusion','task']:c[k]=adapt(c[k])
    for k in ['paragraphs','prompts','checks']:c[k]=[adapt(x) for x in c[k]]
    CHAPTERS.append(c)

method(0,'Define the home energy improvement brief')
chapter('Request the right assessment and report','An audit fee needs an exact scope.',[
'Describe the household concern and desired result before booking an assessment. Cost, comfort, recurring service, room conditions and planned equipment changes can raise different questions. Department of Energy assessment guidance explains the role of evaluating the actual home before selecting improvements [2].',
'Ask the provider what the assessment includes, which methods and records it uses, what limitations remain and what report will be supplied. Keep an energy assessment separate from a general property inspection or a specific trade diagnosis. A broad service label does not define every included task.',
'Compare providers on the same documented scope, relevant qualifications and useful deliverables. Ask how recommendations, assumptions, proposed costs and savings estimates will be explained. This book supplies no testing, equipment operation or technical audit procedure.',
'Record follow-up and any relationship between the assessor and proposed installation services. A report can support a decision without guaranteeing the performance of a future project. Retain the actual report version used for pricing and planning.'
], 'A fictional assessment is $300 including a defined report. Another matched base visit is $250 but needs a separately quoted $75 report service.', [('Complete first assessment','$300'),('Second visit plus report','$325'),('Matched-scope difference','$25'),('Actual local audit cost','Not established')],
'The figures illustrate scope comparison, not an energy-audit market range. Confirm actual deliverables and terms.',
['Household questions / desired results / current records','Assessment scope / method references / limitations','Provider qualifications / deliverables / reporting','Complete fee / separate services / actual terms','Recommendation basis / conflicts or relationships / follow-up'],
['Audit and general inspection scope are distinguished.','Report services are included in the comparison.','No future performance guarantee is inferred.'], 'Ask for the written assessment scope and sample report structure before comparing fees.')

chapter('Build a baseline from actual bills','Usage needs units and period length.',[
'Collect the available energy bills and record fuel or service type, consumption units, billing days and whether readings are measured or estimated. Keep electricity, gas and other units on their own lines unless a documented conversion is explicitly required.',
'Calculate daily averages where useful while retaining actual dates and seasonal context. A lower monthly total can result from fewer days rather than a change in the home. A normalized daily figure helps ask questions but does not identify a technical cause.',
'Record missing periods, tariff changes and unusual occupancy or equipment use. Keep the baseline representative of the actual household question. A previous owner bill may reflect a different household and is not a guaranteed forecast for the new owner.',
'Use the actual bills and context with the qualified assessor. This planner does not replace an energy model or technical diagnosis. Retain the baseline version so later comparisons do not quietly change the starting point.'
], 'Fictional electricity bills show 1,200 kWh over 30 days and 1,120 kWh over 28 days. Both average 40 kWh per day.', [('1,200 / 30','40 kWh per day'),('1,120 / 28','40 kWh per day'),('Raw usage difference','80 kWh'),('Daily-average difference','0 kWh')],
'The lower raw total is not evidence of an efficiency improvement. Even daily averages need weather and household context.',
['Bills / units / exact dates / measured or estimated','Consumption / days / daily-average calculation','Tariff / occupancy / equipment changes / missing periods','Baseline scope and limitations / assessor questions','Current baseline version / retained original records'],
['Unlike energy units remain distinct.','Period length is normalized explicitly.','A bill comparison is not a diagnosis.'], 'Create one dated baseline table before accepting a savings estimate or choosing an upgrade.')

chapter('Separate consumption from tariff and fixed charges','A smaller bill does not necessarily mean less energy use.',[
'Record the rate structure and fixed charges relevant to each bill. Consumption, energy price and standing or other charges can change independently. Do not attribute the entire bill movement to an upgrade without separating those effects.',
'For a simple single-rate scenario, multiply usage by the stated unit price and add the explicit fixed charge. More complex actual tariffs may need provider or assessor help. This book supplies no utility-rate recommendation or universal conversion.',
'When comparing energy scenarios, state whether the same tariff is used for both or whether an actual rate change is modeled. Keep assumptions and dates visible. A projected lower energy total can still cost more under a sufficiently higher rate.',
'Retain actual billed costs separately from a normalized comparison. Both can be useful, but they answer different questions. Confirm estimated charges and adjustments before describing a credit or saving as realized.'
], 'An invented month uses 500 kWh at $0.20 per kWh plus $15 fixed charges. A second scenario uses 450 kWh at $0.25 plus the same $15.', [('500 × $0.20 + $15','$115.00'),('450 × $0.25 + $15','$127.50'),('Consumption difference','−50 kWh'),('Bill scenario difference','+$12.50')],
'Lower use and higher cost coexist in this simple example. Actual tariffs and bills can be more complex.',
['Consumption / energy units / actual bill dates','Unit rates / fixed and other charges / source','Common-tariff or actual-tariff comparison basis','Scenario arithmetic / excluded tariff effects','Billed versus normalized result / adjustments / limits'],
['Usage and price changes are separated.','Fixed charges remain visible.','Modeled savings are distinct from actual bill changes.'], 'Ask a savings proposal to show the tariff and fixed-charge assumptions used in its dollar result.')

chapter('Record weather, occupancy and comfort context','Before-and-after totals cannot establish every cause.',[
'Keep relevant context for the periods being compared, including weather differences, time at home, room use and major equipment changes. Use actual records where available and mark missing context honestly. A household behavior change can affect energy use alongside building work.',
'Ask the assessor how the model or comparison handles those differences and what limitations remain. This planner provides no weather-normalization formula or causal measurement method. A daily average alone does not correct for every condition.',
'Record comfort outcomes separately from energy quantities. A household may use newly conditioned rooms or choose different comfort settings after an upgrade. Those changes can matter to the decision without fitting a simple same-use savings calculation.',
'Retain uncertainty rather than forcing a precise performance claim. A useful review can show what changed, what was observed and what still needs explanation. Do not describe a raw bill difference as verified savings caused by the project.'
], 'A fictional comparison has four changed conditions: a longer occupied period, a different weather period, one newly used room and a changed tariff. None has been quantitatively normalized.', [('Changed conditions recorded','4'),('Quantitatively normalized here','0'),('Raw bill comparison','Available'),('Verified causal project saving','Not established')],
'The example shows why context matters. It does not say the project performed well or badly.',
['Compared dates / weather information / evidence limits','Occupancy / use / equipment / tariff changes','Assessor normalization approach / unresolved effects','Comfort outcomes / newly served areas / observations','Reported result / uncertainty / further review needed'],
['Context is retained beside the numbers.','Daily averages are not complete normalization.','Causal savings are not claimed from raw bills.'], 'Ask how the proposed savings analysis handles actual weather and household-use differences.')

chapter('Turn report recommendations into decision records','A list of measures needs scope and evidence.',[
'Give each recommendation an ID, report reference and stated purpose. Record the finding supporting it and the qualified provider responsible for further design or assessment. A recommendation heading alone does not define a complete installation scope.',
'Separate essential assessed work, optional improvements and recommendations requiring more information. Keep uncertainty, prerequisites and related technical questions visible. Do not rank an unresolved safety or condition issue solely through a financial return score.',
'Ask for the assumptions behind costs and savings, including whether they apply to an individual measure or a combined package. Keep model version, tariff and household-use assumptions with the recommendation. A rounded headline number is not enough to reproduce the scenario.',
'Use the register to request complete proposals and identify decisions before procurement. The assessment can inform the selection, while actual design, local requirements and installation checks remain with the relevant professionals and authorities.'
], 'A fictional report has eight recommendations: three ready for defined pricing, three needing further assessment and two optional ideas outside the current plan.', [('Ready for defined pricing','3'),('Further assessment needed','3'),('Optional ideas','2'),('All eight approved','No')],
'Report inclusion is not approval to buy or build every recommended item.',
['Recommendation ID / finding / report version','Purpose / priority / actual qualified responsibility','Prerequisites / missing inputs / optional status','Cost and savings assumptions / package or standalone','Proposal request / decision gate / approval evidence'],
['Recommendations have supporting findings.','Model assumptions remain attached.','Report lists are not treated as purchase authorizations.'], 'Create a recommendation register and resolve the next assessment or pricing action for each item.')

chapter('Coordinate envelope and comfort-system decisions','Changes can interact across the whole home.',[
'Ask the qualified assessment and design team how proposed building-envelope and comfort-system work should be coordinated. Record the actual recommendations and dependencies. ENERGY STAR home-upgrade resources describe planning improvements together [3].',
'Keep air, insulation, windows, moisture, ventilation and system questions with the responsible providers as relevant to the actual project. This handbook supplies no sealing, insulation, ventilation, load, refrigerant or building-assembly procedure.',
'Compare the complete package outcome rather than assuming a sequence or system size from a rule of thumb. A change to the building can affect a professional equipment decision. Have the relevant providers review the current design and selected scope.',
'Record technical gates before orders and dependent finishes. A cheaper isolated measure may create later rework or omit a supporting requirement. Retain the complete assessed alternative and professional explanation instead of adding unrelated sales claims.'
], 'A fictional coordinated package has $4,000 envelope work, $500 separate assessment/design and $7,000 defined comfort-system work, with no overlap.', [('Envelope scope','$4,000'),('Assessment/design','$500'),('Comfort-system scope','$7,000'),('Defined package cost','$11,500')],
'The example does not recommend a sequence, assembly or equipment size. Actual design determines viable work.',
['Current assessment / envelope and system recommendations','Qualified providers / relevant condition and service questions','Design dependencies / selection and order gates','Complete package / supporting work / scope overlaps','Accepted sequence / actual technical evidence / revisions'],
['Interactions receive qualified review.','No owner design shortcut is used.','Isolated sales claims are not simply added.'], 'Ask the assessment and installation team to explain the coordinated package and its prerequisites.')

chapter('Compare equipment as complete installed alternatives','An efficiency label is one input, not the entire outcome.',[
'Record exact proposed heating, cooling, water-heating or other equipment and the assessed household need. Ask qualified providers to establish suitability, required capacity and supporting work. The owner should retain the decision basis without performing technical sizing.',
'Compare the same served areas and desired results across alternatives. Include installation, distribution, utilities, controls, access, approvals and restoration as relevant. A product-only price cannot be compared directly with a complete installed offer.',
'Keep energy-performance information separate from assumed household operating cost. Actual use, climate, tariffs and the installed arrangement affect the scenario. Do not convert a label improvement directly into a guaranteed percentage saving.',
'Retain operating, care, warranty and required-check records for the actual selected system. Review product substitutions with all affected providers. This book provides no installation, service, electrical or fuel procedure.'
], 'A fictional option is $3,000 equipment plus $1,200 supporting installation and $300 restoration. A matched complete alternative is $4,700.', [('First option complete scope','$4,500'),('Matched alternative','$4,700'),('Initial difference','$200'),('Actual operating saving','Not established')],
'The $200 difference is not a life-cycle recommendation. Actual suitability and operating assumptions still need review.',
['Exact models / assessed need / qualified selection basis','Same served areas / complete installed scope','Supporting utilities / controls / access / restoration','Ratings / operating assumptions / tariff and use context','Substitution review / checks / care / warranty records'],
['Equipment price is distinct from installed price.','Actual needs use qualified assessment.','Label differences are not bill-saving guarantees.'], 'Request complete assessed installed alternatives and the actual operating-cost assumptions separately.')

chapter('Include electrical readiness and other supporting work','The energy measure may depend on a separate package.',[
'Give the qualified electrical and other relevant providers the actual selected equipment information and proposed scope. Ask them to assess requirements and viable supporting options. This guide performs no load, service-capacity, circuit, wiring or fuel-system design.',
'Record retained infrastructure, actual utility coordination and relevant local-review gates. Do not assume every electric product needs the same upgrade or that an unused equipment space proves adequate capacity. Keep the actual professional conclusion.',
'Price the supporting package and its interfaces with access, restoration and household arrangements. A rebate or attractive equipment offer does not itself cover those tasks. Assign each required service to an accountable provider.',
'Review the complete plan before procurement. If selections or requirements change, update the cost model and sequence together. Keep supporting costs separate enough that they are included once across several energy measures.'
], 'An invented project has $1,500 shared electrical support serving two measures. It is included once, rather than added as $1,500 to each measure.', [('Confirmed shared support','$1,500'),('If duplicated across two measures','$3,000'),('Overstatement avoided','$1,500'),('Actual technical scope','Professionally assessed')],
'Shared pricing must be confirmed. Similar task names alone do not prove that two scopes overlap.',
['Actual selected equipment / qualified supporting assessments','Retained infrastructure / utility / local questions','Supporting package / access / restoration / owners','Shared versus separate services / provider confirmation','Changed selections / cost-model revision / current sequence'],
['No capacity assumption comes from appearance.','Shared work is reconciled with providers.','Equipment incentives do not define installed scope.'], 'Obtain the complete supporting-work assessment before relying on the equipment quote.')

chapter('Avoid double-counting combined savings','Standalone estimates do not necessarily add into a package result.',[
'Ask whether each saving estimate models a measure alone or a complete package. Measures can affect the same energy use or change the conditions under which another measure operates. Keep the model scope and baseline attached to every result.',
'Request a combined analysis from the qualified assessor where interactions matter. This workbook provides no simulation or causal savings calculation. Do not simply sum several sales claims to create a larger promised project benefit.',
'Distinguish energy quantities from dollar estimates and comfort outcomes. Use consistent units, tariffs, horizons and household assumptions. If a result includes more than one fuel, keep its conversion and price basis traceable to the actual analysis.',
'Use a range or sensitivity scenario only with explicit assumptions and limitations. Retain the source and version so revised selections can be re-evaluated. A package figure is still an estimate unless supported by an appropriate outcome-verification method.'
], 'For teaching only, two standalone estimates are $500 and $400 per year. A fictional qualified combined model estimates $750 because its assumptions include interaction.', [('Standalone estimate A','$500 per year'),('Standalone estimate B','$400 per year'),('Naive sum','$900 per year'),('Assumed combined-model result','$750 per year'),('Difference','$150 per year')],
'The numbers illustrate model boundaries, not actual savings or a universal interaction amount.',
['Each measure / standalone or package model scope','Common baseline / use / tariff / units / horizon','Qualified combined analysis / assumptions / version','Energy / dollar / comfort outcomes kept distinct','Sensitivity / uncertainty / revised selections / verification'],
['Standalone claims are not automatically added.','Unlike units stay separate.','Combined results retain their assumptions.'], 'Ask for one traceable package estimate rather than summing unrelated measure-level claims.')

chapter('Verify incentives before calculating net cost','An advertised amount is not available household cash.',[
'Record the actual program, administrator, eligible dates, property and product conditions, required approvals, documents and payment timing. Check current official information and appropriate tax advice where relevant. Program terms can change and differ from old marketing material.',
'As checked October 25, 2026, the IRS Energy Efficient Home Improvement Credit page limits qualifying improvements to those made through December 31, 2025 [4]. Do not carry an older advertised credit into a new project assumption. This guide assumes no federal credit or other incentive is available.',
'Keep unverified, applied-for, approved and received benefits separate. A tax item, later reimbursement and immediate supplier discount can affect cash at different times. An expected later benefit does not automatically fund an invoice due now.',
'Model complete project cost before benefits, then show only appropriately verified assumptions on separate scenario lines. Retain evidence and avoid counting the same discount or benefit twice. This book does not determine individual eligibility or provide tax advice.'
], 'A fictional $5,000 invoice has a confirmed immediate $300 supplier discount. An unverified $600 program benefit is excluded from the current funding calculation.', [('Quoted invoice','$5,000'),('Confirmed immediate discount','−$300'),('Current required payment','$4,700'),('Unverified program benefit','$0 counted now')],
'The $600 is not a claim about any actual program. Eligibility and timing require current official verification.',
['Actual program / administrator / current official source','Dates / property / product / approval / document conditions','Unverified / applied / approved / received status','Gross cost / confirmed discount / cash timing','Evidence / relevant tax advice / no-duplication check'],
['Older marketing is not current eligibility evidence.','Unverified benefits do not fund today invoice.','Discounts and later benefits have separate timing.'], 'Verify actual eligibility, dates and payment timing before reducing the funding plan by an incentive.')

chapter('Use simple payback with sensitivity','A quotient is a scenario, not a return guarantee.',[
'State the complete cost and net annual saving assumption used for a simple-payback calculation. Divide the cost by that annual amount only where the units and scope match. Keep verified benefits, maintenance differences and other assumptions visible.',
'Identify excluded effects such as financing, time value, future tariffs, repairs, useful-life limits and changed household use. A simple quotient does not model those factors. An estimate of savings does not become more certain because the result has decimal places.',
'Test a lower and higher annual-saving scenario using clearly labeled teaching inputs. If the ranking depends heavily on an uncertain assumption, retain that sensitivity in the decision record. Do not present the result as investment advice or a guaranteed equipment life.',
'Compare comfort, function and required work separately from financial payback. A necessary assessed repair can be important even without a short energy-payback result. Use appropriate qualified advice for the actual project and commitments.'
], 'A fictional $8,000 complete cost has alternative net saving assumptions of $500 and $800 per year. No other effects are modeled.', [('$8,000 / $500','16 years'),('$8,000 / $800','10 years'),('Assumption-driven difference','6 years'),('Actual achieved payback','Not established')],
'The six-year difference comes entirely from the saving input. Neither horizon predicts actual performance or useful life.',
['Complete cost / benefits treatment / actual evidence','Net annual saving / source / scope / units','Excluded financing / time / tariff / repair effects','Lower and higher scenarios / sensitivity / limits','Comfort and required work / decision rationale / advice'],
['Payback uses net annual saving on matching scope.','Excluded effects are explicit.','A scenario horizon is not equipment life.'], 'Ask how the decision changes under a reasonable lower-saving scenario before relying on simple payback.')

chapter('Connect phases, upfront cash and future benefits','A later saving cannot automatically pay today invoice.',[
'Map assessment, design, prerequisites, product availability, installation and required checks into the actual provider sequence. Keep dates and assumptions labeled. A technically dependent measure should not be advanced solely to chase an unverified benefit.',
'Compare combined and staged work with repeated services, access and restoration visible. A lower first-stage payment can come with a higher total. Keep the actual functional outcome and technical feasibility of each phase confirmed by qualified providers.',
'Build a cash calendar using confirmed inflows and actual invoice dates. Keep reserve, unpaid accepted obligations and any verified later reimbursement separate. Projected bill savings over future years are not opening cash.',
'Review the whole cost model when scope or timing changes. A product substitution can affect technical decisions, benefits and forecast savings. Retain the complete accepted version rather than combining figures from several inconsistent scenarios.'
], 'A fictional period has $4,000 opening funds and $6,000 due for accepted work. A possible $1,000 later reimbursement is unverified and excluded.', [('Opening available funds','$4,000'),('Accepted payment due','−$6,000'),('Current funding gap','−$2,000'),('Unverified later benefit','$0 counted now')],
'The gap remains $2,000. The worksheet does not authorize late payment or recommend borrowing.',
['Current sequence / professional prerequisites / actual dates','Combined and staged scope / repeated-service costs','Opening funds / confirmed inflows / invoice timing','Reserve / unpaid obligations / later benefits status','Changed selections / consistent cost and savings model'],
['Future savings are not available upfront cash.','Unverified benefits remain outside funding.','Phase changes update the complete model.'], 'Check the early payment periods using confirmed funds before accepting the upgrade sequence.')

chapter('Verify handover and review actual outcomes','Keep technical completion and measured results distinct.',[
'Collect actual installed product records, qualified checks, relevant authority documents, operating guidance and warranties for the accepted scope. A product invoice or owner visual review does not replace required professional completion evidence.',
'Retain the baseline, model assumptions and date of each change before comparing subsequent bills. Record weather, occupancy, tariff and use differences. Ask the qualified assessor about an appropriate verification method and the limits of any result.',
'Keep comfort observations, energy quantities, dollar costs and maintenance outcomes on separate lines. A useful review can show improvement in one dimension without claiming a verified saving in every other dimension. Preserve unresolved concerns with a responsible provider and date.',
'Reconcile final scope, changes, confirmed credits, payments and outstanding obligations. Keep actual care tasks and review dates sourced to the selected products and provider guidance. The owner file supports future decisions without guaranteeing performance or a financial return.'
], 'An invented accepted project is $11,500 with $400 approved additions and a confirmed $200 credit. Payments total $10,000.', [('Accepted scope plus additions','$11,900'),('Confirmed credit','−$200'),('Reconciled defined cost','$11,700'),('Paid / unpaid','$10,000 / $1,700'),('Verified energy outcome','Separate analysis required')],
'The cost reconciliation does not establish actual energy savings. Keep outcome verification and unpaid obligations separately visible.',
['Actual products / qualified completion / operating records','Baseline / model / change dates / comparison context','Comfort / energy / dollar / care outcomes and limits','Final scope / additions / credits / payments / obligations','Follow-up / sourced care tasks / assessor review'],
['Technical completion has actual evidence.','Raw bills are not claimed causal savings.','Financial and performance records remain separate.'], 'Save the complete handover and agree on the actual outcome-review method with the qualified provider.')

method(2,'Build the all-in home energy upgrade budget')
method(5,'Normalize contractor proposals')
method(6,'Review the live cost forecast')
method(17,'Approve changes and reconcile the reserve')
method(18,'Close out and retain project records')
SOURCES=[('1','FTC: Home Repair Scams','https://consumer.ftc.gov/features/pass-it-on/home-repair-scams'),('2','Department of Energy: Professional Home Energy Assessments','https://www.energy.gov/articles/professional-home-energy-audits'),('3','ENERGY STAR: Home Upgrade planning resources','https://www.energystar.gov/products/energy_star_home_upgrade'),('4','IRS: Energy Efficient Home Improvement Credit','https://www.irs.gov/credits-deductions/energy-efficient-home-improvement-credit')]

STORE=dict(slug='home-energy-upgrade-savings-planner',title='Home Energy Audit Cost Guide',category='Energy Assessments & Upgrades',amount=1499,route='/api/download-energy-guide',number=20,test='scripts/test_energy_delivery.mjs',
description='A 64-page energy assessment and upgrade guide with 19 worked examples and 19 fillable worksheets. Compare audit scope, bill baselines, complete upgrade packages, funding assumptions and outcome records.',
eyebrow='Check the evidence behind the savings claim',why_title='Why buy this home energy planning guide?',why='An audit fee, equipment price and projected saving answer different questions. This guide helps you connect the assessment and complete scope to traceable bill assumptions, realistic funding and an outcome-review record.',
benefits=[('Compare the actual assessment scope.','Record deliverables, provider evidence, limitations and recommendation assumptions.'),('Check the financial scenarios.','Separate usage, tariffs, package interactions, verified benefits and simple-payback sensitivity.'),('Keep the whole project connected.','Include supporting work, phases, upfront cash, qualified completion and actual outcome review.')],
reader='U.S. homeowners choosing a professional energy assessment or comparing assessed upgrade packages. Actual qualified providers must establish technical needs, design, installation and suitable performance analysis.',
difference_title='What does the paid guide add to a calculator?',difference='It connects cost arithmetic to assessment, baseline, recommendation, package and outcome records, with 19 worked cases, 19 worksheets and 95 fillable fields.',
limits='One-time purchase. No subscription. Example costs, savings and tariffs are hypothetical. No audit price, program eligibility, bill saving, payback or financial return is promised.',
helps=['Define and compare professional assessment deliverables','Build an actual-bill baseline with units and context','Separate tariffs, weather, occupancy and comfort outcomes','Compare complete packages without adding overlapping claims','Verify benefit assumptions and review cash, payback and actual outcomes'],
sequence='assessment scope, actual bills, tariff and context records, recommendations, coordinated packages, verified funding assumptions and outcome review',
example='A fictional $8,000 complete project cost divided by an assumed $500 net annual saving gives 16 years simple payback. At an assumed $800 annual saving, it gives 10 years. The six-year difference comes only from the saving input; neither result predicts actual performance or equipment life.',
calculator_html='<p>Use the free <a href="/calculators/">HomeCostEngine calculators</a> for individual quantities and the <a href="/calculators/contractor-quote-comparison">quote comparison calculator</a> with complete matched scope. Retain the actual assessment and model assumptions.</p>',
examples='Work through matched audit fees, daily-use baselines, tariff-versus-consumption effects, assessment gates, coordinated scope, shared support, package savings assumptions, unverified incentives, payback sensitivity, early cash gaps and final obligations. Six general owner-budget chapters use the HomeCostEngine renovation method with energy adaptation; thirteen chapters add energy decisions. No technical audit, installation, tax-eligibility determination or causal savings method is supplied.')
PDF_META=dict(key='energy',subject='Original home energy assessment and upgrade owner guide with 19 fillable worksheets',header='ENERGY OWNER PLANNING',cover_title='Home Energy Audit<br/>Cost Guide',cover_lines=['Check the assessment. Trace the assumptions.','Compare complete costs and savings scenarios.'],
preface=['An energy project begins with questions about the actual home and household. This guide helps you connect a professional assessment to complete upgrade scope, realistic funding and a record for reviewing outcomes without promising a bill result.',
'Start with the brief and assessment deliverables. Build the baseline from actual bills, distinguish consumption from tariffs and retain weather and household context. Then connect recommendations, technical providers, complete packages, verified benefits and cash timing.',
'Each working chapter contains an explanation, an original hypothetical case and a reusable sheet. Six general owner-budget chapters use the HomeCostEngine renovation method with energy adaptation. Thirteen chapters add assessment, financial-scenario and outcome decisions.',
'All costs, tariffs and saving inputs are invented USD teaching assumptions, not local quotes or guaranteed results. Standalone saving estimates are not automatically additive. Simple payback excludes many ownership effects and does not predict equipment life.',
'Qualified providers must establish technical needs, design, required work and appropriate outcome analysis. Verify current official program dates and eligibility before using a benefit; no incentive is assumed available. This book gives no technical audit or installation procedure. Keep actual reports, model assumptions, accepted scope, changes and completion records with the sheets.'],
workflow=['Record household energy and comfort questions, current evidence and funding boundaries.','Collect actual bills, qualified findings, current product and model assumptions.','Match audit scope, complete packages, supporting work and consistently modeled benefits.','Track accepted work, verified benefit status, payments, cash needs and obligations.','Reconcile handover and review actual outcomes with context and appropriate analysis.'],
afterword='A useful energy owner record connects the actual assessment to complete scope, traceable assumptions and realistic funding. Keep usage separate from tariffs, compare packages without adding unsupported claims, verify current benefit rules and retain the evidence needed for a careful outcome review.')

