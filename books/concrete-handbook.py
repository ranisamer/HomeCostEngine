"""Original concrete planning and quantity cases, with established owner-budget methods."""
from pathlib import Path
import runpy,copy
base=runpy.run_path(str(Path(__file__).with_name('renovation-blueprint.py')))
CHAPTERS=[]
def chapter(title,deck,paragraphs,example,rows,conclusion,prompts,checks,task):
    CHAPTERS.append(dict(title=title,deck=deck,paragraphs=paragraphs,example=example,rows=rows,conclusion=conclusion,prompts=prompts,checks=checks,task=task))
def method(index,title):
    c=copy.deepcopy(base['CHAPTERS'][index]);c['title']=title
    replacements={'renovation':'concrete project','Make the kitchen usable for two cooks':'Make the outdoor area usable for the household','buy new cabinets':'order concrete','A bathroom project in a one-bath home has a different temporary-use problem from the same work in an empty property.':'Replacing the only access path creates different temporary-use needs from placing a separate patio.','fixture allowance':'finish-selection allowance'}
    def adapt(s):
        for a,b in replacements.items():s=s.replace(a,b)
        return s
    for k in ['deck','example','conclusion','task']:c[k]=adapt(c[k])
    for k in ['paragraphs','prompts','checks']:c[k]=[adapt(x) for x in c[k]]
    CHAPTERS.append(c)

method(0,'Define the concrete project brief')
chapter('Record the site and existing conditions','The same area can involve very different preparation.',[
'Create a dated sketch showing the proposed work, adjoining structures, access and surfaces to remain. Assign area IDs so measurements and quotes can refer to the same locations. Record known prior repairs, visible damage and any existing drawings or reports without treating an owner observation as a technical assessment.',
'Ask the responsible professional to assess site conditions and any drainage, soil, structural or utility questions relevant to the proposed work. A calculator cannot confirm those conditions or determine the appropriate construction. Keep each unresolved issue as an open decision with a verifier and a date.',
'List existing material to remove and how adjacent surfaces are protected and restored. Identify access restrictions, shared-property coordination and the limits of the contractor work area. An apparently simple concrete price can exclude substantial removal, disposal or preparation.',
'Use safe records and professional assessments rather than digging, testing or disturbing utilities yourself. This handbook is for owner planning and arithmetic. It does not locate utilities, approve excavation or provide site investigation, structural design or construction instructions.'
], 'An owner records four area IDs: two new-work areas, one retained access path and one area awaiting drainage assessment. The unresolved area remains a decision gate.', [('New-work areas','2'),('Retained access area','1'),('Assessment area','1'),('Total identified areas','4')],
'Area counts organize responsibility; they do not establish usable dimensions, drainage design or site suitability.',
['Site sketch / area IDs / dated records','Visible conditions / prior reports / retained surfaces','Professional site questions / utility coordination','Removal / protection / restoration boundaries','Open assessments / responsible parties / deadlines'],
['Observed conditions are distinct from diagnoses.','Required assessments have an owner.','The workbook does not authorize digging or site changes.'], 'Provide the same site record to bidders before asking for complete prices.')

chapter('Separate project use from construction design','A quantity input is not a recommended slab specification.',[
'Write the intended use and the outcome the project must provide. A walkway, patio, vehicle area and structural element can have different design questions. Record expected use and relevant site information for the qualified professional instead of selecting thickness, reinforcement or a mixture from a generic example.',
'Ask who establishes the dimensions, support, material requirements and applicable approvals for the actual project. Identify the drawing or specification version used in each proposal. The owner needs to understand the scope and responsibility; the technical design must remain with the appropriate provider.',
'Keep quantity checking separate from suitability checking. If a designer supplies a thickness, the owner can verify the arithmetic using that value. The fact that a volume calculation works does not show that the thickness, area or material is appropriate.',
'When use or layout changes, identify which professional decisions and quantities need review. A larger parking area or changed boundary is not merely another multiplication if it alters the design or drainage problem. Revise the scope before treating a supplier order as final.'
], 'For arithmetic only, an area of 120 sq ft has a geometric volume of 40 cu ft at 4 in thickness, or 60 cu ft at 6 in. Neither thickness is recommended for any use.', [('120 × 4 / 12','40 cu ft'),('120 × 6 / 12','60 cu ft'),('Difference','20 cu ft'),('Suitable thickness','Not determined here')],
'The increase demonstrates quantity sensitivity, not a design choice. Use professionally established specifications for the actual project.',
['Intended use / required outcomes / site references','Responsible designer or qualified provider','Approved dimensions / specification version','Requirements and approvals to confirm','Changes triggering reassessment / owner decisions'],
['Quantity examples are not treated as designs.','The actual specification has a responsible author.','Changed use triggers an explicit review.'], 'Obtain the project-specific scope and specifications before requesting a firm supply order.')

