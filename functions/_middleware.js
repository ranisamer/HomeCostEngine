const GA_MEASUREMENT_ID = "G-T47EEK5EH0";

const EXTERNAL_RESOURCES = {
  roofing: [
    ["NRCA Consumer Roofing Information","https://www.nrca.net/roofing-guidelines/consumer-information"],
    ["NRCA Roofing Resources","https://www.nrca.net/roofing-guidelines/resources"],
    ["FEMA Building Science for Homeowners","https://www.fema.gov/emergency-managers/risk-management/building-science/homeowners"],
    ["ENERGY STAR Roof Products","https://www.energystar.gov/products/roof_products"],
    ["OSHA Roofing Safety","https://www.osha.gov/roofing"]
  ],
  concrete: [
    ["American Concrete Institute","https://www.concrete.org/"],
    ["National Ready Mixed Concrete Association","https://www.nrmca.org/"],
    ["Portland Cement Association","https://www.cement.org/"],
    ["FHWA Concrete Resources","https://www.fhwa.dot.gov/pavement/concrete/"],
    ["OSHA Concrete and Masonry Construction","https://www.osha.gov/concrete-masonry"]
  ],
  hvac: [
    ["ENERGY STAR Heating and Cooling","https://www.energystar.gov/saveathome/heating-cooling"],
    ["U.S. Department of Energy Home Upgrades","https://www.energy.gov/save/home-upgrades"],
    ["EPA Refrigerant Management","https://www.epa.gov/section608"],
    ["AHRI Certified Product Directory","https://www.ahridirectory.org/"],
    ["ASHRAE Technical Resources","https://www.ashrae.org/technical-resources/free-resources"]
  ],
  painting: [
    ["EPA Lead-Safe Renovation Steps","https://www.epa.gov/lead/steps-lead-safe-renovation-repair-and-painting"],
    ["EPA Renovation, Repair and Painting Program","https://www.epa.gov/lead/lead-renovation-repair-and-painting-program"],
    ["EPA Indoor Air Quality","https://www.epa.gov/indoor-air-quality-iaq"],
    ["CPSC Lead Safety Center","https://www.cpsc.gov/Safety-Education/Safety-Education-Centers/Lead"],
    ["OSHA Painting and Coating Safety","https://www.osha.gov/etools/shipyard/general-requirements/painting"]
  ],
  flooring: [
    ["National Wood Flooring Association","https://nwfa.org/"],
    ["EPA Indoor Air Quality","https://www.epa.gov/indoor-air-quality-iaq"],
    ["NWFA Homeowner Resources","https://www.woodfloors.org/"],
    ["Resilient Floor Covering Institute","https://rfci.com/"],
    ["Carpet and Rug Institute","https://carpet-rug.org/"]
  ],
  gravel: [
    ["EPA WaterSense Landscaping Tips","https://www.epa.gov/watersense/landscaping-tips"],
    ["EPA WaterSense Outdoors","https://www.epa.gov/watersense/outdoors"],
    ["FHWA Gravel Roads Guide","https://www.fhwa.dot.gov/construction/pubs/ots15002.pdf"],
    ["USGS Aggregates Information","https://www.usgs.gov/centers/national-minerals-information-center/aggregates-data"],
    ["USDA Web Soil Survey","https://websoilsurvey.nrcs.usda.gov/"]
  ],
  landscaping: [
    ["EPA WaterSense Landscaping Tips","https://www.epa.gov/watersense/landscaping-tips"],
    ["EPA WaterSense Outdoors","https://www.epa.gov/watersense/outdoors"],
    ["USDA Natural Resources Conservation Service","https://www.nrcs.usda.gov/"],
    ["USDA Web Soil Survey","https://websoilsurvey.nrcs.usda.gov/"],
    ["U.S. Forest Service Native Gardening","https://www.fs.usda.gov/wildflowers/Native_Plant_Materials/Native_Gardening/index.shtml"]
  ],
  windows: [
    ["ENERGY STAR Windows, Doors and Skylights","https://www.energystar.gov/products/res_windows_doors_skylights"],
    ["U.S. Department of Energy Home Upgrades","https://www.energy.gov/save/home-upgrades"],
    ["National Fenestration Rating Council","https://nfrc.org/"],
    ["DOE Energy-Efficient Windows","https://www.energy.gov/energysaver/energy-efficient-windows"],
    ["Efficient Windows Collaborative","https://efficientwindows.org/"]
  ],
  plumbing: [
    ["U.S. Department of Energy Water Heating","https://www.energy.gov/topics/water-heating"],
    ["EPA WaterSense","https://www.epa.gov/watersense"],
    ["EPA Fix a Leak Week","https://www.epa.gov/watersense/fix-leak-week"],
    ["CDC Drinking Water Resources","https://www.cdc.gov/drinking-water/"],
    ["International Plumbing Code","https://www.iccsafe.org/products-and-services/i-codes/2024-i-codes/ipc/"]
  ],
  general: [
    ["NIST Office of Weights and Measures","https://www.nist.gov/pml/owm"],
    ["U.S. Department of Energy Home Upgrades","https://www.energy.gov/save/home-upgrades"],
    ["FTC Home Improvement Guidance","https://consumer.ftc.gov/articles/home-improvement-scams"],
    ["HUD Healthy Homes","https://www.hud.gov/hud-partners/healthy-homes"],
    ["EPA Indoor Air Quality","https://www.epa.gov/indoor-air-quality-iaq"]
  ]
};

