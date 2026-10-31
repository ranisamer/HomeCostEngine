"""Replayable artifact, arithmetic, price and link checks. No external requests."""
from pathlib import Path
from decimal import Decimal as D
import json,re,base64,hashlib,textwrap,xml.etree.ElementTree as E
from pypdf import PdfReader,PdfWriter
import fitz
from PIL import Image,ImageOps
R=Path(__file__).resolve().parents[1];slug='garage-conversion-decision-workbook';p=R/'output/pdf'/f'{slug}.pdf';O=R/'output/garage-qa';O.mkdir(parents=True,exist_ok=True)
gross=D(22)*D(20);room=gross-D(40)-D(60);assert gross==440 and room==340;assert D(44880)/gross==102;assert D(44880)/room==132
a=D(650)+D(350)+24*D(95);b=D(350)+24*D(185);assert a==3280 and b==4790 and b-a==1510
total=D(1400)+D(3600)+D(1800)+D(42000)+a;assert total==52080;assert D(55000)-total==2920;assert total+D(3500)==55580;assert total+D(3500)-D(55000)==580
assert max(D(2),D(3))+D(2)+D(4)+D(6)==15;assert max(D(2),D(3))+D(2)+D(7)+D(6)==18;assert D(2)+D(3)+D(2)+D(4)+D(6)==17
r=PdfReader(p);assert len(r.pages)==26;assert len(r.get_fields())==35;assert len(r.outline)==26
text=' '.join(' '.join(pg.extract_text() for pg in r.pages).split());assert all(s in text for s in ['440 square feet','340 square feet','$3,280','$4,790','$52,080','$55,580','18 weeks'])
uris=[a.get_object().get('/A',{}).get('/URI') for pg in r.pages for a in pg.get('/Annots',[])];assert sum(bool(x) for x in uris)==4
for i in [14,15]:assert 'Invented record' in r.pages[i].extract_text()
widgets=[a.get_object() for pg in r.pages for a in pg.get('/Annots',[]) if a.get_object().get('/Subtype')=='/Widget'];assert len(widgets)==35;assert len({x['/T'] for x in widgets})==35;assert all(x['/MaxLen']==1000 for x in widgets)
w=PdfWriter();w.clone_document_from_reader(r);vals={n:'QA / saved '+n+'\n'+textwrap.fill('Owner scenario: selected overnight services. Inputs are assumed for this test. Ask the qualified provider to confirm starting capability, circuit coverage and the AC-available energy boundary.',width=80) for n in r.get_fields()};w.update_page_form_field_values(None,vals,auto_regenerate=False);filled=O/'filled-test.pdf';w.write(filled);rr=PdfReader(filled);assert all(rr.get_fields()[n]['/V']==v for n,v in vals.items())
for pg in rr.pages:
 for a in pg.get('/Annots',[]):
  x=a.get_object()
  if x.get('/Subtype')!='/Widget':continue
  assert x['/V']==vals[x['/T']];assert x['/AP']['/N'].get_object().get_data()
f=fitz.open(p);thumbs=[]
for pg in f:
 assert len(pg.get_text())>100
 pix=pg.get_pixmap(matrix=fitz.Matrix(.45,.45));im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples);thumbs.append(ImageOps.expand(im,border=5,fill='#ddd'))
contact=Image.new('RGB',(thumbs[0].width*5,thumbs[0].height*6),'#ddd')
for i,im in enumerate(thumbs):contact.paste(im,((i%5)*im.width,(i//5)*im.height))
contact.save(O/'contact.jpg')
for i in [4,7,10,14,15,24]:f[i].get_pixmap(matrix=fitz.Matrix(1.2,1.2)).save(str(O/f'page-{i+1}.png'))
fitz.open(filled)[21].get_pixmap().save(str(O/'filled.png'))
for route in (R/'functions/api').glob('download-*.js'):
 s=route.read_text();m=re.search(r'const PDF_BASE64\s*=\s*"(.*?)"',s);name=re.search(r'filename="([a-z0-9-]+\.pdf)"',s)
 if m and name:
  data=base64.b64decode(m[1]);(R/'output'/name[1]).write_bytes(data);(R/'output/pdf'/name[1]).write_bytes(data)
for name in ['ebooks/'+slug+'.html','blog/questions-before-budgeting-garage-conversion.html']:
 s=(R/name).read_text();assert len(re.findall(r'<h1(?:>| )',s))==1
 for u in re.findall(r'(?:href|src)="([^\"]*)"',s):
  u=u.split('#')[0].split('?')[0]
  if not u.startswith('/') or u.startswith('//') or u.startswith('/api/'):continue
  local=R/u.lstrip('/');assert local.exists() or local.with_suffix('.html').exists(),(name,u)
article=(R/'blog/questions-before-budgeting-garage-conversion.html').read_text().split('<article',1)[1].split('</article>',1)[0];assert len(re.findall(r'href="https://',article))==3;E.parse(R/'sitemap.xml')
d=json.loads((R/'books/daily/garage-conversion.json').read_text());paras=[t for s in d['sections'] for t in s['paras']];norm=lambda t:re.sub(r'[^a-z0-9 ]','',t.lower());legacy=' '.join(norm(x.read_text()) for x in (R/'books').rglob('*') if x.is_file() and x.suffix in ['.py','.json'] and x.name!='garage-conversion.json');assert not any(norm(t) in legacy for t in paras)
prior=json.loads((R/'docs/garage-price-baseline.json').read_text());cat=json.loads(re.search(r'const catalog=(\{.*?\});',(R/'functions/api/create-checkout-session.js').read_text(),re.S)[1]);assert set(prior['amounts'])<=set(cat);assert slug in cat;assert all(cat[k]['amount']==v for k,v in prior['amounts'].items());assert cat[slug]['amount']==999
v=json.loads((R/'docs/garage-validation.json').read_text());v.update(sha256=hashlib.sha256(p.read_bytes()).hexdigest(),arithmetic='all 4 cases independently recomputed with Decimal: area denominators, displaced storage, revised budget gap and parallel schedule',field_roundtrip='35 canonical and widget values over 100 characters, saved appearances, 1,000-character limits, 4 URL links and 26 outline entries verified',demonstrations='two labeled completed records use the five prompts of worksheets 3 and 6; no actual customer data',copy_screen='0 of 36 substantive paragraphs exactly copied from existing manuscript files; semantic originality assessed editorially',links='new local links, one H1, three primary article references, sitemap XML passed',prices='all 25 prior catalog amounts preserved against immutable recorded baseline; 999 pence for new product');v.setdefault('status','automated QA passed; visual inspection pending');(R/'docs/garage-validation.json').write_text(json.dumps(v,indent=2)+'\n');print(v)
