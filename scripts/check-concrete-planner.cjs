const assert = require('node:assert/strict');
const { calculate } = require('../assets/concrete-planner.js');
const plan = () => ({version:2,zones:[{length:20,width:12,thickness:4}],edge:{enabled:false,width:12,depth:12},allowance:10,increment:.25,bagYield:.6,yardPrice:null,delivery:0,placement:0});
const near=(a,b)=>assert.ok(Math.abs(a-b)<1e-9,`${a} != ${b}`);
let p=plan(), r=calculate(p);
near(r.slabFeet,80);near(r.planningYards,88/27);near(r.orderYards,3.5);assert.equal(r.bags,147);assert.equal(r.deliveredCost,null);
p.yardPrice=160;p.delivery=75;r=calculate(p);near(r.deliveredCost,635);
p.edge.enabled=true;r=calculate(p);near(r.edgeFeet,40);near(r.netFeet,120);near(r.orderYards,5);assert.equal(r.bags,220);
p.edge.depth=4;r=calculate(p);near(r.edgeFeet,0);
p=plan();p.zones.push({length:10,width:10,thickness:4});r=calculate(p);near(r.netFeet,80+100/3);
p=plan();p.allowance=0;p.increment=0;r=calculate(p);near(r.orderYards,80/27);
p={...plan(),zones:[{length:9,width:9,thickness:4}],allowance:0,increment:.25};r=calculate(p);near(r.orderYards,1);assert.equal(r.bags,45);
p={...plan(),zones:[{length:9,width:9,thickness:4.000001}],allowance:0,increment:.25};r=calculate(p);near(r.orderYards,1.25);
p=plan();p.bagYield=.45;r=calculate(p);assert.equal(r.bags,196);
for(const mutate of [p=>p.zones[0].length=0,p=>p.zones[0].width=-1,p=>p.zones[0].thickness=NaN,p=>p.allowance=31,p=>p.increment=-.25,p=>p.bagYield=0,p=>p.yardPrice=-1,p=>p.delivery=-1,p=>p.placement=Infinity,p=>p.zones=[],p=>p.zones=Array(9).fill(p.zones[0]),p=>{p.edge.enabled=true;p.edge.depth=2},p=>{p.edge.enabled=true;p.edge.width=72}]){p=plan();mutate(p);assert.throws(()=>calculate(p),RangeError);}
p=plan();p.yardPrice=0;r=calculate(p);assert.equal(r.deliveredCost,0);
const immutable=JSON.stringify(p);calculate(p);assert.equal(JSON.stringify(p),immutable);
for(let i=1;i<=100;i++){p=plan();p.zones[0]={length:i/3,width:17.31,thickness:4.125};p.allowance=i%31;p.increment=.25;r=calculate(p);assert.ok(r.orderYards+1e-12>=r.planningYards);assert.ok(r.roundingYards<.25+1e-10);near(r.orderYards/.25,Math.round(r.orderYards/.25));}
console.log('PASS: geometry, non-overlapping perimeter corners, multiple sections, allowances, rounding boundaries, custom bag yields, optional/zero prices, invalid inputs, immutable inputs and 100 rounding scenarios.');