function externalLinksSection(pathname) {
  const topic = topicForPath(pathname);
  const links = EXTERNAL_RESOURCES[topic] || EXTERNAL_RESOURCES.general;
  const items = links.map(([label, href]) =>
    `<li style="margin:8px 0"><a href="${href}" target="_blank" rel="noopener noreferrer" style="color:#176b5b;font-weight:700;text-decoration:underline">${label} ↗</a></li>`
  ).join("");
  return `<aside class="seo-link-panel hce-server-resources" aria-label="Trusted external resources" style="margin:36px 0 22px;padding:22px;border:1px solid #d7e2dd;border-radius:18px;background:#f5faf8"><h2 style="margin:0 0 9px">Trusted external resources</h2><p style="margin:0 0 14px">Verify project details with these independent government and industry resources.</p><ul style="margin:0;padding-left:22px">${items}</ul></aside>`;
}

function humanizeSlug(pathname) {
  const slug = pathname.split('/').pop().replace(/\.html$/i, '');
  return slug
    .split('-')
    .map((w) => (/^(hvac|ac|seo)$/i.test(w) ? w.toUpperCase() : w.charAt(0).toUpperCase() + w.slice(1)))
    .join(' ')
    .replace(/ Sq Ft /g, ' sq ft ')
    .replace(/ Vs /g, ' vs ');
}

function topicForPath(pathname) {
  const s = pathname.toLowerCase();
  if (/water-heater|toilet|water-leak|plumb/.test(s)) return 'plumbing';
  if (/window/.test(s)) return 'windows';
  if (/hvac|heat-pump|seer|air-condition|ac-repair|furnace/.test(s)) return 'hvac';
  if (/paint/.test(s)) return 'painting';
  if (/floor|vinyl|laminate/.test(s)) return 'flooring';
  if (/gravel/.test(s)) return 'gravel';
  if (/mulch|landscap/.test(s)) return 'landscaping';
  if (/concrete|cubic-yard|slab|patio|ready-mix/.test(s)) return 'concrete';
  if (/roof|shingle|attic-ventilation/.test(s)) return 'roofing';
  return 'general';
}

