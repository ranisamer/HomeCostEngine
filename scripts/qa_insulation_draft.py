from pathlib import Path
from decimal import Decimal as D,ROUND_CEILING
import json,re,hashlib,base64,textwrap
from pypdf import PdfReader,PdfWriter
from PIL import Image,ImageOps
import fitz
R=Path(__file__).resolve().parents[1];slug='insulation-quote-scope-workbook';p=R/'output/pdf'/f'{slug}.pdf';O=R/'output/insulation-qa';O.mkdir(parents=True,exist_ok=True)
excluded=D(100)+D(150)-D(40);assert excluded==210 and D(1250)-excluded==1040
coverage=D(34)*D(28);assert coverage==952 and D(1000)-coverage==48
assert (D(1000)/D(28)).to_integral_value(rounding=ROUND_CEILING)==36;assert D(36)*28==1008
assert D(420)*D('1.10')==462 and max(D(600),D(462))==600;assert D(600)-575==25 and D(575)-462==113
a=D(2080)+D(360)+D(240)+D(180);assert a==2860 and a-2750==110
delta=D(300)-D(180);assert delta==120 and a+delta==2980 and D(2750)+delta==2870
r=PdfReader(p);assert len(r.pages)==25 and len(r.get_fields())==30 and len(r.outline)==25
text=' '.join(' '.join(pg.extract_text() for pg in r.pages).split());assert all(x in text for x in ['DRAFT','1,040','952','1,008','$2,980','$2,870'])
widgets=[a.get_object() for pg in r.pages for a in pg.get('/Annots',[]) if a.get_object().get('/Subtype')=='/Widget'];assert len(widgets)==30 and len({w['/T'] for w in widgets})==30;assert all(w['/MaxLen']==1000 for w in widgets)
w=PdfWriter();w.clone_document_from_reader(r);values={n:'QA saved '+n+'\n'+textwrap.fill('Zone I-01: provider drawing pending. Confirm product and installed-result basis, retained material and completion evidence. These entries test persistence and are not actual customer records.',width=78) for n in r.get_fields()};w.update_page_form_field_values(None,values,auto_regenerate=False);w.write(O/'filled.pdf');rr=PdfReader(O/'filled.pdf');assert all(rr.get_fields()[n]['/V']==v for n,v in values.items())
for pg in rr.pages:
 for ref in pg.get('/Annots',[]):
  x=ref.get_object()
  if x.get('/Subtype')=='/Widget':assert x['/V']==values[x['/T']] and x['/AP']['/N'].get_object().get_data()
f=fitz.open(p);thumbs=[]
for pg in f:
 pix=pg.get_pixmap(matrix=fitz.Matrix(.45,.45));thumbs.append(ImageOps.expand(Image.frombytes('RGB',[pix.width,pix.height],pix.samples),border=5,fill='#ddd'))
im=Image.new('RGB',(thumbs[0].width*5,thumbs[0].height*5),'#ddd')
for i,t in enumerate(thumbs):im.paste(t,((i%5)*t.width,(i//5)*t.height))
im.save(O/'contact.jpg')
for i in [4,6,8,10,14,15,23]:f[i].get_pixmap(matrix=fitz.Matrix(1.2,1.2)).save(str(O/f'page-{i+1}.png'))
fitz.open(O/'filled.pdf')[19].get_pixmap().save(str(O/'filled.png'))
d=json.loads((R/'books/daily/insulation-scope.json').read_text());ps=[t for s in d['sections'] for t in s['paras']];norm=lambda s:re.sub(r'[^a-z0-9 ]','',s.lower());old=' '.join(norm(q.read_text()) for q in (R/'books').rglob('*') if q.suffix in ['.json','.py'] and q.name!='insulation-scope.json');assert not any(norm(t) in old for t in ps)
catalog=json.loads(re.search(r'const catalog=(\{.*?\});',(R/'functions/api/create-checkout-session.js').read_text(),re.S)[1]);assert slug not in catalog
for name in ['ebooks/index.html','blog/index.html','sitemap.xml']:assert slug not in (R/name).read_text() and d['article'] not in (R/name).read_text()
for name in ['insulation-product.html','insulation-article.html']:
 s=(R/'books/drafts'/name).read_text();assert len(re.findall(r'<h1>',s))==1 and 'DRAFT' in s and '<button' not in s
 for link in re.findall(r'(?:href|src)="([^"]+)"',s):
  if link.startswith('/'):assert (R/link.lstrip('/')).exists() or (R/link.lstrip('/')).with_suffix('.html').exists(),link
article=(R/'books/drafts/insulation-article.html').read_text();assert len(re.findall('href="https://',article))==3
v=json.loads((R/'docs/insulation-validation.json').read_text());v.update(status='draft: arithmetic/fields/local files passed; visual and staging review pending',arithmetic='4 cases independently recomputed with Decimal including overlap, coverage ceiling, job minimum and net allowance',field_roundtrip='30 canonical/widget values and saved appearances; 25 outline entries; 1,000-character limits',originality='Zero exact copies among 36 method paragraphs; semantic originality requires editorial judgment',publication='Absent from live catalog, blog index and sitemap; no active checkout',sha256=hashlib.sha256(p.read_bytes()).hexdigest());(R/'docs/insulation-validation.json').write_text(json.dumps(v,indent=2)+'\n')
# Restore immutable existing artifacts for legacy mocks; do not commit static copies.
for q in (R/'functions/api').glob('download-*.js'):
 s=q.read_text();b=re.search(r'const PDF_BASE64\s*=\s*"(.*?)"',s);n=re.search(r'filename="([a-z0-9-]+\.pdf)"',s)
 if b and n:
  raw=base64.b64decode(b[1]);(R/'output'/n[1]).write_bytes(raw);(R/'output/pdf'/n[1]).write_bytes(raw)
print(v)
