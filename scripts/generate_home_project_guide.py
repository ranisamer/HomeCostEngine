from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, PageBreak,
    Table, TableStyle, KeepTogether, HRFlowable
)
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "guides" / "home-project-cost-planning-guide.pdf"
OUT.parent.mkdir(parents=True, exist_ok=True)

INK = colors.HexColor("#102033")
TEXT = colors.HexColor("#405064")
GREEN = colors.HexColor("#176b5b")
MINT = colors.HexColor("#d8efe9")
PAPER = colors.HexColor("#fbfaf7")
LINE = colors.HexColor("#dfe5e8")
WARM = colors.HexColor("#f0b56a")
WHITE = colors.white

for path, name in [
    ("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", "DejaVu"),
    ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", "DejaVu-Bold"),
]:
    if Path(path).exists():
        pdfmetrics.registerFont(TTFont(name, path))

FONT = "DejaVu" if "DejaVu" in pdfmetrics.getRegisteredFontNames() else "Helvetica"
BOLD = "DejaVu-Bold" if "DejaVu-Bold" in pdfmetrics.getRegisteredFontNames() else "Helvetica-Bold"

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="BookTitle", fontName=BOLD, fontSize=30, leading=34, textColor=WHITE, alignment=TA_LEFT, spaceAfter=15))
styles.add(ParagraphStyle(name="CoverSub", fontName=FONT, fontSize=13, leading=20, textColor=colors.HexColor("#dce6eb"), spaceAfter=16))
styles.add(ParagraphStyle(name="H1x", fontName=BOLD, fontSize=23, leading=28, textColor=INK, spaceAfter=14))
styles.add(ParagraphStyle(name="H2x", fontName=BOLD, fontSize=15, leading=20, textColor=INK, spaceBefore=14, spaceAfter=7))
styles.add(ParagraphStyle(name="Bodyx", fontName=FONT, fontSize=9.5, leading=15, textColor=TEXT, spaceAfter=8))
styles.add(ParagraphStyle(name="Smallx", fontName=FONT, fontSize=7.5, leading=11, textColor=TEXT))
styles.add(ParagraphStyle(name="Calloutx", fontName=FONT, fontSize=9, leading=14, textColor=INK, leftIndent=10, rightIndent=10, spaceBefore=5, spaceAfter=5))
styles.add(ParagraphStyle(name="Linkx", fontName=BOLD, fontSize=9, leading=14, textColor=GREEN, spaceAfter=6))
styles.add(ParagraphStyle(name="TOCx", fontName=FONT, fontSize=10, leading=16, textColor=INK, leftIndent=8, spaceAfter=5))


def link(label, url):
    return f'<link href="{url}" color="#176b5b"><u>{label}</u></link>'


def p(text, style="Bodyx"):
    return Paragraph(text, styles[style])


def table(rows, widths=None, header=True):
    data = [[Paragraph(str(cell), styles["Smallx"]) for cell in row] for row in rows]
    t = Table(data, colWidths=widths, repeatRows=1 if header else 0, hAlign="LEFT")
    cmds = [
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), .5, LINE),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("BACKGROUND", (0, 0), (-1, 0), INK if header else PAPER),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE if header else INK),
    ]
    for i in range(1 if header else 0, len(rows)):
        if i % 2 == 0:
            cmds.append(("BACKGROUND", (0, i), (-1, i), colors.HexColor("#f4f7f6")))
    t.setStyle(TableStyle(cmds))
    return t


def callout(title, body):
    box = Table([[Paragraph(f"<b>{title}</b><br/>{body}", styles["Calloutx"])]], colWidths=[6.7*inch])
    box.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), MINT),
        ("BOX", (0,0), (-1,-1), 1, colors.HexColor("#b9dcd3")),
        ("LEFTPADDING", (0,0), (-1,-1), 11),
        ("RIGHTPADDING", (0,0), (-1,-1), 11),
        ("TOPPADDING", (0,0), (-1,-1), 9),
        ("BOTTOMPADDING", (0,0), (-1,-1), 9),
    ]))
    return box


