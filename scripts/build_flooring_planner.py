#!/usr/bin/env python3
"""Reproducible 64-page original handbook, real page previews and cover.
Run from repository root. Full PDF is a build artifact; only the first 3 chapter
pages are published statically. Paid download bytes live in a verified route.
"""
from pathlib import Path
import importlib.util, re, json, hashlib, base64
from html import escape
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import fitz
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('manuscript',ROOT/'books/flooring-planner.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
assert len(m.CHAPTERS)==19
OUT=ROOT/'output';OUT.mkdir(exist_ok=True)
ASSETS=ROOT/'assets/books/flooring-project-planner';ASSETS.mkdir(parents=True,exist_ok=True)
FONTS=Path('/usr/share/fonts/truetype/dejavu')
for name,file in [('Body','DejaVuSerif.ttf'),('BodyBold','DejaVuSerif-Bold.ttf'),('Sans','DejaVuSans.ttf'),('SansBold','DejaVuSans-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(name,str(FONTS/file)))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='BodyBold',italic='Body',boldItalic='BodyBold')
pdfmetrics.registerFontFamily('Sans',normal='Sans',bold='SansBold',italic='Sans',boldItalic='SansBold')
NAVY=colors.HexColor('#162d3b');INK=colors.HexColor('#263b46');MUTED=colors.HexColor('#5a6b71');GOLD=colors.HexColor('#a87d38');CREAM=colors.HexColor('#faf7ef');LINE=colors.HexColor('#d5dedf')
W,H=432,648;L=48;WIDTH=336
pdf=OUT/'flooring-project-planner.pdf'
c=canvas.Canvas(str(pdf),pagesize=(W,H),pageCompression=1,invariant=1)
c.setTitle('Flooring Project Planner');c.setAuthor('HomeCostEngine Editorial Team');c.setSubject('Original flooring quantity and cost planning handbook and 19 fillable worksheets; 2026-10-25 edition')
styles={'body':ParagraphStyle('body',fontName='Body',fontSize=10,leading=14,textColor=INK,spaceAfter=11), 'small':ParagraphStyle('small',fontName='Sans',fontSize=8.3,leading=12,textColor=MUTED), 'deck':ParagraphStyle('deck',fontName='Body',fontSize=12,leading=18,textColor=MUTED), 'title':ParagraphStyle('title',fontName='BodyBold',fontSize=21,leading=26,textColor=NAVY), 'sub':ParagraphStyle('sub',fontName='SansBold',fontSize=11,leading=16,textColor=NAVY), 'table':ParagraphStyle('table',fontName='Sans',fontSize=9,leading=13,textColor=INK)}
page=0;bounds=[]
def para(text,y,kind='body',width=WIDTH,x=L):
    p=Paragraph(text,styles[kind]);_,h=p.wrap(width,900)
    if y-h<48: raise ValueError(f'Page {page}: overflow {text[:60]}, bottom={y-h}')
    p.drawOn(c,x,y-h);bounds.append((page,x,y-h,x+width,y));return y-h-(11 if kind=='body' else 8)
def begin(label,chapter=None):
    global page
    page+=1;c.setFillColor(colors.white);c.rect(0,0,W,H,fill=1,stroke=0)
    c.setStrokeColor(LINE);c.line(L,H-37,W-L,H-37)
    c.setFont('Sans',7);c.setFillColor(MUTED);c.drawString(L,H-27,'HOME COST ENGINE  /  FLOORING PLANNING')
    c.setFont('Sans',7.5);c.drawString(L,29,label.upper()[:65]);c.drawRightString(W-L,29,str(page))
    if chapter:
        c.bookmarkPage(f'ch{chapter}');c.addOutlineEntry(f'{chapter}. {label}',f'ch{chapter}',0)
    return H-66

def end():c.showPage()
def title(text,y): return para(escape(text),y,'title')-9

def table(rows,y):
    cells=[[Paragraph(escape(a),styles['table']),Paragraph(escape(b),styles['table'])]for a,b in rows]
    t=Table(cells,colWidths=[235,101]);t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),10),('RIGHTPADDING',(0,0),(-1,-1),9),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7),('ROWBACKGROUNDS',(0,0),(-1,-1),[CREAM,colors.white]),('LINEBELOW',(0,-1),(-1,-1),.7,GOLD)]))
    _,h=t.wrap(WIDTH,1000)
    if y-h<55:raise ValueError(f'Table overflow {page}')
    t.drawOn(c,L,y-h);return y-h-18

def source(text,y):return para(escape(text),y,'small')
# Cover, restrained typography like the supplied reference, with original layout.
page+=1;c.setFillColor(NAVY);c.rect(0,0,W,H,fill=1,stroke=0)
c.setStrokeColor(GOLD);c.setLineWidth(1);c.rect(28,28,W-56,H-56,fill=0,stroke=1)
c.setFillColor(colors.HexColor('#f6efd9'));c.setFont('SansBold',10);c.drawCentredString(W/2,563,'HOME COST ENGINE')
coverstyle=ParagraphStyle('cover',fontName='BodyBold',fontSize=33,leading=41,textColor=CREAM,alignment=1)
p=Paragraph('Flooring Project<br/>Planner',coverstyle);_,h=p.wrap(340,400);p.drawOn(c,46,460-h)
c.setStrokeColor(GOLD);c.line(148,257,284,257)
for i,line in enumerate(['Measure the rooms. Check the pack count.','Compare the complete installed scope.']):
 c.setFont('Sans',10.5);c.setFillColor(CREAM);c.drawCentredString(W/2,225-i*20,line)