chapter('Check rectangular quantities and units','Keep the arithmetic visible from sketch to order.',[
'Record length and width in feet and thickness in a clearly labeled unit. Convert inches carefully: a 4 in depth is one-third of a foot, not four feet. Retain the original measurement record so another person can verify both the conversion and the dimensions used.',
'For a rectangular volume with length and width in feet and thickness in inches, cubic yards equal length times width times thickness divided by 324. The divisor combines 12 inches per foot with 27 cubic feet per cubic yard. This is a geometric conversion only.',
'Calculate separate areas before adding them, keeping unrounded values until the total and selected allowance are considered. Mark excluded steps, edges, openings or irregular sections. Ask the installer to verify the actual takeoff before the supplier receives a final quantity.',
'Use an independent arithmetic check to catch typing mistakes. A plausible-looking result can still be wrong if the width, thickness or unit was entered incorrectly. No calculator can verify site dimensions or approve the construction represented by the numbers.'
], 'A fictional rectangular section measures 12 ft × 10 ft × 4 in solely for arithmetic. It has no thickened edges or other additional volume in this example.', [('Area: 12 × 10','120 sq ft'),('Volume: 12 × 10 × 4 / 324','1.48148 cu yd'),('Same volume in cubic feet','40 cu ft'),('Allowance','Not yet added')],
'Do not round 1.48148 down to a supplier order. Confirm the full takeoff, any selected allowance and the supplier ordering increment first.',
['Area ID / measurement source / date','Length / width / thickness / labeled units','Geometric formula / unrounded result','Excluded or additional volumes','Installer-confirmed takeoff / order responsibility'],
['Feet and inches have not been confused.','The quantity refers to the approved geometry.','A geometric result is not a ready-to-place order.'], 'Use the HomeCostEngine concrete calculator as a second arithmetic check, then retain the sketch.')

chapter('Break irregular shapes into checkable parts','Prevent gaps and double-counted overlaps.',[
'Divide the proposed area into rectangles, triangles or other simple shapes that match the actual sketch. Give each part an ID and mark shared boundaries. Add only non-overlapping areas; two rectangles that cover the same corner will overstate the quantity if their full areas are simply added.',
'For a triangle, area is one-half times its base times perpendicular height. For a circle, area is pi times radius squared. Keep radius distinct from diameter, and do not substitute a sloped edge for a perpendicular height. Ask the installer to verify irregular field dimensions.',
'If thickness differs by section, calculate each volume separately before adding cubic yards. Multiplying the combined area by one average thickness can obscure the specification or a transcription error. Record the source of each thickness rather than inventing one for a tidy worksheet.',
'Retain the drawing and the calculation together. Use a revised version when a boundary moves, and reconcile that revision against the contractor and supplier records. This calculation does not design curves, drainage, stairs or structural elements.'
], 'A fictional non-overlapping layout has a 10 × 8 ft rectangle and a triangle with 6 ft base and 4 ft perpendicular height. Both use an assumed 4 in thickness for arithmetic only.', [('Rectangle area','80 sq ft'),('Triangle area: 0.5 × 6 × 4','12 sq ft'),('Combined area','92 sq ft'),('92 × 4 / 324','1.13580 cu yd')],
'The example has no overlap and no additional edge volume. Confirm actual boundaries and specifications before ordering.',
['Part IDs / sketch / boundary version','Shape formulas / verified dimensions','Overlap and opening adjustments','Thickness by part / volume subtotals','Combined unrounded volume / installer check'],
['Shared areas are counted once.','Radius, diameter and height are distinguished.','Different thicknesses are calculated separately.'], 'Have another person trace the calculation back to the labeled sketch before accepting the quantity.')