function intentForPath(pathname) {
  const s = pathname.toLowerCase();
  if (/vs|compare/.test(s)) return 'comparison';
  if (/repair-vs-replacement|repair|replace/.test(s) && !/replacement-cost/.test(s)) return 'repair';
  if (/how-much|how-many|square|yard|need|quantity|thickness|pitch/.test(s)) return 'quantity';
  if (/cost|price|budget/.test(s)) return 'cost';
  if (/checklist|choose|what-affects|explained|factors|detect/.test(s)) return 'decision';
  return 'decision';
}

const TOPIC_BLOCKS = {
  roofing: `
    <h2>Roofing details that deserve a second look</h2>
    <p>Roofing prices and material quantities are unusually sensitive to scope. A homeowner may know the house is 2,000 square feet, but the roof surface can be larger because of pitch, overhangs, attached garages, porches, dormers, valleys and other geometry. That is why a useful roof budget starts with measured roof area rather than living area alone. When comparing bids, verify whether each contractor measured the same roof surface and whether the proposal includes tear-off, disposal, underlayment, flashing, ventilation, edge metal, starter materials, ridge components and any expected deck repair.</p>
    <p>Material labels can also hide meaningful differences. “Asphalt shingles” may refer to different product lines, wind ratings, impact ratings, algae protection, warranties and installation systems. Metal roofing can mean exposed-fastener panels, concealed-fastener systems or standing seam, each with different labor and accessory requirements. A low headline price is not automatically a better value if important accessories or labor steps are missing. Ask for product names, manufacturer specifications and a written scope that makes exclusions obvious.</p>
    <p>Local climate and code matter too. Wind, snow, hail, wildfire exposure, coastal conditions and ventilation requirements can change the recommended assembly. Permit rules and inspection requirements vary by jurisdiction. Use the <a href="/calculators/roof-replacement.html">Roof Replacement Cost Calculator</a>, <a href="/calculators/roofing-square.html">Roofing Square Calculator</a> and <a href="/calculators/roof-pitch.html">Roof Pitch Calculator</a> as planning tools, then verify final details with a qualified local roofer. For independent industry information, review consumer resources from the <a href="https://www.nrca.net/roofing-guidelines/consumer-information" target="_blank" rel="noopener noreferrer">National Roofing Contractors Association</a>.</p>
  `,
  concrete: `
    <h2>Concrete planning: quantity is only the first step</h2>
    <p>Concrete math looks simple because volume is length × width × thickness, but field conditions make the practical order more complicated. Forms are rarely perfect, the subgrade may vary slightly, some material can be lost during placement, and ready-mix suppliers often have minimums or ordering increments. A small waste allowance is therefore common, but it should be reasonable for the shape and conditions of the project rather than added blindly.</p>
    <p>Thickness is a design decision, not just a cost input. A patio, walkway, driveway and structural slab do not carry the same loads or require the same base preparation. Soil, drainage, freeze-thaw exposure, reinforcement, joints and local code can all affect the final design. The cost of the concrete itself is also only part of the installed project. Excavation, base material, forming, reinforcement, pumping, short-load charges, finishing, curing, access and demolition can materially change the total.</p>
    <p>Before ordering, convert your measurements with the <a href="/calculators/concrete.html">Concrete Calculator</a> or <a href="/calculators/cubic-yard.html">Cubic Yard Calculator</a>. For larger pours, confirm the quantity, mix and delivery plan with the supplier or contractor. Technical information from the <a href="https://www.concrete.org/" target="_blank" rel="noopener noreferrer">American Concrete Institute</a> and the <a href="https://www.nrmca.org/" target="_blank" rel="noopener noreferrer">National Ready Mixed Concrete Association</a> can help homeowners understand why mix design, placement and curing matter.</p>
  `,
  hvac: `
    <h2>HVAC costs depend on the whole system, not just the equipment</h2>
    <p>Heating and cooling replacement quotes can differ widely even when two contractors appear to be proposing the same tonnage. Equipment efficiency, matched indoor and outdoor components, controls, line-set condition, electrical work, condensate management, duct changes, filtration, permits and commissioning can all change the installed price. A useful comparison therefore looks at the entire scope rather than the model number or equipment price alone.</p>
    <p>System size is especially important. Square footage is only a rough starting point; proper sizing also considers climate, insulation, windows, orientation, air leakage, occupancy and duct performance. Oversizing can create comfort and humidity problems, while undersizing can leave the system struggling during peak conditions. For a real replacement decision, ask the contractor how sizing was determined and whether a load calculation is appropriate for the project.</p>
    <p>Use the <a href="/calculators/hvac.html">HVAC Replacement Cost Calculator</a> to create an early planning range, then compare proposals line by line. Homeowners can also review efficiency and upgrade guidance from <a href="https://www.energystar.gov/saveathome/heating-cooling" target="_blank" rel="noopener noreferrer">ENERGY STAR</a> and the <a href="https://www.energy.gov/save/home-upgrades" target="_blank" rel="noopener noreferrer">U.S. Department of Energy</a>. Those resources are useful when evaluating heat pumps, efficiency levels and broader home-envelope improvements.</p>
  `,
  painting: `
    <h2>Painting estimates should separate coverage from preparation</h2>
    <p>A paint calculator can estimate gallons from surface area, coats and expected coverage, but the installed cost of painting is driven heavily by preparation. Wall repairs, sanding, patching, caulking, stain blocking, priming, trim work, ceiling work, furniture protection and difficult access can take more labor than rolling the finish coat itself. Two proposals can therefore use similar paint and still have very different labor scopes.</p>
    <p>Coverage numbers on a paint can are planning values, not guarantees. Texture, porosity, color changes, application method and product type affect real-world coverage. Deep color changes may require additional coats, while new drywall or repaired surfaces may need primer. When buying material, keep the room dimensions, number of openings, number of coats and product coverage assumptions consistent so the estimate can be checked later.</p>
    <p>Start with the <a href="/calculators/paint.html">Paint Calculator</a>, then read related planning guides on <a href="/blog/interior-painting-cost-per-square-foot.html">painting cost per square foot</a> and <a href="/blog/how-much-does-it-cost-to-paint-a-room.html">room painting cost</a>. For homes where older coatings may be disturbed, review the <a href="https://www.epa.gov/lead/lead-renovation-repair-and-painting-program" target="_blank" rel="noopener noreferrer">EPA Renovation, Repair and Painting Program</a> and follow applicable safety requirements.</p>
  `,
  flooring: `
    <h2>Flooring cost is more than the price printed on the box</h2>
    <p>Flooring projects are often compared using material price per square foot, but the installed budget usually includes more. Waste, delivery, removal, disposal, subfloor repair, leveling, moisture work, underlayment, transitions, trim, stairs and labor can all change the total. The shape of the room and installation pattern also affect waste. Simple rectangular layouts are usually more efficient than diagonal layouts, many small rooms or spaces with numerous cuts.</p>
    <p>Measure the actual floor area first and then apply a waste allowance that fits the product and layout. Packaging matters because flooring is sold by the carton, so the purchase quantity may need to be rounded up. Keep some matching material when appropriate for future repairs, especially when a color or product line could be discontinued. For a contractor quote, ask whether baseboards, transitions, moving furniture and disposal are included or separate.</p>
    <p>Use the <a href="/calculators/flooring.html">Flooring Cost Calculator</a> to separate material, labor and waste. You can also compare <a href="/blog/vinyl-plank-vs-laminate-flooring-cost.html">vinyl plank vs laminate</a> and estimate <a href="/blog/how-much-flooring-do-i-need.html">how much flooring you need</a>. For wood-flooring technical resources, the <a href="https://nwfa.org/" target="_blank" rel="noopener noreferrer">National Wood Flooring Association</a> publishes industry information for installation and care.</p>
  `,
  gravel: `
    <h2>Gravel projects depend on depth, base and delivery</h2>
    <p>Gravel planning begins with area and depth, but the material actually ordered may be sold by weight rather than volume. Different stone sizes and materials have different densities, and moisture can affect delivered weight. A calculator can convert the dimensions into cubic yards and estimate tons, but the supplier should confirm the conversion for the exact product being purchased.</p>
    <p>Driveways and paths also depend on what is under the visible surface. Excavation, grading, geotextile, base stone, compaction, drainage and edge restraint can be more important to long-term performance than simply adding more top-layer gravel. If the existing surface has rutting or drainage problems, placing a thin new layer over it may improve appearance temporarily without correcting the underlying cause.</p>
    <p>Use the <a href="/calculators/gravel.html">Gravel Calculator</a> and <a href="/calculators/cubic-yard.html">Cubic Yard Calculator</a> to estimate quantity. Then ask the supplier about truck capacity, minimum delivery, material density and access requirements. For outdoor water and landscape planning, the <a href="https://www.epa.gov/watersense/outdoors" target="_blank" rel="noopener noreferrer">EPA WaterSense outdoor resources</a> provide useful context for drainage and water-efficient landscape decisions.</p>
  `,
  landscaping: `
    <h2>Landscape material estimates should reflect the real site</h2>
    <p>Mulch and other bulk landscape materials are commonly estimated from bed area and installation depth. The calculation is straightforward, but irregular beds, slopes, existing material, settling and delivery increments can change the practical order. Measuring each bed separately and adding the areas is usually more accurate than guessing one large rectangle around the entire landscape.</p>
    <p>Depth should match the purpose and material. Adding too little may not provide the appearance or moisture-management benefit you expect, while piling material too deeply can create problems around plants and structures. Keep mulch away from direct contact with trunks and building components where moisture accumulation could be undesirable, and follow local horticultural guidance for the plants on the property.</p>
    <p>Use the <a href="/calculators/mulch.html">Mulch Calculator</a> or <a href="/calculators/cubic-yard.html">Cubic Yard Calculator</a> to build an order estimate, then check the supplier's bag or bulk-yard sizes. The <a href="https://www.epa.gov/watersense/landscaping-tips" target="_blank" rel="noopener noreferrer">EPA WaterSense landscaping tips</a> are a useful independent resource when the project also involves irrigation, plant selection or water efficiency.</p>
  `,
  windows: `
    <h2>Window replacement quotes are easiest to compare by specification</h2>
    <p>Window pricing can vary because of frame material, glass package, size, operating style, grids, exterior finish, installation method and trim work. A “double-pane window” is not a complete specification. U-factor, solar heat gain coefficient, low-e coatings, gas fills and regional performance requirements may all matter, especially when energy performance is one of the reasons for replacement.</p>
    <p>Installation scope is just as important as the unit itself. Insert replacement, full-frame replacement, exterior cladding, sill repair and water-management details can produce very different labor and material requirements. Ask each contractor to state whether interior trim, exterior trim, disposal, flashing, sealants, permits and repair of damaged surrounding materials are included. Comparing identical scope reduces the chance that the lowest bid is simply missing work.</p>
    <p>Read our <a href="/blog/window-replacement-cost-per-window.html">window replacement cost per window</a> guide and <a href="/blog/double-pane-vs-triple-pane-windows.html">double-pane vs triple-pane comparison</a> alongside local quotes. For independent performance information, see <a href="https://www.energystar.gov/products/res_windows_doors_skylights" target="_blank" rel="noopener noreferrer">ENERGY STAR windows, doors and skylights</a>.</p>
  `,
  plumbing: `
    <h2>Plumbing repair decisions should include risk, access and remaining life</h2>
    <p>Plumbing costs are affected by more than the price of a fixture or appliance. Access behind walls or floors, shutoff condition, drain or vent work, permits, disposal, code upgrades and water damage can change the final scope. A simple visible repair may be inexpensive, while a hidden leak or aging connection can require diagnostic work before the contractor can price the job confidently.</p>
    <p>For repair-versus-replacement decisions, consider age, reliability, recurring service calls, efficiency, availability of parts and the consequences of another failure. Water heaters, toilets and supply components can have very different risk profiles. A lower-cost repair can make sense when the rest of the system is sound, while repeated failures may justify pricing replacement so you can compare the total expected cost instead of making one isolated decision.</p>
    <p>Continue with our guides on <a href="/blog/how-to-detect-hidden-water-leak.html">detecting hidden water leaks</a> and <a href="/blog/water-heater-repair-vs-replacement.html">water-heater repair vs replacement</a>. For independent information on water efficiency, see <a href="https://www.epa.gov/watersense" target="_blank" rel="noopener noreferrer">EPA WaterSense</a>; for water-heating efficiency information, review the <a href="https://www.energy.gov/topics/water-heating" target="_blank" rel="noopener noreferrer">U.S. Department of Energy water-heating resources</a>.</p>
  `,
  general: `
    <h2>Turn measurements into a project plan</h2>
    <p>A calculator is most useful when the inputs are measured carefully and the result is treated as a planning estimate rather than a guaranteed price. Record where each measurement came from, keep units consistent and note any assumptions about waste, labor, delivery or market conditions. That makes it much easier to update the estimate later or compare it with a contractor proposal.</p>
    <p>Real projects also include items that pure quantity math cannot see: access, demolition, permits, disposal, site protection, repair of hidden damage and local labor conditions. Use the number from a calculator as a baseline, then add the scope items that apply to the property. When a project affects structure, safety, electrical work, plumbing, combustion equipment or code compliance, use qualified local professionals and applicable permits.</p>
    <p>HomeCostEngine provides a <a href="/calculators/">library of free calculators</a> for square footage, cubic yards, roofing, concrete, HVAC, paint, flooring and landscape materials. For measurement standards and unit information, the <a href="https://www.nist.gov/pml/owm" target="_blank" rel="noopener noreferrer">NIST Office of Weights and Measures</a> is an independent reference.</p>
  `
};