c.setFont('Sans',9);c.drawCentredString(W/2,135,'A practical U.S. homeowner handbook')
c.drawCentredString(W/2,115,'19 worked examples + 19 fillable planning sheets')
c.setFont('Sans',8);c.drawCentredString(W/2,70,'FIRST EDITION  /  OCTOBER 2026');end()
y=begin('Rights and reader notes');y=title('Rights and reader notes',y)
for s in ['© 2026 HomeCostEngine. Original text, examples and worksheets. First edition, reviewed October 25, 2026. Editorial author: HomeCostEngine Editorial Team.',
'Personal-use edition. You may print the worksheets and share completed project records with your own contractors and advisers. Please do not redistribute or resell the uncompleted book.',
'This is a planning handbook, not a construction specification, contractor bid, safety procedure or professional legal, tax or engineering advice. Have qualified local professionals verify site conditions, installation needs, permits and applicable requirements.',
'All project dollar amounts in worked examples are hypothetical U.S. dollars (USD). They demonstrate arithmetic and scope comparisons, not local market prices. The store purchase price is separately displayed in British pounds (GBP).',
'The supplied reference book informed the broad sequence: preface, foundations, working methods, practical applications and afterword. All flooring content, calculations and worksheets here were written independently.',
'PDF fields can be completed in a compatible PDF reader. Save a copy before editing and confirm that entered values persist. Blank lines also work for printing. Fields do not calculate automatically. Your saved entries remain in your local PDF; this book does not upload them.']:
 y=para(escape(s),y)
end()
contents=[('1','Preface: how to use this book',5)]+[(str(i+2),ch['title'],7+i*3)for i,ch in enumerate(m.CHAPTERS)]+[('21','Afterword and source notes',64)]
for idx,entries in enumerate([contents[:11],contents[11:]]):
 y=begin('Contents');y=title('Contents' if idx==0 else 'Contents / continued',y)
 for number,name,pno in entries:
  y=para(f'<b>{number}.</b> {escape(name)} <font color="#a87d38">/ {pno}</font>',y,'body')-8
 if idx==1:y=para('Each chapter from 2 to 20 has three pages: understand the decision, work through an example, then complete a planning sheet.',y-12,'deck')
 end()
y=begin('Preface: how to use this book',1);y=title('Preface',y)
for s in ['Flooring decisions connect room measurements, selected materials and the work that makes a floor ready to use. This handbook helps you check quantities and complete proposals while keeping product-specific technical decisions with the responsible installer.',
'Start with the brief and room schedule. Check net area, layout allowance and pack rounding before comparing prices. Then connect the selected product, spare stock, removal, preparation, assembly accessories, interfaces, layout, logistics and final handover.',
'Every working chapter contains an explanation, a hypothetical example and a reusable planning sheet. Six general budgeting chapters use the HomeCostEngine renovation method with flooring adaptation. Thirteen flooring chapters supply ordering cases and project-specific scope questions.',
'All project amounts and example allowances are invented USD teaching inputs, not local prices or universal ordering recommendations. Example pack coverage and allowance percentages are assumptions; use the selected product and installer-approved takeoff for the actual order.',
'Have qualified providers assess site conditions, product suitability, substrate readiness and installation requirements. This book provides no removal, testing, installation or repair procedure. Keep the room plan, product labels, orders, approved changes, invoices and care records with your completed sheets.']:
 y=para(escape(s),y)
end()
y=begin('Your planning workflow');y=title('A five-pass workflow',y)
for head,body in [('1 / Define','Record room boundaries, desired outcomes, occupied-area needs and the spending ceiling.'),('2 / Measure','Check net area, the approved layout allowance, pack coverage and installer-confirmed order.'),('3 / Compare','Match removal, preparation, products, accessories, installation and logistics before ranking bids.'),('4 / Commit and review','Record the contract, allowance basis, paid amounts, unpaid obligations and approved changes.'),('5 / Close out','Reconcile obligations and credits. Save product records, warranties and the punch list.')]:
 y=para(head,y,'sub');y=para(escape(body),y)
