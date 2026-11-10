"""Film B « Trois onglets » : génère STORYBOARD.md et les 15 séquences (compositions/frames/*.html).

Un seul auteur, un seul décor : le kit du mur (../film-marque/reference/mur.html) + le kit B ci-dessous, recopiés à
l'identique dans chaque séquence. La continuité est garantie par construction :
- le fond et le groupe « caméra » G dérivent selon le temps GLOBAL du film (aucun saut aux coutures) ;
- chaque couture a un état unique (téléphone, cartes, carton, logo) écrit une fois et repris des deux côtés.
Usage : python3 build.py   (puis bash assemble.sh)
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
REF = os.path.join(HERE, "..", "film-marque", "reference", "mur.html")
ref = open(REF, encoding="utf-8").read().split("-->", 1)[1]
KIT_CSS = re.search(r'<style id="em-kit">(.*?)</style>', ref, re.S).group(1).replace("../assets/", "assets/")
KIT_JS = re.search(r'<script id="em-kit-js">(.*?)</script>', ref, re.S).group(1).replace("../assets/", "assets/")
KIT_JS = KIT_JS.replace('ease:"power2.out"},at)}', 'ease:"power2.out",autoRound:false},at)}')

B_CSS = r"""
.b-bg{position:absolute;left:0;top:0;width:1080px;height:1920px;transform-origin:540px 960px}
.b-full{position:absolute;inset:0}
.b-g{position:absolute;left:0;top:0;width:1080px;height:1920px;transform-origin:540px 800px}
.b-card{position:absolute;left:0;top:0;width:760px;height:420px;border-radius:24px;background:#fffdf9;box-shadow:0 30px 70px rgba(44,36,32,.22),0 3px 8px rgba(44,36,32,.12);transform-origin:0 0}
.b-photo{position:absolute;left:0;top:0;border-radius:24px 0 0 24px}
.b-vase{position:absolute;transform-origin:50% 100%}
.b-tt{position:absolute;left:290px;top:28px;font:600 30px/1.1 "Inter";white-space:nowrap}
.b-pr{position:absolute;left:290px;top:74px;font:600 32px/1 "Inter"}
.b-row{position:absolute;left:290px;width:440px;height:30px;font:500 24px/30px "Inter";color:rgba(44,36,32,.6);white-space:nowrap}
.b-row b{font-weight:600;color:#2c2420}
.b-val{position:absolute;left:125px;top:0;color:#2c2420;display:inline-block}
.b-val .q{color:#8c3b2e;font-weight:600}
.b-btn{position:absolute;left:290px;top:340px;width:260px;height:52px;border-radius:26px;background:#3a2f2a;color:#f5f0e8;font:600 22px/52px "Inter";text-align:center}
.b-chip{position:absolute;left:0;top:0;padding:16px 28px;border-radius:32px;background:#fffdf9;font:600 40px/1 "Inter";box-shadow:0 18px 40px rgba(44,36,32,.18);white-space:nowrap;opacity:0}
.b-box{position:absolute;left:0;top:0;width:440px;height:320px}
.b-box .in{position:absolute;left:14px;top:26px;width:412px;height:40px;background:#2c2420;border-radius:4px}
.b-box .body{position:absolute;left:0;top:40px;width:440px;height:280px;border-radius:8px;background:linear-gradient(#c8a074,#b38a5e);box-shadow:0 30px 60px rgba(44,36,32,.25)}
.b-box .tape{position:absolute;left:200px;top:40px;width:40px;height:280px;background:rgba(245,240,232,.35)}
.b-box .fl{position:absolute;top:8px;width:220px;height:34px;background:linear-gradient(#d4ae82,#c29a6d);border-radius:6px 6px 2px 2px}
.b-lock{position:absolute;inset:0;background:linear-gradient(#241d1a,#3a2f2a);color:#f5f0e8;text-align:center}
.b-lock .tm{position:absolute;left:0;width:590px;top:200px;font:600 150px/1 "Inter";letter-spacing:-.03em}
.b-lock .dy{position:absolute;left:0;width:590px;top:390px;font:500 36px/1 "Inter";opacity:.8}
.b-tabs{position:absolute;inset:0;background:#ece6dd;opacity:0}
.b-tabs .hd{position:absolute;left:44px;top:120px;font:600 36px/1 "Inter"}
.b-tb{position:absolute;left:65px;width:460px;height:300px;border-radius:26px;background:#fffdf9;box-shadow:0 14px 30px rgba(44,36,32,.16);overflow:hidden;opacity:0}
.b-tb .t1{position:absolute;left:185px;top:60px;font:600 24px/1.2 "Inter"}
.b-tb .t2{position:absolute;left:185px;top:120px;font:500 21px/1.3 "Inter";color:rgba(44,36,32,.6);width:250px}
.b-tb .t2 span{color:#2c2420}
.b-faq{position:absolute;left:0;top:150px;width:590px;height:1100px;box-sizing:border-box;padding:34px;background:#fffdf9;font:500 28px/1.35 "Inter"}
.b-faq .tag{font:500 22px/1 "Inter";letter-spacing:.12em;text-transform:uppercase;color:rgba(44,36,32,.55)}
.b-faq .pd{font:500 26px/1.3 "Inter";color:rgba(44,36,32,.55);margin-top:10px}
.b-faq .q{font:600 36px/1.2 "Inter";margin:22px 0 24px;color:rgba(44,36,32,.35)}
.b-faq .a{position:relative;padding:24px 26px;border-radius:22px;background:#f4efe7}
.b-aw{opacity:0}
.b-badge{position:absolute;right:-14px;top:-18px;width:52px;height:52px;opacity:0}
.b-lens{position:absolute;left:0;top:0;width:200px;height:250px;opacity:0}
.b-ring{position:absolute;left:0;top:0;overflow:visible}
.b-logo{position:absolute;left:480px;top:240px;width:120px;height:120px;opacity:0;transform-origin:50% 50%}
.b-plaque{position:absolute;left:300px;top:370px;width:480px;height:84px;border-radius:20px;background:#3a2f2a;opacity:0;transform-origin:50% 50%}
.b-plaque img{position:absolute;left:30px;top:16px;width:420px}
.b-shelves{position:absolute;left:280px;top:472px;width:520px;opacity:0;transform-origin:50% 50%;filter:drop-shadow(0 30px 40px rgba(60,40,20,.22))}
.b-end-btn{position:absolute;left:280px;top:1098px;width:520px;height:104px;border-radius:52px;background:#f5f0e8;color:#3a2f2a;font:600 44px/104px "Inter";text-align:center;opacity:0;box-shadow:0 0 60px rgba(200,162,124,.35)}
"""

B_JS = r"""
var B={};
B.T0=0;B.D=1;
/* le monde : fond (flou, net), voile du soir, groupe caméra G ; tout dépend du temps GLOBAL g = T0 + t */
B.gs=function(g){return 1+0.0008*g};B.gy=function(g){return -0.5*g};
B.world=function(st,P,T0,D,tl){
  var bg=emEl("img","b-bg",st,P+"-bg");bg.src="assets/img/mur-flou.png";
  var net=emEl("img","b-bg",st,P+"-bgnet");net.src="assets/img/mur-net.png";net.style.opacity=0;
  var dim=emEl("div","b-full",st,P+"-dim");dim.style.background="#2c2420";
  var G=emEl("div","b-g",st,P+"-g");
  var c={t:0};
  function up(t){var g=T0+t,s=1.08+0.0016*g,tr="translate("+(-0.8*g).toFixed(2)+"px,"+(30-1.2*g).toFixed(2)+"px) scale("+s.toFixed(4)+")";
    bg.style.transform=tr;net.style.transform=tr;dim.style.opacity=Math.max(0,0.5-0.125*g).toFixed(3);
    G.style.transform="translate(0px,"+B.gy(g).toFixed(2)+"px) scale("+B.gs(g).toFixed(5)+")"}
  tl.fromTo(c,{t:0},{t:D,duration:D,ease:"none",onUpdate:function(){up(c.t)}},0);up(0);
  return {bg:bg,net:net,dim:dim,G:G};
};
/* point nominal du groupe G -> point écran au temps global g */
B.gp=function(x,y,g){var s=B.gs(g);return {x:540+(x-540)*s,y:800+(y-800)*s+B.gy(g)}};
B.place=function(el,cx,cy,s,r){gsap.set(el,{x:cx-320,y:cy-650,scale:s,rotation:r||0,transformOrigin:"50% 50%"})};
B.ph=function(tl,el,cx,cy,s,r,at,dur,ease){tl.to(el,{x:cx-320,y:cy-650,scale:s,rotation:r||0,duration:dur,ease:ease||"power3.inOut"},at)};
B.cardAt=function(el,x,y,s){gsap.set(el,{x:x,y:y,scale:s,transformOrigin:"0 0"})};
B.inn=function(tl,el,at,s0){tl.fromTo(el,{opacity:0,scale:s0||1.2,filter:"blur(8px)"},{opacity:1,scale:1,filter:"blur(0px)",duration:0.2,ease:"expo.out",immediateRender:false},at)};
B.shelfSvg=function(w,h,vases){return '<svg width="'+w+'" height="'+h+'" viewBox="0 0 260 420" preserveAspectRatio="xMidYMid slice"><rect width="260" height="420" fill="#e8dfd0"/><rect x="30" y="250" width="200" height="16" rx="3" fill="#9b7650"/><path d="M55 266 v40 l30 -40 M205 266 v40 l-30 -40" stroke="#2c2420" stroke-width="7" fill="none" stroke-linejoin="round"/>'+(vases?'<path d="M80 168 h20 v14 c0 8 22 18 22 44 c0 12 -6 24 -12 24 h-40 c-6 0 -12 -12 -12 -24 c0 -26 22 -36 22 -44 z" fill="#cfc6b6"/><path d="M155 150 h18 v22 c0 8 18 22 18 46 c0 14 -4 24 -8 32 h-38 c-4 -8 -8 -18 -8 -32 c0 -24 18 -38 18 -46 z" fill="#b9a58c"/>':'')+'</svg>'};
/* carte d'une boutique anonyme (760 x 420, origine en haut à gauche) */
B.card=function(par,id,v){var c=emEl("div","b-card",par,id);
  c.innerHTML='<div class="b-photo" style="width:260px;height:420px;overflow:hidden">'+B.shelfSvg(260,420,false)+'</div>'+
  '<svg class="b-vase" id="'+id+'-v1" style="left:56px;top:168px" width="68" height="82" viewBox="56 168 68 82"><path d="M80 168 h20 v14 c0 8 22 18 22 44 c0 12 -6 24 -12 24 h-40 c-6 0 -12 -12 -12 -24 c0 -26 22 -36 22 -44 z" fill="#cfc6b6"/></svg>'+
  '<svg class="b-vase" id="'+id+'-v2" style="left:137px;top:150px" width="54" height="100" viewBox="137 150 54 100"><path d="M155 150 h18 v22 c0 8 18 22 18 46 c0 14 -4 24 -8 32 h-38 c-4 -8 -8 -18 -8 -32 c0 -24 18 -38 18 -46 z" fill="#b9a58c"/></svg>'+
  '<div class="b-tt" id="'+id+'-tt">Étagère murale en bois</div><div class="b-pr" id="'+id+'-pr">'+v.p+'</div>'+
  '<div class="b-row" style="top:132px"><b>Matière&nbsp;:</b><span class="b-val" id="'+id+'-mat">'+v.m+'</span></div>'+
  '<div class="b-row" style="top:178px"><b>Charge&nbsp;:</b><span class="b-val" id="'+id+'-chg">'+v.c+'</span></div>'+
  '<div class="b-row" id="'+id+'-r3" style="top:224px;opacity:0"><b>Dimensions&nbsp;:</b><span class="b-val" style="left:165px"><span class="q">?</span></span></div>'+
  '<div class="b-row" id="'+id+'-r4" style="top:270px;opacity:0"><b>Dans le colis&nbsp;:</b><span class="b-val" style="left:170px"><span class="q">?</span></span></div>'+
  '<div class="b-btn" id="'+id+'-btn">Ajouter au panier</div>';return c};
B.box=function(par,id){var b=emEl("div","b-box",par,id);
  b.innerHTML='<div class="in"></div><div class="body"></div><div class="tape"></div><div class="fl" id="'+id+'-fl" style="left:0;transform-origin:0% 100%"></div><div class="fl" id="'+id+'-fr" style="left:220px;transform-origin:100% 100%"></div>';return b};
B.lock=function(screen,P){var l=emEl("div","b-lock",screen,P+"-lk");l.innerHTML='<div class="tm" id="'+P+'-lk-time" style="opacity:0">21:47</div><div class="dy" id="'+P+'-lk-day" style="opacity:0">dimanche</div>';return l};
B.tabs=function(screen,P){var t=emEl("div","b-tabs",screen,P+"-tabs");
  var M=["bois massif","bois","effet bois"],h='<div class="hd" id="'+P+'-tb-head" style="opacity:0">3 onglets</div>';
  for(var i=0;i<3;i++)h+='<div class="b-tb" id="'+P+'-tb'+i+'" style="top:'+(210+i*320)+'px"><div style="position:absolute;left:0;top:0;width:160px;height:300px">'+B.shelfSvg(160,300,true)+'</div><div class="t1">Étagère murale</div><div class="t2">Matière&nbsp;: <span>'+M[i]+'</span></div></div>';
  t.innerHTML=h;return t};
B.faq=function(screen,id,prod,q,words){var f=emEl("div","b-faq",screen,id);
  f.innerHTML='<div class="tag">Questions fréquentes</div><div class="pd">'+prod+'</div><div class="q" id="'+id+'-q">'+q+'</div><div class="a"><span>'+
  words.map(function(w,i){return '<span class="b-aw" id="'+id+'-a'+i+'">'+w+'</span>'}).join(' ')+'</span>'+
  '<svg class="b-badge" id="'+id+'-ok" viewBox="0 0 40 40"><circle cx="20" cy="20" r="20" fill="#a97c50"/><path d="M11 21 l6 6 l12 -13" fill="none" stroke="#f5f0e8" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/></svg></div>';return f};
B.faqDone=function(f){f.querySelectorAll(".b-aw,.b-badge").forEach(function(e){e.style.opacity=1});f.querySelector(".q").style.color="#2c2420"};
B.words=function(tl,f,n,t0,t1){for(var i=0;i<n;i++)tl.to(f.querySelector("#"+f.id+"-a"+i),{opacity:1,duration:0.08},t0+(t1-t0)*i/Math.max(1,n-1))};
B.check=function(tl,P,k,at){tl.to("#"+P+"-pge-c"+k+" .em-pen",{strokeDashoffset:0,duration:0.2,ease:"power2.out",autoRound:false},at);tl.to("#"+P+"-pge-r"+k,{color:"#2c2420",duration:0.15},at)};
B.checkDone=function(P,ks){ks.forEach(function(k){var c=document.querySelector("#"+P+"-pge-c"+k+" .em-pen");if(c)c.style.strokeDashoffset=0;var r=document.getElementById(P+"-pge-r"+k);if(r)r.style.color="#2c2420"})};
B.ring=function(par,id,x,y,w,h,col){var d=emSvg(par,id,w,h,'<ellipse class="em-pen" cx="'+(w/2)+'" cy="'+(h/2)+'" rx="'+(w/2-4)+'" ry="'+(h/2-4)+'" fill="none" stroke="'+col+'" stroke-width="4" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1" transform="rotate(-4 '+(w/2)+' '+(h/2)+')"/>',x,y);d.classList.add("b-ring");return d};
B.chip=function(par,id,txt){var c=emEl("div","b-chip",par,id,txt);return c};
B.type=function(st,id,words){var d=emEl("div","em-type",st,id);d.style.top="760px";d.innerHTML=words.map(function(w,i){return '<span class="em-w" id="'+id+'-w'+i+'" style="opacity:0">'+w+'</span>'}).join(' ');return d};
B.typeTL=function(tl,d,cues){cues.forEach(function(t,i){tl.fromTo(d.querySelector("#"+d.id+"-w"+i),{opacity:0,scale:1.2,filter:"blur(8px)"},{opacity:1,scale:1,filter:"blur(0px)",duration:0.2,ease:"expo.out",immediateRender:false},t)})};
"""

# états aux coutures (téléphone : cx, cy, échelle)
PH0, PH1, PH10, PH11, PH12, PH13 = (540, 772, .85), (540, 760, .95), (540, 760, .90), (540, 740, 1.0), (540, 730, 1.04), (540, 760, .95)
V = '[{m:"bois massif",c:"voir photo",p:"39,90 €"},{m:"bois",c:"–",p:"42,00 €"},{m:"effet bois",c:"non précisée",p:"38,50 €"}]'

F = []
def frame(fid, dur, voice, scene, js, words=""):
    F.append(dict(id=fid, dur=dur, voice=voice, scene=scene, js=js, words=words))

frame("01-dimanche", 3.0, "Dimanche soir. Trois onglets ouverts.",
"Le soir, le téléphone s'allume devant le mur flou : 21:47, dimanche ; l'écran passe à la vue des onglets, trois fiches s'empilent",
r"""
var K=emBuildPhone(G,P);B.place(K.phone,540,772,.85);var lk=B.lock(K.screen,P);var tb=B.tabs(K.screen,P);K.off.style.opacity=1;
tl.to(K.off,{opacity:0,duration:.25,ease:"power2.out"},.10);
B.inn(tl,$("lk-time"),.20);B.inn(tl,$("lk-day"),.45);
tl.to($("lk-time"),{y:-14,duration:.6,ease:"power2.out"},.75);
tl.to(lk,{y:-260,opacity:0,duration:.3,ease:"power2.in"},1.20);
tl.fromTo(tb,{opacity:0},{opacity:1,duration:.2,immediateRender:false},1.30);
B.inn(tl,$("tb-head"),1.40);
[0,1,2].forEach(function(i){tl.fromTo($("tb"+i),{opacity:0,y:140},{opacity:1,y:0,duration:.25,ease:"expo.out",immediateRender:false},1.55+i*.25)});
tl.to([$("tb0"),$("tb1"),$("tb2")],{rotation:function(i){return [-3,0,3][i]},duration:.3,ease:"power2.out"},2.30);
tl.fromTo($("tb-head"),{scale:1},{scale:1.08,duration:.12,yoyo:true,repeat:1,immediateRender:false},2.60);
B.ph(tl,K.phone,540,760,.95,0,0,3.0,"none");
var s1=emSub(st,P+"-s1",["Dimanche","soir."],1,-1);emSubTL(tl,s1,[.30,.72],1,-1,1.30);
var s2=emSub(st,P+"-s2",["Trois","onglets","ouverts."],1,-1);emSubTL(tl,s2,[1.50,1.78,2.20],1,-1,2.78);
""", "Dimanche@0.30 soir.@0.72 Trois@1.50 onglets@1.78 ouverts.@2.20")

frame("02-trois-fiches", 3.2, "La même étagère… trois fiches différentes.",
"Les trois onglets sortent du téléphone et deviennent trois cartes de boutiques anonymes : la même étagère, trois matières différentes",
r"""
var K=emBuildPhone(G,P);B.place(K.phone,540,760,.95);var tb=B.tabs(K.screen,P);tb.style.opacity=1;$("tb-head").style.opacity=1;
[0,1,2].forEach(function(i){var t=$("tb"+i);t.style.opacity=1;gsap.set(t,{rotation:[-3,0,3][i]})});
var C=__V.map(function(v,i){return B.card(G,P+"-c"+i,v)});
tl.to([$("tb0"),$("tb1"),$("tb2")],{opacity:0,duration:.1},.12);
C.forEach(function(c,i){B.cardAt(c,540-114,600+i*90-63,.3);c.style.opacity=0;tl.set(c,{opacity:1},.12);
  tl.to(c,{x:266,y:240+i*320,scale:.72,duration:.45,ease:"expo.out"},.15+i*.12)});
B.ph(tl,K.phone,540,3300,.95,0,.12,.45,"power2.in");tl.to(K.phone,{opacity:0,duration:.1},.5);
tl.fromTo(K.phone,{filter:"blur(0px)"},{filter:"blur(8px)",duration:.3,immediateRender:false},.15);
tl.fromTo(C.map(function(c){return c.querySelector(".b-photo")}),{scale:1},{scale:1.05,duration:.15,yoyo:true,repeat:1,immediateRender:false,transformOrigin:"50% 60%"},.85);
[1.55,1.80,2.15].forEach(function(t,i){tl.to($("c"+i+"-mat"),{color:"#8c3b2e",scale:1.12,duration:.16,ease:"power2.out",transformOrigin:"0% 50%"},t)});
tl.to(C.map(function(c,i){return $("c"+i+"-mat")}),{scale:1,duration:.3},2.55);
var s=emSub(st,P+"-s1",["La","même","étagère…","trois","fiches","différentes."],5,-1);emSubTL(tl,s,[.15,.30,.55,1.55,1.80,2.15],5,-1,2.98);
""", "La@0.15 même@0.30 étagère…@0.55 trois@1.55 fiches@1.80 différentes.@2.15")

STACK = r"""var C=__V.map(function(v,i){return B.card(G,P+"-c"+i,v)});C.forEach(function(c,i){B.cardAt(c,266,240+i*320,.72);$("c"+i+"-mat").style.color="#8c3b2e"});"""

frame("03-hesite", 2.6, "",
"Temps muet : le curseur va sur « Ajouter au panier » de la première carte, hésite, recule ; l'onglet se ferme d'un geste, les deux autres cartes remontent",
STACK + r"""
var k=emCursor(st,P);var bt=B.gp(568,503,T0+.75);
tl.set(k.cursor,{x:900,y:1250,opacity:1},.25);tl.to(k.cursor,{x:bt.x-8,y:bt.y-6,duration:.45,ease:"power3.out"},.30);
tl.to($("c0-btn"),{backgroundColor:"#5a4636",scale:1.05,duration:.15},.78);
tl.to(k.cursor,{x:bt.x+70,y:bt.y+90,duration:.4,ease:"power2.inOut"},1.15);
tl.to($("c0-btn"),{backgroundColor:"#3a2f2a",scale:1,duration:.2},1.20);
tl.to(C[0],{x:-900,rotation:-8,duration:.35,ease:"power2.in"},1.60);tl.to(k.cursor,{opacity:0,duration:.15},1.62);
tl.to(C[1],{y:240,duration:.4,ease:"power3.out"},1.85);tl.to(C[2],{y:560,duration:.4,ease:"power3.out"},1.95);
tl.fromTo(C[1],{rotation:0},{rotation:-1.2,duration:.15,yoyo:true,repeat:1,immediateRender:false},2.30);
""")

TWO = r"""var C1=B.card(G,P+"-c1",__V[1]),C2=B.card(G,P+"-c2",__V[2]);$("c1-mat").style.color="#8c3b2e";$("c2-mat").style.color="#8c3b2e";"""

frame("04-prix", 2.8, "Le problème, ce n’est pas le prix.",
"La deuxième carte vient au premier plan ; son prix est entouré, trois prix voisins arrivent puis se rangent ensemble : le prix n'est pas le problème",
TWO + r"""
B.cardAt(C1,266,240,.72);B.cardAt(C2,266,560,.72);
tl.to(C1,{x:65,y:337.5,scale:1.25,duration:.55,ease:"power3.inOut"},0);
tl.to(C2,{y:1900,filter:"blur(8px)",duration:.35,ease:"power2.in"},0);
var rg=B.ring(C1,P+"-rg",278,62,170,64,"#2c2420");emPen(tl,rg,.70,.3);
var X=[200,540,880],T=["39,90 €","42,00 €","38,50 €"],ch=T.map(function(t,i){var c=B.chip(G,P+"-ch"+i,t);gsap.set(c,{x:X[i],y:1000,xPercent:-50,yPercent:-50});return c});
ch.forEach(function(c,i){B.inn(tl,c,1.0+i*.2)});
tl.to(ch,{x:function(i){return 540+(i-1)*215},opacity:.55,duration:.35,ease:"power3.inOut"},1.90);
tl.to(ch,{opacity:0,y:980,duration:.2,ease:"power2.in"},2.40);tl.to(rg,{opacity:0,duration:.2},2.40);
var s=emSub(st,P+"-s1",["Le","problème,","ce","n’est","pas","le","prix."],6,-1);emSubTL(tl,s,[.10,.25,.75,.88,1.05,1.22,1.35],6,-1,2.58);
""", "Le@0.10 problème,@0.25 ce@0.75 n’est@0.88 pas@1.05 le@1.22 prix.@1.35")

ONE = r"""var C1=B.card(G,P+"-c1",__V[1]);$("c1-mat").style.color="#8c3b2e";"""

frame("05-non-dit", 2.6, "C’est tout ce qu’on ne vous dit pas.",
"Sur la carte, les lignes « Dimensions : ? » et « Dans le colis : ? » apparaissent ; le bouton pâlit",
ONE + r"""
B.cardAt(C1,65,337.5,1.25);
tl.to(C1,{x:38.4,y:322.8,scale:1.32,duration:2.6,ease:"none"},0);
B.inn(tl,$("c1-r3"),.45,1.08);B.inn(tl,$("c1-r4"),.75,1.08);
tl.fromTo(C1.querySelectorAll(".q"),{scale:1},{scale:1.4,duration:.12,yoyo:true,repeat:1,immediateRender:false,transformOrigin:"50% 60%"},1.10);
tl.to($("c1-chg"),{color:"#8c3b2e",duration:.15},1.35);
tl.to($("c1-btn"),{opacity:.4,duration:.3},1.80);
tl.fromTo(C1.querySelectorAll(".q"),{x:0},{x:4,duration:.05,yoyo:true,repeat:3,immediateRender:false},2.20);
var s=emSub(st,P+"-s1",["C’est","tout","ce","qu’on","ne","vous","dit","pas."],1,-1);emSubTL(tl,s,[.10,.28,.48,.60,.78,.88,1.02,1.20],1,-1,2.38);
""", "C’est@0.10 tout@0.28 ce@0.48 qu’on@0.60 ne@0.78 vous@0.88 dit@1.02 pas.@1.20")

CARD5 = ONE + r"""$("c1-r3").style.opacity=1;$("c1-r4").style.opacity=1;$("c1-btn").style.opacity=.4;$("c1-chg").style.color="#8c3b2e";"""

frame("06-bois", 2.6, "Du « bois »… qui n’en est pas.",
"La caméra plonge sur « Matière : bois » ; le mot se fissure, ses lettres tombent, l'étiquette « aggloméré » prend sa place",
CARD5 + r"""
B.cardAt(C1,38.4,322.8,1.32);
var m=$("c1-mat");m.innerHTML="bois".split("").map(function(l,i){return '<span id="'+P+'-L'+i+'" style="display:inline-block">'+l+'</span>'}).join("");
tl.to(C1,{x:-338,y:346,scale:2.0,duration:.45,ease:"power3.inOut"},0);
tl.to(m,{scale:1.1,duration:.15,transformOrigin:"0% 50%"},.25);
var cr=emSvg(C1,P+"-crack",70,34,'<path class="em-pen" d="M2 18 L14 10 L24 22 L36 8 L46 20 L58 12 L68 18" fill="none" stroke="#8c3b2e" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>',412,131);
emPen(tl,cr,.60,.25);
[0,1,2,3].forEach(function(i){tl.to($("L"+i),{y:46,rotation:[-25,18,-12,30][i],opacity:0,duration:.35,ease:"power2.in"},1.10+i*.05)});
tl.to(cr,{opacity:0,duration:.15},1.20);
var n=emNote(G,P+"-n1","aggloméré",452,596);B.inn(tl,n,1.40);
tl.fromTo(n,{rotation:0},{rotation:-3,duration:.08,yoyo:true,repeat:3,immediateRender:false},1.90);
var s=emSub(st,P+"-s1",["Du","« bois »…","qui","n’en","est","pas."],1,-1);emSubTL(tl,s,[.10,.25,1.10,1.25,1.40,1.55],1,-1,2.38);
""", "Du@0.10 «bois»…@0.25 qui@1.10 n’en@1.25 est@1.40 pas.@1.55")

frame("07-charge", 2.4, "Une charge… introuvable.",
"La caméra descend sur « Charge : – » ; une loupe balaie la ligne et ne trouve rien",
CARD5 + r"""
B.cardAt(C1,-338,346,2.0);$("c1-mat").style.opacity=0;
var n=emNote(G,P+"-n1","aggloméré",452,596);n.style.opacity=1;
tl.to(C1,{y:254,duration:.35,ease:"power3.inOut"},0);tl.to(n,{y:-92,opacity:0,duration:.3,ease:"power2.in"},0);
var L=emSvg(G,P+"-lens",200,250,'<circle cx="90" cy="90" r="70" fill="rgba(255,253,249,.25)" stroke="#2c2420" stroke-width="9"/><path d="M140 140 L190 200" stroke="#2c2420" stroke-width="16" stroke-linecap="round"/><text id="'+P+'-lq" x="90" y="112" text-anchor="middle" font-family="Inter" font-weight="600" font-size="64" fill="#8c3b2e" opacity="0">?</text>',0,0);
L.classList.add("b-lens");gsap.set(L,{x:110,y:550});
B.inn(tl,L,.35);tl.to(L,{x:414,duration:.65,ease:"power2.inOut"},.40);
tl.to($("lq"),{opacity:1,duration:.15},1.15);
tl.fromTo(L,{rotation:0},{rotation:6,duration:.08,yoyo:true,repeat:3,immediateRender:false,transformOrigin:"45% 36%"},1.60);
tl.to(L,{opacity:0,scale:1.1,duration:.2,ease:"power2.in"},2.00);
var s=emSub(st,P+"-s1",["Une","charge…","introuvable."],2,-1);emSubTL(tl,s,[.10,.25,1.10],2,-1,2.18);
""", "Une@0.10 charge…@0.25 introuvable.@1.10")

frame("08-colis", 3.0, "Des vases sur la photo… pas dans le colis.",
"La caméra recule sur la photo ; les deux vases sortent de l'image, un carton monte, les vases rebondissent sur le couvercle et tombent hors champ",
CARD5 + r"""
B.cardAt(C1,-338,254,2.0);$("c1-mat").style.opacity=0;
tl.to(C1,{x:65,y:337.5,scale:1.25,duration:.45,ease:"power3.inOut"},0);
var v1=$("c1-v1"),v2=$("c1-v2");
tl.to([v1,v2],{y:-36,scale:1.12,duration:.25,ease:"power2.out"},.60);
var bx=B.box(G,P+"-box");gsap.set(bx,{x:20,y:1500});
tl.to(bx,{y:960,duration:.4,ease:"expo.out"},1.00);
tl.to([v1,v2],{y:240,duration:.25,ease:"power2.in"},1.70);
tl.to(v1,{y:170,x:-170,rotation:-28,opacity:0,duration:.35,ease:"power2.out"},1.95);
tl.to(v2,{y:170,x:170,rotation:24,opacity:0,duration:.35,ease:"power2.out"},1.95);
tl.fromTo(bx,{scaleY:1},{scaleY:.97,duration:.06,yoyo:true,repeat:1,immediateRender:false,transformOrigin:"50% 100%"},1.95);
var n=emNote(G,P+"-n1","pas inclus",500,1000);B.inn(tl,n,2.30);tl.to(n,{opacity:0,duration:.15},2.75);
var s=emSub(st,P+"-s1",["Des","vases","sur","la","photo…","pas","dans","le","colis."],8,-1);emSubTL(tl,s,[.10,.25,.62,.75,.88,1.70,1.86,2.00,2.10],8,-1,2.78);
""", "Des@0.10 vases@0.25 sur@0.62 la@0.75 photo…@0.88 pas@1.70 dans@1.86 le@2.00 colis.@2.10")

frame("09-pivot", 4.2, "Et si la fiche répondait vraiment ?",
"Le carton s'ouvre, la caméra plonge dedans jusqu'au noir ; la question tombe mot à mot ; un point de lumière sable s'ouvre en cercle crème",
CARD5 + r"""
B.cardAt(C1,65,337.5,1.25);$("c1-mat").style.opacity=0;$("c1-v1").style.opacity=0;$("c1-v2").style.opacity=0;
var bx=B.box(G,P+"-box");gsap.set(bx,{x:20,y:960});
tl.to(C1,{opacity:0,filter:"blur(10px)",duration:.4},.05);
tl.to($("box-fl"),{rotation:-140,duration:.3,ease:"power2.out"},.10);tl.to($("box-fr"),{rotation:140,duration:.3,ease:"power2.out"},.10);
tl.to(bx,{scale:9,duration:.45,ease:"power2.in",transformOrigin:"220px 50px"},.35);
var dk=emEl("div","b-full",st,P+"-dark");dk.style.background="#2c2420";dk.style.opacity=0;tl.to(dk,{opacity:1,duration:.15},.62);
var ty=B.type(st,P+"-ty",["Et","si","la","fiche","répondait","vraiment&#8239;?"]);B.typeTL(tl,ty,[.80,.92,1.04,1.16,1.40,1.90]);
tl.to(ty,{scale:1.04,y:-12,duration:2.0,ease:"none"},.80);
tl.to(ty.querySelectorAll(".em-w"),{opacity:0,y:-10,duration:.15,stagger:.03},2.70);
var pt=emEl("div","",st,P+"-pt");pt.style.cssText="position:absolute;left:528px;top:808px;width:24px;height:24px;border-radius:50%;background:#c8a27c;box-shadow:0 0 40px 16px rgba(200,162,124,.45);opacity:0";
tl.fromTo(pt,{opacity:0,scale:.2},{opacity:1,scale:1,duration:.25,ease:"expo.out",immediateRender:false},2.95);
tl.to(pt,{scale:2.4,duration:.4,ease:"power2.inOut"},3.25);
var cr=emEl("div","b-full",st,P+"-cream");cr.style.background="#f4efe7";cr.style.clipPath="circle(0% at 540px 820px)";
tl.to(cr,{clipPath:"circle(150% at 540px 820px)",duration:.55,ease:"power2.in"},3.60);
""")

PAGE = r"""var K=emBuildPhone(G,P);var pg=emPageEM(K.screen,P);"""

frame("10-vraie-fiche", 3.2, "Chez Étagères Murales, chaque fiche dit ce que vous recevez.",
"Le cercle crème est l'écran : la caméra recule, le téléphone apparaît devant le mur, la vraie fiche se remplit",
PAGE + r"""
B.place(K.phone,540,980,3.4);var cr=emEl("div","b-full",st,P+"-cream");cr.style.background="#f4efe7";
tl.to(cr,{opacity:0,duration:.25,ease:"power2.out"},.10);
B.ph(tl,K.phone,540,772,.85,0,0,.8,"expo.out");B.ph(tl,K.phone,540,740,.90,0,.8,2.4,"none");
var ph=$("pge-photo"),ti=pg.querySelector(".title"),pr=pg.querySelector(".price"),rows=[1,2,3,4].map(function(k){return $("pge-r"+k)});
gsap.set([$("pge-img"),ti,pr].concat(rows),{opacity:0});
B.inn(tl,$("pge-img"),.90);tl.to(ti,{opacity:1,duration:.2},1.30);B.inn(tl,pr,1.80);
rows.forEach(function(r,i){tl.fromTo(r,{opacity:0,y:14},{opacity:1,y:0,duration:.2,ease:"power2.out",immediateRender:false},2.20+i*.15)});
var s=emSub(st,P+"-s1",["Chez","Étagères","Murales,","chaque","fiche","dit","ce","que","vous","recevez."],9,-1);emSubTL(tl,s,[.20,.36,.75,1.30,1.55,1.82,2.00,2.12,2.24,2.40],9,-1,2.98);
""", "Chez@0.20 Étagères@0.36 Murales,@0.75 chaque@1.30 fiche@1.55 dit@1.82 ce@2.00 que@2.12 vous@2.24 recevez.@2.40")

FQ1 = ('"Étagères murales flottantes lot de 3 VASAGLE","C’est du bois massif&#8239;?",["Non.","Les","plateaux","sont","en","panneau","de","particules","avec","un","effet","bois","vintage."]', 13)
FQ2 = ('"Étagère d’angle de douche en inox 304","Quelle charge peut-elle porter&#8239;?",["Le","vendeur","ne","l’a","pas","encore","communiquée.","Nous","lui","avons","posé","la","question."]', 13)

frame("11-bois-massif", 3.4, "C’est du bois massif ? Non, et on l’écrit.",
"La FAQ de la fiche VASAGLE monte dans l'écran : « C’est du bois massif ? », la réponse s'écrit, une coche sable",
PAGE + r"""
B.place(K.phone,540,740,.90);
var f=B.faq(K.screen,P+"-fq",""" + FQ1[0] + r""");gsap.set(f,{y:1200});
tl.to(f,{y:0,duration:.45,ease:"expo.out"},.10);
tl.to($("fq-q"),{color:"#2c2420",duration:.2},.62);
B.words(tl,f,""" + str(FQ1[1]) + r""",1.40,2.40);B.inn(tl,$("fq-ok"),2.65);
B.ph(tl,K.phone,540,720,.98,0,0,3.4,"none");
var s=emSub(st,P+"-s1",["C’est","du","bois","massif&#8239;?","Non,","et","on","l’écrit."],4,-1);emSubTL(tl,s,[.15,.30,.42,.62,1.40,1.75,1.88,2.00],4,-1,3.18);
""", "C’est@0.15 du@0.30 bois@0.42 massif?@0.62 Non,@1.40 et@1.75 on@1.88 l’écrit.@2.00")

frame("12-charge-connue", 3.4, "La charge n’est pas connue ? On l’écrit aussi.",
"Une autre vraie FAQ glisse par la droite (étagère d’angle de douche) : la charge n'est pas connue, la réponse le dit",
PAGE + r"""
B.place(K.phone,540,720,.98);
var f1=B.faq(K.screen,P+"-fa",""" + FQ1[0] + r""");B.faqDone(f1);
var f=B.faq(K.screen,P+"-fq",""" + FQ2[0] + r""");gsap.set(f,{x:600});
tl.to(f1,{x:-600,duration:.45,ease:"expo.out"},.10);tl.to(f,{x:0,duration:.45,ease:"expo.out"},.10);
tl.to($("fq-q"),{color:"#2c2420",duration:.2},.92);
B.words(tl,f,""" + str(FQ2[1]) + r""",1.70,2.70);B.inn(tl,$("fq-ok"),2.85);
B.ph(tl,K.phone,540,700,1.0,0,0,3.4,"none");
var s=emSub(st,P+"-s1",["La","charge","n’est","pas","connue&#8239;?","On","l’écrit","aussi."],7,-1);emSubTL(tl,s,[.15,.28,.62,.78,.92,1.70,1.85,2.15],7,-1,3.18);
""", "La@0.15 charge@0.28 n’est@0.62 pas@0.78 connue?@0.92 On@1.70 l’écrit@1.85 aussi.@2.15")

frame("13-pas-inclus", 3.4, "Les objets de la photo ? Pas inclus. C’est écrit.",
"La FAQ redescend, la vraie fiche se coche ligne par ligne jusqu'à « Les objets des photos ne sont pas inclus »",
PAGE + r"""
B.place(K.phone,540,700,1.0);
var f=B.faq(K.screen,P+"-fq",""" + FQ2[0] + r""");B.faqDone(f);
tl.to(f,{y:1300,duration:.4,ease:"power2.in"},.10);
tl.fromTo($("pge-img"),{scale:1},{scale:1.05,duration:.15,yoyo:true,repeat:1,immediateRender:false},.55);
B.check(tl,P,1,.80);B.check(tl,P,2,1.05);B.check(tl,P,3,1.30);B.check(tl,P,4,1.62);
tl.fromTo($("pge-r4"),{scale:1},{scale:1.04,duration:.15,yoyo:true,repeat:1,immediateRender:false,transformOrigin:"0% 50%"},2.45);
B.ph(tl,K.phone,540,740,.92,0,0,3.4,"none");
var s=emSub(st,P+"-s1",["Les","objets","de","la","photo&#8239;?","Pas","inclus.","C’est","écrit."],6,8);emSubTL(tl,s,[.15,.28,.58,.68,.80,1.45,1.62,2.25,2.45],6,8,3.18);
""", "Les@0.15 objets@0.28 de@0.58 la@0.68 photo?@0.80 Pas@1.45 inclus.@1.62 C’est@2.25 écrit.@2.45")

frame("14-mur", 4.2, "Étagères Murales. Pour sublimer vos murs et finir vos pièces.",
"Le téléphone s'efface, le mur devient net ; le carton remonte, s'ouvre, et les vraies étagères VASAGLE en sortent pour se poser au mur ; le logo arrive",
PAGE + r"""
B.place(K.phone,540,740,.92);B.checkDone(P,[1,2,3,4]);
B.ph(tl,K.phone,540,3300,.92,0,0,.35,"power2.in");tl.to(K.phone,{opacity:0,duration:.1},.36);tl.fromTo(K.phone,{filter:"blur(0px)"},{filter:"blur(8px)",duration:.3,immediateRender:false},.02);
tl.to(W.net,{opacity:1,duration:.5,ease:"power2.inOut"},.15);
var sh=emEl("img","b-shelves",G,P+"-sh");sh.src="assets/img/vasagle-3-etageres.png";gsap.set(sh,{y:500,scale:.35});var bx=B.box(G,P+"-box");gsap.set(bx,{x:320,y:1700});tl.to(bx,{y:900,duration:.4,ease:"expo.out"},.10);
tl.to($("box-fl"),{rotation:-140,duration:.3,ease:"power2.out"},.55);tl.to($("box-fr"),{rotation:140,duration:.3,ease:"power2.out"},.55);
tl.to(sh,{opacity:1,duration:.1},.75);tl.to(sh,{y:0,scale:1,duration:.5,ease:"expo.out"},.75);
tl.to(bx,{y:2600,duration:.4,ease:"power2.in"},1.30);tl.to(bx,{opacity:0,duration:.1},1.65);
tl.fromTo(sh,{y:0},{y:-6,duration:.12,yoyo:true,repeat:1,immediateRender:false},1.25);
var lg=emEl("img","b-logo",G,P+"-logo");lg.src="assets/img/logo-em.png";B.inn(tl,lg,.20);
var pq=emEl("div","b-plaque",G,P+"-pq",'<img src="assets/img/logo-texte.png">');B.inn(tl,pq,.60);
tl.fromTo(lg,{scale:1},{scale:1.06,duration:.15,yoyo:true,repeat:1,immediateRender:false},2.70);
tl.fromTo(sh,{rotation:0},{rotation:-.6,duration:.2,yoyo:true,repeat:1,immediateRender:false},3.40);
var s=emSub(st,P+"-s1",["Pour","sublimer","vos","murs","et","finir","vos","pièces."],3,-1);emSubTL(tl,s,[1.40,1.55,2.05,2.20,2.55,2.68,3.00,3.15],3,-1,3.95);
""", "Étagères@0.20 Murales.@0.60 Pour@1.40 sublimer@1.55 vos@2.05 murs@2.20 et@2.55 finir@2.68 vos@3.00 pièces.@3.15")

frame("15-fin", 3.6, "Lien dans la bio.",
"Un iris brun s'ouvre depuis le logo ; logo et nom se posent sur la carte de fin, le curseur clique « etageres-murales.fr »",
r"""
W.net.style.opacity=1;
var sh=emEl("img","b-shelves",G,P+"-sh");sh.src="assets/img/vasagle-3-etageres.png";sh.style.opacity=1;
var ir=emEl("div","b-full",G,P+"-iris");ir.style.cssText+="inset:-400px;background:#3a2f2a;clip-path:circle(0% at 940px 700px)";
tl.to(ir,{clipPath:"circle(150% at 940px 700px)",duration:.55,ease:"power2.inOut"},0);
var lg=emEl("img","b-logo",G,P+"-logo");lg.src="assets/img/logo-em.png";lg.style.opacity=1;
var pq=emEl("div","b-plaque",G,P+"-pq",'<img src="assets/img/logo-texte.png">');pq.style.opacity=1;
tl.to(lg,{y:300,scale:220/120,duration:.6,ease:"power3.inOut"},.15);
tl.to(pq,{y:448,scale:640/420,duration:.6,ease:"power3.inOut"},.25);
var bt=emEl("div","b-end-btn",G,P+"-btn","etageres-murales.fr");B.inn(tl,bt,.70,1.15);
tl.fromTo(bt,{boxShadow:"0 0 60px rgba(200,162,124,.35)"},{boxShadow:"0 0 90px rgba(200,162,124,.65)",duration:.4,yoyo:true,repeat:1,immediateRender:false},.95);
var k=emCursor(st,P),c=B.gp(560,1150,T0+1.75);emClick(tl,k,980,1700,c.x,c.y,1.30);
tl.to(bt,{backgroundColor:"#a97c50",color:"#f5f0e8",duration:.15},1.77);
tl.to(lg,{y:290,duration:1.5,ease:"none"},2.0);
var bk=emEl("div","b-full",st,P+"-black");bk.style.background="#000";bk.style.opacity=0;tl.to(bk,{opacity:1,duration:.22},3.38);
var s=emSub(st,P+"-s1",["Lien","dans","la","bio."],3,-1,true);emSubTL(tl,s,[.55,.75,.92,1.05],3,-1,3.20);
""", "Lien@0.55 dans@0.75 la@0.92 bio.@1.05")

# ------------------------------------------------------------------ écriture
V_JS = V
T = 0.0
os.makedirs(os.path.join(HERE, "compositions", "frames"), exist_ok=True)
sb = ["---", "format: 1080x1920", f'duration: "{sum(f["dur"] for f in F):.2f}s"',
      'message: "Chez Étagères Murales, chaque fiche répond vraiment : bois, charge, contenu du colis."',
      "arc: Hook → Silence → Problem → Pivot → Solution → Proof → CTA",
      'audience: "Particuliers qui comparent des étagères en ligne et hésitent"', "mode: autonomous", "captions: disabled",
      'music: "aucune (voix et bruitages)"', 'direction: "B « Trois onglets » (SCRIPT.md), 15 séquences générées par build.py"',
      'styleframes: "aucun"', "patterns: ../patterns/STORYBOARD-CRAFT.md, ../patterns/PATTERNS.md", "---", "",
      "# Storyboard · « Trois onglets » (généré par build.py, ne pas éditer à la main)", ""]
for i, f in enumerate(F):
    n = i + 1
    P = f"s{n:02d}"
    js = f["js"].replace("__V", V_JS)
    html = (f'<template>\n<div id="root" data-composition-id="{f["id"]}" data-width="1080" data-height="1920" data-start="0" data-duration="{f["dur"]}">\n'
            f'<script src="assets/gsap.min.js"></script>\n<style id="{P}-kit">{KIT_CSS}{B_CSS}</style>\n'
            f'<div class="em-stage clip" id="{P}-stage" data-start="0" data-duration="{f["dur"]}" data-track-index="0"></div>\n'
            f'<script id="{P}-kit-js">{KIT_JS}{B_JS}\n(function(){{\nvar P="{P}",D={f["dur"]},T0={T:.2f};\n'
            'var $=function(i){return document.getElementById(P+"-"+i)};var st=$("stage");\n'
            'var tl=gsap.timeline({paused:true});var W=B.world(st,P,T0,D,tl);var G=W.G;\n'
            f'{js}\nwindow.__timelines=window.__timelines||{{}};window.__timelines["{f["id"]}"]=tl;\n}})();\n</script>\n</div>\n</template>\n')
    open(os.path.join(HERE, "compositions", "frames", f'{f["id"]}.html'), "w", encoding="utf-8").write(html)
    sb += [f'## Frame {n} : {f["id"]} · {T:.2f} → {T + f["dur"]:.2f}', "",
           f'- scene: {f["scene"]}', f'- duration: {f["dur"]}s', "- transition_in: cut", "- status: outline",
           f'- src: compositions/frames/{f["id"]}.html', f'- voiceover: "{f["voice"]}"', "- world: light",
           "- handoff_in: état de couture défini dans build.py (fond et caméra G calculés sur le temps global)",
           "- handoff_out: état de couture défini dans build.py (fond et caméra G calculés sur le temps global)", "",
           f'Word cues: {f["words"] or "(aucun mot : silence)"}', ""]
    T += f["dur"]
open(os.path.join(HERE, "STORYBOARD.md"), "w", encoding="utf-8").write("\n".join(sb))
print(f"{len(F)} séquences, {T:.2f} s")
