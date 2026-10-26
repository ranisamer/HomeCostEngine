from pathlib import Path
import json,base64,hashlib,html
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import fitz
from pypdf import PdfReader
R=Path(__file__).resolve().parents[1];d=json.loads((R/'books/daily/change-order-cost-control.json').read_text());slug=d['slug']
O=R/'output/pdf';O.mkdir(parents=True,exist_ok=True);A=R/'assets/books'/slug;A.mkdir(parents=True,exist_ok=True)
for n,f in [('Body','DejaVuSans.ttf'),('Bold','DejaVuSans-Bold.ttf')]:pdfmetrics.registerFont(TTFont(n,'/usr/share/fonts/truetype/dejavu/'+f))
W,H=612,792;L=55;width=502;p=O/(slug+'.pdf');c=canvas.Canvas(str(p),pagesize=(W,H),invariant=1);c.setTitle(d['title']);c.setAuthor('HomeCostEngine Editorial Team')
navy=colors.HexColor('#162d3b');teal=colors.HexColor('#147b78');muted=colors.HexColor('#52656e');page=0
styles={k:ParagraphStyle(k,fontName='Bold' if k=='title' else 'Body',fontSize=z,leading=lead,textColor=navy) for k,z,lead in [('body',10.5,16.5),('title',25,32),('small',9,14)]}
def para(t,y,kind='body'):
 q=Paragraph(html.escape(t),styles[kind]);_,h=q.wrap(width,1000);assert y-h>55,(page,t[:40],y-h);q.drawOn(c,L,y-h);return y-h-17
def begin(t,label='METHOD'):
 global page
 page+=1;c.setFillColor(teal);c.rect(0,H-11,W,11,fill=1,stroke=0);c.setFillColor(muted);c.setFont('Body',8);c.drawString(L,H-43,'HOME COST ENGINE  /  CHANGE CONTROL  /  '+label);c.drawString(L,30,'Personal planning aid | Original edition | October 26, 2026');c.drawRightString(W-L,30,str(page));return para(t,H-74,'title')-12
def end():c.showPage()
y=begin(d['title'],'OWNER WORKBOOK');y=para('From a changed scope to a checked price and a traceable decision.',y);y-=20
for t in ['3 complete worked cases','6 reusable worksheets / 30 fillable fields','Credits, quantities, revisions, timing and invoice checks']:
 c.setFillColor(teal);c.rect(L,y-37,width,2,fill=1,stroke=0);y=para(t,y-5)-25
y=para('For U.S. homeowners reviewing changes during an existing project. Hypothetical project amounts use USD; the store price is £9.99 GBP.',y,'small');end()
y=begin('Your route through this workbook','START HERE')
for t in ['Reader outcome: produce one change-review packet that connects baseline evidence, scope difference, net price, approval status, funding exposure and later billing. If evidence is missing, leave with precise provider questions rather than a false final number.','Read pages 3-13 for the method and three checked cases. Complete worksheets on pages 14-19. Copy the provider questions on page 20. Use page 21 for source boundaries and page 22 for the final review.','First edition. Original text, cases and worksheet wording © 2026 HomeCostEngine. Personal use includes printing pages and sharing your completed records with your own contractors and advisers; redistribution or resale of the blank book is not permitted.','This workbook does not authorize work, determine legal liability, provide a technical specification or replace a professional assessment. No customer trial, guaranteed savings or validated purchase demand is claimed.']:
 y=para(t,y)
end()
for s in d['sections']:
 y=begin(s['title'])
 for t in s['paras']:y=para(t,y)
 end()
assert page==13
for i,(t,fields) in enumerate(d['worksheets'],1):
 y=begin(t,'WORKSHEET '+str(i));y=para('Use one change ID throughout. Enter concise notes and evidence references; attach supporting records separately. Fields do not calculate.',y,'small')
 for j,f in enumerate(fields):
  y=para(f,y,'small')
  c.acroForm.textfield(name=f'w{i}_{j}',tooltip=f,fontName='Helvetica',fontSize=10,x=L,y=y-57,width=width,height=57,fieldFlags='multiline',borderColor=colors.HexColor('#bacccd'),fillColor=colors.HexColor('#f6f9f9'),textColor=navy,forceBorder=True)
  y-=74
 end()
y=begin('Questions to send your provider','COPY-READY')
for i,t in enumerate(d['questions'],1):y=para(str(i)+'. '+t,y,'small')
end()
y=begin('Sources and boundaries','SOURCE NOTES')
y=para('Primary sources checked October 26, 2026. Their guidance supports limited factual context; our arithmetic, decision sequence and worksheets are independently authored. No source endorses this book.',y)
for name,url,note in d['sources']:
 y=para(name+': '+note,y,'small');y=para(url,y,'small')
y=para('FTC informs the written-estimate and recordkeeping discussion. CSLB informs only the labeled California approval example. The Mississippi board guide informs the record categories in the invoice and handover discussion. Local requirements vary; verify the rules applicable to your home and agreement.',y)
y=para('Overlap: existing HomeCostEngine general budget and contractor comparison books include introductory change concepts. No prose or worked case is copied from them here. The distinct output is an in-project change-review packet rather than initial quote selection. The related free article gives one checklist and one case; this book adds the full record set and two further cases.',y)
end()
y=begin('Before you treat a number as final','FINAL REVIEW')
for t in ['Can another person find the baseline and the exact revision used? Keep source files unchanged and cross-reference the accepted evidence.','Does the net price include supported credits and each shared cost only once? Check the base of every percentage and the quoted tax treatment.','Have you separated accepted value, pending exposure, owner-only costs and payment timing? Do not mistake scenario headroom for cash available on a due date.','Is the required approval evidence complete under the actual agreement and local process? An owner worksheet is not a signed change order.','Can you match the next invoice to the accepted change and identify prior billing? Record open issues and seek appropriate help for disputes.','Save the completed PDF, close it and reopen it to test field persistence. Keep a blank master. Preview before printing and use actual-size printing if your reader scales pages unexpectedly.','Continue with the free companion checklist: https://homecostengine.com/blog/check-contractor-change-order-price . Keep the book only if its workflow is useful for your particular decision.']:
 y=para(t,y)
end();assert page==22;c.save()
r=PdfReader(p);assert len(r.pages)==22;assert len(r.get_fields())==30
widgets=[a.get_object() for pg in r.pages for a in pg.get('/Annots',[])];assert len(widgets)==30;assert all(x.get('/AP') for x in widgets)
f=fitz.open(p)
for n,name in [(0,'cover'),(6,'page-1'),(9,'page-2'),(15,'page-3')]:
 pix=f[n].get_pixmap(matrix=fitz.Matrix(1.3,1.3));pix.pil_save(str(A/(name+'.webp')))
route=(R/'functions/api/download-quote-playbook.js').read_text();import re
route=re.sub(r'const PDF_BASE64 = ".*?";',lambda _: 'const PDF_BASE64 = "'+base64.b64encode(p.read_bytes()).decode()+'";',route)
route=route.replace('contractor-quote-comparison-playbook',slug);(R/'functions/api/download-change-order-workbook.js').write_text(route)
checks={'pages':22,'fields':30,'widgets':30,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'cases':{'substitution':814,'quantity_low':1010.88,'quantity_high':1237.68,'forecast':44174.88,'gap':950},'sources_checked':'2026-10-26','status':'built; layout and saved-field QA pending'}
(R/'docs/change-order-validation.json').write_text(json.dumps(checks,indent=2)+'\n');print(checks)