chapter('Add extra depth and edge volume once','Count only the part missing from the main slab calculation.',[
'Where a professional design identifies deeper sections, calculate their additional volume separately. If the main slab already includes the top portion of a thickened edge, adding the full edge depth again would duplicate that portion. Label total depth and additional depth explicitly.',
'Record the actual edge length, width and depth from the approved specification. Corners or intersecting strips may overlap, so the takeoff needs a defined method for accounting for those intersections. The simplified example here assumes a non-overlapping strip.',
'Keep footings, steps or separate components as their own scope and quantity records when applicable. Do not infer their dimensions from the slab example. Have the responsible professional confirm geometry and the installer confirm the full takeoff.',
'Ask whether the quoted order quantity already contains the deeper sections and any allowance. A supplier ticket or one-line proposal may show a total without explaining its components. Reconcile those records before approving a revised order.'
], 'A fictional design has a main slab already counted at 4 in. A non-overlapping edge strip is 30 ft long, 1 ft wide and 10 in total depth. Only the extra 6 in belongs in the addition.', [('Additional depth: 10 − 4','6 in'),('Added volume: 30 × 1 × 6 / 324','0.55556 cu yd'),('Main slab example volume','1.48148 cu yd'),('Combined geometric volume','2.03704 cu yd')],
'The dimensions are not design recommendations. The strip example excludes corner overlaps and other components.',
['Approved detail / strip or component ID','Main depth / total depth / additional depth','Length and width / overlap treatment','Added volume / existing slab quantity','Full takeoff confirmation / allowance already included'],
['Only uncounted depth is added.','Intersections and corners are checked.','All dimensions come from the responsible design.'], 'Ask the installer to show separate base and additional-volume lines in the takeoff.')

chapter('Turn a takeoff into an approved order','An allowance and a supplier increment are separate decisions.',[
'Start with the complete geometric quantity and the verified scope. Record a selected allowance for actual ordering uncertainty with a stated reason. Do not use an example percentage as a construction rule, and do not add a second allowance if the contractor quantity already includes one.',
'Ask the installer and supplier how quantities are ordered and billed, including any minimum or increment. Round only at the appropriate ordering stage and retain the unrounded calculation. The order should identify who confirms the final amount and who communicates a change.',
'For packaged material, use the actual product yield stated by the supplier or manufacturer. Bag weight alone does not tell you the finished volume. Site preparation, mixing and placement are separate professional questions; this workbook supplies no mix or construction instructions.',
'Keep the confirmed order, takeoff and delivery record together. If the delivered or used quantity differs, document the reason and reconcile billing against the accepted terms. A small order may still involve fixed fees that a volume-only calculation omits.'
], 'A fictional complete takeoff is 2.03704 cu yd. A chosen 8% allowance gives 2.20000 cu yd approximately. The hypothetical supplier order increment is 0.25 cu yd, giving a rounded order of 2.25 cu yd.', [('Geometric volume','2.03704 cu yd'),('With 8% selected allowance','2.20 cu yd'),('Round up at 0.25 cu yd increment','2.25 cu yd'),('Supplier policy','Must be confirmed locally')],
'The 8% and increment are invented inputs. They are not universal ordering recommendations.',
['Complete takeoff / version / verifier','Allowance / reason / already-included check','Supplier minimum / increment / billing terms','Rounded approved quantity / confirming person','Change contact / order reference / delivery reconciliation'],
['An allowance has a documented basis.','Rounding is applied after the allowance.','Supplier terms are verified rather than assumed.'], 'Obtain installer and supplier confirmation of the final quantity and order terms before delivery.')