const INTENT_BLOCKS = {
  cost: `
    <h2>How to turn a cost estimate into a useful budget</h2>
    <p>Start by separating quantity from price. Quantity answers “how much work or material is involved,” while price answers “what does that amount cost in this market with this scope.” Keeping those two ideas separate makes it easier to understand why contractor quotes differ. If one bid is much higher, look first for a scope difference: better materials, more demolition, difficult access, additional preparation, permit work, longer warranty, cleanup or repairs that another proposal omitted.</p>
    <p>Use a range instead of one precise number. Early project estimates contain uncertainty, so a low-to-high planning range is more useful than pretending the project will cost exactly one amount. As you collect local quotes and confirm measurements, narrow the range. Keep a contingency for unknown conditions when the project can expose hidden damage or when site conditions are not fully visible before work starts.</p>
    <p>Before signing, compare the payment schedule, exclusions, change-order process, product specifications, warranty responsibilities and cleanup requirements. A quote that is clear about what is not included can be easier to manage than a cheaper quote with vague language. The goal of the estimate is not to pick the lowest number automatically; it is to help you ask better questions and recognize when two proposals are not actually pricing the same job.</p>
  `,
  quantity: `
    <h2>Measure twice before you order material</h2>
    <p>Quantity errors usually come from the inputs, not the formula. Recheck length, width, depth, pitch or surface area and make sure every measurement uses the same unit. For irregular projects, break the area into simple rectangles, triangles or other manageable shapes, calculate them separately, then add the results. This is usually more reliable than forcing a complicated space into one rough measurement.</p>
    <p>After calculating the theoretical quantity, think about waste and purchase increments. Cuts, breakage, compaction, spillage, pattern matching and packaging can create a gap between calculated quantity and what you actually need to buy. The correct allowance depends on the material and project. Avoid adding a large arbitrary percentage “just in case”; instead, use supplier packaging, installation guidance and the shape of the project to choose a sensible buffer.</p>
    <p>Finally, confirm the order with the supplier or installer when mistakes would be expensive. Ask how the product is sold, whether quantities are rounded, whether there is a minimum order and how returns are handled. Save your measurements and calculation so you can explain the order later and compare it with the contractor's takeoff.</p>
  `,
  comparison: `
    <h2>Compare options on equivalent scope</h2>
    <p>A fair comparison uses the same project boundaries for both options. Match demolition, preparation, accessories, labor, delivery, permits, cleanup and warranty before deciding that one material or system is cheaper. If one option lasts longer or changes maintenance needs, include that difference in the decision rather than looking only at the first invoice.</p>
    <p>List the factors that matter for the property: upfront budget, expected ownership period, appearance, maintenance, repairability, energy use, comfort, resilience and resale considerations. Not every factor deserves the same weight. A homeowner planning to stay for twenty years may reasonably prioritize lifecycle performance differently from someone preparing a property for sale.</p>
    <p>Ask contractors to quote the alternatives in writing with product names and clearly defined scope. That reduces the risk of comparing a premium version of one option with an entry-level version of another. When there is no single “best” answer, the useful outcome is a documented trade-off that fits the home, budget and expected use.</p>
  `,
  repair: `
    <h2>Repair or replace: use a structured decision</h2>
    <p>Repair-versus-replacement decisions are easier when you look beyond the immediate invoice. Start with the cause of the problem, the age and condition of the surrounding system, the history of previous repairs, remaining expected life and the consequences of another failure. A small repair can be sensible when the rest of the system is healthy. Repeated service calls on an aging system may justify getting a replacement price for comparison.</p>
    <p>Ask whether the repair addresses the root cause or only the visible symptom. Also ask what warranty applies to the repair and what happens if another related component fails soon afterward. For replacement, request a full scope so the comparison includes demolition, disposal, code upgrades, accessories and commissioning rather than only the new product.</p>
    <p>There is no universal percentage rule that automatically tells every homeowner when to replace. Use the cost, risk and remaining life together. If a failure could cause water damage, unsafe operation or major disruption, risk may matter more than simple payback. When the decision involves safety or code compliance, have a qualified professional inspect the condition before relying on a calculator or article.</p>
  `,
  decision: `
    <h2>Questions to ask before hiring or buying</h2>
    <p>Turn the article into a short checklist before contacting contractors or suppliers. Write down the project size, the problem you are trying to solve, preferred materials, any known damage, access constraints and the result from the relevant calculator. Then ask each bidder to explain the scope in the same categories. Consistent questions make proposals easier to compare.</p>
    <p>For contractor work, verify licensing or registration where applicable, insurance, references, product specifications, permits, schedule, cleanup, warranty and how change orders are approved. Avoid relying on a verbal promise for a major scope item. If something affects price or responsibility, it should be written in the proposal or contract so both sides understand it the same way.</p>
    <p>Use outside sources for technical claims and local authorities for permit or code requirements. Manufacturer instructions are also important because warranties and installation requirements can be product-specific. A planning article should help you organize the decision, but it cannot see the property or replace an on-site inspection when one is needed.</p>
  `
};

