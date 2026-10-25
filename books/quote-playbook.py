"""Original contractor proposal comparison cases, with established owner-budget methods."""
from pathlib import Path
import runpy,copy
base=runpy.run_path(str(Path(__file__).with_name('renovation-blueprint.py')))
CHAPTERS=[]
def chapter(title,deck,paragraphs,example,rows,conclusion,prompts,checks,task):
    CHAPTERS.append(dict(title=title,deck=deck,paragraphs=paragraphs,example=example,rows=rows,conclusion=conclusion,prompts=prompts,checks=checks,task=task))
def method(index,title):
    c=copy.deepcopy(base['CHAPTERS'][index]);c['title']=title
    replacements={'renovation':'contractor-led project','Make the kitchen usable for two cooks':'Choose a complete proposal for the intended outcome','buy new cabinets':'accept a contractor price','A bathroom project in a one-bath home has a different temporary-use problem from the same work in an empty property.':'Work in an occupied home creates different temporary-use needs from the same scope in an empty property.','fixture allowance':'finish-selection allowance'}
    def adapt(s):
        for a,b in replacements.items():s=s.replace(a,b)
        return s
    for k in ['deck','example','conclusion','task']:c[k]=adapt(c[k])
    for k in ['paragraphs','prompts','checks']:c[k]=[adapt(x) for x in c[k]]
    CHAPTERS.append(c)

method(0,'Define the contractor comparison brief')
chapter('Send one common request for proposals','Comparable answers begin with comparable questions.',[
'Create a dated request describing the desired outcome, project areas, retained elements and known constraints. Include relevant measurements and professional documents, clearly marking which are verified and which need contractor confirmation. A request for the best price without a common scope invites different interpretations.',
'Give each bidder the same information and reasonable opportunity to assess the property. Record the documents supplied, visit dates and questions raised. If one bidder identifies a material scope issue, resolve it and communicate the revised common requirement to all bidders rather than comparing answers to different briefs.',
'Identify the response format you need: work description, exact products where selected, included and excluded tasks, allowances, pricing basis, timing, payments and completion documents. A structured request makes gaps easier to find without forcing contractors to reveal an invented internal cost breakdown.',
'Assign a version and response deadline, and keep later revisions separate. A telephone clarification should become a written confirmation when it affects price or responsibility. Retain original proposals so you can trace the accepted scope instead of silently overwriting its history.'
], 'A fictional request goes to three bidders with the same four attachments: scope, plan, selections and assessed-condition report. One revised selection replaces its earlier version for all three.', [('Bidders','3'),('Common current attachments','4'),('Superseded selection','Archived, not current'),('Comparable request version','Same for all bidders')],
'Attachment counts do not establish completeness. Check that every bidder acknowledges the same current documents.',
['Project outcome / areas / retained work / constraints','Verified inputs / open assessments / document list','Bidder visits / questions / common clarifications','Requested scope / pricing / dates / response format','Current version / deadline / acknowledgments'],
['All bidders use the same current brief.','Unverified inputs remain labeled.','Price-affecting clarifications are written.'], 'Issue a single dated request and ask each bidder to acknowledge its attachments.')

chapter('Classify every scope line','Included, excluded, allowance and unresolved mean different things.',[
'Break the project into clear work packages and give each line an ID. For every bidder, mark each line included, excluded, allowance or unresolved. Do not use a blank cell to mean both included at no extra charge and not yet discussed.',
'Treat an inclusion as a defined obligation only when the proposal describes its boundary. A phrase such as all necessary work may still leave unclear which product, area or supporting service is covered. Ask for a written explanation rather than assuming the broadest interpretation.',
'For exclusions, identify whether the work is required for the intended outcome and who would deliver it. For allowances, record the quantity or selection basis and adjustment terms. For unresolved items, obtain an answer before declaring the comparison complete.',
'Keep technical suitability and approvals separate from scope status. A clearly priced line can still need professional assessment. The table organizes the owner decision without certifying design, code compliance or the legal meaning of contract language.'
], 'A fictional ten-line proposal has six defined inclusions, two required exclusions, one allowance and one unresolved item.', [('Defined inclusions','6'),('Required exclusions','2'),('Allowance','1'),('Unresolved','1'),('Total scope lines','10')],
'A low total covering six lines cannot be ranked as a complete ten-line project price without resolving the other categories.',
['Common work-package IDs / boundaries','Included lines / written evidence','Excluded required work / responsible provider','Allowance basis / adjustment terms','Unresolved items / assessor / answer deadline'],
['Blank cells do not conceal uncertainty.','Required exclusions have an action owner.','Pricing status is separate from technical suitability.'], 'Mark every line for each bidder and send the unresolved items back for written clarification.')

