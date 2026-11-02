const a=require('../assets/roof-project.js'),assert=require('node:assert');let count=0;
function ok(f){f();count++;}
let p=a.empty();p.quotes=[{name:'A',price:15000,extras:1800,unresolved:true,notes:'Remove layers'}, {name:'B',price:16500,extras:0,unresolved:false,notes:''},null];p.selected='0';p.budget=20000;p.reserve=1000;p.paid=3000;
p=a.normalize(p);ok(()=>assert.deepEqual(a.summary(p),{known:16800,cash:17800,unpaid:13800,remaining:14800,gap:2200,paidAboveKnown:false,unresolved:true}));
p.selected='1';ok(()=>assert.equal(a.summary(p).known,16500));p.paid=18000;ok(()=>assert(a.summary(p).paidAboveKnown));p.budget=null;ok(()=>assert.equal(a.summary(p).gap,null));p.selected='';ok(()=>assert.equal(a.summary(p),null));
for(const value of ['',-1,Infinity,NaN,100000001,'0.001',{},true])ok(()=>assert.throws(()=>a.amount(value)));
for(const value of [0,100000000,'0','1234.56'])ok(()=>assert(Number.isFinite(a.amount(value))));
ok(()=>assert.equal(a.amount('',true),null));ok(()=>assert.equal(a.amount(0,true),0));
for(const mutate of [p=>p.version=2,p=>p.name='',p=>p.quotes=[],p=>p.selected='7',p=>{p.selected='2';p.quotes[2]=null},p=>p.updatedAt='bad',p=>p.quotes[0].extras='',p=>p.quotes[0].price=-5,p=>p.reserve=-1,p=>p.snapshot={inputs:{}}]){
 const raw=JSON.parse(JSON.stringify(p));mutate(raw);ok(()=>assert.throws(()=>a.normalize(raw)));
}
let raw=JSON.parse(JSON.stringify(p));raw.email='secret@example.com';raw.quotes[0].phone='555';raw.unsubscribed=false;const clean=a.normalize(raw);ok(()=>assert(!('email'in clean)));ok(()=>assert(!('phone'in clean.quotes[0])));ok(()=>assert(!('unsubscribed'in clean)));ok(()=>assert.deepEqual(a.normalize(JSON.parse(JSON.stringify(clean))),clean));
console.log(count+' model assertions passed (arithmetic, zero, limits, invalid/malicious backup shapes, allowlist and roundtrip).');