const COMMON_BLOCK = `
  <h2>A practical way to use this HomeCostEngine guide</h2>
  <p>Use this article in three passes. First, understand the cost or quantity drivers so you know what information matters. Second, run the related calculator with your own measurements instead of relying on a national average. Third, compare the result with local supplier prices or written contractor proposals. That sequence turns a general online guide into a project-specific planning tool.</p>
  <p>Keep a simple project file with measurements, screenshots, product names, quotes and notes from contractor conversations. When a number changes, update the assumption instead of starting from scratch. This is especially useful when bids arrive weeks apart or when one proposal contains a different material, warranty or scope. A documented baseline helps you notice meaningful differences rather than being distracted by the final total alone.</p>
  <p>Remember that HomeCostEngine estimates are for budgeting and education. They do not include every local code requirement, permit rule, hidden condition or labor-market difference, and they are not a substitute for a site inspection. For structural, electrical, plumbing, HVAC, roofing or other work where safety and code compliance matter, verify the final plan with qualified local professionals. If a contractor discovers hidden damage after work begins, ask for photos, an explanation and a written change order before approving additional work whenever practical.</p>
  <h2>Common mistakes that make online estimates less accurate</h2>
  <ul>
    <li><strong>Using living area instead of project area.</strong> Roof surface, paintable wall area, flooring area and landscape beds can all differ from the home's advertised square footage.</li>
    <li><strong>Comparing incomplete scopes.</strong> Demolition, disposal, preparation, permits, delivery and accessories may be included in one quote and excluded from another.</li>
    <li><strong>Ignoring purchase increments.</strong> Bags, cartons, bundles, truckloads and supplier minimums can force the real order above the theoretical calculation.</li>
    <li><strong>Assuming one national price fits every location.</strong> Labor rates, access, codes, climate and material availability vary across U.S. markets.</li>
    <li><strong>Choosing only on price.</strong> Product specification, workmanship, warranty, schedule and clarity of scope can be as important as the lowest total.</li>
  </ul>
  <h2>Before you approve the project</h2>
  <p>Recheck the final measurements and confirm who is responsible for permits, site protection, disposal and cleanup. Make sure important materials are identified by product or performance specification rather than a vague category. Review deposit and progress-payment terms, start and completion expectations, warranty language and the process for unexpected conditions. Keep copies of signed documents and receipts.</p>
  <p>If the project is still in the research stage, use the related HomeCostEngine calculators and articles linked throughout this page to test more than one scenario. Changing the project size, material or labor assumption can show which inputs have the biggest effect on the budget. That is usually more useful than chasing one “perfect” average price from the internet.</p>
`;