class GuideDoc(BaseDocTemplate):
    pass


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(LINE)
    canvas.line(.7*inch, .55*inch, 7.8*inch, .55*inch)
    canvas.setFont(FONT, 7.5)
    canvas.setFillColor(TEXT)
    canvas.drawString(.7*inch, .34*inch, "HomeCostEngine - U.S. Home Project Cost Planning Guide")
    canvas.drawRightString(7.8*inch, .34*inch, f"{doc.page}")
    canvas.restoreState()


doc = GuideDoc(str(OUT), pagesize=letter, rightMargin=.7*inch, leftMargin=.7*inch, topMargin=.68*inch, bottomMargin=.72*inch,
               title="The U.S. Home Project Cost Planning Guide", author="HomeCostEngine Editorial Team",
               subject="A practical guide to budgeting, comparing contractor quotes, permits and contingency planning.")
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main")
doc.addPageTemplates([PageTemplate(id="content", frames=[frame], onPage=footer)])

story = []

# Cover
cover = Table([[
    Paragraph("HCE", ParagraphStyle("mark", fontName=BOLD, fontSize=20, textColor=WHITE, alignment=TA_CENTER))
]], colWidths=[.75*inch], rowHeights=[.75*inch])
cover.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),GREEN),("VALIGN",(0,0),(-1,-1),"MIDDLE"),("BOX",(0,0),(-1,-1),0, GREEN)]))
story += [Spacer(1,.3*inch), cover, Spacer(1,.55*inch),
          Paragraph("The U.S. Home Project<br/>Cost Planning Guide", styles["BookTitle"]),
          Paragraph("A practical, no-sales-pressure system for building a project budget, comparing contractor proposals and protecting your contingency.", styles["CoverSub"]),
          Spacer(1,.25*inch), HRFlowable(width="72%", color=WARM, thickness=3, hAlign="LEFT"), Spacer(1,.25*inch),
          Paragraph("Includes a complete worked example, quote-comparison checklist, project worksheets and direct links to free HomeCostEngine calculators.", styles["CoverSub"]),
          Spacer(1,1.1*inch), Paragraph("Prepared by the HomeCostEngine Editorial Team<br/>Published and reviewed September 21, 2026", styles["CoverSub"]),
          Spacer(1,.55*inch), Paragraph("Planning information only. This guide is not a contractor quote, engineering opinion, code interpretation, tax advice or guarantee of final cost.", styles["Smallx"]), PageBreak()]

story += [p("How to use this guide", "H1x"),
          p("This book helps you turn a rough home-improvement idea into a budget that can survive real proposals. It does not tell you what a contractor in your ZIP code must charge. Instead, it gives you a repeatable process: define the same scope for every bidder, measure what you can, separate known work from allowances, reserve money for uncertainty, and compare complete proposals rather than headline prices."),
          callout("Best result", "Use the worksheets before requesting bids, then rebuild the budget with the actual quantities and written scope supplied by qualified local professionals."),
          p("Contents", "H2x")]

toc = [
    "1. Start with scope, not price", "2. Build low, typical and high planning cases",
    "3. Measure quantities before estimating", "4. Separate labor, materials and project overhead",
    "5. Set contingency by uncertainty", "6. Compare contractor proposals fairly",
    "7. Permits, code, safety and older homes", "8. Worked example: a roofing budget",
    "9. Project-by-project planning prompts", "10. Final decision checklist",
    "11. Printable worksheets", "12. Sources and free tools"
]
story += [p(item, "TOCx") for item in toc]
story += [Spacer(1,.12*inch), p("The online calculators linked throughout the guide are free and editable. Save your inputs and assumptions alongside every estimate so a future change in scope is easy to trace."), PageBreak()]

