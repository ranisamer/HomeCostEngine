import fs from 'node:fs';
import vm from 'node:vm';
import assert from 'node:assert/strict';
const src=fs.readFileSync(new URL('../functions/_middleware.js',import.meta.url),'utf8');
const ctx={URL,Response,exports:{}};vm.runInNewContext(src.replace('export async function onRequest','exports.onRequest = async function onRequest'),ctx);
for(const path of ['/output','/output/pdf/solar-quote-comparison-workbook.pdf','/%6futput/pdf/change-order-cost-control-workbook.pdf']){
 let called=false;const r=await ctx.exports.onRequest({request:new Request('https://homecostengine.com'+path),next:async()=>{called=true;return new Response('unexpected')}});
 assert.equal(r.status,404);assert.equal(called,false);assert.equal(r.headers.get('cache-control'),'private, no-store');
}
let called=false;const r=await ctx.exports.onRequest({request:new Request('https://homecostengine.com/assets/books/solar-quote-comparison-workbook/cover.webp'),next:async()=>{called=true;return new Response('public image',{headers:{'content-type':'image/webp'}})}});assert.equal(called,true);assert.equal(await r.text(),'public image');
console.log('PASS: direct build artifacts denied before static lookup; public cover unaffected. Paid routes are tested separately.');
