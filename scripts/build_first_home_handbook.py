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
spec=importlib.util.spec_from_file_location('manuscript',ROOT/'books/first-home-handbook.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
assert len(m.CHAPTERS)==19
OUT=ROOT/'output';OUT.mkdir(exist_ok=True)
ASSETS=ROOT/'assets/books/first-time-homeowner-cost-maintenance-handbook';ASSETS.mkdir(parents=True,exist_ok=True)
FONTS=Path('/usr/share/fonts/truetype/dejavu')
for name,file in [('Body','DejaVuSerif.ttf'),('BodyBold','DejaVuSerif-Bold.ttf'),('Sans','DejaVuSans.ttf'),('SansBold','DejaVuSans-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(name,str(FONTS/file)))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='BodyBold',italic='Body',boldItalic='BodyBold')
pdfmetrics.registerFontFamily('Sans',normal='Sans',bold='SansBold',italic='Sans',boldItalic='SansBold')
NAVY=colors.HexColor('#162d3b');INK=colors.HexColor('#263b46');MUTED=colors.HexColor('#5a6b71');GOLD=colors.HexColor('#a87d38');CREAM=colors.HexColor('#faf7ef');LINE=colors.HexColor('#d5dedf')
W,H=432,648;L=48;WIDTH=336
pdf=OUT/'first-time-homeowner-cost-maintenance-handbook.pdf'
c=canvas.Canvas(str(pdf),pagesize=(W,H),pageCompression=1,invariant=1)
c.setTitle('Home Maintenance Checklist & Cost Planner');c.setAuthor('HomeCostEngine Editorial Team');c.setSubject('Original first-year homeowner organization and cost handbook and 19 fillable worksheets; 2026-10-25 edition')
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
    c.setFont('Sans',7);c.setFillColor(MUTED);c.drawString(L,H-27,'HOME COST ENGINE  /  FIRST-YEAR OWNERSHIP')
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
coverstyle=ParagraphStyle('cover',fontName='BodyBold',fontSize=29,leading=37,textColor=CREAM,alignment=1)
p=Paragraph('Home Maintenance<br/>Checklist &amp;<br/>Cost Planner',coverstyle);_,h=p.wrap(340,400);p.drawOn(c,46,460-h)
c.setStrokeColor(GOLD);c.line(148,257,284,257)
for i,line in enumerate(['Collect the records. Assign the tasks.','Build a practical first-year care routine.']):
 c.setFont('Sans',10.5);c.setFillColor(CREAM);c.drawCentredString(W/2,225-i*20,line)
c.setFont('Sans',9);c.drawCentredString(W/2,135,'A practical U.S. homeowner handbook')
c.drawCentredString(W/2,115,'19 worked examples + 19 fillable planning sheets')
c.setFont('Sans',8);c.drawCentredString(W/2,70,'FIRST EDITION  /  OCTOBER 2026');end()
y=begin('Rights and reader notes');y=title('Rights and reader notes',y)
for s in ['© 2026 HomeCostEngine. Original text, examples and worksheets. First edition, reviewed October 25, 2026. Editorial author: HomeCostEngine Editorial Team.',
'Personal-use edition. You may print the worksheets and share completed project records with your own contractors and advisers. Please do not redistribute or resell the uncompleted book.',
'This is a planning handbook, not a construction specification, contractor bid, safety procedure or professional legal, tax or engineering advice. Have qualified local professionals verify site conditions, installation needs, permits and applicable requirements.',
'All project dollar amounts in worked examples are hypothetical U.S. dollars (USD). They demonstrate arithmetic and scope comparisons, not local market prices. The store purchase price is separately displayed in British pounds (GBP).',
'The supplied reference book informed the broad sequence: preface, foundations, working methods, practical applications and afterword. All first-year homeowner content, calculations and worksheets here were written independently.',
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
for s in ['The first year of ownership brings records, service decisions and costs that can feel scattered. This handbook helps you organize the handover file, responsibilities, current asset information and a realistic care routine without pretending to inspect the home.',
'Start with the first-year brief and handover records. Establish responsibilities, asset details, contacts and a household readiness record. Turn inspection follow-ups and actual manuals into assigned actions before building the care spending plan and service history.',
'Every working chapter contains an explanation, an original hypothetical example and a planning sheet. These nineteen chapters organize the first year of ownership. Asset, task and funding principles also appear in our ongoing maintenance planner; this edition emphasizes handover, responsibility and first-year setup.',
'All costs, counts and saving horizons in examples are invented USD teaching inputs, not local prices, universal service intervals or predictions of asset life. The first-month setup window is an organization choice and never overrides an actual urgent requirement.',
'Use actual instructions, official local information and qualified provider findings for technical condition, required care and urgent response. This handbook supplies no technical servicing or emergency procedure. Keep manuals, relevant reports, accepted work, invoices and follow-up records with the sheets.']:
 y=para(escape(s),y)
end()
y=begin('Your planning workflow');y=title('A five-pass workflow',y)
for head,body in [('1 / Define','Record first-year needs, responsibilities, existing records and the household care boundary.'),('2 / Measure','Collect actual asset details, manuals, contacts and inspection follow-up questions.'),('3 / Compare','Compare assessed work and matched service scope before accepting proposals.'),('4 / Commit and review','Track sourced care tasks, accepted work, paid costs, unpaid obligations and reserve movements.'),('5 / Close out','Reconcile the first-year record and set the next sourced tasks and funding assumptions.')]:
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
y=para('A useful first-year record connects the home information to clear responsibilities, sourced tasks, qualified findings and a realistic care budget. Keep unknowns visible, preserve unpaid obligations, and use the service history to make the next year more manageable.',y)
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
sheet.save(OUT/'first-home-contact-sheet.jpg',quality=90)
text='\n'.join(p.get_text()for p in doc)
fields=sum(len(list(p.widgets() or []))for p in doc)
assert fields==95,fields
for p in doc:
 for block in p.get_text('blocks'):
  assert block[0]>=25 and block[2]<=W-24,(p.number,block)
  assert block[1]>=15 and block[3]<=H-15,(p.number,block)
assert len(doc.get_toc())==21
report=dict(pages=len(doc),fillable_fields=fields,chapters=len(doc.get_toc()),word_count=len(text.split()),sha256=hashlib.sha256(pdf.read_bytes()).hexdigest(),preview_physical_pages=[7,8,9],edition='2026-10-25')
(OUT/'first-home-validation.json').write_text(json.dumps(report,indent=2));print(json.dumps(report))

# Rebuild the server-bundled entitlement-gated bytes along with the review PDF.
route=(ROOT/'functions/api/download-mini-guide.js').read_text()
route=re.sub(r'const PDF_BASE64 = "[^"]+";', 'const PDF_BASE64 = "'+base64.b64encode(pdf.read_bytes()).decode()+'";',route,count=1)
route=route.replace('project-quote-mini-workbook','first-time-homeowner-cost-maintenance-handbook').replace('This purchase does not include this workbook.','This purchase does not include this book.')
(ROOT/'functions/api/download-first-home-handbook.js').write_text(route)