chapter('Budget removal, excavation and base scope','Concrete volume does not measure the whole project.',[
'Identify existing material to remove, required preparation and the scope of any base work from the professional assessment. Concrete supply, removal, excavation, disposal and preparation are different services. A low price per cubic yard does not establish the installed cost of the completed area.',
'Record quantities and units for each task. A square-foot removal rate, a cubic-yard disposal amount and a fixed mobilization charge cannot be compared as if they described the same work. Ask what each quoted unit includes and how unknown conditions are handled.',
'Have qualified providers address utilities, soil, support and drainage questions relevant to excavation. This book does not approve digging, specify compaction or determine base depth. Identify investigation and approval responsibilities before work starts.',
'Keep evidence for conditional preparation work and an agreed change process. If additional scope is needed, reconcile it against any existing allowance before drawing on reserve. Assign restoration of adjacent surfaces and access routes as part of the complete project.'
], 'A fictional proposal has $600 removal, $450 disposal and $900 defined base preparation. Concrete supply and placement are priced separately and do not include those tasks.', [('Removal','$600'),('Disposal','$450'),('Defined preparation','$900'),('Supporting scope subtotal','$1,950')],
'Confirm that disposal is not already inside the removal rate. The figures do not specify the depth or method of preparation.',
['Remove / retain / preparation scope by area','Quantity units / rate inclusions / fixed charges','Professional site review / utility coordination','Conditional work / evidence / allowance / approval','Access and adjacent-surface restoration responsibility'],
['Preparation is distinct from material supply.','Disposal appears in one line only.','Technical site requirements have a qualified reviewer.'], 'Request an itemized supporting-work scope before comparing installed concrete prices.')

chapter('Ask about reinforcement, joints and interfaces','A material list does not replace a project-specific design.',[
'Ask the responsible professional to identify reinforcement and joint requirements for the actual use, geometry and conditions. Record the drawing or specification reference and the installer responsible. This handbook does not provide a reinforcement schedule, joint layout or spacing rule.',
'Clarify material supply, installation and any related preparation or supports within the quote. A line naming a material is not a complete description of its installed scope. Do not assume different reinforcement options are interchangeable because two bids use similar prices.',
'Identify interfaces with existing structures and adjoining concrete. Ask who evaluates the proposed connection or separation and how the decision is recorded. Keep those requirements with the accepted scope rather than allowing an owner sketch to become an unreviewed construction instruction.',
'Agree what records or checks are required before work is concealed or placement begins. Photos may support the project file but do not replace professional verification or required inspection. Resolve substitutions and changes through the agreed approval process.'
], 'A fictional comparison includes $420 specified material supply, $380 defined installation and $200 agreed interface work. The example assumes non-overlapping scope only.', [('Specified material supply','$420'),('Defined installation','$380'),('Interface scope','$200'),('Comparison subtotal','$1,000')],
'The sum compares documented scope; it does not approve a reinforcement or joint design.',
['Design and specification references / responsible reviewer','Supply / installation / inclusions by component','Joint and interface scope / adjoining structures','Required checks / records / timing','Substitutions / approved changes / price effects'],
['Technical details have a responsible design source.','Alternative materials are not assumed equivalent.','Concealed work has defined evidence and approval.'], 'Ask each bidder to identify the same design and interface requirements in their proposal.')

chapter('Confirm the mixture and supplier information','Order against the actual project requirements.',[
'Ask the responsible designer or qualified provider to establish the required concrete properties and project specifications. NRMCA ordering guidance describes the role of project-specific requirements and producer coordination [2]. Do not select a generic mixture from a price comparison or a workbook example.',
'Record the supplier, specified mixture reference, approved quantity and placement location. Keep the actual specification and any accepted revision with the order. The provider should explain the designation used so the site team can identify the intended material on the delivery record.',
'Clarify which party is ordering and which party accepts or communicates changes to the supplier. Record delivery timing, contact details and the process for an unavailable or substituted material. This handbook provides no recipe, strength requirement, slump target or authority to modify a load.',
'Retain delivery and billing documents with the project record. A mismatch needs review by the responsible provider using the agreed process, not an owner guess based on appearance. Keep quality decisions separate from the arithmetic of how many yards were ordered.'
], 'A fictional supply quote is 2.25 cu yd at $180 per cu yd, plus a $120 stated delivery fee. No other minimum or fixed charges are included in this example.', [('Volume charge: 2.25 × $180','$405'),('Stated delivery fee','$120'),('Defined supply subtotal','$525'),('Other fees or taxes','Not established')],
'The invented unit rate is not a local benchmark. Confirm minimum-load, waiting, tax and other charges before calling this the complete delivered price.',
['Project specification / author / version','Supplier / mixture designation / placement area','Quantity / order owner / authorized contacts','Timing / substitutions / change process','Delivery record / billing terms / reconciliation'],
['The order uses project-specific requirements.','Only authorized parties communicate technical changes.','Volume cost and quality acceptance are distinguished.'], 'Have the responsible purchaser confirm the supplier order against the approved specification and takeoff.')

