"""Original home maintenance planning and cost cases, with established owner-budget methods."""
from pathlib import Path
import runpy,copy
base=runpy.run_path(str(Path(__file__).with_name('renovation-blueprint.py')))
CHAPTERS=[]
def chapter(title,deck,paragraphs,example,rows,conclusion,prompts,checks,task):
    CHAPTERS.append(dict(title=title,deck=deck,paragraphs=paragraphs,example=example,rows=rows,conclusion=conclusion,prompts=prompts,checks=checks,task=task))
def method(index,title):
    c=copy.deepcopy(base['CHAPTERS'][index]);c['title']=title
    replacements={'renovation':'home maintenance program','Make the kitchen usable for two cooks':'Keep the home serviceable with a documented care plan','buy new cabinets':'buy replacement equipment','A bathroom project in a one-bath home has a different temporary-use problem from the same work in an empty property.':'Servicing the only heating system creates different temporary-use needs from routine work on a spare appliance.','fixture allowance':'finish-selection allowance'}
    def adapt(s):
        for a,b in replacements.items():s=s.replace(a,b)
        return s
    for k in ['deck','example','conclusion','task']:c[k]=adapt(c[k])
    for k in ['paragraphs','prompts','checks']:c[k]=[adapt(x) for x in c[k]]
    CHAPTERS.append(c)

method(0,'Define the home maintenance brief')
chapter('Create a system and asset register','A useful schedule begins with what the home actually contains.',[
'List the equipment, building elements and services the household is responsible for maintaining. Give each asset an ID and location. Record product details from accessible labels or existing documents, with installation dates marked unknown when no reliable record exists. Do not invent an age to complete a spreadsheet.',
'Link manuals, warranty documents, inspection reports and service invoices to the asset record. For shared buildings, identify which responsibilities belong to the owner, association or another party. A component visible from the home may still have a different maintenance owner.',
'Separate observed condition from assessed condition. A noisy appliance or a stain is an observation to report, not a diagnosis or evidence of remaining life. Assign relevant assessment questions to qualified providers and retain their findings with the asset.',
'Start with the assets that affect household continuity or have known service obligations, then improve the register over time. The goal is a useful decision record rather than a complete technical survey. Do not open equipment, enter hazardous spaces or climb to collect information for this book.'
], 'A fictional register has twelve identified assets: eight owner-managed, three managed by an association and one awaiting responsibility confirmation.', [('Owner-managed','8 assets'),('Association-managed','3 assets'),('Responsibility unresolved','1 asset'),('Total register','12 assets')],
'The unresolved item is not assumed covered by someone else. Resolve its owner before relying on a service plan.',
['Asset ID / location / accessible product information','Installation-date evidence / unknowns','Manuals / warranties / service-report references','Owner / association / other responsibility','Condition observations / assessment owner / next action'],
['Dates and condition are evidence-based.','Every asset has a responsibility status.','No hazardous access is needed to complete the register.'], 'Create the first register from records you already have and ask providers to supply missing details.')

chapter('Turn manuals into a task register','A generic calendar cannot replace equipment-specific requirements.',[
'Read the current instructions and service records for each actual asset, then list the maintenance tasks that apply. Record the source, trigger, responsible provider and completion evidence. A task may depend on time, use, observed condition or a professional recommendation rather than one universal season.',
'Separate tasks the manufacturer permits an owner to do from work needing a qualified service provider. This handbook supplies no technical maintenance procedure. Ask the provider to resolve uncertain tasks and document the appropriate boundary instead of treating a short checklist as authorization.',
'Keep task intervals traceable to their source. Do not assume that a neighbor schedule, equipment age or a previous owner habit applies to a different model and environment. If instructions or assessed conditions change, revise the task and retain the reason.',
'Give each task one next-action date or trigger and one accountable owner. A reminder that is repeatedly dismissed should become an open decision, not silently disappear. Record completion only when the defined task and evidence are actually available.'
], 'A fictional six-task register has three time-triggered tasks, two usage-triggered tasks and one unresolved provider recommendation.', [('Time triggers','3 tasks'),('Usage triggers','2 tasks'),('Awaiting provider clarification','1 task'),('Total tasks','6')],
'Only the five defined tasks can enter the working calendar. Clarify the unresolved task without inventing an interval.',
['Asset and task IDs / source document version','Time / use / condition trigger and rationale','Owner-permitted task or qualified provider','Next action / accountable owner / access needs','Completion evidence / revision reason / open questions'],
['Each interval has a source.','Technical work has an appropriate provider.','Unresolved tasks remain visible.'], 'Build the task list from actual manuals and ask the relevant provider to confirm uncertain requirements.')