story += [p("1. Start with scope, not price", "H1x"),
          p("A price is only comparable when the scope behind it is comparable. Before asking what a project costs, write down the result you expect: the area being improved, materials or performance level, removal and disposal, preparation, access constraints, permits, protection of occupied spaces, cleanup, and warranty deliverables."),
          p("For example, two roof proposals can differ because one includes full tear-off, flashing replacement, ventilation correction, deck-repair allowances and permit fees while the other lists only shingles and installation. Calling the second proposal 'cheaper' before reconciling those differences is misleading."),
          p("A useful scope brief answers six questions:", "H2x"),
          table([["Question","What to record"],["What changes?","Exact rooms, surfaces, systems or assemblies"],["What stays?","Items to protect, reuse or exclude"],["Who supplies?","Owner-supplied versus contractor-supplied materials"],["What condition?","Known damage, access, demolition and disposal"],["What standard?","Product grade, efficiency, finish or performance target"],["What proof?","Permits, inspections, photos, warranties and closeout documents"]], [1.35*inch,5.35*inch]),
          p("Write the scope in plain language and give the same version to every bidder. If a contractor proposes a better method, ask for the change to be shown as a separate option. That preserves comparability."),
          callout("Free tool", f"Use the {link('Contractor Quote Comparison Calculator','https://homecostengine.com/calculators/contractor-quote-comparison.html')} after you receive itemized proposals."), PageBreak()]

story += [p("2. Build low, typical and high planning cases", "H1x"),
          p("A single estimate creates false precision. A planning range is more useful because quantity, specification, access, regional labor, permit requirements and concealed conditions can change. Build three cases with the same measurement base."),
          table([["Case","Use it for","Typical assumptions"],["Low","Simple, well-defined work","Easy access, standard materials, minimal repairs, competitive local bids"],["Typical","Your working budget","Normal access, mid-grade selections, ordinary prep, expected fees and a realistic reserve"],["High","Stress test","Complex access, premium selections, more preparation, higher local labor or uncertain existing conditions"]],[1.05*inch,1.7*inch,3.95*inch]),
          p("Do not create the high case by adding an arbitrary percentage to everything. Identify which variables can actually move: more deck replacement on a roof, more subfloor preparation under flooring, electrical upgrades for HVAC, wall repairs before painting, or excavation and base correction under concrete."),
          p("A simple planning model", "H2x"),
          p("Known scope subtotal = measured quantity x unit allowance + fixed known costs. Planning total = known scope subtotal + allowances for unresolved selections + contingency for uncertainty."),
          callout("Important distinction", "An allowance is an expected but not fully selected cost, such as fixtures. Contingency is money held for uncertainty, not a shopping budget."),
          p(f"Build the reserve separately with the {link('Project Contingency Calculator','https://homecostengine.com/calculators/project-contingency.html')}."), PageBreak()]

story += [p("3. Measure quantities before estimating", "H1x"),
          p("Quantity is the bridge between a project idea and a reviewable budget. Measure the surface, volume or unit count before attaching prices. Keep original measurements, conversion assumptions and waste in separate lines so they can be checked."),
          table([["Project","Primary quantity","Common adjustment"],["Roofing","Roof area in square feet or roofing squares","Pitch multiplier, waste, valleys, hips and penetrations"],["Concrete","Length x width x thickness converted to cubic yards","Thickened edges, uneven grade and ordering reserve"],["Painting","Paintable wall and ceiling area","Doors/windows deducted, coats and coverage"],["Flooring","Net floor area","Layout waste, pattern matching and attic stock"],["HVAC","Load and system requirements","Ductwork, electrical, drainage and controls"],["Landscaping","Area and material depth","Compaction, settlement and delivery units"]],[1.05*inch,2.6*inch,3.05*inch]),
          p("Measure twice and record the source of every number. A contractor or designer may later replace your planning measurement with a field-verified quantity. That is normal; the original record lets you understand why the budget changed."),
          p("Useful calculators", "H2x"),
          p(f"Start with the {link('Square Footage Calculator','https://homecostengine.com/calculators/square-footage.html')}, {link('Concrete Calculator','https://homecostengine.com/calculators/concrete.html')}, {link('Paint Calculator','https://homecostengine.com/calculators/paint.html')} or {link('Flooring Calculator','https://homecostengine.com/calculators/flooring.html')}."), PageBreak()]

