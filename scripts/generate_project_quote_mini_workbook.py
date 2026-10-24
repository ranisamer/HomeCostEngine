"""Generate the three-page, printable HomeCostEngine mini workbook."""
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
import textwrap

out = Path(__file__).resolve().parents[1] / 'output/pdf/project-quote-mini-workbook.pdf'
out.parent.mkdir(parents=True, exist_ok=True)
c = canvas.Canvas(str(out), pagesize=A4)
c.setTitle('Project Quote Mini Workbook')
c.setAuthor('HomeCostEngine Editorial Team')
W, H = A4
ink, teal, muted = map(HexColor, ['#172c3a', '#166d70', '#526372'])

def text(x, y, value, size=11, bold=False, color=ink):
    c.setFillColor(color)
    c.setFont('Helvetica-Bold' if bold else 'Helvetica', size)
    c.drawString(x, y, value)

def paragraph(y, value):
    for line in textwrap.wrap(value, 88):
        text(44, y, line, 11)
        y -= 17
    return y

def page(number, title, subtitle):
    c.setFillColor(teal); c.rect(0, H-16, W, 16, fill=1, stroke=0)
    text(44, H-52, 'HOME COST ENGINE  /  MINI WORKBOOK', 10, True, teal)
    text(44, H-95, title, 25, True)
    paragraph(H-122, subtitle)
    c.setStrokeColor(HexColor('#d3dee2')); c.line(44, 51, W-44, 51)
    text(44, 34, 'HomeCostEngine | Personal use | October 2026', 9, color=muted)
    text(W-89, 34, f'{number} / 3', 9, color=muted)

def field(y, label):
    text(44, y, label, 11, True)
    c.setStrokeColor(HexColor('#b7c6cd')); c.line(44, y-28, W-44, y-28)
    return y-60

def checks(y, items):
    for item in items:
        c.setStrokeColor(teal); c.rect(44, y-2, 9, 9, fill=0, stroke=1)
        text(62, y, item, 10)
        y -= 25
    return y

page(1, 'Define the same job', 'A compact companion for collecting project facts before asking contractors for comparable proposals. Print these pages and complete them by hand.')
y = field(H-188, 'Project / room / property:')
y = field(y, 'Required result and boundaries of the work:')
y = field(y, 'Measured quantities, units and who verified them:')
y = field(y, 'Product / finish specifications or owner selections:')
y = field(y, 'Unknown conditions requiring a site visit:')
text(44, y, 'Before you request prices', 14, True, teal)
checks(y-30, ['Give each contractor the same scope and measurements.', 'Ask who handles access, protection, disposal and restoration.', 'Ask who confirms permits, inspections and local requirements.', 'Keep assumptions separate from verified conditions.'])
paragraph(112, 'Planning aid only. This workbook is not an engineering design, contractor quote or statement of local code requirements.')
c.showPage()

page(2, 'Compare two proposals', 'Copy the written inclusions first. An unknown item is a question for the contractor, not a zero-cost assumption. Use one currency consistently throughout your comparison.')
left, right, top, row = 44, W-44, H-184, 37
columns = [left, 280, 411, right]
rows = ['Item / written scope', 'Base proposal amount', 'Quantity and material specification', 'Permit / inspection responsibility', 'Removal and disposal', 'Access and site protection', 'Allowances and owner purchases', 'Restoration / finishing', 'Warranty and exclusions', 'Confirmed excluded costs', 'Comparable planning total']
c.setFillColor(HexColor('#e6f0f0')); c.rect(left, top-row, right-left, row, fill=1, stroke=0)
for i, label in enumerate(rows):
    yy = top-i*row
    text(left+8, yy-23, label, 9, bold=(i==0 or i==len(rows)-1))
    c.setStrokeColor(HexColor('#c3d0d6')); c.line(left, yy-row, right, yy-row)
for x in columns: c.line(x, top, x, top-len(rows)*row)
c.line(left, top, right, top)
text(288, top-23, 'Proposal A', 10, True)
text(419, top-23, 'Proposal B', 10, True)
y = top-len(rows)*row-30
text(44, y, 'Comparable total = base + confirmed excluded costs', 12, True, teal)
y = paragraph(y-27, 'Do not add an allowance twice. If a selected product exceeds an included allowance, add only the confirmed shortfall. Keep unresolved items on a separate risk list.')
paragraph(y-18, 'A lower total does not establish better workmanship, insurance, licensing or contract terms. Verify these separately before choosing a contractor.')
c.showPage()

page(3, 'Close the gaps in writing', 'Resolve scope questions before signing. Keep this record with the proposal and any agreed change orders. A verbal promise is difficult to compare or audit later.')
y = H-192
checks(y, ['Confirm legal business identity and required local credentials.', 'Verify insurance and references using independent contact details.', 'Write the scope, exclusions, products and allowances into the contract.', 'Agree milestones, payment schedule and completion expectations.', 'Document how concealed conditions and changes will be approved.', 'Record warranty coverage, limitations and who handles claims.'])
y = field(H-375, 'Question still open / person responsible / due date:')
y = field(y, 'Agreed clarification / date / proposal reference:')
y = field(y, 'Change description / agreed cost / schedule effect / approval:')
text(44, y, 'Continue with the free planning tools', 14, True, teal)
for label, url in [('Project calculators', 'https://homecostengine.com/calculators/'), ('Contractor selection guide', 'https://homecostengine.com/blog/how-to-choose-roofing-contractor'), ('Order and download help', 'https://homecostengine.com/contact.html')]:
    y -= 26
    text(44, y, label, 11, color=teal)
    c.linkURL(url, (44, y-3, W-44, y+13), relative=0)
paragraph(105, 'Keep a copy of the final contract and receipts. Download help: reports@homecostengine.com. This is a 3-page mini workbook, not a full-length field guide.')
c.save()
print(out)