function depthSection(pathname) {
  const topic = topicForPath(pathname);
  const intent = intentForPath(pathname);
  const title = humanizeSlug(pathname);
  const topicBlock = TOPIC_BLOCKS[topic] || TOPIC_BLOCKS.general;
  const intentBlock = INTENT_BLOCKS[intent] || INTENT_BLOCKS.decision;
  return `<section class="hce-depth-section" data-hce-expanded="true">
    <h2>Detailed planning notes for ${title}</h2>
    <p>The sections below expand this guide so you can move from a quick answer to a more complete homeowner planning process. They focus on measurements, scope, quote comparison and the questions that reduce expensive surprises.</p>
    ${topicBlock}
    ${intentBlock}
    ${COMMON_BLOCK}
  </section>`;
}

export async function onRequest(context) {
  const response = await context.next();
  const contentType = response.headers.get("content-type") || "";

  if (!contentType.includes("text/html")) {
    return response;
  }

  const pathname = new URL(context.request.url).pathname;
  const isBlogArticle = /^\/blog\/[^/.]+(?:\\.html)?\/?$/i.test(pathname);
  const rewriter = new HTMLRewriter().on("head", {
    element(element) {
      element.append(
        `<script async src="https://www.googletagmanager.com/gtag/js?id=${GA_MEASUREMENT_ID}"></script>\n<script>\n  window.dataLayer = window.dataLayer || [];\n  function gtag(){dataLayer.push(arguments);}\n  gtag('js', new Date());\n  gtag('config', '${GA_MEASUREMENT_ID}');\n</script>`,
        { html: true }
      );
    }
  });

  if (isBlogArticle) {
    rewriter.on("main article.info-copy", {
      element(element) {
        element.append(externalLinksSection(pathname), { html: true });
        element.append(depthSection(pathname), { html: true });
      }
    });
  }

  return rewriter.transform(response);
}