chapter('Build a seasonal review calendar','Use seasons to review the plan, not to invent service rules.',[
'Group the sourced tasks into a calendar that suits local conditions and household availability. A spring or fall review can help coordinate work, but the season itself does not establish a technical maintenance interval. Keep each task linked to its documented requirement.',
'Add lead time for booking providers, obtaining approvals and clearing access. A task due at the start of a busy season may need arranging earlier. Record preferred dates and constraints without treating a tentative booking as a completed service.',
'Keep weather-related and usage-related triggers visible beside the calendar. If the home is vacant for a period or equipment use changes, ask the appropriate provider how the plan should be reviewed. Do not extend a required interval merely because the calendar is crowded.',
'Review the calendar at a practical recurring point chosen by the household. Move completed work into the service history and keep overdue items in an action queue. The calendar should show responsibility and next steps rather than create a false sense that every system has been inspected.'
], 'A fictional annual calendar has eight confirmed service tasks: two in the first quarter, three in the second, one in the third and two in the fourth.', [('Quarter 1','2 tasks'),('Quarter 2','3 tasks'),('Quarter 3','1 task'),('Quarter 4','2 tasks'),('Annual scheduled tasks','8')],
'The distribution is invented, not a recommended seasonal schedule. Actual manuals, conditions and provider requirements determine the tasks.',
['Sourced tasks / timing / local condition questions','Provider lead times / booking and access owners','Preferred dates / confirmed appointments / dependencies','Weather or usage triggers / reassessment contacts','Completed / overdue / rescheduled status and evidence'],
['Seasons organize sourced tasks.','A booking is not marked completed.','Overdue items remain in the action queue.'], 'Place confirmed tasks on the household calendar with lead time and an accountable owner.')

chapter('Triage observations without diagnosing the home','Urgency and price are separate decisions.',[
'Record observations with a date, location and description of what happened. Keep photographs where they can be obtained without approaching a hazard. A symptom record helps the appropriate provider assess the issue; it does not tell the owner which component has failed.',
'Use a simple decision queue: matters needing immediate qualified attention, matters needing prompt assessment, and routine planning items. Actual urgency comes from the situation and qualified guidance. If there is an immediate danger, use the relevant emergency or utility response rather than waiting for a budget review.',
'Assign the next safe action and a contact, then record who determines whether use or access must change. This book gives no electrical, gas, structural, roof-access or water-isolation procedure. Do not investigate technical systems to obtain a better worksheet entry.',
'Track the assessment result and revised task separately from the initial observation. A resolved symptom and an unresolved cause are different records. If the finding changes the budget, revise the forecast using the assessed scope and approved obligations.'
], 'A fictional queue has one item awaiting immediate provider contact, two awaiting scheduled assessment and four routine planning items. No diagnosis or repair cost is assumed.', [('Immediate contact queue','1 item'),('Assessment queue','2 items'),('Routine planning queue','4 items'),('Total open observations','7 items')],
'These labels organize follow-up; they do not classify the urgency of any actual home condition.',
['Observation / date / location / accessible evidence','Immediate-danger response or assessment contact','Use or access guidance / responsible provider','Assessed finding / task / decision deadline','Budget effect / action owner / resolution evidence'],
['Observations remain separate from diagnoses.','Urgent attention is not delayed for price comparison.','Use decisions come from appropriate qualified guidance.'], 'Assign a next action and responsible contact to each observation instead of leaving it as a vague note.')

