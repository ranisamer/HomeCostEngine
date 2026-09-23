/* HomeCostEngine Interactive Book Preview — 2026-09-23 */
(function(){
"use strict";
if(window.__HCE_EBOOK_PREVIEW_LOADED__) return;
window.__HCE_EBOOK_PREVIEW_LOADED__=true;
const BOOKS={
"smart-home-renovation-budget-blueprint":{
 category:"Smart Renovation",
 p1:{title:"Plan the Smart Layer Before Walls Close",intro:"Smart-home upgrades cost less and perform better when power, low-voltage wiring, Wi-Fi coverage and device locations are defined before finish work begins.",bullets:["Map switches, sensors, cameras and control points before rough-in.","Separate must-have automations from nice-to-have devices.","Confirm neutral wires, power supplies, network drops and equipment hubs.","Decide which systems must keep working if the internet goes down."]},
 p2:{title:"Build a Smart-Upgrade Budget",intro:"Keep the technology budget separate from the core renovation budget so optional devices do not hide structural or MEP costs.",table:[["Planning item","Example allowance"],["Network & Wi-Fi","$1,200"],["Lighting controls","$1,800"],["Security / sensors","$900"],["Smart thermostats","$500"],["Contingency","$660"]],note:"Example only: verify product compatibility, electrician requirements and local permit rules before purchase."},
 p3:{title:"Compare Systems by Lifetime Cost",intro:"A cheaper device can become expensive if it needs proprietary subscriptions, hubs or replacement parts.",table:[["Compare","System A","System B"],["Local control","Yes","Cloud only"],["Monthly fee","$0","$18"],["Works offline","Most functions","Limited"],["Open integrations","Broad","Restricted"],["5-year service cost","$0","$1,080"]],note:"Document recurring fees and platform dependencies before committing to a whole-home ecosystem."},
 locked:["Room-by-room automation map","Low-voltage rough-in checklist","Network coverage worksheet","Device compatibility matrix","Technology allowance tracker","Commissioning checklist"]
},
"roof-replacement-planning-handbook":{
 category:"Roofing",
 p1:{title:"Define the Roof Scope Before You Compare Quotes",intro:"A roofing price is only useful when every contractor is pricing the same tear-off, underlayment, flashing, ventilation and cleanup scope.",bullets:["Record roof size, pitch, stories and access constraints.","State whether existing layers are removed or covered.","Identify flashing, penetrations, valleys and ventilation work.","Create a written decking-repair allowance before work starts."]},
 p2:{title:"Turn the Quote Into a Real Budget",intro:"Headline price can exclude items that appear only after tear-off. Put them into one planning worksheet.",table:[["Cost item","Example"],["Base roofing proposal","$12,900"],["Permit","$350"],["Flashing allowance","$480"],["Decking allowance","$950"],["Disposal","$650"],["Adjusted planning cost","$15,330"]],note:"A lower base quote is not automatically a lower final cost. Compare inclusions line by line."},
 p3:{title:"Normalize Three Roofing Proposals",intro:"Before choosing a contractor, compare scope and warranty alongside price.",table:[["Check","A","B"],["Permit included","Yes","No"],["Flashing included","Yes","Allowance"],["Decking allowance","$1,000","$0"],["Workmanship warranty","10 yr","2 yr"],["Written change orders","Yes","Ask"]],note:"Ask what triggers a change order, who approves it and how labor/material markups are calculated."},
 locked:["Roof measurement worksheet","Shingle vs metal comparison","Ventilation checklist","Decking repair decision tree","Warranty comparison sheet","Final roof inspection checklist"]
},
"kitchen-remodel-cost-planner":{
 category:"Kitchen Remodel",
 p1:{title:"Separate Layout Changes From Finish Upgrades",intro:"Moving plumbing, gas, walls or appliance locations can change a kitchen budget much more than choosing a different cabinet color.",bullets:["Mark every wall, door, window and appliance location.","Identify plumbing, gas and electrical moves before cabinet design.","Confirm cabinet layout before countertop templating.","List owner-supplied appliances and contractor-installed items separately."]},
 p2:{title:"Build the Kitchen Cost Stack",intro:"Use category allowances so a beautiful finish selection does not silently consume money needed for labor or utilities.",table:[["Category","Example budget"],["Cabinetry","$14,000"],["Countertops","$4,800"],["Appliances","$6,500"],["Electrical / plumbing","$4,200"],["Floor / paint / trim","$3,600"],["Contingency","$4,000"]],note:"Keep allowances visible and update them as selections become fixed-price purchases."},
 p3:{title:"Control the Change-Order Risk",intro:"Most kitchen overruns come from late selections, hidden conditions and scope gaps.",table:[["Risk","Before contract"],["Cabinet lead time","Confirm delivery window"],["Panel capacity","Verify before appliance upgrade"],["Wall condition","Add repair allowance"],["Countertop cutouts","Confirm sink/cooktop specs"],["Temporary kitchen","Plan duration and cost"]],note:"Freeze critical dimensions and appliance specifications before cabinets are ordered."},
 locked:["Cabinet allowance worksheet","Appliance specification tracker","Countertop measurement checklist","Kitchen electrical planning sheet","Change-order log","Final punch-list template"]
},
"bathroom-remodel-budget-guide":{
 category:"Bathroom Remodel",
 p1:{title:"Define What Is Behind the Tile",intro:"A bathroom budget is not only tile and fixtures. Waterproofing, substrate, plumbing access and ventilation determine whether the scope is complete.",bullets:["Confirm demolition limits and what remains in place.","Specify waterproofing system and wet-area coverage.","Identify fixture relocations before pricing labor.","Check ventilation, electrical protection and access requirements."]},
 p2:{title:"Budget the Hidden Work",intro:"Create allowances for items that cannot be fully verified until demolition.",table:[["Cost category","Example"],["Demo & disposal","$1,200"],["Waterproofing / substrate","$2,100"],["Tile & setting materials","$3,400"],["Fixtures / vanity","$3,800"],["Plumbing / electrical","$2,600"],["Hidden-condition reserve","$1,800"]],note:"If a contractor excludes water damage or subfloor repair, record the labor rate and material markup before signing."},
 p3:{title:"Compare Bathroom Quotes on Equal Scope",intro:"Two bids can look similar while one includes far more prep and finish work.",table:[["Scope item","Quote A","Quote B"],["Waterproofing","Full system","Membrane only"],["Tile layout","Included","Extra"],["Fixture install","Included","Owner to arrange"],["Paint / trim","Included","Excluded"],["Cleanup","Daily","Final only"]],note:"Ask each contractor to state exclusions in writing, not only what is included."},
 locked:["Waterproofing checklist","Tile quantity worksheet","Fixture allowance tracker","Ventilation planning page","Bathroom quote comparison","Final leak-test checklist"]
},
"hvac-replacement-buyers-guide":{
 category:"HVAC",
 p1:{title:"Size the Decision, Not Just the Equipment",intro:"Replacing an HVAC system by copying the old model number can repeat an old sizing problem. The project starts with load, duct and comfort questions.",bullets:["Record conditioned area, insulation changes and problem rooms.","Ask how equipment sizing was determined.","Inspect duct condition, return-air capacity and filter location.","List electrical, drain, thermostat and permit work separately."]},
 p2:{title:"Compare Total Installed Cost",intro:"Equipment price is only one part of replacement cost.",table:[["Cost item","Example"],["Equipment package","$7,800"],["Labor / startup","$2,900"],["Duct modifications","$1,250"],["Electrical / disconnect","$600"],["Permit / disposal","$450"],["Planning total","$13,000"]],note:"Efficiency ratings should be compared together with climate, utility rates, duct losses and actual operating pattern."},
 p3:{title:"Normalize HVAC Proposals",intro:"Use a common checklist so model numbers do not distract from installation quality and scope.",table:[["Compare","Bid A","Bid B"],["Load calculation","Provided","Not stated"],["Duct testing","Included","Optional"],["Labor warranty","2 yr","1 yr"],["Startup report","Included","Ask"],["Permit","Included","Excluded"]],note:"Request exact model numbers and matched-system ratings before paying a deposit."},
 locked:["HVAC proposal worksheet","Load-calculation questions","Duct inspection checklist","Efficiency comparison table","Warranty tracker","Startup & commissioning checklist"]
},
"concrete-project-cost-handbook":{
 category:"Concrete",
 p1:{title:"Measure Volume Before You Price the Pour",intro:"Concrete projects are sensitive to dimensions, thickness, base preparation, reinforcement and access. Start with quantities, then build the installed scope.",bullets:["Record length, width and thickness for each section.","Separate concrete volume from base material and excavation.","Identify reinforcement, forms, joints and finish type.","Plan pump, wheelbarrow or truck access before ordering."]},
 p2:{title:"Add Waste and Site Work",intro:"The concrete order is rarely the whole project budget.",table:[["Planning item","Example"],["Concrete order","7.5 yd³"],["Waste / irregularity","0.6 yd³"],["Base & compaction","$900"],["Forms / reinforcement","$1,150"],["Placement / finish labor","$2,400"],["Cleanup / disposal","$450"]],note:"Round order quantities according to supplier policy and project conditions; short-load fees can matter on small pours."},
 p3:{title:"Compare Concrete Proposals",intro:"A fair comparison needs the same thickness, reinforcement, base and finish assumptions.",table:[["Scope","Proposal A","Proposal B"],["Slab thickness","4 in","4 in"],["Base depth","4 in","Not stated"],["Reinforcement","Mesh","Fiber only"],["Control joints","Saw cut","Tooled"],["Sealer","Included","Excluded"]],note:"Ask how soft subgrade, extra excavation and weather delays are handled before work starts."},
 locked:["Volume calculation worksheet","Base preparation checklist","Reinforcement options","Finish selection guide","Pour-day checklist","Concrete quote comparison"]
},
"flooring-project-planner":{
 category:"Flooring",
 p1:{title:"Measure Purchase Quantity, Not Just Room Area",intro:"Flooring orders need waste, pattern direction, closets, transitions and attic stock. Installation cost also depends on what is under the old floor.",bullets:["Measure each room separately and note transitions.","Choose a waste factor based on layout and product format.","Document removal and disposal of existing flooring.","Inspect subfloor flatness, moisture and repair needs."]},
 p2:{title:"Build the Installed Flooring Budget",intro:"Separate product cost from preparation and finishing work.",table:[["Category","Example"],["Flooring material","$4,800"],["Waste / attic stock","$520"],["Removal / disposal","$900"],["Subfloor prep","$1,100"],["Installation labor","$2,700"],["Trim / transitions","$650"]],note:"A low material price can be offset by high preparation cost. Confirm subfloor requirements from the flooring manufacturer."},
 p3:{title:"Compare Installation Scope",intro:"Different installers may quote the same square footage but include different prep, trim and furniture handling.",table:[["Check","Installer A","Installer B"],["Removal","Included","Extra"],["Leveling allowance","$500","None"],["Transitions","Included","Owner buys"],["Baseboard","Reinstall","Replace extra"],["Moisture test","Included","Not stated"]],note:"Get the flatness or moisture correction price structure in writing before demolition."},
 locked:["Room measurement worksheet","Waste-factor calculator","Subfloor inspection page","Material comparison matrix","Installer quote checklist","Care & warranty record"]
},
"painting-budget-and-quote-guide":{
 category:"Painting",
 p1:{title:"Price the Surface Preparation First",intro:"Painting quotes vary because preparation can vary. Wall area matters, but repairs, sanding, caulking, priming and protection often drive labor.",bullets:["List walls, ceilings, doors, trim and cabinets separately.","Document cracks, stains, peeling paint and patch areas.","Specify number of coats and primer requirements.","Confirm furniture moving, masking and daily cleanup."]},
 p2:{title:"Estimate Materials and Labor Separately",intro:"A simple worksheet makes upgrades and extra coats easier to understand.",table:[["Budget item","Example"],["Paint & primer","$950"],["Repair materials","$180"],["Prep labor","$1,350"],["Painting labor","$2,900"],["Trim / doors","$850"],["Contingency","$450"]],note:"Coverage varies by product, color change and surface porosity. Use manufacturer spread rates as a planning input, not a guarantee."},
 p3:{title:"Normalize Painting Quotes",intro:"The lowest price can reflect fewer coats or less preparation.",table:[["Scope","Painter A","Painter B"],["Wall coats","2","1 + touch-up"],["Ceilings","Included","Excluded"],["Minor repairs","Included","Allowance"],["Brand / line","Specified","Not stated"],["Protection","Full floor cover","Drop cloths"]],note:"Ask what condition the surface must be in before a warranty applies."},
 locked:["Paintable-area worksheet","Room-by-room color schedule","Prep checklist","Paint quantity planner","Quote comparison page","Final walkthrough checklist"]
},
"homeowner-maintenance-cost-planner":{
 category:"Home Maintenance",
 p1:{title:"Turn Maintenance Into a Calendar",intro:"A home is easier to manage when recurring tasks, inspections and replacements are assigned a month and an expected cost.",bullets:["List systems by monthly, seasonal and annual frequency.","Record installation age for roof, HVAC, water heater and appliances.","Separate routine maintenance from long-term replacement reserves.","Track completed work, contractor and next due date."]},
 p2:{title:"Build an Annual Maintenance Reserve",intro:"Use your own home, climate and equipment age to build a cash plan.",table:[["Reserve category","Example annual amount"],["HVAC service / filters","$420"],["Plumbing / drains","$300"],["Exterior / gutters","$500"],["Landscape / irrigation","$600"],["Small repairs","$700"],["Long-term replacement reserve","$1,800"]],note:"This is an example budget, not a universal percentage. Older homes and complex systems may need a larger reserve."},
 p3:{title:"Prioritize by Consequence, Not Convenience",intro:"Use a simple risk screen to decide what gets attention first.",table:[["Item","Condition","Priority"],["Active leak","Water damage","Immediate"],["Loose handrail","Safety issue","High"],["Aging water heater","No leak yet","Plan"],["Cosmetic paint","Worn","Low"],["Old appliance","Working","Reserve"]],note:"Safety, water intrusion and electrical issues generally deserve faster professional review than cosmetic work."},
 locked:["12-month maintenance calendar","Replacement-age tracker","Emergency contact sheet","Annual reserve worksheet","Home inventory page","Year-end maintenance review"]
},
"contractor-quote-comparison-playbook":{
 category:"Contractor Quotes",
 p1:{title:"Make Every Contractor Price the Same Job",intro:"You cannot compare quotes until the scope is normalized. Create one written project brief and give it to every bidder.",bullets:["Use the same drawings, measurements and finish assumptions.","Require inclusions, exclusions and allowances to be listed.","Ask who obtains permits and inspections.","Request payment schedule, warranty and change-order procedure."]},
 p2:{title:"Convert Base Price to Comparable Price",intro:"Normalize excluded costs before ranking proposals.",table:[["Adjustment","Quote B"],["Base proposal","$28,500"],["Permit excluded","+ $900"],["Fixture allowance shortfall","+ $1,200"],["Cleanup excluded","+ $650"],["Missing paint scope","+ $1,100"],["Comparable planning price","$32,350"]],note:"Comparable price is a planning tool. Final contract terms still require careful review."},
 p3:{title:"Score the Proposal Structure",intro:"Price matters, but a complete proposal should also make responsibilities and risk visible.",table:[["Check","A","B"],["Detailed scope","Strong","Partial"],["Allowances","Itemized","Combined"],["Schedule","Milestones","Start only"],["Change orders","Written approval","Not stated"],["Warranty","Defined","Verbal"]],note:"Do not infer missing terms. Ask for them in writing before signing."},
 locked:["Bid-normalization worksheet","Contractor interview questions","Allowance tracker","Payment schedule template","Change-order script","Final selection checklist"]
},
"complete-home-renovation-master-planner":{
 category:"Whole-Home Renovation",
 p1:{title:"Break a Whole-Home Remodel Into Phases",intro:"A large renovation becomes manageable when design, enabling work, structural work, MEP, finishes and closeout are planned as connected phases.",bullets:["Define rooms and systems included in the project.","Separate design decisions from construction decisions.","Identify temporary living, storage and access needs.","Create decision deadlines for long-lead selections."]},
 p2:{title:"Use a Phase-Based Master Budget",intro:"One grand total hides where contingency is needed.",table:[["Phase","Example allocation"],["Design / permits","$8,000"],["Demo / structural","$24,000"],["MEP systems","$28,000"],["Kitchens / baths","$42,000"],["Finishes","$26,000"],["Contingency","$16,000"]],note:"Update the master budget whenever scope moves between phases so contingency is not spent twice."},
 p3:{title:"Track Decisions That Control the Schedule",intro:"Late approvals can delay construction even when labor is available.",table:[["Decision","Needed by"],["Windows / exterior doors","Before rough opening work"],["Cabinet order","Before wall close"],["Plumbing fixtures","Before rough-in"],["Tile / flooring","Before finish schedule"],["Lighting fixtures","Before trim-out"]],note:"Link every major selection to a decision date, responsible person and delivery date."},
 locked:["Master scope register","Room-by-room budget","Selection deadline tracker","Long-lead item log","Renovation cash-flow plan","Final closeout binder"]
},
"first-time-homeowner-cost-maintenance-handbook":{
 category:"First-Time Homeowner",
 p1:{title:"Build Your First 90-Day Home Plan",intro:"New homeowners often discover small issues after move-in. A structured first 90 days helps separate urgent repairs from optional upgrades.",bullets:["Locate water, gas and electrical shutoffs.","Record filter sizes, appliance models and service dates.","Prioritize safety, leaks and active damage first.","Delay cosmetic projects until core systems are understood."]},
 p2:{title:"Create a Starter Home Reserve",intro:"A reserve should reflect the age and condition of your actual home, not a generic rule.",table:[["Category","Example reserve"],["Routine service","$600"],["Small repairs","$900"],["Appliance reserve","$700"],["Exterior upkeep","$600"],["Emergency buffer","$1,200"],["Planned upgrades","Separate savings"]],note:"Use inspection findings and equipment ages to adjust these numbers for your property."},
 p3:{title:"Know What to Document",intro:"Good records reduce guesswork when something fails.",table:[["Record","Why it matters"],["Roof age","Replacement planning"],["HVAC model / serial","Parts & warranty"],["Water heater date","Failure risk"],["Paint / flooring product","Future matching"],["Contractor invoices","Warranty / resale"]],note:"Photograph model plates and save documents in one cloud folder plus a local backup."},
 locked:["Move-in inspection checklist","Shutoff location sheet","Home systems inventory","Annual maintenance calendar","Replacement reserve planner","Contractor record log"]
},
"home-addition-cost-planning-guide":{
 category:"Home Addition",
 p1:{title:"Define the Addition Before Cost Per Square Foot",intro:"An addition changes structure, envelope and building systems. Size matters, but foundation type, roof tie-in and utility work can change cost dramatically.",bullets:["Confirm intended use, size and connection to existing rooms.","Identify foundation and roof connection concept.","Check HVAC, electrical and plumbing capacity early.","Plan site access, setbacks and permit requirements."]},
 p2:{title:"Build a System-Based Addition Budget",intro:"Break the project into major construction systems.",table:[["System","Example allowance"],["Design / permits","$9,000"],["Foundation","$18,000"],["Framing / exterior","$28,000"],["MEP systems","$19,000"],["Interior finishes","$24,000"],["Contingency","$12,000"]],note:"Site conditions, structural design and local code can materially change these allowances."},
 p3:{title:"Track Existing-Home Impacts",intro:"The addition budget should include work required to connect and restore the existing house.",table:[["Connection item","Check"],["Roof tie-in","Flashing / drainage"],["Floor level","Transition detail"],["HVAC","Capacity verified"],["Electrical","Panel capacity"],["Interior opening","Temporary support / finish repair"]],note:"Ask designers and contractors to identify restoration work on the existing house explicitly."},
 locked:["Addition scope worksheet","Site-access checklist","Existing-system capacity page","Permit question list","Phase budget tracker","Final inspection checklist"]
},
"basement-remodeling-budget-planner":{
 category:"Basement Remodel",
 p1:{title:"Solve Water and Egress Before Finishes",intro:"A basement can look dry on a walkthrough and still have moisture, drainage or code constraints that affect the entire remodel.",bullets:["Document water entry, humidity and foundation conditions.","Verify egress and bedroom requirements before layout.","Check ceiling height, ducts, beams and utility access.","Keep service clearances around panels, equipment and shutoffs."]},
 p2:{title:"Budget the Basement Infrastructure",intro:"Finish materials should come after moisture, insulation and systems are planned.",table:[["Category","Example"],["Moisture / drainage","$2,000"],["Framing / insulation","$5,500"],["Electrical / lighting","$3,200"],["Ceiling / drywall","$4,600"],["Flooring","$3,800"],["Contingency","$2,400"]],note:"If you add a bathroom, bedroom or wet bar, create separate plumbing and permit allowances."},
 p3:{title:"Compare Basement Quotes by Hidden Scope",intro:"Contractors may treat utility relocation and moisture correction very differently.",table:[["Scope","A","B"],["Insulation","Included","Owner choice"],["Sump work","Allowance","Excluded"],["Ceiling obstructions","Included","Change order"],["Egress work","Included","Separate quote"],["Paint / trim","Included","Excluded"]],note:"Get a written rule for unforeseen foundation or moisture conditions before demolition."},
 locked:["Moisture inspection checklist","Basement layout worksheet","Egress planning page","Utility relocation log","Room budget planner","Final basement walkthrough"]
},
"deck-outdoor-living-cost-planner":{
 category:"Deck & Outdoor",
 p1:{title:"Design the Structure Before Choosing Boards",intro:"Deck cost is shaped by height, footings, framing spans, stairs, railings and site access before the surface material is selected.",bullets:["Record deck dimensions, height and attachment method.","Count stairs, landings and railing length.","Identify footing access and excavation constraints.","Separate framing material from decking and railing systems."]},
 p2:{title:"Build the Installed Deck Budget",intro:"Use quantities for both structure and finish systems.",table:[["Category","Example"],["Footings / site work","$2,200"],["Framing","$5,800"],["Decking","$4,600"],["Railings / stairs","$3,400"],["Labor","$6,300"],["Contingency","$2,200"]],note:"Composite or specialty railing upgrades can shift the budget quickly; track them as explicit selections."},
 p3:{title:"Compare Deck Proposals",intro:"Check structural and finish assumptions together.",table:[["Scope","Builder A","Builder B"],["Permit","Included","Excluded"],["Footings","Specified","Not stated"],["Joist protection","Included","Optional"],["Railing model","Named","Allowance"],["Cleanup","Included","Included"]],note:"Ask how hidden conditions at the house ledger or existing foundation are priced."},
 locked:["Deck quantity worksheet","Footing / framing checklist","Railing cost tracker","Stair planning page","Builder quote comparison","Seasonal maintenance schedule"]
},
"window-door-replacement-buyers-guide":{
 category:"Windows & Doors",
 p1:{title:"Define the Installation Method",intro:"Window replacement cost depends on whether the project is insert replacement, full-frame replacement or an opening modification.",bullets:["Measure each opening and record window type.","Identify insert vs full-frame installation.","Document interior trim and exterior finish restoration.","Confirm flashing, air sealing and water-management scope."]},
 p2:{title:"Compare Product and Installation Cost",intro:"Keep unit price separate from installation and restoration.",table:[["Budget item","Example"],["Window units","$8,400"],["Removal / disposal","$900"],["Installation","$3,600"],["Flashing / air seal","$1,100"],["Trim / paint repair","$1,300"],["Contingency","$1,200"]],note:"Performance labels and installation quality both matter. Verify product ratings for your climate and opening type."},
 p3:{title:"Normalize Window Quotes",intro:"A quote with a lower unit price may exclude finish restoration or full water-management work.",table:[["Check","Quote A","Quote B"],["Install method","Full frame","Insert"],["Flashing","Included","Existing retained"],["Interior trim","New","Reuse"],["Exterior repair","Included","Allowance"],["Labor warranty","5 yr","2 yr"]],note:"Make sure every opening is listed with size, operation, glass package and installation method."},
 locked:["Opening measurement sheet","Insert vs full-frame guide","Performance-rating worksheet","Flashing checklist","Quote comparison matrix","Final operation inspection"]
},
"plumbing-project-cost-quote-handbook":{
 category:"Plumbing",
 p1:{title:"Separate the Plumbing Repair From the Access Repair",intro:"A plumbing job can require opening and restoring walls, ceilings, floors or cabinets. The quote should state who owns each part.",bullets:["Identify fixture, pipe or equipment being repaired.","Document how the plumber will gain access.","Clarify drywall, tile, paint and cabinet restoration.","Ask whether shutoff, drain-down and testing are included."]},
 p2:{title:"Build the Full Repair Budget",intro:"Use separate allowances for plumbing and restoration.",table:[["Cost item","Example"],["Plumbing labor","$1,450"],["Pipe / fittings","$420"],["Access opening","$250"],["Wall / ceiling repair","$650"],["Paint / finish repair","$300"],["Contingency","$400"]],note:"Emergency, after-hours and difficult-access work may use different rates. Ask before authorizing service."},
 p3:{title:"Compare Plumbing Proposals",intro:"For larger repairs, compare material, access and testing scope—not just hourly rate.",table:[["Scope","Plumber A","Plumber B"],["Material specified","Yes","Generic"],["Pressure / leak test","Included","Included"],["Permit","Included","If required extra"],["Restoration","Excluded","Allowance"],["Warranty","2 yr","1 yr"]],note:"For concealed piping, ask what happens if the opened area reveals a larger damaged section."},
 locked:["Plumbing scope worksheet","Access & restoration checklist","Fixture allowance page","Water-heater comparison","Quote normalization sheet","Leak-test closeout page"]
},
"electrical-upgrade-cost-planning-guide":{
 category:"Electrical",
 p1:{title:"Define Service, Panel and Circuit Scope",intro:"An electrical upgrade can involve utility coordination, service equipment, grounding, panel work, new circuits and repairs to finishes.",bullets:["Record existing service and panel ratings.","List new loads such as EV charging, heat pump or induction cooking.","Identify circuits being added, moved or consolidated.","Confirm utility, permit and inspection responsibilities."]},
 p2:{title:"Build the Electrical Upgrade Budget",intro:"Separate core equipment from branch circuits and restoration.",table:[["Category","Example"],["Panel / service equipment","$3,200"],["Labor","$2,600"],["New circuits","$1,800"],["Grounding / bonding","$650"],["Permit / utility coordination","$450"],["Wall repair reserve","$700"]],note:"Actual service-upgrade requirements depend on load calculations, utility rules and local electrical code."},
 p3:{title:"Compare Electrician Proposals",intro:"Model numbers and scope detail matter more than a one-line 'panel upgrade' description.",table:[["Check","A","B"],["Panel rating","200A","200A"],["Surge protection","Included","Optional"],["Circuit labeling","Included","Included"],["Utility coordination","Included","Owner"],["Wall patching","Excluded","Excluded"]],note:"Ask for written clarification on shutdown duration, inspection timing and temporary power needs."},
 locked:["Electrical load question sheet","Panel inventory worksheet","New-circuit planner","Permit / utility tracker","Electrician quote comparison","Final circuit test checklist"]
},
"landscaping-backyard-budget-planner":{
 category:"Landscaping",
 p1:{title:"Plan Drainage Before Planting",intro:"Backyard projects perform better when grading, drainage, irrigation and hardscape are resolved before decorative planting.",bullets:["Map slopes, low spots and downspout discharge.","Mark irrigation zones and water sources.","Separate hardscape, planting and lighting scopes.","Identify access for soil, stone and equipment."]},
 p2:{title:"Build a Backyard Budget by System",intro:"A single landscaping allowance makes tradeoffs hard to manage.",table:[["System","Example"],["Grading / drainage","$2,400"],["Irrigation","$1,800"],["Hardscape","$6,500"],["Planting / soil","$3,200"],["Lighting","$1,200"],["Contingency","$1,500"]],note:"Plant size, site access and drainage correction can materially change installed cost."},
 p3:{title:"Compare Landscape Proposals",intro:"Make sure each bidder is using the same quantities and plant sizes.",table:[["Scope","A","B"],["Topsoil","4 yd³","Not stated"],["Mulch","3 in depth","2 in depth"],["Plant sizes","Specified","Mixed"],["Irrigation changes","Included","Allowance"],["Cleanup","Included","Included"]],note:"Ask who is responsible for plant establishment, irrigation adjustments and replacement warranty."},
 locked:["Site map worksheet","Drainage checklist","Plant quantity schedule","Irrigation zone planner","Landscape quote comparison","Seasonal care calendar"]
},
"home-energy-upgrade-savings-planner":{
 category:"Home Energy",
 p1:{title:"Start With the Building, Then the Equipment",intro:"Energy upgrades work as a system. Air sealing, insulation, ducts, HVAC and windows influence one another.",bullets:["List comfort problems by room and season.","Record insulation, air leakage and duct observations.","Separate maintenance issues from efficiency upgrades.","Identify utility rebates before equipment is ordered."]},
 p2:{title:"Compare Cost, Savings and Useful Life",intro:"A simple payback snapshot helps organize options without pretending future utility prices are certain.",table:[["Upgrade","Cost example","Annual savings example"],["Air sealing","$1,400","$220"],["Attic insulation","$2,600","$310"],["Smart controls","$450","$70"],["Heat-pump upgrade","$8,500","$620"],["Window upgrade","$14,000","$380"]],note:"Savings are examples only. Use local utility rates, climate and an energy assessment for project-specific estimates."},
 p3:{title:"Sequence Upgrades to Avoid Rework",intro:"Some improvements should happen before equipment is sized or finishes are closed.",table:[["Step","Reason"],["Air sealing","Reduce uncontrolled leakage"],["Insulation","Improve envelope"],["Duct repairs","Reduce distribution loss"],["HVAC sizing","Reflect improved load"],["Controls","Tune operation"]],note:"Recalculate equipment needs after major envelope improvements rather than automatically replacing like-for-like."},
 locked:["Home energy inventory","Air-sealing checklist","Insulation worksheet","Upgrade payback table","Rebate tracker","Post-upgrade verification page"]
}
};
const BOOK_CALCULATORS={
"smart-home-renovation-budget-blueprint":[["Remodeling Cost Calculator","/calculators/remodeling-cost.html"],["Project Contingency Calculator","/calculators/project-contingency.html"],["Contractor Quote Comparison","/calculators/contractor-quote-comparison.html"]],
"roof-replacement-planning-handbook":[["Roof Replacement Calculator","/calculators/roof-replacement"],["Roofing Square Calculator","/calculators/roofing-square.html"],["Roof Pitch Calculator","/calculators/roof-pitch.html"]],
"kitchen-remodel-cost-planner":[["Remodeling Cost Calculator","/calculators/remodeling-cost.html"],["Project Contingency Calculator","/calculators/project-contingency.html"],["Contractor Quote Comparison","/calculators/contractor-quote-comparison.html"]],
"bathroom-remodel-budget-guide":[["Remodeling Cost Calculator","/calculators/remodeling-cost.html"],["Project Contingency Calculator","/calculators/project-contingency.html"],["Contractor Quote Comparison","/calculators/contractor-quote-comparison.html"]],
"hvac-replacement-buyers-guide":[["HVAC Replacement Calculator","/calculators/hvac.html"],["Project Contingency Calculator","/calculators/project-contingency.html"],["Contractor Quote Comparison","/calculators/contractor-quote-comparison.html"]],
"concrete-project-cost-handbook":[["Concrete Calculator","/calculators/concrete.html"],["Cubic Yard Calculator","/calculators/cubic-yard.html"],["Contractor Quote Comparison","/calculators/contractor-quote-comparison.html"]],
"flooring-project-planner":[["Flooring Calculator","/calculators/flooring.html"],["Square Footage Calculator","/calculators/square-footage.html"],["Contractor Quote Comparison","/calculators/contractor-quote-comparison.html"]],
"painting-budget-and-quote-guide":[["Paint Calculator","/calculators/paint.html"],["Square Footage Calculator","/calculators/square-footage.html"],["Contractor Quote Comparison","/calculators/contractor-quote-comparison.html"]],
"homeowner-maintenance-cost-planner":[["Home Maintenance Budget Calculator","/calculators/home-maintenance-budget.html"],["Project Contingency Calculator","/calculators/project-contingency.html"],["Remodeling Cost Calculator","/calculators/remodeling-cost.html"]],
"contractor-quote-comparison-playbook":[["Contractor Quote Comparison","/calculators/contractor-quote-comparison.html"],["Labor & Material Split Calculator","/calculators/labor-material-split.html"],["Project Contingency Calculator","/calculators/project-contingency.html"]],
"complete-home-renovation-master-planner":[["Remodeling Cost Calculator","/calculators/remodeling-cost.html"],["Project Contingency Calculator","/calculators/project-contingency.html"],["Contractor Quote Comparison","/calculators/contractor-quote-comparison.html"]],
"first-time-homeowner-cost-maintenance-handbook":[["Home Maintenance Budget Calculator","/calculators/home-maintenance-budget.html"],["Project Contingency Calculator","/calculators/project-contingency.html"],["Remodeling Cost Calculator","/calculators/remodeling-cost.html"]],
"home-addition-cost-planning-guide":[["Square Footage Calculator","/calculators/square-footage.html"],["Remodeling Cost Calculator","/calculators/remodeling-cost.html"],["Project Contingency Calculator","/calculators/project-contingency.html"]],
"basement-remodeling-budget-planner":[["Square Footage Calculator","/calculators/square-footage.html"],["Remodeling Cost Calculator","/calculators/remodeling-cost.html"],["Project Contingency Calculator","/calculators/project-contingency.html"]],
"deck-outdoor-living-cost-planner":[["Concrete Calculator","/calculators/concrete.html"],["Cubic Yard Calculator","/calculators/cubic-yard.html"],["Project Contingency Calculator","/calculators/project-contingency.html"]],
"window-door-replacement-buyers-guide":[["Square Footage Calculator","/calculators/square-footage.html"],["Remodeling Cost Calculator","/calculators/remodeling-cost.html"],["Contractor Quote Comparison","/calculators/contractor-quote-comparison.html"]],
"plumbing-project-cost-quote-handbook":[["Toilet Installation Cost Calculator","/calculators/toilet-installation-cost.html"],["Project Contingency Calculator","/calculators/project-contingency.html"],["Contractor Quote Comparison","/calculators/contractor-quote-comparison.html"]],
"electrical-upgrade-cost-planning-guide":[["Labor & Material Split Calculator","/calculators/labor-material-split.html"],["Project Contingency Calculator","/calculators/project-contingency.html"],["Contractor Quote Comparison","/calculators/contractor-quote-comparison.html"]],
"landscaping-backyard-budget-planner":[["Mulch Calculator","/calculators/mulch.html"],["Gravel Calculator","/calculators/gravel.html"],["Cubic Yard Calculator","/calculators/cubic-yard.html"]],
"home-energy-upgrade-savings-planner":[["HVAC Replacement Calculator","/calculators/hvac.html"],["Home Maintenance Budget Calculator","/calculators/home-maintenance-budget.html"],["Project Contingency Calculator","/calculators/project-contingency.html"]]
};
const slug=()=>location.pathname.split("/").filter(Boolean).pop()?.replace(/\.html$/,"")||"";
function moneyText(){
 return (document.querySelector(".ebook-top-price")?.textContent||document.querySelector(".book-price")?.textContent||"$9").trim();
}
function totalPages(){
 const t=document.body.innerText||"";
 const m=t.match(/\b(\d{2,3})[- ]page\b/i)||t.match(/\b(\d{2,3}) pages\b/i);
 return m?m[1]:"";
}
function esc(s){return String(s??"").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));}
function tableHtml(rows){
 if(!rows||!rows.length)return"";
 const cols=rows[0].length;
 return '<div class="hce-preview-table-wrap"><table class="hce-preview-table"><tbody>'+rows.map((r,i)=>'<tr>'+r.map(x=>(i===0?'<th':'<td')+'>'+esc(x)+(i===0?'</th>':'</td>')).join("")+'</tr>').join("")+'</tbody></table></div>';
}
function pageHtml(p,i,total,bookTitle){
 if(!p)return"";
 const tool=p.tool?'<a class="hce-page-tool-link" href="'+esc(p.tool[1])+'"><span>Free calculator</span><strong>'+esc(p.tool[0])+' →</strong></a>':"";
 return '<div class="hce-page-kicker"><span>'+esc(p.label||"Book preview")+'</span><span>Preview '+(i+1)+' of 3</span></div>'+
 '<h3>'+esc(p.title)+'</h3><p class="hce-page-intro">'+esc(p.intro)+'</p>'+
 (p.bullets?'<ul class="hce-page-list">'+p.bullets.map(x=>'<li>'+esc(x)+'</li>').join("")+'</ul>':"")+
 tableHtml(p.table)+
 (p.note?'<div class="hce-page-note"><strong>Planning note:</strong> '+esc(p.note)+'</div>':"")+
 tool+
 '<div class="hce-page-footer"><span>'+esc(bookTitle)+'</span><span>Full guide: '+esc(total||"digital")+" pages</span></div>";
}
function lockedHtml(cfg,total,price){
 const topics=(cfg.locked||[]).map(x=>'<span>'+esc(x)+'</span>').join("");
 return '<div class="hce-lock-content"><div class="hce-page-kicker"><span>Next section</span><span>Locked</span></div><h3>Continue with the complete guide</h3><p class="hce-page-intro">More worksheets, checklists and planning tools continue here.</p>'+tableHtml([["Tool","Status"],["Budget worksheet","Included"],["Quote checklist","Included"],["Planning templates","Included"],["Closeout tools","Included"]])+'</div>'+
 '<div class="hce-lock-panel"><div class="hce-lock-icon">🔒</div><h3>You’ve previewed 3 sample pages</h3><p>The complete guide contains '+esc(total||"many more")+' pages of project-specific planning content.</p><div class="hce-lock-topics">'+topics+'</div><button class="btn hce-buy-now" type="button">Get the Full Guide — '+esc(price)+'</button></div>';
}
function buy(){
 const b=document.querySelector(".ebook-top-buy,.book-buy-button,.ebook-bottom-buy-btn");
 if(b){b.click();return}
 window.scrollTo({top:0,behavior:"smooth"});
}
function enhanceProduct(){
 const key=slug(),cfg=BOOKS[key],section=document.getElementById("sample-pages");
 if(!cfg||!section)return;
 const title=(document.querySelector("main h1")?.textContent||document.title).trim();
 const cover=document.querySelector(".mobile-book-cover img,.desktop-book-cover img,.premium-book-art img")?.src||"";
 const pages=totalPages(),price=moneyText();
 const calcLinks=BOOK_CALCULATORS[key]||[];
 const data=[
  Object.assign({label:cfg.category,tool:calcLinks[0]},cfg.p1),
  Object.assign({label:"Planning worksheet",tool:calcLinks[1]},cfg.p2),
  Object.assign({label:"Decision tool",tool:calcLinks[2]},cfg.p3)
 ];
 const buyPanel=document.querySelector(".ebook-top-buy-panel");
 if(buyPanel){buyPanel.id="buy-book";if(location.hash==="#buy-book")setTimeout(()=>buyPanel.scrollIntoView({behavior:"smooth",block:"center"}),120);}
 section.className="section alt ebook-sample-section hce-book-preview";
 /* trailer-first placement */
 section.innerHTML='<div class="container">'+
 '<div class="section-head"><div><span class="eyebrow">3-page book trailer</span><h2>Read the book first. Decide after.</h2></div><p>The first thing on this page is a three-page interactive trailer. Explore the content and use the linked HomeCostEngine calculators before you see the purchase section.</p></div>'+
 '<div class="hce-preview-meta hce-preview-meta-top"><span>'+esc(pages?pages+" pages":"Digital guide")+'</span><span>3-page interactive trailer</span><span>Free calculator links inside</span></div>'+
 '<div class="hce-preview-shell"><div class="hce-reader"><div class="hce-reader-top"><strong>'+esc(title)+' • Free 3-page trailer</strong><div class="hce-reader-progress"><i></i></div></div><div class="hce-book-spread"><article class="hce-book-page hce-page-left"></article><article class="hce-book-page hce-page-right"></article></div><div class="hce-reader-nav"><button class="btn secondary prev" type="button" aria-label="Previous preview page">← Previous</button><span class="indicator"></span><button class="btn secondary next" type="button" aria-label="Next preview page">Next →</button></div><div class="hce-preview-tools"><strong>Free calculators used with this guide</strong><div>'+calcLinks.map(x=>'<a href="'+esc(x[1])+'">'+esc(x[0])+' →</a>').join("")+'</div></div><button class="btn hce-buy-now hce-mobile-buy" type="button">Get the Full Guide — '+esc(price)+'</button></div></div></div>';
 const detailContainer=document.querySelector(".book-detail .container");
 const breadcrumb=detailContainer?.querySelector(".breadcrumb");
 const grid=detailContainer?.querySelector(".book-detail-grid");
 if(detailContainer&&grid){
   detailContainer.insertBefore(section,grid);
 }
 const topBuy=document.querySelector(".ebook-top-buy-panel");
 if(topBuy){
   topBuy.classList.add("hce-buy-after-preview");
 }
 const shell=section.querySelector(".hce-preview-shell"),reader=section.querySelector(".hce-reader"),left=section.querySelector(".hce-page-left"),right=section.querySelector(".hce-page-right"),prev=section.querySelector(".prev"),next=section.querySelector(".next"),indicator=section.querySelector(".indicator"),progress=section.querySelector(".hce-reader-progress i");
 let current=0;
 const maxCurrent=()=>window.innerWidth<=760?3:2;
 function draw(dir){
  const max=maxCurrent(); if(current>max)current=max;
  const leftContent=current<3?pageHtml(data[current],current,pages,title):lockedHtml(cfg,pages,price);
  const ri=current+1;
  const rightContent=ri<3?pageHtml(data[ri],ri,pages,title):lockedHtml(cfg,pages,price);
  left.innerHTML=leftContent;right.innerHTML=rightContent;
  left.classList.remove("hce-locked-page");right.classList.remove("hce-locked-page");
  if(current>=3)left.classList.add("hce-locked-page");
  if(ri>=3)right.classList.add("hce-locked-page");
  [left,right].forEach(el=>{el.classList.remove("is-flipping");void el.offsetWidth;el.classList.add("is-flipping")});
  prev.disabled=current===0;
  const atEnd=current===max;
  next.textContent=atEnd?"Unlock Full Guide →":"Next →";
  indicator.textContent=window.innerWidth<=760?(current<3?"Preview page "+(current+1)+" of 3":"Full guide locked"):"Preview spread "+(current+1)+" of "+(max+1);
  progress.style.width=(atEnd?100:((Math.min(current,3)+1)/4*100))+"%";
  shell.classList.toggle("show-mobile-buy",window.innerWidth<=760&&current>=2);
 }
 draw("initial");
 prev.addEventListener("click",()=>{if(current>0){current--;draw("prev")}});
 next.addEventListener("click",()=>{const max=maxCurrent();if(current>=max){buy()}else{current++;draw("next")}});
 section.addEventListener("click",e=>{if(e.target.closest(".hce-buy-now"))buy()});
 let sx=0;
 reader.addEventListener("touchstart",e=>{sx=e.changedTouches[0].clientX},{passive:true});
 reader.addEventListener("touchend",e=>{const dx=e.changedTouches[0].clientX-sx;if(Math.abs(dx)<45)return;if(dx<0&&current<maxCurrent()){current++;draw("swipe")}else if(dx>0&&current>0){current--;draw("swipe")}},{passive:true});
 window.addEventListener("resize",()=>{if(!reader.hidden)draw("resize")});
}
function enhanceLibrary(){
 const p=location.pathname.replace(/\/+$/,"");
 if(p!=="/ebooks"&&!p.endsWith("/ebooks/index.html"))return;
 document.querySelectorAll(".book-card").forEach(card=>{
  const titleLink=card.querySelector("h2 a"),actions=card.querySelector(".book-card-actions"),price=card.querySelector(".book-meta strong")?.textContent.trim()||"$9";
  if(!titleLink||!actions||actions.classList.contains("hce-library-actions"))return;
  const href=titleLink.getAttribute("href");
  const primary=actions.querySelector(".btn");
  if(primary){primary.textContent="Preview Book";primary.href=href+"#sample-pages";}
  const buyLink=document.createElement("a");buyLink.className="btn hce-card-buy";buyLink.href=href+"#buy-book";buyLink.textContent="Buy Now — "+price;actions.appendChild(buyLink);actions.classList.add("hce-library-actions");
  const note=document.createElement("span");note.className="hce-library-preview-note";note.textContent="3-page interactive preview • Instant digital access";actions.insertAdjacentElement("afterend",note);
 });
}
function init(){enhanceLibrary();enhanceProduct();}
if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",init);else init();
})();