story += [p("4. Separate labor, materials and project overhead", "H1x"),
          p("A useful budget shows why the total exists. Separate direct material, direct labor, removal and disposal, equipment, delivery, permit or inspection fees, protection and cleanup, and contractor overhead/profit when a proposal provides that detail. Do not assume a percentage split is universal; trade, market and scope all matter."),
          p("Materials", "H2x"), p("Record product, grade, quantity, waste, delivery, tax and any owner-supplied items. Confirm whether quoted materials are exact products or allowances. Product substitutions should be documented before installation."),
          p("Labor", "H2x"), p("Labor is affected by access, occupied-home protection, demolition, preparation, height, sequencing, crew availability and local requirements. A low material cost does not make a labor-intensive project inexpensive."),
          p("Overhead and risk", "H2x"), p("A legitimate proposal may include supervision, insurance, licensing, scheduling, warranty administration and business overhead. Comparing only material receipts to a full-service contractor price is not a like-for-like comparison."),
          callout("Decision rule", "Ask what is included and excluded. Do not demand a contractor use your internal budget categories if their proposal clearly defines scope, price, payment schedule and change-order rules."),
          p(f"Use the {link('Labor and Material Split Calculator','https://homecostengine.com/calculators/labor-material-split.html')} to organize a planning scenario, not to dictate a contractor's accounting."), PageBreak()]

story += [p("5. Set contingency by uncertainty", "H1x"),
          p("Contingency should follow uncertainty. A cosmetic project with visible surfaces and complete selections may justify a smaller reserve than demolition in an older home where framing, wiring, plumbing or moisture conditions are unknown. The reserve should be controlled by the owner and released only for documented changes."),
          table([["Uncertainty level","Planning signal","Reserve approach"],["Lower","Visible conditions, complete design, firm selections, simple access","Smaller reserve; still protect against quantity or minor repair changes"],["Moderate","Some demolition, a few allowances, ordinary older-home conditions","Working reserve tied to specific risk items"],["Higher","Concealed systems, structural questions, incomplete design or difficult access","Larger reserve and more investigation before contract"]],[1.1*inch,3.25*inch,2.35*inch]),
          p("Never hide desired upgrades inside contingency. If you already want premium tile, upgraded windows or a higher-efficiency system, place that selection in the base scope. Contingency is not evidence that surprise work will occur and should not automatically be paid to the contractor."),
          p("Change control", "H2x"),
          p("For every change, record the condition discovered, proposed solution, price and schedule effect. Approve the change in writing before work proceeds when practical. Keep photos and inspection records with the project file."), PageBreak()]

story += [p("6. Compare contractor proposals fairly", "H1x"),
          p("The Federal Trade Commission advises homeowners to get multiple written estimates, check credentials where required, understand the contract and avoid paying the full amount up front. Treat a bid review as both a price comparison and a scope-quality review."),
          table([["Review item","Proposal A","Proposal B","Proposal C"],["Total price","$________","$________","$________"],["Exact scope attached","Yes / No","Yes / No","Yes / No"],["Allowances identified","$________","$________","$________"],["Exclusions clear","Yes / No","Yes / No","Yes / No"],["Permit responsibility","________","________","________"],["Payment schedule","________","________","________"],["Warranty in writing","________","________","________"],["Schedule / duration","________","________","________"]],[1.8*inch,1.63*inch,1.63*inch,1.63*inch]),
          p("Normalize each proposal before ranking price. Add missing scope to the cheapest bid or remove optional scope from the others. A proposal with a large fixture allowance is not directly comparable with one that excludes fixtures."),
          p(f"Read the {link('roofing quote comparison guide','https://homecostengine.com/blog/how-to-compare-roofing-quotes.html')} for a trade-specific example, then enter three bids in the {link('quote comparison calculator','https://homecostengine.com/calculators/contractor-quote-comparison.html')}."), PageBreak()]

story += [p("7. Permits, code, safety and older homes", "H1x"),
          p("Permit and inspection rules are local. Contact the authority having jurisdiction before assuming work is exempt. Ask each bidder who obtains the permit, who schedules inspections, and whether permit fees are included. A calculator cannot determine local code compliance."),
          p("Homes built before 1978 require special attention when painted surfaces will be disturbed. The U.S. Environmental Protection Agency's Renovation, Repair and Painting program requires lead-safe practices for covered work performed for compensation in pre-1978 housing and child-occupied facilities. Confirm whether the work and contractor are covered; do not treat a visual inspection as a lead test."),
          p("Safety and hidden conditions", "H2x"),
          p("Roofing, electrical, gas, structural, excavation and refrigerant work can create serious hazards. Use qualified professionals where the scope, law or risk requires them. Stop work when unexpected structural movement, unsafe wiring, gas odor, significant moisture or suspected hazardous material is found and obtain appropriate professional guidance."),
          callout("Local verification", "Prices, adopted codes, permit processes, license rules and incentives vary by jurisdiction. Verify them with official local and state sources before signing a contract."), PageBreak()]