chapter('Price access, delivery and placement logistics','Getting material to the work area is part of the budget.',[
'Ask the contractor and supplier to assess the actual delivery route, site access and working space. Record restrictions involving vehicles, overhead obstacles, driveways and occupied routes. A standard delivery assumption may not suit the property or the selected placement method.',
'Clarify the scope of any pump, handling equipment, placement crew and related charges. Identify who books each service and who confirms the site is ready. The owner needs clear responsibility and cost boundaries, not instructions for operating equipment or directing concrete placement.',
'Request written terms for minimum charges, waiting time, additional trips, cancellation and changes where applicable. Keep the terms with the order confirmation. A small material order can involve substantial fixed logistics costs even when the per-yard number looks modest.',
'Coordinate protection, cleanup, washout arrangements and restoration through the responsible providers and applicable requirements. Record dates and contacts for delays. A logistics allowance should state its trigger and approval process instead of functioning as an undefined addition after delivery.'
], 'A fictional project adds $450 equipment mobilization, $200 defined handling and $100 agreed cleanup. These services are expressly excluded from supply and placement prices elsewhere.', [('Equipment mobilization','$450'),('Handling scope','$200'),('Cleanup','$100'),('Logistics additions','$750')],
'Check that equipment and cleanup are not already inside another package. Actual access and supplier terms determine the relevant scope.',
['Site access / supplier and contractor assessment','Placement and handling services / booking owner','Fixed fees / waiting / cancellation / change terms','Protection / cleanup / restoration responsibilities','Ready-to-start checks / contacts / allowance triggers'],
['The delivery route is assessed before booking.','Fixed costs are visible beside unit prices.','Site operations remain with responsible qualified providers.'], 'Obtain the complete logistics price and readiness checklist before confirming delivery.')

chapter('Plan weather, curing and use restrictions','The surface looking finished does not determine readiness.',[
'Ask the contractor to explain the project-specific weather plan and who decides whether work proceeds. Record how a changed forecast affects delivery, placement, protection and cost. A date agreed early in planning is not proof that conditions will support the intended work.',
'NRMCA curing guidance explains that early moisture and temperature management support the intended properties of concrete [3]. Request the responsible provider\'s curing and protection plan for the actual mixture and conditions. This handbook gives no curing procedure, universal duration or return-to-use instruction.',
'Assign responsibility for maintaining the agreed protection and communicating restrictions to occupants. Record who confirms when specific uses may resume and what evidence is required. Do not infer readiness from appearance, a generic number of days or the removal of equipment from the site.',
'Keep delays and conditional costs visible. If the schedule changes, use the agreed approval process for additional services or temporary arrangements. Retain the care instructions and completion record so later concerns can be discussed against the actual scope and conditions.'
], 'A fictional delay adds one agreed $120 rescheduling charge and $80 additional protection, with no other change to scope. The charges are supported by the accepted terms.', [('Confirmed rescheduling charge','$120'),('Additional protection','$80'),('Approved change total','$200'),('Readiness for actual use','Provider confirmation required')],
'The example prices a documented change; it does not establish a weather threshold or curing period.',
['Weather decision owner / forecast review / contacts','Project-specific curing and protection plan','Occupant restrictions / responsible communication','Provider readiness confirmation / evidence','Delay terms / approved changes / retained care record'],
['Use timing comes from the responsible provider.','Protection responsibility is assigned.','Generic example timing is not treated as construction guidance.'], 'Obtain written care and use instructions for the actual project before the work begins.')