chapter('Separate recurring service from replacement funding','One annual allowance cannot explain every type of spending.',[
'Create distinct categories for routine recurring service, assessed repairs, future replacement planning and optional upgrades. A service visit may help maintain an asset, but it does not establish that replacement funding is unnecessary. An upgrade choice should not quietly consume money assigned to essential obligations.',
'For each recurring service, record the expected number of events and actual quoted scope. Keep conditional work separate. For repairs, use an assessed proposal rather than a guessed average cost. For future replacement, label all timing and cost assumptions as planning inputs.',
'Distinguish an annual spending forecast from money transferred into a household reserve. A contribution is cash set aside, not a contractor expense. When the reserve later pays a bill, do not count both the transfer and the bill as two project costs.',
'Review categories when an assessment changes the plan. A large repair may make a replacement comparison useful, but a cost threshold alone does not determine what the system needs. Record the qualified findings and household decision alongside the financial scenario.'
], 'A fictional annual plan has $600 recurring service, $900 assessed repairs and a $1,200 contribution to future replacement funds.', [('Service spending forecast','$600'),('Assessed repair spending','$900'),('Current-year expense forecast','$1,500'),('Separate reserve contribution','$1,200'),('Cash allocated across both','$2,700')],
'The $1,200 transfer is not an additional service expense. Keep contributions and later bills distinct.',
['Recurring service / scope / event counts','Assessed repairs / proposals / timing','Replacement assumptions / optional upgrades','Expense forecast / reserve contribution / separate totals','Reclassification decisions / evidence / funding impact'],
['Expenses and reserve transfers are distinct.','Repair inputs come from assessed scope.','Optional upgrades have a visible funding decision.'], 'Split the annual plan into spending and reserve movements before choosing a monthly contribution.')

chapter('Calculate annual and monthly service provision','Convert event costs without hiding their frequency.',[
'List each recurring task, expected count in the planning period and quoted price per event. Multiply event count by matching cost, then add fixed plan fees only where they are separate. A monthly service plan and a one-time visit are different payment structures.',
'Use twelve months for an annual monthly-equivalent figure, while retaining actual payment dates. Dividing the annual forecast by twelve helps household planning but does not change when a bill becomes due. A large early-year payment may require opening cash.',
'State whether tax, travel, consumables and optional work are included. If a quote is incomplete, keep the gap visible and ask the provider for clarification. Do not hide uncertainty by rounding the annual total into a convenient monthly number.',
'Review forecast versus actual invoices periodically. A change in event count or service scope should have a reason, not merely a new total. Keep the forecast useful by updating known obligations while preserving the original plan for comparison.'
], 'A fictional year has two service events at $150, one inspection at $180 and four consumable purchases at $30. These non-overlapping teaching prices include all costs in this example.', [('2 × $150','$300'),('1 × $180','$180'),('4 × $30','$120'),('Annual service provision','$600'),('$600 / 12','$50 monthly equivalent')],
'The $50 is a planning equivalent, not the actual payment schedule or a local service benchmark.',
['Task IDs / events per year / quoted price unit','Tax / travel / consumable inclusion basis','Annual line calculations / separate fixed fees','Monthly equivalent / actual invoice dates / opening cash','Actual spending / revised forecast / explanation'],
['Frequency is applied once.','Monthly equivalents do not hide due dates.','Costs have explicit scope and inclusions.'], 'Check the annual calculation against the task calendar and actual invoice timing.')

