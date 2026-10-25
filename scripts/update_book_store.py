#!/usr/bin/env python3
"""Apply a reviewed manuscript's STORE metadata to its storefront and catalogs.
Run with a books/*.py path. Keeps the existing server-controlled product price.
The series template is the reviewed contractor comparison page, not a mock PDF.
"""
from pathlib import Path
from html import escape
import re,json,runpy,sys
ROOT=Path(__file__).resolve().parents[1]
module=runpy.run_path(str(ROOT/sys.argv[1]));b=module['STORE']
slug=b['slug'];title=b['title'];amount=b['amount'];price=f'{amount/100:.2f}';display=price.removesuffix('.00')
old='contractor-quote-comparison-playbook';oldtitle='Contractor Quote Comparison Playbook'
s=(ROOT/f'ebooks/{old}.html').read_text().replace(old,slug).replace(oldtitle,escape(title)).replace('£9','£'+display)
s=s.replace('<span class="eyebrow">Contractor Comparisons</span>','<span class="eyebrow">'+escape(b['category'])+'</span>')
old_desc='A 64-page contractor comparison playbook with 19 worked examples and 19 fillable worksheets. Match scope, normalize allowances, review evidence and compare payment and schedule assumptions.'
s=s.replace(old_desc,escape(b['description'],quote=True))
benefits='<section class="book-value" aria-labelledby="why-buy"><span class="eyebrow">'+escape(b['eyebrow'])+'</span><h2 id="why-buy">'+escape(b['why_title'])+'</h2><p>'+escape(b['why'])+'</p><ul class="ebook-checks">'
benefits+=''.join('<li><strong>'+escape(a)+'</strong> '+escape(c)+'</li>' for a,c in b['benefits'])+'</ul>'
benefits+='<h3>Who will get the most from it?</h3><p>'+escape(b['reader'])+'</p><h3>'+escape(b['difference_title'])+'</h3><p>'+escape(b['difference'])+'</p>'
benefits+='<p><a class="btn" href="#sample-pages">See the real pages first →</a> <a class="card-link" href="#buy-book">Get the complete PDF for £'+display+' →</a></p><p class="micro">'+escape(b['limits'])+'</p></section>'
s=re.sub(r'<section class="book-value".*?</section>',lambda _:benefits,s,flags=re.S)
helps='<h2>What this guide helps you do</h2><ul class="ebook-checks">'+''.join('<li>'+escape(x)+'</li>' for x in b['helps'])+'</ul>'
s=re.sub(r'<h2>What this guide helps you do</h2>.*?</ul>',lambda _:helps,s,flags=re.S)
s=s.replace('common bidder requests, scope and allowance checks, provider evidence, schedule and payment comparison, decisions and accepted documents',escape(b['sequence']))
example='<h3>Try the method before buying</h3><p>'+escape(b['example'])+'</p>'+b['calculator_html']+'<h3>Complete chapter list</h3>'
s=re.sub(r'<h3>Try the method before buying</h3>.*?<h3>Complete chapter list</h3>',lambda _:example,s,flags=re.S)
chapters=['Preface: how to use this book']+[c['title'] for c in module['CHAPTERS']]+['Afterword and source notes']
assert len(chapters)==21
s=re.sub(r'<ol class="ebook-chapter-list">.*?</ol>',lambda _:'<ol class="ebook-chapter-list">'+''.join('<li>'+escape(x)+'</li>' for x in chapters)+'</ol>',s,flags=re.S)
s=re.sub(r'<h3>What the examples cover</h3>.*?<h3>What you receive after payment</h3>',lambda _:'<h3>What the examples cover</h3><p>'+escape(b['examples'])+'</p><h3>What you receive after payment</h3>',s,flags=re.S)
sources='Source notes link to '+', '.join('<a href="'+escape(url,quote=True)+'" target="_blank" rel="noopener">'+escape(name)+'</a>' for _,name,url in module['SOURCES'])+'. These organizations do not endorse the book.'
s=re.sub(r'Source notes link to .*?These organizations do not endorse the book\.',lambda _:sources,s)
s=s.replace('v=20261025-book10','v=20261025-book'+str(b['number']))
mt=re.search(r'<script type="application/ld\+json">(.*?)</script>',s,re.S);data=json.loads(mt[1]);data.update(name=title,description=b['description']);data['offers']['price']=price
s=s[:mt.start(1)]+json.dumps(data,separators=(',',':'),ensure_ascii=False)+s[mt.end(1):]
(ROOT/f'ebooks/{slug}.html').write_text(s.rstrip()+'\n')
for file in ['functions/api/create-checkout-session.js','functions/api/verify-purchase.js']:
 p=ROOT/file;s=p.read_text();mt=re.search(r'const catalog=(\{.*?\});',s,re.S);data=json.loads(mt[1]);data[slug].update(title=title,download=b['route'])
 if 'create-checkout' in file:
  assert data[slug]['amount']==amount,'Changing a product price requires an explicit separate decision'
  data[slug].update(desc=b['description'],pages=64)
 s=s[:mt.start(1)]+json.dumps(data,separators=(',',':'),ensure_ascii=False)+s[mt.end(1):];p.write_text(s)
p=ROOT/'ebooks/index.html';s=p.read_text()
def card(mt):
 c=mt[0]
 if f'/ebooks/{slug}.html' not in c:return c
 c=c.replace('<article class="book-card">','<article class="book-card" data-actual-edition="2026-10-25">')
 c=re.sub(r'<div class="book-card-rating".*?</div>','<p class="micro">Original edition · 19 fillable worksheets</p>',c,flags=re.S)
 c=re.sub(r'(<img )src="[^"]+"',lambda x:x[1]+'src="/assets/books/'+slug+'/cover.webp"',c,count=1)
 c=re.sub(r'(<h2><a[^>]*>).*?(</a></h2>)',lambda x:x[1]+escape(title)+x[2],c,flags=re.S)
 return re.sub(r'\b\d+-page','64-page',c)
s=re.sub(r'<article class="book-card".*?</article>',card,s,flags=re.S);p.write_text(s)
test=(ROOT/'scripts/test_quote_delivery.mjs').read_text().replace(old,slug).replace('download-quote-playbook',b['route'].split('/')[-1])
test=test.replace("s===slug?'900':'50'",f"s===slug?'{amount}':'50'").replace("schema.offers.price,'9.00'",f"schema.offers.price,'{price}'").replace('£9 GBP/64-page','£'+display+' GBP/64-page')
(ROOT/b['test']).write_text(test)
print('Updated reviewed product:',slug,'price preserved:',price,'GBP')