story += [p("8. Worked example: a roofing budget", "H1x"),
          p("This hypothetical example demonstrates method, not a market price. A homeowner is planning replacement of an asphalt-shingle roof. The measured roof area is 2,100 square feet. The homeowner uses a 10% planning allowance for cuts and complexity, producing 2,310 square feet, or 23.1 roofing squares."),
          table([["Budget line","Planning input","Amount"],["Base replacement scope","2,310 sq ft x hypothetical $7.25/sq ft","$16,747.50"],["Permit allowance","Local amount not yet verified","$450.00"],["Deck repair allowance","150 sq ft x hypothetical $5.00/sq ft","$750.00"],["Known + allowed subtotal","Sum of lines above","$17,947.50"],["Contingency","8% of subtotal","$1,435.80"],["Planning total","Subtotal + contingency","$19,383.30"]],[1.85*inch,3.05*inch,1.8*inch]),
          p("The homeowner should not tell bidders that $19,383.30 is the correct price. Instead, the number tests affordability and highlights unresolved items: actual roof measurement, tear-off layers, flashing, ventilation, disposal, deck condition, permit fee and product specification."),
          p("When proposals arrive, the homeowner replaces hypothetical inputs with written bid amounts and keeps deck repair as a unit-price or documented allowance if the deck is concealed."),
          p(f"Build your own scenario with the {link('Roof Replacement Cost Calculator','https://homecostengine.com/calculators/roof-replacement')}, then check pitch using the {link('Roof Pitch Calculator','https://homecostengine.com/calculators/roof-pitch.html')}."), PageBreak()]

story += [p("9. Project-by-project planning prompts", "H1x"),
          p("Roofing", "H2x"), p("Confirm roof area, material system, tear-off, deck repair unit pricing, flashing, ventilation, underlayment, ice/water protection where applicable, disposal, permits, workmanship warranty and manufacturer documentation."),
          p("HVAC", "H2x"), p("Confirm load-sizing method, equipment pairing and efficiency, ductwork, electrical, condensate handling, thermostat, refrigerant work, permits, commissioning, warranty registration and removed-equipment disposal. A house-size shortcut is only an early planning input."),
          p("Concrete", "H2x"), p("Confirm dimensions, thickness, base preparation, reinforcement, drainage, forms, joints, finish, access, short-load or delivery charges, curing, demolition, disposal and weather plan."),
          p("Painting", "H2x"), p("Confirm exact surfaces, repairs, cleaning, primer, number of coats, product line and sheen, occupied-space protection, moving furniture, trim/doors/ceilings, cleanup and touch-up process."),
          p("Flooring", "H2x"), p("Confirm net area, waste, demolition, subfloor preparation, moisture testing, transitions, stairs, baseboards, furniture/appliance moving, acclimation, disposal and attic stock."),
          p("Kitchen and bath", "H2x"), p("Confirm design completeness, fixture and finish allowances, plumbing/electrical moves, ventilation, waterproofing, cabinetry, countertops, appliance interfaces, demolition, permits and whether the home remains usable during construction."), PageBreak()]

story += [p("10. Final decision checklist", "H1x"),
          table([["Before signing","Complete"],["The same written scope was issued to every bidder","[  ]"],["Proposal includes product/specification details","[  ]"],["Allowances and exclusions are clearly identified","[  ]"],["Permit and inspection responsibility is written","[  ]"],["License and insurance were checked where applicable","[  ]"],["Payment schedule is tied to clear milestones","[  ]"],["Change-order process is written","[  ]"],["Start date, expected duration and access rules are written","[  ]"],["Cleanup, disposal and protection are included","[  ]"],["Labor and product warranties are documented","[  ]"],["Contingency remains under owner control","[  ]"],["Financing terms and total repayment are understood","[  ]"]],[5.85*inch,.85*inch]),
          Spacer(1,.16*inch), callout("Red flags", "Pressure to decide immediately, requests for full payment up front, refusal to provide a written contract, unverifiable credentials, vague product descriptions, or instructions to avoid required permits deserve additional scrutiny."), PageBreak()]