chapter('Build a replacement reserve scenario','An assumed life is not a prediction of failure.',[
'Identify assets for which the household wants a future replacement planning scenario. Use a clearly labeled target amount, existing designated balance and chosen saving horizon. Do not present a generic equipment lifespan as a remaining-life assessment for the actual asset.',
'Subtract available designated funds from the target, then divide the gap by the chosen number of months. This simple model ignores interest, inflation and changes in scope unless those are modeled explicitly. Keep the assumptions visible instead of implying a guaranteed future purchase price.',
'Separate the saving horizon from any professional advice about serviceability or safe operation. An asset needing attention now cannot be made acceptable by planning to save over several years. Obtain the appropriate assessment and record its effect on the scenario.',
'Review the target when a current proposal, major repair or household priority changes. Keep separate balances or a clear internal ledger when several assets share one bank account. The same reserve dollar cannot fully fund multiple replacement targets at once.'
], 'A fictional replacement target is $6,000, with $1,200 already designated and a chosen 48-month saving horizon. The scenario assumes no interest, inflation or additional spending.', [('Target amount','$6,000'),('Existing designated funds','−$1,200'),('Unfunded target','$4,800'),('$4,800 / 48','$100 per month')],
'The 48 months is a household planning choice, not an estimate of remaining equipment life or assurance that replacement can wait.',
['Asset / assessed condition / replacement-scope assumptions','Target evidence / date / future-price uncertainty','Existing designated balance / other claims on funds','Chosen months / contribution / excluded effects','Review triggers / immediate needs / revised scenario'],
['Saving horizon is not labeled useful life.','Existing funds are not assigned twice.','The model states its excluded effects.'], 'Choose a review date for each reserve scenario and keep urgent assessed needs outside a long-horizon assumption.')

chapter('Keep maintenance cash flow separate from cost','The calendar can expose a funding gap hidden by an annual total.',[
'Build a month-by-month cash schedule using opening designated funds, planned contributions and expected payments. An affordable annual total can still create an early shortfall if a large obligation comes due before contributions accumulate. Record actual due dates rather than assuming every bill is evenly spread.',
'Calculate closing balance as opening balance plus contributions minus paid bills. Carry that balance into the next period. A negative result is a funding gap to resolve, not evidence that the service can be skipped or the invoice date changed without agreement.',
'Keep unpaid commitments visible beside the cash balance. Money in the account is not fully available if it is already assigned to accepted work. Distinguish budget cost, invoice, payment and reserve transfer so the same amount is not counted multiple times.',
'Revise the schedule when timing changes and record the funding decision. Use actual household constraints and confirmed terms when considering alternatives. This workbook provides arithmetic, not a borrowing recommendation or a substitute for personal financial advice.'
], 'A fictional month opens with $400, receives a $100 designated contribution and pays a $450 approved service bill. A separate $80 invoice remains unpaid.', [('Opening funds','$400'),('Contribution','+$100'),('Paid service bill','−$450'),('Closing cash','$50'),('Unpaid commitment','$80'),('Cash less unpaid commitment','−$30')],
'The account still has $50, but it does not cover the $80 outstanding obligation. The $30 funding gap needs a concrete decision.',
['Opening designated balance / date','Planned contributions / timing / source','Accepted bills / due dates / payments','Closing cash / outstanding commitments','Funding gaps / agreed decisions / revised schedule'],
['Transfers and expenses are not duplicated.','Unpaid commitments remain visible.','Closing cash is not treated as uncommitted money.'], 'Check the next three months of actual due dates before relying on the annual monthly average.')

chapter('Compare service plans and pay-per-visit scope','A subscription price does not establish complete coverage.',[
'List the actual included visits, tasks, consumables and response terms for each service option. Distinguish a scheduled inspection from repair coverage. Record exclusions, cancellation terms and conditional charges from the current written offer rather than relying on a headline benefit.',
'Compare an annual plan with separately priced visits using the same assumed service need. If the plan includes tasks or benefits that the visit quote lacks, record the difference instead of assigning them an invented cash value. A response promise may have conditions that affect its usefulness to the household.',
'Separate predictable fees from uncertain repair spending. A discount on future work is not a guaranteed saving if no qualifying work occurs. Keep the repair event count as a scenario input and show how the result changes without predicting failures.',
'Review provider suitability, documentation and access arrangements before selecting a plan. A lower expected price does not make an unsuitable service scope adequate. Save the accepted terms and record renewal dates so recurring charges remain an explicit household choice.'
], 'A fictional plan costs $30 per month and includes two defined visits. Two matched pay-per-visit services cost $150 each. Repairs and all other benefits are excluded from this narrow comparison.', [('Annual plan: 12 × $30','$360'),('Matched visits: 2 × $150','$300'),('Plan premium in this scenario','$60'),('Other plan benefits','Not valued or assumed')],
'The $60 difference is not a recommendation. Compare the actual included work, provider terms and relevant household needs.',
['Plan fee / renewal / cancellation / current terms','Included tasks / visits / consumables / exclusions','Matched visit alternative / scope differences','Repair scenarios / conditional discounts / unknowns','Provider suitability / selection rationale / review date'],
['Visits are compared on matched scope.','Conditional discounts are not guaranteed savings.','Renewal terms are retained.'], 'Request the complete written service-plan inclusions before comparing its monthly price with a visit quote.')