chapter('Normalize quantities and price units','A unit rate is meaningful only with its denominator.',[
'Record the actual quantity and unit behind each rate: square feet, linear feet, pieces, hours or another stated measure. Distinguish net installed quantity from ordered material coverage and identify fixed charges. Do not multiply every rate by one convenient area when the quote uses several different bases.',
'Convert units explicitly before comparing. One square yard is nine square feet, while a linear yard is three linear feet. The units describe different dimensions. A material sold by the pack needs its exact coverage before its price can be translated into an area rate.',
'Check whether the rate includes material, labor, preparation or disposal. Two identical rates can buy different scope. For an indivisible package, compare the complete package rather than inventing a precise component price the contractor has not supplied.',
'Retain the original rate and conversion beside the normalized result. Ask the contractor to confirm the quantity basis and whether a revised measurement changes the price. A successful multiplication does not verify site dimensions or authorize a scope change.'
], 'One fictional material quote is $4 per sq ft. Another is $36 per sq yd for the same product and inclusions. Each applies to 100 sq ft of purchased coverage.', [('$36 / 9','$4 per sq ft'),('100 × $4','$400'),('Normalized material difference','$0'),('Installed total','Not established')],
'Only the material scope has been matched. Labor, fixed fees and other exclusions still need comparison.',
['Original quantities / units / measurement source','Rate inclusions / net or purchased basis','Conversion formula / normalized rate','Fixed fees / package boundaries / separate labor','Contractor confirmation / revision terms / open questions'],
['Linear and area units are distinguished.','Price inclusions match before ranking.','The original rates remain traceable.'], 'Check one representative rate independently and confirm its quantity basis with the bidder.')

chapter('Replace allowances with a common comparison basis','A small allowance can make an incomplete bid look cheaper.',[
'List allowances separately from fixed defined work. Record what each allowance covers, its assumed quantity or selection, and how the final charge will be determined. A supply-only allowance and a complete installed allowance are different scopes.',
'For comparison, choose a common documented scenario for the allowance item and replace each bidder allowance with that scenario cost on a clearly labeled comparison sheet. Keep the original quoted total intact. The normalized scenario is an owner analysis, not a revised contractor offer.',
'Show any applicable quoted markup or other adjustment terms separately. If the contractor has not confirmed how an allowance difference is treated, keep the normalized total conditional. Do not invent a markup to make the table appear precise.',
'Use actual selected products and updated proposals to resolve the allowance before commitment where practical. An allowance is not a reserve for every unknown condition, and a larger allowance does not itself guarantee that the included work is suitable or complete.'
], 'Fictional bid A is $10,000 including a $500 supply allowance. Bid B is $10,600 including a $1,200 allowance. A common $1,000 supply scenario replaces each allowance, with no other adjustments assumed.', [('A: $10,000 − $500 + $1,000','$10,500'),('B: $10,600 − $1,200 + $1,000','$10,400'),('Scenario difference','$100 in B’s favor'),('Revised binding offers','Not established')],
'The lower headline bid becomes $100 higher in this limited common scenario. Confirm actual adjustment terms and remaining scope before choosing.',
['Allowance item / original amount / included scope','Quantity or selection basis / adjustment terms','Common scenario / source / excluded effects','Original total less allowance plus scenario','Contractor clarification / selected product / revised offer'],
['The original allowance is removed first.','Normalization is labeled a scenario.','Unknown adjustment terms remain visible.'], 'Ask each bidder to price the same final selection and explain how its original allowance is replaced.')