chapter('Compare finishes and ongoing obligations','A sample and an installed scope need the same reference.',[
'Record the selected finish, appearance expectations and any accepted sample or reference. Clarify the boundaries, edges and transitions included in the proposal. Product names or pictures alone do not establish the work, tolerances or maintenance obligations of the installed result.',
'Ask the qualified provider to confirm suitability for intended use, exposure and adjacent materials. This guide does not specify slip performance, finishing methods or sealers. Keep the relevant product and professional information with the scope so an attractive upgrade does not become an unassessed change.',
'Compare an upgrade using its incremental installed cost over the same baseline. Identify preparation, material, labor, protection and any later maintenance differences. A material-only premium may omit work that changes the actual project total.',
'Record care, warranty and renewal obligations and who explains them at handover. Keep genuine observations and a punch list separate from assumptions about technical defects. If the finished result is disputed, use the agreed review process and the responsible professional evidence.'
], 'A fictional decorative option adds $500 materials and $650 defined labor over a matched baseline, with a separately assumed $150 future maintenance event used only to illustrate ownership cost.', [('Initial material premium','$500'),('Initial labor premium','$650'),('Initial installed premium','$1,150'),('With one assumed later event','$1,300')],
'The future event is hypothetical, not a maintenance forecast. Confirm actual product and care requirements before comparing options.',
['Finish specification / sample / acceptance references','Suitability reviewer / use / exposure questions','Incremental material and labor / baseline scope','Care and renewal obligations / evidence','Handover / warranty / punch-list review process'],
['The sample and contract identify the same finish.','Suitability is professionally confirmed.','An invented maintenance event is not presented as fact.'], 'Ask for the complete installed upgrade price and care obligations before choosing a finish.')

chapter('Write a complete concrete proposal scope','Connect the takeoff to the work that delivers the result.',[
'Build the scope from the approved project use, drawings, site record and takeoff. Identify removal, preparation, supply, placement, finishing, protection, cleanup and restoration as applicable. Give tasks and areas IDs so quantities and changes can be traced to the same version.',
'Mark every component included, excluded, allowance or unresolved. Assign the design, ordering, inspection and site responsibilities rather than assuming they belong to whichever company supplies material. An unclear interface is a question to resolve before price ranking.',
'Keep conditional pricing tied to quantity, unit, evidence and approval. An allowance does not authorize undefined work, and an installed rate may already contain several cost components. Reconcile supplied material, placement services and fixed fees so no task appears twice.',
'Request the relevant handover records, care instructions and completion evidence in the accepted proposal. Technical acceptance and applicable requirements remain with the responsible providers and authorities. The owner worksheet supports the decision trail without certifying design or workmanship.'
], 'A fictional complete-scope comparison has $525 supply, $1,950 supporting work, $750 logistics and $1,600 defined placement and finish work. The provider has confirmed the categories do not overlap.', [('Supply','$525'),('Supporting work','$1,950'),('Logistics','$750'),('Placement and finish','$1,600'),('Defined comparison total','$4,825')],
'This total excludes unresolved items, reserve and tax unless expressly included. Confirm all scope boundaries before using it as the all-in funding plan.',
['Approved design / takeoff / site record versions','Included / excluded / allowance / unresolved tasks','Design / ordering / inspection / site owners','Unit rates / fixed fees / no-duplication check','Care / completion evidence / warranty / changes'],
['The takeoff and proposal use the same version.','Each required interface has an accountable party.','The comparison total is distinguished from the all-in plan.'], 'Send the same complete scope record to every bidder before selecting an offer.')

method(2,'Build the all-in concrete project budget')
method(5,'Normalize contractor proposals')
method(6,'Review the live cost forecast')
method(17,'Approve changes and reconcile the reserve')
method(18,'Close out and retain project records')

SOURCES=[('1','FTC: Home Repair Scams','https://consumer.ftc.gov/features/pass-it-on/home-repair-scams'),('2','NRMCA CIP 31: Ordering Ready Mixed Concrete','https://www.nrmca.org/wp-content/uploads/2021/01/31pr.pdf'),('3','NRMCA CIP 11: Curing In-Place Concrete','https://www.nrmca.org/wp-content/uploads/2021/01/11pr.pdf')]