chapter('Track water observations and repair follow-up','Water bills can prompt a question without diagnosing its cause.',[
'Keep accessible observations of drips, unusual usage or recurring wet areas with dates and locations. EPA WaterSense provides home-maintenance resources for water-related checks and professional follow-up [2]. This book does not supply a leak-test, plumbing repair or isolation procedure.',
'Compare water usage only with the bill units, billing-period length and occupancy changes visible. A cost increase can reflect a rate change, fees or a longer period rather than a leak. Report unexplained differences to the appropriate provider instead of labeling every higher bill a fault.',
'Give any assessed repair a defined scope, responsible provider and follow-up record. A completed repair invoice does not show whether every concern has been resolved. Ask the provider which evidence or observation should confirm the outcome and when to review it.',
'Keep repair spending distinct from assumed future water savings. The household can record subsequent usage without claiming that one intervention caused the entire change. Weather, occupancy and other uses may differ across periods.'
], 'A fictional bill records 6,000 gallons over 30 days; the comparison bill records 5,600 gallons over 28 days. Daily average use is the same.', [('6,000 / 30','200 gallons per day'),('5,600 / 28','200 gallons per day'),('Raw bill-volume difference','400 gallons'),('Daily-average difference','0 gallons')],
'Raw bill volume alone would suggest a change. Equal daily averages still do not diagnose the condition of the plumbing.',
['Dated observations / accessible evidence / locations','Bill units / days / usage / occupancy changes','Qualified assessment / repair scope / provider','Follow-up evidence / review date / unresolved issues','Actual repair cost / usage comparison / limits'],
['Billing periods are normalized.','Higher cost is not automatically labeled a leak.','Repair outcomes have a follow-up owner.'], 'Compare bill units and period length, then ask the appropriate provider about unexplained observations.')

chapter('Organize heating and cooling service records','One generic checklist cannot describe every system.',[
'Link the actual system inventory and current manufacturer instructions to the maintenance register. ENERGY STAR provides a maintenance overview [3]; use it as a question list with the service provider rather than as a substitute for the selected equipment requirements.',
'Record the defined work, provider findings and any follow-up recommendation from each service visit. Keep owner observations, measured professional findings and proposed repairs separate. This handbook contains no electrical, combustion, refrigerant or equipment-opening procedure.',
'Clarify what a service package includes and how additional work is authorized. A visit fee may exclude parts, repairs or another call. Keep those exclusions visible and avoid treating a general inspection as a warranty that every component will continue to function.',
'Use the record when comparing a repair and replacement proposal. A service history can improve the evidence available, but it cannot guarantee remaining life or future energy savings. Preserve relevant reports and ask the qualified provider to explain the actual options.'
], 'A fictional service visit costs $150. A separate assessed $90 repair is proposed but not yet approved. Only the visit is a committed expense at this point.', [('Completed agreed visit','$150'),('Unapproved repair option','$90'),('Committed scope','$150'),('If repair is later approved','$240 combined scope')],
'Do not label an optional proposal as a paid or approved obligation. Follow the actual assessed findings and authorization process.',
['Equipment IDs / manual / service requirement sources','Visit scope / provider / dated report','Observations / professional findings / proposed repairs','Approved / unapproved / paid status and exclusions','Follow-up / repair-replacement comparison / retained records'],
['Technical findings identify their provider.','Optional proposals are not treated as approved costs.','A service visit does not promise future reliability.'], 'Ask for a dated service record and a separately defined proposal for any additional work.')

