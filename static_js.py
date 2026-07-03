# JavaScript served by Flask  
SCRIPTS = """

var defaultSvcs=[
  {id:1,icon:"GEN",name:"General Car Service",desc:"Complete inspection and maintenance of your vehicle including all vital systems and components.",bullets:"Engine oil change,Air filter check,Fuel filter check,Coolant top-up,Battery check,All fluid levels,Tyre pressure,Brake inspection",price:"Starting Rs 1,499"},
  {id:2,icon:"ENG",name:"Engine Diagnostics",desc:"Advanced computerized engine scanning using latest OBD tools to pinpoint any fault or issue quickly.",bullets:"OBD2 scan,Error code reading,Engine health report,Performance analysis,Fuel system check",price:"Starting Rs 499"},
  {id:3,icon:"OIL",name:"Oil Change",desc:"Engine oil and oil filter replacement using premium quality oil recommended for your specific car model.",bullets:"Premium engine oil,Oil filter replacement,Engine flush if needed,Level check post fill,Free basic inspection",price:"Starting Rs 399"},
  {id:4,icon:"BRK",name:"Brake Repair",desc:"Complete brake system service for safe and confident stopping every time you need it.",bullets:"Brake pad replacement,Rotor check and resurfacing,Brake fluid flush,Caliper inspection,Handbrake adjustment",price:"Starting Rs 799"},
  {id:5,icon:"SUS",name:"Suspension Repair",desc:"Full suspension system overhaul for a smooth, comfortable, and safe driving experience.",bullets:"Shock absorber check,Strut replacement,Spring inspection,Wheel alignment,Steering linkage check",price:"Starting Rs 999"},
  {id:6,icon:"AC",name:"AC Service",desc:"Complete AC system restoration so your car stays cool even in the harshest Nashik summer heat.",bullets:"AC gas refilling,Compressor check,Condenser cleaning,Evaporator inspection,Cooling performance test",price:"Starting Rs 699"},
  {id:7,icon:"BAT",name:"Battery Replacement",desc:"Battery testing, jump start, and replacement with reliable branded batteries with warranty.",bullets:"Battery load test,Terminal cleaning,New battery fitting,Alternator check,Free disposal of old battery",price:"Starting Rs 2,499"},
  {id:8,icon:"ALN",name:"Wheel Alignment",desc:"Computerized 4-wheel alignment and dynamic balancing for even tyre wear and straight, safe driving.",bullets:"4-wheel laser alignment,Dynamic wheel balancing,Tyre rotation if needed,Tyre pressure adjustment,Toe and camber correction",price:"Starting Rs 599"},
  {id:9,icon:"WSH",name:"Car Washing",desc:"Professional full car wash including exterior, interior, engine bay, and tyre shine for that showroom look.",bullets:"Full exterior hand wash,Interior vacuum cleaning,Dashboard wipe and polish,Tyre shine application,Engine bay cleaning",price:"Starting Rs 299"},
  {id:10,icon:"P&D",name:"Pickup and Drop",desc:"Too busy to come to the garage? We will pick up your car from your location and drop it back when done.",bullets:"Doorstep car pickup,WhatsApp status updates,Convenient drop-back,Available Mon-Sat,Nashik city coverage",price:"Call for rates"}
];

var defaultRevs=[
  {id:1,name:"Amit Deshmukh",stars:5,text:"Best garage in Nashik hands down! Shantanu bhai fixed my Swift Dzire AC in just 2 hours. Very professional, transparent billing, and reasonable price.",loc:"Nashik, Swift Dzire owner"},
  {id:2,name:"Priya Kulkarni",stars:5,text:"My i20 engine was making a rattling noise for months. Took it to 4x4 Mechanics and they diagnosed and fixed it same day. Highly recommend!",loc:"Nashik, Hyundai i20 owner"},
  {id:3,name:"Ravi Patil",stars:5,text:"Transparent billing, genuine parts used, quick service - finally found a garage I can fully trust. My Creta runs perfectly after the full service.",loc:"Nashik, Hyundai Creta owner"},
  {id:4,name:"Snehal Joshi",stars:5,text:"Got my Honda City full service done here. Very thorough and detailed work. The car drives like it is brand new. Excellent team!",loc:"Nashik, Honda City owner"},
  {id:5,name:"Mahesh Gaikwad",stars:4,text:"Good service at reasonable rates. Got wheel alignment and brake pads done. Very professional setup with modern equipment.",loc:"Nashik, Maruti Baleno owner"},
  {id:6,name:"Kavita Sharma",stars:5,text:"Used the pickup and drop service - they were very prompt and professional. Car was returned spotless with all issues fixed.",loc:"Nashik, Hyundai Verna owner"}
];

function ld(k,d){try{var v=localStorage.getItem(k);return v?JSON.parse(v):d;}catch(e){return d;}}
function sd(k,v){try{localStorage.setItem(k,JSON.stringify(v));}catch(e){}}

var svcs=ld("4x4_svcs",defaultSvcs);
var revs=ld("4x4_revs",defaultRevs);
var bks=ld("4x4_bks",[]);
var appC=ld("4x4_app",{biz:"4x4 Mechanics Garage",tag:"Nashik ka Trusted Garage"});
var heroC=ld("4x4_hero",{l1:"Trusted",l2:"4-Wheeler",l3:"Service",sub:"Professional car repair and maintenance by expert mechanics. Genuine parts, honest pricing, quick turnaround.",badge:"Open Now - Amrutdham, Nashik"});
var setC=ld("4x4_set",{owner:"Shantanu Pawar",phone:"9403666931",addr:"Amrutdham, Nashik, Maharashtra",hrs:"Mon-Sat: 9:00 AM - 7:00 PM, Sunday: 10:00 AM - 4:00 PM"});
var logoSrc=ld("4x4_logo","/logo.png");
var adminPw=ld("4x4_pw","4x4admin@2026");
var bkFilter="all";

function gi(id){return document.getElementById(id);}

function applyAll(){applyLogo();applyApp();applyHero();applySet();renderSvcs();renderRevs();}

function applyLogo(){
  var ids=["login-logo","a-top-logo","logo-prev","pub-logo-nav","pub-logo-hero","pub-logo-about","pub-logo-footer"];
  for(var i=0;i<ids.length;i++){var el=gi(ids[i]);if(el)el.src=logoSrc;}
}

function applyApp(){
  var biz=appC.biz||"4x4 Mechanics Garage";
  var tag=appC.tag||"Nashik ka Trusted Garage";
  var el=gi("pub-biz-name");
  if(el){
    var parts=biz.split(" ");
    if(parts.length>=2){el.innerHTML=parts[0]+' <span>'+parts.slice(1).join(" ")+'</span>';}
    else{el.textContent=biz;}
  }
  var t=gi("pub-tagline");if(t)t.textContent=tag;
  var fns=["pub-footer-nm","footer-biz-nm","about-biz-nm"];
  for(var i=0;i<fns.length;i++){var e=gi(fns[i]);if(e)e.textContent=biz;}
  gi("a-biz").value=biz;
  gi("a-tag").value=tag;
}

function applyHero(){
  var t=gi("pub-hero-title");
  if(t)t.innerHTML=(heroC.l1||"Trusted")+'<br><span class="gold">'+(heroC.l2||"4-Wheeler")+'</span><br>'+(heroC.l3||"Service");
  var s=gi("pub-hero-sub");if(s)s.textContent=heroC.sub||"";
  var b=gi("pub-badge");if(b)b.textContent=heroC.badge||"Open Now - Amrutdham, Nashik";
  gi("h-l1").value=heroC.l1||"";
  gi("h-l2").value=heroC.l2||"";
  gi("h-l3").value=heroC.l3||"";
  gi("h-sub").value=heroC.sub||"";
  gi("h-badge").value=heroC.badge||"";
}

function applySet(){
  var p=setC.phone||"9403666931";
  var wa="https://wa.me/91"+p+"?text=Hi! I want to book a service at 4x4 Mechanics Garage, Nashik.";
  var o1=gi("pub-owner");if(o1)o1.textContent=setC.owner||"Shantanu Pawar";
  var a1=gi("pub-addr");if(a1)a1.textContent=setC.addr||"Amrutdham, Nashik";
  var hrs=gi("pub-hrs");if(hrs)hrs.innerHTML=(setC.hrs||"").replace(",","<br>");
  var pp=gi("pub-phone");if(pp){pp.textContent="+91 "+p;pp.href="tel:"+p;}
  var fpl=gi("f-phone-link");if(fpl){fpl.textContent=p;fpl.href="tel:"+p;}
  var ids1=["pub-call-btn","f-call","footer-call-btn"];
  for(var i=0;i<ids1.length;i++){var e=gi(ids1[i]);if(e)e.href="tel:"+p;}
  var ids2=["pub-wa-link","f-wa","footer-wa-btn","f-wa-link"];
  for(var j=0;j<ids2.length;j++){var e2=gi(ids2[j]);if(e2)e2.href=wa;}
  gi("promo-phone").href="tel:"+p;
  gi("promo-phone").textContent=p;
  var initials=(setC.owner||"SP").split(" ").map(function(w){return w[0];}).join("").substring(0,2);
  gi("owner-av").textContent=initials;
  gi("owner-nm").textContent=setC.owner||"Shantanu Pawar";
  gi("s-owner").value=setC.owner||"";
  gi("s-phone").value=p;
  gi("s-addr").value=setC.addr||"";
  gi("s-hrs").value=setC.hrs||"";
}

function renderSvcs(){
  var g=gi("pub-svc-grid");
  if(!g)return;
  var html="";
  for(var i=0;i<svcs.length;i++){
    var s=svcs[i];
    html+='<div class="svc-card" data-svcid="'+s.id+'"><div class="si">'+s.icon+'</div><h3>'+s.name+'</h3><p>'+s.desc+'</p><div class="sp">'+s.price+'</div><div class="tap-hint">Tap for details</div></div>';
  }
  g.innerHTML=html;
  var cards=g.querySelectorAll(".svc-card");
  for(var k=0;k<cards.length;k++){
    cards[k].addEventListener("click",function(){openMod(parseInt(this.getAttribute("data-svcid")));});
  }
}

function renderRevs(){
  var g=gi("pub-testi-grid");
  if(!g)return;
  var html="";
  for(var i=0;i<revs.length;i++){
    var r=revs[i];
    var starsStr="";
    for(var s=0;s<r.stars;s++){starsStr+="*";}
    html+='<div class="testi-card"><div class="stars">'+starsStr+'</div><p class="testi-txt">'+r.text+'</p><div class="testi-author"><div class="tav">'+r.name[0]+'</div><div class="tinfo"><h5>'+r.name+'</h5><p>'+r.loc+'</p><div class="verified">Verified Customer</div></div></div></div>';
  }
  g.innerHTML=html;
}

function openMod(id){
  var s=null;
  for(var i=0;i<svcs.length;i++){if(svcs[i].id===id){s=svcs[i];break;}}
  if(!s)return;
  gi("mod-icon").textContent=s.icon;
  gi("mod-title").textContent=s.name;
  gi("mod-desc").textContent=s.desc;
  gi("mod-price").textContent=s.price;
  var bullets=(s.bullets||"").split(",");
  var bhtml="";
  for(var b=0;b<bullets.length;b++){
    if(bullets[b].trim())bhtml+="<li>"+bullets[b].trim()+"</li>";
  }
  gi("mod-bullets").innerHTML=bhtml;
  var p=setC.phone||"9403666931";
  gi("mod-wa").href="https://wa.me/91"+p+"?text="+encodeURIComponent("Hi! I need "+s.name+" service for my car.");
  gi("svc-modal").classList.add("open");
}
function closeMod(){gi("svc-modal").classList.remove("open");}

function submitBooking(){
  var name=gi("f-name").value.trim();
  var phone=gi("f-phone").value.trim();
  var car=gi("f-car").value.trim();
  var svc=gi("f-svc").value;
  var issue=gi("f-issue").value.trim();
  if(!name||!phone){showToast("Naam aur phone number zaroori hai!");return;}
  var bk={id:Date.now(),name:name,phone:phone,car:car,service:svc||"General Service",issue:issue,status:"pending",date:new Date().toLocaleString("en-IN")};
  bks.unshift(bk);sd("4x4_bks",bks);
  var p=setC.phone||"9403666931";
  var msg="Hello 4x4 Mechanics Garage!\n\nName: "+name+"\nPhone: "+phone+"\nCar: "+(car||"Not specified")+"\nService: "+(svc||"General Service")+"\nIssue: "+(issue||"Will discuss in person")+"\n\nKripya meri booking confirm karein. Thank you!";
  window.open("https://wa.me/91"+p+"?text="+encodeURIComponent(msg),"_blank");
  showToast("Booking WhatsApp pe bhej di gayi!");
  var clearIds=["f-name","f-phone","f-car","f-issue"];
  for(var i=0;i<clearIds.length;i++){gi(clearIds[i]).value="";}
  gi("f-svc").value="";
}

function openLogin(){gi("login-modal").classList.add("active");}
function closeLogin(){gi("login-modal").classList.remove("active");}
function doLogin(){
  var u=gi("lu").value.trim();
  var p=gi("lp").value;
  if(u==="admin"&&p===adminPw){
    closeLogin();
    gi("public-site").style.display="none";
    gi("admin-panel").style.display="block";
    gi("a-date").textContent=new Date().toLocaleDateString("en-IN",{weekday:"long",day:"numeric",month:"long",year:"numeric"});
    refreshAdmin();
  } else {
    gi("lerr").style.display="block";
  }
}
function logout(){
  gi("admin-panel").style.display="none";
  gi("public-site").style.display="block";
}

function goTab(name,el){
  var tabs=document.querySelectorAll(".atab");
  for(var i=0;i<tabs.length;i++){tabs[i].classList.remove("on");}
  var secs=document.querySelectorAll(".asec");
  for(var j=0;j<secs.length;j++){secs[j].classList.remove("on");}
  el.classList.add("on");
  gi("tab-"+name).classList.add("on");
}

function filterBks(f){bkFilter=f;renderAdminBks();}

function refreshAdmin(){
  gi("st-total").textContent=bks.length;
  gi("st-pend").textContent=bks.filter(function(b){return b.status==="pending";}).length;
  gi("st-conf").textContent=bks.filter(function(b){return b.status==="confirmed";}).length;
  gi("st-done").textContent=bks.filter(function(b){return b.status==="done";}).length;
  gi("bk-ct").textContent="("+bks.length+")";
  gi("svc-ct").textContent="("+svcs.length+")";
  gi("rev-ct").textContent="("+revs.length+")";
  renderAdminBks();

  var svcHtml="";
  for(var i=0;i<svcs.length;i++){
    var s=svcs[i];
    svcHtml+='<div class="svc-ac"><div class="ic">'+s.icon+'</div><h4>'+s.name+'</h4><p>'+s.desc.substring(0,55)+'...</p><div class="pr">'+s.price+'</div><button class="btn-r" data-delsvc="'+s.id+'">Delete</button></div>';
  }
  gi("a-svc-list").innerHTML=svcHtml;
  var delSvcBtns=gi("a-svc-list").querySelectorAll("[data-delsvc]");
  for(var k=0;k<delSvcBtns.length;k++){
    delSvcBtns[k].addEventListener("click",function(){delSvc(parseInt(this.getAttribute("data-delsvc")));});
  }

  if(revs.length===0){
    gi("a-rev-list").innerHTML='<p style="color:var(--gray);font-size:.84rem;">No reviews yet.</p>';
  } else {
    var revHtml="";
    for(var r=0;r<revs.length;r++){
      var rv=revs[r];
      var starsStr="";
      for(var s2=0;s2<rv.stars;s2++){starsStr+="*";}
      revHtml+='<div class="ritem"><div><h5>'+rv.name+" "+starsStr+'</h5><p>"'+rv.text.substring(0,80)+'..."</p><p style="color:var(--gold);font-size:.73rem;margin-top:3px;">'+rv.loc+'</p></div><button class="btn-r" data-delrev="'+rv.id+'">X</button></div>';
    }
    gi("a-rev-list").innerHTML=revHtml;
    var delRevBtns=gi("a-rev-list").querySelectorAll("[data-delrev]");
    for(var m=0;m<delRevBtns.length;m++){
      delRevBtns[m].addEventListener("click",function(){delRev(parseInt(this.getAttribute("data-delrev")));});
    }
  }

  var recent=bks.slice(0,5);
  if(recent.length===0){
    gi("dash-bks").innerHTML='<p style="color:var(--gray);font-size:.84rem;">No bookings yet.</p>';
  } else {
    var dh="";
    for(var d=0;d<recent.length;d++){dh+=bkHtml(recent[d]);}
    gi("dash-bks").innerHTML=dh;
    attachBkListeners(gi("dash-bks"));
  }
}

function renderAdminBks(){
  var filtered=bkFilter==="all"?bks:bks.filter(function(b){return b.status===bkFilter;});
  if(filtered.length===0){
    gi("all-bks-list").innerHTML='<p style="color:var(--gray);font-size:.84rem;">No '+(bkFilter!=="all"?bkFilter+" ":"")+'bookings.</p>';
  } else {
    var html="";
    for(var i=0;i<filtered.length;i++){html+=bkHtml(filtered[i]);}
    gi("all-bks-list").innerHTML=html;
    attachBkListeners(gi("all-bks-list"));
  }
}

function bkHtml(b){
  return '<div class="bitem"><div><h4>'+b.name+' | '+b.phone+'</h4><p>'+(b.car||"N/A")+' | '+b.service+' | '+b.date+'</p>'+(b.issue?'<p style="margin-top:3px;color:#999;">'+b.issue+'</p>':'')+'</div><div style="display:flex;gap:7px;align-items:center;flex-wrap:wrap;"><button class="bs s-'+b.status+'" data-cyclebk="'+b.id+'">'+b.status.toUpperCase()+'</button><a href="tel:'+b.phone+'" style="color:var(--gold);font-size:.75rem;text-decoration:none;">Call</a><a href="https://wa.me/91'+b.phone+'" target="_blank" style="color:#25D366;font-size:.75rem;text-decoration:none;">WA</a><button class="btn-r" data-delbk="'+b.id+'">X</button></div></div>';
}

function attachBkListeners(container){
  var cycleBtns=container.querySelectorAll("[data-cyclebk]");
  for(var i=0;i<cycleBtns.length;i++){
    cycleBtns[i].addEventListener("click",function(){cycleS(parseInt(this.getAttribute("data-cyclebk")));});
  }
  var delBtns=container.querySelectorAll("[data-delbk]");
  for(var j=0;j<delBtns.length;j++){
    delBtns[j].addEventListener("click",function(){delBk(parseInt(this.getAttribute("data-delbk")));});
  }
}

function cycleS(id){
  var b=null;
  for(var i=0;i<bks.length;i++){if(bks[i].id===id){b=bks[i];break;}}
  if(!b)return;
  var s=["pending","confirmed","done"];
  b.status=s[(s.indexOf(b.status)+1)%s.length];
  sd("4x4_bks",bks);refreshAdmin();showToast("Status updated: "+b.status);
}
function delBk(id){
  if(!confirm("Delete this booking?"))return;
  bks=bks.filter(function(x){return x.id!==id;});
  sd("4x4_bks",bks);refreshAdmin();
}

function uploadLogo(e){
  var f=e.target.files[0];if(!f)return;
  var r=new FileReader();
  r.onload=function(ev){logoSrc=ev.target.result;gi("logo-prev").src=logoSrc;};
  r.readAsDataURL(f);
}
function saveLogo(){sd("4x4_logo",logoSrc);applyLogo();showToast("Logo updated everywhere!");}

function saveAppearance(){
  appC.biz=gi("a-biz").value||"4x4 Mechanics Garage";
  appC.tag=gi("a-tag").value||"";
  sd("4x4_app",appC);applyApp();showToast("Name and tagline updated!");
}

function prevHero(){
  var l1=gi("h-l1").value||"Trusted";
  var l2=gi("h-l2").value||"4-Wheeler";
  var l3=gi("h-l3").value||"Service";
  var sub=gi("h-sub").value||"";
  gi("hero-prev").innerHTML='<div class="pt">'+l1+' <span>'+l2+'</span> '+l3+'</div><div class="ps">'+sub+'</div>';
}
function saveHero(){
  heroC={l1:gi("h-l1").value||"Trusted",l2:gi("h-l2").value||"4-Wheeler",l3:gi("h-l3").value||"Service",sub:gi("h-sub").value,badge:gi("h-badge").value};
  sd("4x4_hero",heroC);applyHero();showToast("Hero section updated!");
}

function addService(){
  var n=gi("sn").value.trim();
  var ic=gi("si").value.trim()||"SVC";
  var d=gi("sd").value.trim();
  var bul=gi("sb").value.trim();
  var p=gi("sp").value.trim()||"Call for price";
  if(!n||!d){showToast("Service name aur description zaroori hai");return;}
  svcs.push({id:Date.now(),icon:ic,name:n,desc:d,bullets:bul,price:p});
  sd("4x4_svcs",svcs);
  var clearIds=["sn","si","sd","sb","sp"];
  for(var i=0;i<clearIds.length;i++){gi(clearIds[i]).value="";}
  renderSvcs();refreshAdmin();showToast("Service add ho gayi!");
}
function delSvc(id){
  if(!confirm("Delete this service?"))return;
  svcs=svcs.filter(function(x){return x.id!==id;});
  sd("4x4_svcs",svcs);renderSvcs();refreshAdmin();showToast("Service removed");
}

function addReview(){
  var n=gi("rn").value.trim();
  var s=parseInt(gi("rs").value);
  var t=gi("rt").value.trim();
  var l=gi("rl").value.trim()||"Nashik";
  if(!n||!t){showToast("Naam aur review text zaroori hai");return;}
  revs.unshift({id:Date.now(),name:n,stars:s,text:t,loc:l});
  sd("4x4_revs",revs);
  var clearIds=["rn","rt","rl"];
  for(var i=0;i<clearIds.length;i++){gi(clearIds[i]).value="";}
  renderRevs();refreshAdmin();showToast("Review add ho gayi!");
}
function delRev(id){
  if(!confirm("Delete this review?"))return;
  revs=revs.filter(function(x){return x.id!==id;});
  sd("4x4_revs",revs);renderRevs();refreshAdmin();
}

function saveSettings(){
  setC={owner:gi("s-owner").value,phone:gi("s-phone").value,addr:gi("s-addr").value,hrs:gi("s-hrs").value};
  sd("4x4_set",setC);applySet();showToast("Settings saved!");
}
function changePass(){
  var np=gi("np").value;
  var cp=gi("cp").value;
  if(!np){showToast("New password enter karo");return;}
  if(np!==cp){showToast("Passwords match nahi ho rahe");return;}
  if(np.length<6){showToast("Minimum 6 characters chahiye");return;}
  adminPw=np;sd("4x4_pw",np);
  gi("np").value="";
  gi("cp").value="";
  showToast("Password change ho gaya!");
}

function toggleMob(){gi("mob-menu").classList.toggle("open");}

function showToast(msg){
  var t=gi("toast");
  t.textContent=msg;t.classList.add("show");
  setTimeout(function(){t.classList.remove("show");},3200);
}

function initEvents(){
  gi("lp").addEventListener("keydown",function(e){if(e.key==="Enter")doLogin();});
  gi("lu").addEventListener("keydown",function(e){if(e.key==="Enter")doLogin();});

  var tabBtns=document.querySelectorAll(".atab");
  for(var i=0;i<tabBtns.length;i++){
    tabBtns[i].addEventListener("click",function(){goTab(this.getAttribute("data-tab"),this);});
  }

  var filterBtns=document.querySelectorAll("[data-filter]");
  for(var j=0;j<filterBtns.length;j++){
    filterBtns[j].addEventListener("click",function(){filterBks(this.getAttribute("data-filter"));});
  }

  gi("logo-file").addEventListener("change",uploadLogo);
  gi("save-logo-btn").addEventListener("click",saveLogo);
  gi("save-app-btn").addEventListener("click",saveAppearance);

  var heroInputs=["h-l1","h-l2","h-l3","h-sub"];
  for(var k=0;k<heroInputs.length;k++){
    gi(heroInputs[k]).addEventListener("input",prevHero);
  }
  gi("save-hero-btn").addEventListener("click",saveHero);

  gi("add-svc-btn").addEventListener("click",addService);
  gi("add-rev-btn").addEventListener("click",addReview);
  gi("save-set-btn").addEventListener("click",saveSettings);
  gi("change-pass-btn").addEventListener("click",changePass);

  gi("hamburger-btn").addEventListener("click",toggleMob);
  var mobLinks=gi("mob-menu").querySelectorAll("a");
  for(var m=0;m<mobLinks.length;m++){
    mobLinks[m].addEventListener("click",toggleMob);
  }

  gi("admin-trigger-btn").addEventListener("click",function(){ window.location.href="/admin/login"; });
  var logoutBtn=document.querySelector(".btn-logout");if(logoutBtn)logoutBtn.addEventListener("click",logout);
  var backLink=document.querySelector(".back-link");if(backLink)backLink.addEventListener("click",closeLogin);
  var loginBtn=document.querySelector(".btn-login");if(loginBtn)loginBtn.addEventListener("click",doLogin);
  gi("submit-booking-btn").addEventListener("click",submitBooking);
  gi("mod-close-btn").addEventListener("click",closeMod);
  gi("mod-book-btn").addEventListener("click",closeMod);
  gi("svc-modal").addEventListener("click",function(e){if(e.target===gi("svc-modal"))closeMod();});

}

window.addEventListener("scroll",function(){
  var nb=gi("navbar");
  if(nb)nb.style.background=window.scrollY>60?"rgba(10,10,10,.98)":"rgba(10,10,10,.96)";
});

document.addEventListener("DOMContentLoaded",function(){
  applyAll();
  initEvents();
});

"""