chapter('Reconcile tax, markups and fixed fees','An addition needs a defined base and inclusion check.',[
'Ask whether the quoted total includes relevant tax, delivery, permit-related fees and other fixed charges. Applicable tax and approval requirements depend on the actual jurisdiction and transaction. This book does not supply a tax rate, legal determination or universal fee schedule.',
'For any percentage addition, identify the exact base to which it applies and whether the quoted amount already contains it. A markup on a defined subcontractor cost is different from a percentage applied to every line. Do not assume that similarly named charges use the same calculation.',
'Keep supply, labor and fixed-fee categories separate when the stated terms require different treatment. Ask the provider to confirm a complete all-in proposal rather than calculating uncertain tax treatment yourself. Use invented examples only to understand arithmetic.',
'Check the normalized comparison for duplication. If delivery is already inside an installed package, adding a separate estimated delivery charge overstates the comparison. Save the written inclusion confirmation so the total can be reviewed later.'
], 'An invented quotation has $1,000 of a specifically defined cost base, an explicitly agreed 10% markup on that base and a separate $50 delivery fee. No tax is modeled.', [('Defined base','$1,000'),('10% of $1,000','$100'),('Separate delivery','$50'),('Example subtotal','$1,150')],
'The 10% is a teaching assumption, not a standard contractor markup. Confirm the actual calculation base and tax-inclusive total.',
['Quoted total / tax and fee inclusion status','Percentage addition / exact base / written terms','Fixed fees / packages / delivery reconciliation','Provider-confirmed complete amount / unresolved treatment','Independent arithmetic / evidence / revision date'],
['Every percentage has a defined base.','Tax treatment is confirmed for the actual transaction.','Package fees are not added twice.'], 'Request a written total that states all included taxes, fees and conditional additions.')

chapter('Compare fixed, unit-rate and cost-based offers','The payment model changes what the quoted number means.',[
'Ask the contractor to explain the pricing arrangement in plain language and identify what can change the final amount. A fixed defined scope, measured unit-rate work and a cost-based arrangement allocate uncertainty differently. The offer label alone does not establish its legal effect.',
'For unit-rate work, record the measurement method, expected quantity and approval process for changes. For cost-based work, ask about allowable costs, documentation, fee basis and any stated limit. Have qualified local advice review legal or financial commitments when needed.',
'Compare scenarios using the actual written terms. A low initial estimate may rise with additional measured quantity, while a fixed offer may still exclude concealed conditions or later owner choices. Keep known differences visible instead of treating every headline as a guaranteed final price.',
'Do not turn a scenario cap into a promise if the contractor has not agreed to it. Record which costs remain conditional and what evidence is needed before more work is authorized. The owner sheet supports review; it is not a model contract.'
], 'A fictional unit-rate offer is $20 per verified unit with an initial estimate of 100 units. An approved final quantity is 120 units, with the same rate and scope.', [('Initial scenario: 100 × $20','$2,000'),('Approved quantity: 120 × $20','$2,400'),('Quantity-driven increase','$400'),('Price per unit change','$0')],
'The increased total comes from quantity, not a higher rate. Actual contractual adjustment rights require review of the written terms.',
['Pricing arrangement / written explanation / scope','Measurement or cost-documentation basis','Fees / limits / exclusions / approval boundaries','Initial and revised scenarios / change causes','Local professional review / unresolved commitments'],
['Offer labels are not treated as legal conclusions.','Conditional quantities and costs stay visible.','An owner scenario is not a contractor promise.'], 'Ask the bidder to demonstrate how the final invoice would be calculated under its actual offer.')

