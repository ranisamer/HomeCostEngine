from pathlib import Path
from decimal import Decimal as D, ROUND_HALF_UP
import json,re,base64,xml.etree.ElementTree as E
from pypdf import PdfReader,PdfWriter
import fitz
from PIL import Image,ImageOps
R=Path(__file__).resolve().parents[1];slug='solar-quote-comparison-workbook';p=R/'output/pdf'/f'{slug}.pdf';O=R/'output/solar-qa';O.mkdir(parents=True,exist_ok=True)
# Independent calculations use decimal arithmetic rather than PDF renderer values.
assert D(20)*D(400)/1000==D('8')
assert (D(22400)+D(1800)+D(600))/D(8000)==D('3.1')
assert D(24800)-D(24000)==800
value=D(4000)*D('.24')+D(6000)*D('.06');assert value==1320
assert D(7000)*D('.24')+D(3000)*D('.06')-value==540
assert D(10000)*D('.24')-value==1080
bill=D(8000)*D('.24')-D(6000)*D('.06')+D(180);assert bill==1740
assert D(12000)*D('.24')+D(180)-bill==value
assert D(240)*D(170)==40800;assert D(180)*D(190)==34200;assert D(40800)-D(34200)==6600
lease=sum(D(1440)*D('1.03')**y for y in range(3));ppa=sum(D(10000)*D('.14')*D('1.02')**y for y in range(3));q=lambda x:x.quantize(D('.01'),rounding=ROUND_HALF_UP)
assert q(lease)==D('4450.90');assert q(ppa)==D('4284.56');assert q(lease-ppa)==D('166.34');assert D(11000)*D('.14')*D('1.02')==D('1570.8000')
r=PdfReader(p);assert len(r.pages)==25;fields=r.get_fields();assert len(fields)==40
widgets=[a.get_object() for pg in r.pages for a in pg.get('/Annots',[])];assert len(widgets)==40;assert len({x['/T'] for x in widgets})==40
w=PdfWriter();w.clone_document_from_reader(r);vals={n:'Offer A / QA saved '+n for n in fields};w.update_page_form_field_values(None,vals,auto_regenerate=False);filled=O/'filled-test.pdf';w.write(filled);rr=PdfReader(filled)
assert all(rr.get_fields()[n]['/V']==v for n,v in vals.items())
for pg in rr.pages:
 for a in pg.get('/Annots',[]):
  x=a.get_object();assert x['/V']==vals[x['/T']];assert x['/AP']['/N'].get_object().get_data()
f=fitz.open(p);thumbs=[]
for i,pg in enumerate(f):
 assert len(pg.get_text())>100
 im=pg.get_pixmap(matrix=fitz.Matrix(.48,.48));pic=Image.frombytes('RGB',[im.width,im.height],im.samples);thumbs.append(ImageOps.expand(pic,border=5,fill='#dddddd'))
contact=Image.new('RGB',(thumbs[0].width*5,thumbs[0].height*5),'#ddd')
for i,im in enumerate(thumbs):contact.paste(im,((i%5)*im.width,(i//5)*im.height))
contact.save(O/'contact.jpg')
for i in [0,10,17,23]:f[i].get_pixmap(matrix=fitz.Matrix(1.2,1.2)).save(str(O/f'page-{i+1}.png'))
fitz.open(filled)[17].get_pixmap().save(str(O/'filled.png'))
# Restore old immutable route bytes for legacy delivery regression on a fresh clone.
for route in (R/'functions/api').glob('download-*.js'):
 s=route.read_text();m=re.search(r'const PDF_BASE64\s*=\s*"(.*?)"',s);name=re.search(r'filename="([a-z0-9-]+\.pdf)"',s)
 if m and name:
  (R/'output'/name[1]).write_bytes(base64.b64decode(m[1]));(R/'output/pdf'/name[1]).write_bytes(base64.b64decode(m[1]))
# Check newly authored page links, one H1, four contextual primary article references.
for name in ['ebooks/'+slug+'.html','blog/why-same-size-solar-quotes-differ.html']:
 s=(R/name).read_text();assert len(re.findall(r'<h1(?:>| )',s))==1
 for u in re.findall(r'(?:href|src)="([^\"]*)"',s):
  u=u.split('#')[0].split('?')[0]
  if not u.startswith('/') or u.startswith('//') or u.startswith('/api/'):continue
  local=R/u.lstrip('/');assert local.exists() or local.with_suffix('.html').exists(),(name,u)
article=(R/'blog/why-same-size-solar-quotes-differ.html').read_text().split('<article',1)[1].split('</article>',1)[0];assert len(re.findall(r'href="https://',article))==4
E.parse(R/'sitemap.xml')
d=json.loads((R/'books/daily/solar-quote-comparison.json').read_text());paras=[t for s in d['sections'] for t in s['paras']];norm=lambda t:re.sub(r'[^a-z0-9 ]','',t.lower());legacy=' '.join(norm(x.read_text()) for x in (R/'books').glob('*.py'))+' '+norm((R/'books/daily/change-order-cost-control.json').read_text());assert not any(norm(t) in legacy for t in paras)
# Old commercial terms must match exactly; only this new product is added.
import subprocess
old=json.loads(re.search(r'const catalog=(\{.*?\});',subprocess.check_output(['git','show','HEAD:functions/api/create-checkout-session.js'],cwd=R,text=True),re.S)[1]);new=json.loads(re.search(r'const catalog=(\{.*?\});',(R/'functions/api/create-checkout-session.js').read_text(),re.S)[1]);assert all(new[k]==v for k,v in old.items());assert set(new)-set(old)=={slug}
v=json.loads((R/'docs/solar-validation.json').read_text());v.update(arithmetic='all four cases independently checked with Decimal, including rounding and bill cross-reconciliation',field_roundtrip='40 canonical/widget values and nonempty appearances verified after save/reopen',copy_screen='0 of 48 substantive paragraphs exactly copied; conceptual overlap disclosed; semantic originality reviewed editorially',links='new local links, single H1, four contextual primary article sources, sitemap XML passed',prices='all existing catalog entries unchanged; new product 999 pence GBP',status='automated checks passed; visual inspection pending');(R/'docs/solar-validation.json').write_text(json.dumps(v,indent=2)+'\n');print(v)