y=para('Quick arithmetic checks',y,'sub')
y=para('Quantity line = verified quantity × matching unit rate.<br/>All-in plan = defined work + allowances + owner costs + reserve.<br/>Variance = forecast total − working ceiling.<br/>A positive variance means the forecast is over the ceiling.',y)
y=para('Use the free calculators at <link href="https://homecostengine.com/calculators/" color="#a87d38">homecostengine.com/calculators/</link> to check quantities. Tool defaults are planning inputs, not verified prices for your house.',y,'small');end()
for i,ch in enumerate(m.CHAPTERS,2):
 y=begin(ch['title'],i);y=para(f'CHAPTER {i:02d}',y,'small');y=title(ch['title'],y);y=para(escape(ch['deck']),y,'deck')-6
 for s in ch['paragraphs']:y=para(escape(s),y)
 end()
 y=begin(f'{i:02d} / Worked example');y=title('Work the numbers',y);y=para('HYPOTHETICAL USD EXAMPLE / NOT A PRICE QUOTE',y,'small')-6
 y=para(escape(ch['example']),y);y=table(ch['rows'],y);y=para(escape(ch['conclusion']),y)
 y=para('Apply the example to your project',y,'sub')
 y=para('Replace the quantities and amounts with your own documented inputs. Keep the same units and list excluded work before treating the result as a complete budget.',y)
 y=para('Next action',y,'sub');y=para(escape(ch['task']),y);end()
 y=begin(f'{i:02d} / Planning sheet');y=title('Your planning sheet',y);y=para(escape(ch['title']),y,'deck')
 y=para('Project / room: ____________________    Date: __________',y,'small')-4
 for j,prompt in enumerate(ch['prompts'],1):
  y=para(f'{j}. {escape(prompt)}',y,'small')
  c.acroForm.textfield(name=f'chapter_{i:02d}_field_{j}',tooltip=f'{ch["title"]}: {prompt}',x=L,y=y-37,width=WIDTH,height=37,fontName='Helvetica',fontSize=9,textColor=INK,borderColor=LINE,fillColor=CREAM,borderWidth=.5,fieldFlags='multiline',maxlen=2000,forceBorder=True)
  y-=49
 y=para('Before moving on',y,'sub')
 for s in ch['checks']:y=para('□ '+escape(s),y,'small')
 end()
y=begin('Afterword and source notes',21);y=title('Afterword',y)
y=para('A useful flooring record connects the room plan and approved product to checked quantities, complete installed scope and available funding. Keep allowances and quantity bases visible, count each obligation once, and retain the completed sheets with labels, orders, care instructions and the final handover.',y)
y=para('Source notes',y,'sub')
y=para('Primary resources checked October 25, 2026. Numbered references identify supporting guidance; these organizations do not endorse this book. The numerical examples and worksheets are original.',y,'small')
for num,name,url in m.SOURCES:
 y=para(f'<b>[{num}] {escape(name)}</b><br/><link href="{url}" color="#a87d38"><font size="7.9">{escape(url)}</font></link>',y,'small')-6
y=para('Questions about the PDF or an order: <link href="mailto:reports@homecostengine.com" color="#a87d38">reports@homecostengine.com</link>. For your own records, retain the edition date and a copy of the original download.',y-3,'small');end()
assert page==64,page
c.save()
doc=fitz.open(pdf)
assert len(doc)==64
# Raster assets are actual pages of this edition, never simulated excerpts.
for index,name in [(0,'cover'),(6,'preview-1'),(7,'preview-2'),(8,'preview-3')]:
 pix=doc[index].get_pixmap(matrix=fitz.Matrix(1.6,1.6),alpha=False)
 from PIL import Image
 image=Image.frombytes('RGB',[pix.width,pix.height],pix.samples)
 image.save(ASSETS/f'{name}.webp','WEBP',quality=88)
# Contact sheet for inspection of every page.
from PIL import Image,ImageDraw
sheet=Image.new('RGB',(8*162,8*258),'#e0e5e6');draw=ImageDraw.Draw(sheet)
for i,p in enumerate(doc):
 pix=p.get_pixmap(matrix=fitz.Matrix(.35,.35),alpha=False);im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples)
 x=(i%8)*162+5;y=(i//8)*258+5;sheet.paste(im,(x,y));draw.text((x,y+229),str(i+1),fill='black')
sheet.save(OUT/'flooring-contact-sheet.jpg',quality=90)
text='\n'.join(p.get_text()for p in doc)
fields=sum(len(list(p.widgets() or []))for p in doc)
assert fields==95,fields
for p in doc:
 for block in p.get_text('blocks'):
  assert block[0]>=25 and block[2]<=W-24,(p.number,block)
  assert block[1]>=15 and block[3]<=H-15,(p.number,block)
assert len(doc.get_toc())==21
report=dict(pages=len(doc),fillable_fields=fields,chapters=len(doc.get_toc()),word_count=len(text.split()),sha256=hashlib.sha256(pdf.read_bytes()).hexdigest(),preview_physical_pages=[7,8,9],edition='2026-10-25')
(OUT/'flooring-validation.json').write_text(json.dumps(report,indent=2));print(json.dumps(report))

# Rebuild the server-bundled entitlement-gated bytes along with the review PDF.
route=(ROOT/'functions/api/download-mini-guide.js').read_text()
route=re.sub(r'const PDF_BASE64 = "[^"]+";', 'const PDF_BASE64 = "'+base64.b64encode(pdf.read_bytes()).decode()+'";',route,count=1)
route=route.replace('project-quote-mini-workbook','flooring-project-planner').replace('This purchase does not include this workbook.','This purchase does not include this book.')
(ROOT/'functions/api/download-flooring-planner.js').write_text(route)