chapter('Review envelope and exterior responsibilities','Plan access and assessment before budgeting physical work.',[
'List the exterior elements the owner is responsible for, including roof, drainage, openings, finishes and accessible site features as applicable. Collect existing reports and observations obtainable from normal safe locations. Do not climb onto roofs, enter hazardous areas or disturb materials to complete the register.',
'Assign questions about water entry, movement, deterioration or drainage to qualified providers. A visual observation is not a diagnosis of structural condition or a repair specification. Keep the location and evidence clear so providers can assess the same reported issue.',
'Define service boundaries with associations, neighbors and other relevant parties where they share responsibility. An exterior maintenance task may involve approval, access or another property. Record who resolves those questions before a proposed visit is treated as ready to proceed.',
'Price assessed scope with access, protection, disposal and restoration included where relevant. A headline cleaning or repair rate may omit supporting services. Keep recurring care, assessed repair and future replacement planning in separate categories.'
], 'A fictional assessed exterior task has $250 defined work and a separate $150 access charge, with both confirmed as non-overlapping.', [('Defined service scope','$250'),('Separate access service','$150'),('Complete quoted task','$400'),('Unassessed additional work','Excluded / unresolved')],
'Access contributes $150 to this invented total. It is not an instruction for reaching any roof or exterior surface.',
['Exterior asset IDs / responsibility / existing reports','Safe observations / locations / assessment questions','Approvals / shared boundaries / access owner','Assessed work / protection / disposal / restoration','Complete price / exclusions / recurring or repair category'],
['No hazardous owner access is required.','Shared responsibilities are resolved.','Supporting service costs are included once.'], 'Give qualified providers the same observation record and request a complete assessed scope.')

chapter('Keep a service history and review the next year','Completion is evidence plus an updated next action.',[
'Record the date, asset, defined task, provider, invoice and outcome for each completed event. Link approved changes and useful findings to the original task. An invoice proves a charge; ask for the service evidence needed to understand what was completed.',
'Update the next-action trigger using the applicable instructions and provider findings. Do not automatically advance every task by a year. A usage-based or condition-based task may need a different review, and an unresolved recommendation should remain open.',
'Compare the original forecast with actual spending and current commitments. Explain differences by scope, quantity, timing or price rather than only recording a variance. Keep confirmed credits and unpaid obligations visible so cash and cost remain reconciled.',
'Use the annual review to revise priorities, reserve assumptions and provider arrangements. Archive superseded records while keeping the current plan clear. A maintenance record supports better decisions; it does not certify that the home has no defects or eliminate the possibility of an unexpected repair.'
], 'A fictional year planned $600 recurring service. Actual completed service totals $570, and a confirmed $30 bill remains unpaid. There is no additional uncommitted work.', [('Paid service','$570'),('Unpaid confirmed bill','$30'),('Total service cost','$600'),('Cost variance to $600 plan','$0'),('Remaining payment obligation','$30')],
'A $570 cash outflow is not a $30 cost saving when the $30 obligation is still due.',
['Completed task / provider / report / invoice references','Findings / unresolved recommendations / action owners','Next trigger / source / revised calendar','Paid / unpaid / credits / cost versus cash variance','Next-year priorities / reserve assumptions / archived history'],
['Completion has supporting evidence.','Next dates use sourced requirements.','Unpaid cost is included in the year-end review.'], 'Reconcile the service history and use its findings to update the next calendar and funding plan.')

method(2,'Build the all-in maintenance funding plan')
method(5,'Normalize contractor proposals')
method(6,'Review the live cost forecast')
method(17,'Approve changes and reconcile the reserve')
method(18,'Close out and retain project records')
SOURCES=[('1','FTC: Home Repair Scams','https://consumer.ftc.gov/features/pass-it-on/home-repair-scams'),('2','EPA WaterSense: Home Maintenance','https://www.epa.gov/watersense/home-maintenance'),('3','ENERGY STAR: Maintenance Checklist','https://www.energystar.gov/saveathome/heating-cooling/maintenance-checklist')]