chapter('Verify the business behind the proposal','A polished document does not verify credentials.',[
'Record the contracting business name, contact details and identifiers needed to check its suitability for the actual work. FTC consumer guidance supports checking providers and obtaining written estimates [1]. Verify current information through relevant official or issuing sources rather than accepting a logo or screenshot alone.',
'Requirements differ by place and work type. Use the relevant state or local authority to determine what applies. California CSLB is one example of a jurisdiction-specific licensing resource [2]; its rules and lookup do not establish requirements for every U.S. project.',
'Ask for current insurance information and verify relevant details with the appropriate issuing source. Keep the scope, dates and named entity aligned with the proposal. This handbook does not determine adequate coverage, legal status or eligibility to perform a particular trade.',
'Record unresolved verification items as decision gates. Do not award a favorable score simply because a document was supplied if its identity, currency or relevance remains unclear. Keep the verification date and source with the decision file.'
], 'A fictional review requests four records. Two are independently checked, one needs a name correction and one remains unanswered.', [('Independently checked','2'),('Needs correction','1'),('Unanswered','1'),('Verification complete','No')],
'Four supplied filenames would not equal four verified requirements. Resolve the two open records before relying on them.',
['Contracting entity / identifiers / proposal match','Relevant local requirements / official source','Current insurance / issuer confirmation / scope questions','Verification date / evidence / provider explanations','Open gates / correction owner / decision deadline'],
['Entity names match the proposal.','Jurisdiction-specific examples are not universalized.','Supplied documents are distinct from verified facts.'], 'Verify the relevant current credentials through appropriate official or issuing sources before commitment.')

chapter('Check references without inventing evidence','Experience claims need relevant, attributable support.',[
'Ask for relevant completed-project references and permission to contact the people offered. Compare project type, scope, timing and the issues important to the current job. A distant project with different responsibilities may provide less useful evidence than a closely matched recent one.',
'Use consistent questions about communication, scope changes, completion and follow-up. Record what the reference actually reports and distinguish first-hand observations from assumptions. Do not publish a reference name, quotation or review without the appropriate permission.',
'Treat online reviews as one source of information whose authenticity and relevance need judgment. Do not create reviews, invent customer outcomes or present marketing examples as verified experience. A numerical average cannot resolve every question about the provider or the proposed project.',
'Keep contradictions and gaps visible. If a bidder cannot supply a relevant reference, ask what other evidence can be reviewed rather than fabricating a positive score. A reference check informs the decision but cannot guarantee future performance.'
], 'A fictional bidder supplies three reference contacts. Two discuss comparable completed work with permission; the third describes a different service and is recorded as less relevant.', [('Contacts supplied','3'),('Relevant completed-work discussions','2'),('Different-scope reference','1'),('Guaranteed future performance','Not established')],
'The book uses hypothetical records, not real endorsements. No review or customer quotation is invented for publication.',
['Relevant project type / dates / reference permission','Consistent questions / first-hand observations','Attributable evidence / relevance / limitations','Online claims / conflicts / clarification needs','Private decision notes / publication permission status'],
['Evidence is recorded faithfully.','Hypothetical cases are not customer testimonials.','References do not become performance guarantees.'], 'Use the same reference questions for shortlisted bidders and retain the limitations of each answer.')

chapter('Compare schedules through dependencies','A short duration may begin after different prerequisites.',[
'Record proposed start conditions, duration, sequencing and completion definition. A two-week installation after material delivery cannot be compared directly with a two-week total from authorization. Ask which approvals, selections and site conditions must be satisfied first.',
'Identify owner decision deadlines and other-trade interfaces. A contractor may depend on product selection, utility coordination or access outside its control. Keep responsibility and dates visible rather than treating every delay as the same kind of event.',
'Ask how the contractor communicates a schedule change and how any related charge is reviewed. This book gives no universal delay entitlement or liquidated-damages term. Actual rights and obligations require the relevant written agreement and appropriate local advice.',
'Compare the practical effect on the household as well as the duration. Temporary facilities, storage, access and time away from work can create owner costs. Add those costs only once and keep assumptions separate from confirmed arrangements.'
], 'Fictional option A starts after 14 days of prerequisites and then takes 10 days. Option B starts after 7 days and takes 14 days. The example assumes consecutive calendar days with no overlap.', [('A: 14 + 10','24 days to completion'),('B: 7 + 14','21 days to completion'),('Duration on site: A / B','10 / 14 days'),('Scenario completion difference','3 days')],
'A has a shorter work duration but a later assumed completion. Actual schedules need confirmed dependencies and dates.',
['Start prerequisites / dates / duration definitions','Selections / approvals / other-trade owners','Sequence / household access / temporary costs','Delay communication / review / written terms','Comparable completion dates / assumptions / gaps'],
['Start conditions are compared explicitly.','Calendar and working days are labeled.','Owner disruption costs are included once.'], 'Ask each bidder for the dependency sequence behind its proposed completion date.')