story += [p("11. Project budget worksheet", "H1x"),
          table([["Budget line","Low","Typical","High","Source / assumption"],
                 ["Materials","$______","$______","$______","________________"],
                 ["Labor","$______","$______","$______","________________"],
                 ["Demolition / disposal","$______","$______","$______","________________"],
                 ["Preparation / repairs","$______","$______","$______","________________"],
                 ["Equipment / delivery","$______","$______","$______","________________"],
                 ["Permits / inspections","$______","$______","$______","________________"],
                 ["Selections / allowances","$______","$______","$______","________________"],
                 ["Known subtotal","$______","$______","$______","________________"],
                 ["Contingency","$______","$______","$______","____%"],
                 ["Planning total","$______","$______","$______","________________"]],
                [1.55*inch,1.05*inch,1.05*inch,1.05*inch,2*inch]),
          p("Scope notes", "H2x"),
          table([["Included","Excluded / owner supplied","Unresolved questions"],["\n\n\n\n","\n\n\n\n","\n\n\n\n"]],[2.23*inch,2.23*inch,2.23*inch]), PageBreak()]

story += [p("12. Sources and free tools", "H1x"),
          p("Authoritative homeowner references", "H2x"),
          p(link("Federal Trade Commission: Home Improvement and Repair Scams", "https://consumer.ftc.gov/articles/home-improvement-scams"), "Linkx"),
          p(link("U.S. EPA: Lead Renovation, Repair and Painting Program", "https://www.epa.gov/lead/lead-renovation-repair-and-painting-program"), "Linkx"),
          p(link("U.S. Department of Energy: Home Upgrades", "https://www.energy.gov/save/home-upgrades"), "Linkx"),
          p(link("HUD: Healthy Homes Program", "https://www.hud.gov/hud-partners/healthy-homes"), "Linkx"),
          p("HomeCostEngine planning tools", "H2x"),
          p(link("All home improvement calculators", "https://homecostengine.com/calculators/"), "Linkx"),
          p(link("Project contingency calculator", "https://homecostengine.com/calculators/project-contingency.html"), "Linkx"),
          p(link("Contractor quote comparison calculator", "https://homecostengine.com/calculators/contractor-quote-comparison.html"), "Linkx"),
          p(link("Home maintenance budget calculator", "https://homecostengine.com/calculators/home-maintenance-budget.html"), "Linkx"),
          p(link("HomeCostEngine cost methodology", "https://homecostengine.com/cost-methodology.html"), "Linkx"),
          Spacer(1,.25*inch), HRFlowable(color=LINE, thickness=1), Spacer(1,.2*inch),
          p("Editorial note", "H2x"),
          p("This guide was prepared by the HomeCostEngine Editorial Team and reviewed on September 21, 2026. Numerical examples are explicitly hypothetical and demonstrate calculation method only. HomeCostEngine does not sell contractor leads or provide contractor recommendations. Always verify local scope, pricing, permits, code requirements, credentials and safety needs."),
          callout("Keep planning", "Revisit your budget when the scope changes. A transparent estimate is valuable because every assumption can be replaced with better information as the project develops.")]

def cover_bg(canvas, doc):
    canvas.saveState()
    if doc.page == 1:
        canvas.setFillColor(INK)
        canvas.rect(0,0,letter[0],letter[1],fill=1,stroke=0)
        canvas.setFillColor(GREEN)
        canvas.circle(7.4*inch,9.7*inch,1.8*inch,fill=1,stroke=0)
        canvas.setFillColor(colors.HexColor("#21405b"))
        canvas.circle(7.0*inch,1.0*inch,2.3*inch,fill=1,stroke=0)
    else:
        footer(canvas, doc)
    canvas.restoreState()

doc.pageTemplates = [PageTemplate(id="all", frames=[frame], onPage=cover_bg)]
doc.build(story)
print(OUT)
