"""Build a reviewed JSON manuscript, interactive PDF, real previews and gated route.
Usage: python scripts/build_daily_workbook.py books/daily/solar-quote-comparison.json
"""
from pathlib import Path
import json,base64,hashlib,html,re,sys
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pypdf import PdfReader
import fitz
R=Path(__file__).resolve().parents[1];d=json.loads((R/sys.argv[1]).read_text());slug=d['slug'];N=2+len(d['sections'])+len(d['worksheets'])+3;F=sum(len(x[1]) for x in d['worksheets'])
O=R/'output/pdf';O.mkdir(parents=True,exist_ok=True);A=R/'assets/books'/slug;A.mkdir(parents=True,exist_ok=True)
for n,f in [('Body','DejaVuSans.ttf'),('Bold','DejaVuSans-Bold.ttf')]:pdfmetrics.registerFont(TTFont(n,'/usr/share/fonts/truetype/dejavu/'+f))
W,H=612,792;L=55;width=502;p=O/(slug+'.pdf');c=canvas.Canvas(str(p),pagesize=(W,H),invariant=1);c.setTitle(d['title']);c.setAuthor('HomeCostEngine Editorial Team');c.setSubject('Original U.S. homeowner decision workbook; '+d['date'])
navy=colors.HexColor('#162d3b');teal=colors.HexColor('#147b78');muted=colors.HexColor('#52656e');page=0
styles={k:ParagraphStyle(k,fontName='Bold' if k=='title' else 'Body',fontSize=z,leading=lead,textColor=navy) for k,z,lead in [('body',10.5,16.5),('title',25,32),('small',8.7,13)]}
def para(t,y,kind='body'):
 q=Paragraph(html.escape(t),styles[kind]);_,h=q.wrap(width,1000);assert y-h>55,(page,t[:40],y-h);q.drawOn(c,L,y-h);return y-h-17
def begin(t,label='METHOD'):
 global page
 page+=1;c.setFillColor(teal);c.rect(0,H-11,W,11,fill=1,stroke=0);c.setFillColor(muted);c.setFont('Body',8);c.drawString(L,H-43,'HOME COST ENGINE  /  SOLAR COMPARISONS  /  '+label);c.drawString(L,30,'Personal planning aid | Original edition | October 27, 2026');c.drawRightString(W-L,30,str(page));c.bookmarkPage('p'+str(page));c.addOutlineEntry(t,'p'+str(page),0);return para(t,H-74,'title')-12
def end():c.showPage()
y=begin(d['title'],'OWNER WORKBOOK');y=para(d['subtitle'],y);y-=15
# Original code-native cover: an abstract comparison of three panel arrays, not an installation diagram.
for k in range(3):
 x=L+k*170;c.setStrokeColor(teal);c.setLineWidth(.8)
 for row in range(2):
  for col in range(3):c.rect(x+col*37,y-row*23,31,18,fill=0,stroke=1)
y-=84
for t in d['cover_lines']:y=para(t,y)-8
para('For U.S. homeowners comparing actual offers. '+str(N)+' pages. Store price £'+f"{d['price_pence']/100:.2f}"+' GBP; project examples use hypothetical USD.',y-8,'small');end()
y=begin('Your comparison packet','START HERE');y=para('Reader outcome: '+d['outcome'],y)
for t in d['intro']:y=para(t,y,'small')
end()
for s in d['sections']:
 y=begin(s['title'])
 for t in s['paras']:y=para(t,y)
 end()
for i,(t,fields) in enumerate(d['worksheets'],1):
 y=begin(t,'WORKSHEET '+str(i));y=para('Use consistent offer IDs. Record evidence and units. Add dated attachments for detailed schedules; these fields do not calculate.',y,'small')
 for j,f in enumerate(fields):
  y=para(f,y,'small');assert y-57>55,(page,f)
  c.acroForm.textfield(name=f'w{i}_{j}',tooltip=f,fontName='Helvetica',fontSize=10,x=L,y=y-57,width=width,height=57,fieldFlags='multiline',borderColor=colors.HexColor('#bacccd'),fillColor=colors.HexColor('#f6f9f9'),textColor=navy,forceBorder=True);y-=74
 end()
y=begin('Questions for your providers','COPY-READY')
for i,t in enumerate(d['questions'],1):y=para(str(i)+'. '+t,y,'small')
end()
y=begin('Primary sources and boundaries','SOURCE NOTES');y=para(d['source_limits'],y,'small')
for name,url,note in d['sources']:
 y=para(name+': '+note,y,'small');y=para(url,y,'small')
para(d['overlap'],y,'small');end()
y=begin('Before you rank the offers','FINAL REVIEW')
for t in d['final_checks']:y=para(t,y)
end();assert page==N;c.save();r=PdfReader(p);assert len(r.pages)==N;assert len(r.get_fields())==F
widgets=[a.get_object() for pg in r.pages for a in pg.get('/Annots',[])];assert len(widgets)==F;assert all(x.get('/AP') for x in widgets)
f=fitz.open(p)
for n,name in [(0,'cover'),(4,'page-1'),(6,'page-2'),(17,'page-3')]:
 pix=f[n].get_pixmap(matrix=fitz.Matrix(1.3,1.3));pix.pil_save(str(A/(name+'.webp')))
route=(R/'functions/api/download-quote-playbook.js').read_text();route=re.sub(r'const PDF_BASE64 = ".*?";',lambda _: 'const PDF_BASE64 = "'+base64.b64encode(p.read_bytes()).decode()+'";',route);route=route.replace('contractor-quote-comparison-playbook',slug);(R/('functions/api/'+d['route']+'.js')).write_text(route)
checks={'pages':N,'fields':F,'widgets':len(widgets),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'sources_checked':d['date'],'status':'built; arithmetic, saved-field and visual QA pending'};(R/'docs/solar-validation.json').write_text(json.dumps(checks,indent=2)+'\n');print(checks)