chapter('Translate payment schedules into cash needs','A lower price may require more money earlier.',[
'Record each proposed payment milestone, amount, due condition and evidence required. Reconcile the payments to the accepted total. Percentages can be easy to misread if the base changes or if a deposit is later counted again rather than credited toward the price.',
'Compare the amount due before work, during work and after defined completion. Keep actual payment timing separate from cost recognition. A milestone payment can fund a project without proving that all technical completion requirements have been met.',
'Check applicable local payment and contract requirements with the appropriate authority or adviser. This guide supplies no universal lawful deposit percentage, retention rule or payment entitlement. Do not use an invented schedule here as contract language.',
'Match the schedule to household available funds and keep unpaid accepted obligations visible. Record payment evidence and verify destination details through a trusted channel where relevant. Do not assume that a financing offer reduces the underlying project cost.'
], 'An invented $10,000 proposal has four agreed payments: $1,000, $4,000, $3,000 and $2,000. The example is arithmetic only, not a recommended or legally approved schedule.', [('Payment 1','$1,000'),('Payment 2','$4,000'),('Payment 3','$3,000'),('Payment 4','$2,000'),('Total payments','$10,000'),('Paid after first two / remaining','$5,000 / $5,000')],
'The first payment is part of the $10,000, not an addition. Actual payment terms and local requirements need separate review.',
['Milestones / amounts / due conditions / evidence','Deposit credit / total reconciliation / payment base','Available cash / actual dates / unpaid obligations','Relevant local review / financing cost questions','Confirmed payee / receipts / change approvals'],
['Scheduled payments sum to the quoted total.','Deposits are credited once.','The example is not used as a legal payment rule.'], 'Reconcile every payment to the price and check the actual terms before authorizing any payment.')

chapter('Use a written clarification log','A question is open until its answer changes the record.',[
'Give each clarification a unique ID, proposal reference and concise question. State what decision depends on the answer and who must respond. Group related scope questions without burying the key issue inside a long email chain.',
'Record the answer, date and evidence. If a response changes a product, price, exclusion or responsibility, ask for the corresponding revised proposal or written incorporation into the accepted documents. A reassuring conversation is not the same as a resolved scope line.',
'Apply material common-scope changes consistently to the remaining bidders. A bidder-specific alternative should be labeled separately so it does not silently change the comparison baseline. Retain the original proposal and version history.',
'Close a question only when the answer is specific enough for the decision and the dependent records are updated. If there is no answer, record the limitation and choose an appropriate next step. Do not interpret silence as agreement.'
], 'A fictional log has eight questions. Five are answered and incorporated, two are answered but await revised prices, and one remains unanswered.', [('Closed with updated evidence','5'),('Answer received, revision pending','2'),('Unanswered','1'),('Open decision items','3')],
'Receiving seven answers does not mean seven items are complete. Two still need their price records updated.',
['Question ID / proposal line / decision dependency','Responsible respondent / due date / contact record','Answer / evidence / scope or price effect','Revised documents / common-baseline effect','Open or closed status / closure evidence'],
['Silence is not treated as approval.','Scope changes reach dependent records.','Answered and closed are different statuses.'], 'Send a short numbered clarification list and request a revised proposal for every price-affecting answer.')

chapter('Use decision scores without hiding essential gaps','A weighted total is a tool, not proof of the right choice.',[
'Set essential requirements before scoring optional preferences. Relevant suitability, complete scope and verified prerequisites should be resolved as decision gates where appropriate. A strong score for appearance or price should not automatically offset an unresolved essential requirement.',
'Choose criteria and weights before seeing the final ranking, and define the scale in plain language. Use evidence for each score and mark missing information as unresolved rather than assigning a flattering number. Keep the financial comparison visible beside the score.',
'Check how the ranking changes when a reasonable assumption or weight changes. If a small preference change reverses the result, explain that sensitivity in the decision record. A score with decimal places is not necessarily more reliable than the evidence behind it.',
'Record the final choice and tradeoffs, including any unresolved item that prevents commitment. The worksheet helps explain the owner decision but cannot guarantee workmanship, enforceability or future outcomes.'
], 'An invented 1–5 preference scale weights matched price at 40%, evidence-based scope confidence at 40% and schedule fit at 20%. All essential gates are assumed resolved. A scores 5, 3, 4; B scores 4, 5, 3.', [('A: 5×0.4 + 3×0.4 + 4×0.2','4.0'),('B: 4×0.4 + 5×0.4 + 3×0.2','4.2'),('Illustrative preference ranking','B ahead by 0.2'),('Guaranteed better outcome','Not established')],
'The weights and scores are invented. A 0.2 lead does not remove the need to inspect evidence and sensitivity.',
['Essential gates / evidence / resolution status','Preference criteria / weights totaling 100%','Defined scale / score evidence / missing information','Weighted totals / sensitivity / financial comparison','Decision rationale / tradeoffs / remaining conditions'],
['Essential gaps are not hidden by averaging.','Weights are explicit and sum to 100%.','Scores are not presented as guarantees.'], 'Write the reason for each score and test whether a modest weight change alters the ranking.')

chapter('Move from comparison to an accepted scope','The spreadsheet does not replace the agreement.',[
'Check that the final documents identify the selected entity, scope, products, price, allowances, dates, payments and responsibilities actually agreed. Carry accepted clarifications and revisions into the final record. A comparison sheet is useful evidence but does not automatically amend a contractor document.',
'Review the written change process before work begins. Identify who can approve an addition, what information must accompany it and how price and timing are recorded. Use appropriate professional advice for legal commitments rather than relying on this book as a contract template.',
'State the completion and handover evidence expected for the actual work, including relevant professional or authority records, product documents, care instructions and punch-list handling. The owner file should distinguish technical approvals from an informal visual walk-through.',
'Retain the accepted version, invoices, payment records, changes and completion file together. Compare the final cost with the original selection rationale so future decisions learn from actual scope and assumptions. Do not erase unresolved obligations simply because work appears finished.'
], 'An invented accepted scope is $10,400. A later written $300 addition and a confirmed $100 credit produce $10,600. Payments total $9,000, leaving $1,600 unpaid.', [('Accepted scope','$10,400'),('Approved addition','$300'),('Confirmed credit','−$100'),('Revised defined cost','$10,600'),('Paid / unpaid','$9,000 / $1,600')],
'The example reconciles cost and payment only. Actual completion acceptance and payment rights require the agreed terms and relevant review.',
['Accepted entity / scope / price / document versions','Clarifications / allowances / responsibility boundaries','Written change authority / price / timing records','Completion evidence / punch list / care / warranties','Final cost / payments / credits / unpaid obligations'],
['Accepted revisions are in the final record.','Technical completion has the appropriate evidence.','Unpaid obligations remain visible at closeout.'], 'Review the final accepted document set and keep one current owner record before work starts.')

method(2,'Build the all-in contractor project budget')
method(5,'Normalize contractor proposals')
method(6,'Review the live cost forecast')
method(17,'Approve changes and reconcile the reserve')
method(18,'Close out and retain project records')
SOURCES=[('1','FTC: Home Repair Scams','https://consumer.ftc.gov/features/pass-it-on/home-repair-scams'),('2','California CSLB: Contractor licensing resource','https://www.cslb.ca.gov/')]

