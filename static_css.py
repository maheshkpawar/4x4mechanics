STYLES = """


:root{--gold:#C9A84C;--gold-l:#E8C96A;--gold-d:#8B6914;--black:#0A0A0A;--dark:#111;--dark2:#1A1A1A;--dark3:#222;--gray:#888;--gray-l:#CCC;--white:#F5F0E8;--red:#C0392B;}
*{margin:0;padding:0;box-sizing:border-box;}
html{scroll-behavior:smooth;}
body{font-family:"Inter",sans-serif;background:var(--black);color:var(--white);overflow-x:hidden;}
::-webkit-scrollbar{width:5px;}
::-webkit-scrollbar-track{background:var(--dark);}
::-webkit-scrollbar-thumb{background:var(--gold-d);border-radius:3px;}
.toast{position:fixed;bottom:24px;left:50%;transform:translateX(-50%) translateY(100px);background:var(--gold);color:var(--black);padding:12px 28px;border-radius:8px;font-weight:700;z-index:99999;transition:transform .4s;pointer-events:none;font-size:.9rem;}
.toast.show{transform:translateX(-50%) translateY(0);}
#login-modal{display:none;position:fixed;inset:0;background:rgba(0,0,0,.97);z-index:10000;align-items:center;justify-content:center;}
#login-modal.active{display:flex;}
.login-box{background:var(--dark2);border:1px solid var(--gold);border-radius:16px;padding:44px 36px;width:90%;max-width:400px;text-align:center;}
.login-box img{width:90px;height:90px;border-radius:50%;object-fit:contain;background:#000;border:2px solid var(--gold);margin:0 auto 16px;display:block;}
.login-box h2{font-family:"Bebas Neue";font-size:2rem;color:var(--gold);margin-bottom:4px;}
.login-box .sub{color:var(--gray);font-size:.82rem;margin-bottom:24px;}
.lerr{color:#e74c3c;font-size:.8rem;margin-bottom:10px;display:none;}
.login-box input{width:100%;padding:13px 15px;margin-bottom:13px;background:var(--dark3);border:1px solid #333;border-radius:8px;color:var(--white);font-size:.95rem;outline:none;transition:border-color .3s;}
.login-box input:focus{border-color:var(--gold);}
.btn-login{width:100%;padding:14px;background:var(--gold);color:var(--black);font-weight:700;border:none;border-radius:8px;cursor:pointer;font-family:"Oswald";letter-spacing:1px;font-size:1.05rem;transition:background .3s;}
.btn-login:hover{background:var(--gold-l);}
.back-link{background:none;border:none;color:var(--gray);cursor:pointer;margin-top:14px;font-size:.76rem;text-decoration:underline;display:block;}
.default-hint{color:#444;font-size:.74rem;margin-top:10px;}
#admin-panel{display:none;min-height:100vh;background:var(--black);}
.a-topbar{background:var(--dark2);border-bottom:2px solid var(--gold);padding:12px 24px;display:flex;align-items:center;justify-content:space-between;position:sticky;top:0;z-index:100;}
.a-topbar-l{display:flex;align-items:center;gap:12px;}
.a-topbar img{width:40px;height:40px;border-radius:50%;object-fit:contain;background:#000;border:2px solid var(--gold);}
.a-topbar h1{font-family:"Bebas Neue";font-size:1.5rem;color:var(--gold);}
.a-topbar span{color:var(--gray);font-size:.75rem;}
.btn-logout{background:transparent;border:1px solid var(--gold);color:var(--gold);padding:7px 18px;border-radius:6px;cursor:pointer;font-size:.8rem;transition:all .3s;}
.btn-logout:hover{background:var(--gold);color:var(--black);}
.a-tabs{display:flex;background:var(--dark);border-bottom:1px solid #222;overflow-x:auto;}
.atab{padding:13px 20px;background:transparent;border:none;color:var(--gray);cursor:pointer;font-family:"Oswald";font-size:.88rem;letter-spacing:.5px;border-bottom:3px solid transparent;transition:all .3s;white-space:nowrap;flex-shrink:0;}
.atab.on{color:var(--gold);border-bottom-color:var(--gold);background:rgba(201,168,76,.04);}
.a-body{padding:24px;max-width:1100px;margin:0 auto;}
.asec{display:none;}.asec.on{display:block;}
.acard{background:var(--dark2);border:1px solid #252525;border-radius:12px;padding:22px;margin-bottom:18px;}
.acard h3{font-family:"Oswald";font-size:1.1rem;color:var(--gold);margin-bottom:14px;padding-bottom:10px;border-bottom:1px solid #252525;}
.a-stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:14px;margin-bottom:20px;}
.astat{background:var(--dark3);border-radius:10px;padding:18px;border-left:3px solid var(--gold);}
.astat h4{font-size:.72rem;color:var(--gray);text-transform:uppercase;letter-spacing:1px;margin-bottom:5px;}
.astat .num{font-family:"Bebas Neue";font-size:2rem;color:var(--gold);}
.af label{display:block;color:var(--gray);font-size:.76rem;text-transform:uppercase;letter-spacing:.5px;margin-bottom:5px;}
.af input,.af textarea,.af select{width:100%;padding:11px 13px;background:var(--dark3);border:1px solid #2e2e2e;border-radius:7px;color:var(--white);font-size:.88rem;outline:none;margin-bottom:13px;transition:border-color .3s;font-family:inherit;}
.af input:focus,.af textarea:focus,.af select:focus{border-color:var(--gold);}
.af textarea{resize:vertical;min-height:76px;}
.af .fr2{display:grid;grid-template-columns:1fr 1fr;gap:14px;}
.btn-g{background:var(--gold);color:var(--black);padding:11px 26px;border:none;border-radius:7px;cursor:pointer;font-family:"Oswald";font-size:.95rem;font-weight:600;letter-spacing:.5px;transition:background .3s;}
.btn-g:hover{background:var(--gold-l);}
.btn-r{background:#c0392b;color:#fff;padding:6px 12px;border:none;border-radius:5px;cursor:pointer;font-size:.76rem;}
.btn-o{background:transparent;color:var(--gold);padding:7px 14px;border:1px solid var(--gold);border-radius:6px;cursor:pointer;font-size:.78rem;transition:all .3s;margin-left:6px;}
.btn-o:hover{background:var(--gold);color:var(--black);}
.blist{display:flex;flex-direction:column;gap:9px;}
.bitem{background:var(--dark3);border-radius:8px;padding:13px 15px;border-left:3px solid var(--gold);display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px;}
.bitem h4{color:var(--white);font-size:.87rem;margin-bottom:2px;}
.bitem p{color:var(--gray);font-size:.77rem;}
.bs{padding:3px 11px;border-radius:20px;font-size:.72rem;font-weight:600;cursor:pointer;border:none;}
.s-pending{background:#2d1b00;color:#f39c12;}
.s-confirmed{background:#0d2e1a;color:#27ae60;}
.s-done{background:#1a1a2e;color:#9b59b6;}
.svc-ag{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:12px;}
.svc-ac{background:var(--dark3);border-radius:9px;padding:16px;border:1px solid #222;}
.svc-ac .ic{font-size:1.6rem;margin-bottom:7px;}
.svc-ac h4{color:var(--white);font-size:.86rem;margin-bottom:3px;}
.svc-ac p{color:var(--gray);font-size:.75rem;margin-bottom:6px;}
.svc-ac .pr{color:var(--gold);font-size:.74rem;margin-bottom:8px;}
.img-up{border:2px dashed #2a2a2a;border-radius:10px;padding:28px;text-align:center;cursor:pointer;transition:border-color .3s;margin-bottom:13px;position:relative;}
.img-up:hover{border-color:var(--gold);}
.img-up input{position:absolute;inset:0;opacity:0;cursor:pointer;width:100%;height:100%;}
.img-up img{width:110px;height:110px;border-radius:50%;object-fit:contain;background:#000;border:2px solid var(--gold);margin:0 auto 10px;display:block;}
.img-up p{color:var(--gray);font-size:.82rem;}
.img-up .hint{color:var(--gold);font-size:.74rem;margin-top:3px;}
.h-prev{background:var(--dark3);border-radius:7px;padding:18px;margin-bottom:14px;border:1px solid #2a2a2a;}
.h-prev .pt{font-family:"Bebas Neue";font-size:1.8rem;color:var(--white);line-height:1.1;}
.h-prev .pt span{color:var(--gold);}
.h-prev .ps{color:var(--gray);font-size:.8rem;margin-top:6px;}
.rlist{display:flex;flex-direction:column;gap:9px;}
.ritem{background:var(--dark3);border-radius:8px;padding:13px;display:flex;justify-content:space-between;align-items:flex-start;gap:10px;}
.ritem h5{color:var(--white);font-size:.84rem;}
.ritem p{color:var(--gray);font-size:.76rem;margin-top:2px;}
#public-site{display:block;}
nav{position:fixed;top:0;left:0;right:0;z-index:1000;background:rgba(10,10,10,.96);backdrop-filter:blur(14px);border-bottom:1px solid rgba(201,168,76,.18);padding:0 5%;display:flex;align-items:center;justify-content:space-between;height:70px;transition:all .3s;}
.nav-logo{display:flex;align-items:center;gap:10px;text-decoration:none;}
.nav-logo img{width:46px;height:46px;border-radius:50%;object-fit:contain;background:#000;border:2px solid var(--gold);padding:2px;flex-shrink:0;}
.nav-logo-t{line-height:1.1;}
.nav-logo-name{font-family:"Bebas Neue";font-size:1.35rem;color:var(--white);letter-spacing:.5px;}
.nav-logo-name span{color:var(--gold);}
.nav-logo-sub{font-size:.6rem;color:var(--gray);letter-spacing:1.5px;text-transform:uppercase;}
.nav-links{display:flex;align-items:center;gap:26px;list-style:none;}
.nav-links a{color:var(--gray-l);text-decoration:none;font-size:.83rem;font-weight:500;transition:color .3s;position:relative;}
.nav-links a::after{content:"";position:absolute;bottom:-4px;left:0;right:0;height:1px;background:var(--gold);transform:scaleX(0);transition:transform .3s;}
.nav-links a:hover{color:var(--gold);}
.nav-links a:hover::after{transform:scaleX(1);}
.nav-cta{background:var(--gold)!important;color:var(--black)!important;padding:9px 18px;border-radius:6px;font-weight:700!important;}
.nav-cta:hover{background:var(--gold-l)!important;}
.nav-cta::after{display:none!important;}
.hamburger{display:none;flex-direction:column;gap:5px;cursor:pointer;background:none;border:none;padding:8px;}
.hamburger span{display:block;width:24px;height:2px;background:var(--white);transition:all .3s;}
.mob-menu{display:none;position:fixed;top:70px;left:0;right:0;background:var(--dark);border-bottom:1px solid rgba(201,168,76,.15);z-index:999;padding:18px 5%;}
.mob-menu.open{display:block;}
.mob-menu a{display:block;color:var(--gray-l);text-decoration:none;padding:11px 0;border-bottom:1px solid #1a1a1a;font-size:.92rem;}
.mob-cta{background:var(--gold);color:var(--black)!important;text-align:center;border-radius:8px;padding:13px!important;margin-top:12px!important;font-weight:700;border:none!important;}
#hero{min-height:100vh;background:linear-gradient(135deg,#0A0A0A 0%,#1a1400 50%,#0A0A0A 100%);display:flex;align-items:center;position:relative;overflow:hidden;padding-top:70px;}
.hero-bg{position:absolute;inset:0;background:radial-gradient(ellipse at 70% 50%,rgba(201,168,76,.13) 0%,transparent 60%),radial-gradient(ellipse at 15% 80%,rgba(201,168,76,.06) 0%,transparent 50%);}
.hero-grid{position:absolute;inset:0;background-image:linear-gradient(rgba(201,168,76,.04) 1px,transparent 1px),linear-gradient(90deg,rgba(201,168,76,.04) 1px,transparent 1px);background-size:60px 60px;}
.hero-inner{position:relative;z-index:2;padding:60px 5%;width:100%;display:flex;align-items:center;justify-content:space-between;gap:40px;flex-wrap:wrap;}
.hero-text{max-width:620px;}
.hero-badge{display:inline-flex;align-items:center;gap:8px;background:rgba(201,168,76,.1);border:1px solid rgba(201,168,76,.3);color:var(--gold);padding:7px 16px;border-radius:30px;font-size:.74rem;font-weight:600;letter-spacing:1px;margin-bottom:22px;}
.hero-badge::before{content:"●";font-size:.44rem;animation:pulse 2s infinite;}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.3}}
.hero-title{font-family:"Bebas Neue";font-size:clamp(3.2rem,9vw,7rem);line-height:.9;margin-bottom:20px;}
.hero-title .gold{color:var(--gold);}
.hero-sub{font-size:clamp(.88rem,1.8vw,1.1rem);color:var(--gray-l);line-height:1.75;max-width:500px;margin-bottom:34px;font-weight:300;}
.hero-btns{display:flex;gap:13px;flex-wrap:wrap;}
.btn-p{background:var(--gold);color:var(--black);padding:15px 30px;border-radius:8px;font-family:"Oswald";font-size:1rem;font-weight:600;letter-spacing:1px;text-decoration:none;border:none;cursor:pointer;transition:all .3s;display:inline-flex;align-items:center;gap:8px;}
.btn-p:hover{background:var(--gold-l);transform:translateY(-2px);box-shadow:0 8px 28px rgba(201,168,76,.4);}
.btn-s{background:transparent;color:var(--white);padding:15px 30px;border-radius:8px;font-family:"Oswald";font-size:1rem;font-weight:600;letter-spacing:1px;text-decoration:none;border:2px solid rgba(255,255,255,.22);transition:all .3s;display:inline-flex;align-items:center;gap:8px;}
.btn-s:hover{border-color:var(--gold);color:var(--gold);}
.hero-stats{display:flex;gap:32px;margin-top:44px;flex-wrap:wrap;}
.hst .n{font-family:"Bebas Neue";font-size:2.4rem;color:var(--gold);}
.hst .l{font-size:.68rem;color:var(--gray);text-transform:uppercase;letter-spacing:1px;}
.hero-logo-side{flex-shrink:0;}
.hero-logo-img{width:clamp(180px,26vw,320px);height:clamp(180px,26vw,320px);object-fit:contain;filter:drop-shadow(0 0 50px rgba(201,168,76,.35));animation:floatY 4s ease-in-out infinite;}
@keyframes floatY{0%,100%{transform:translateY(0)}50%{transform:translateY(-14px)}}
.promo-bar{background:var(--gold);padding:12px 5%;display:flex;align-items:center;justify-content:center;gap:20px;flex-wrap:wrap;}
.promo-bar span{color:var(--black);font-size:.82rem;font-weight:600;}
.promo-bar .divider{color:rgba(0,0,0,.3);}
.promo-bar a{color:var(--black);font-weight:700;text-decoration:none;border-bottom:1px solid rgba(0,0,0,.3);}
section{padding:90px 5%;}
.eyebrow{font-size:.7rem;color:var(--gold);text-transform:uppercase;letter-spacing:3px;font-weight:600;margin-bottom:10px;display:flex;align-items:center;gap:10px;}
.eyebrow::before{content:"";width:28px;height:1px;background:var(--gold);}
.sec-title{font-family:"Bebas Neue";font-size:clamp(2.2rem,5vw,3.8rem);line-height:1;margin-bottom:12px;}
.sec-title .gold{color:var(--gold);}
.sec-desc{color:var(--gray);max-width:540px;line-height:1.8;font-size:.9rem;}
#about{background:var(--dark);}
.about-grid{display:grid;grid-template-columns:1fr 1fr;gap:70px;align-items:center;}
.about-vis{position:relative;text-align:center;}
.about-logo-big{width:280px;height:280px;border-radius:50%;object-fit:contain;background:#000;border:3px solid rgba(201,168,76,.25);padding:8px;margin:0 auto;display:block;box-shadow:0 0 60px rgba(201,168,76,.12);}
.about-badge-box{position:absolute;bottom:-12px;right:10px;background:var(--gold);color:var(--black);padding:14px 18px;border-radius:10px;font-family:"Bebas Neue";text-align:center;box-shadow:0 6px 22px rgba(201,168,76,.4);}
.about-badge-box .yr{font-size:2.2rem;line-height:1;}
.about-badge-box .yt{font-size:.8rem;letter-spacing:1px;}
.about-features{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:28px 0;}
.about-feat{background:var(--dark2);border:1px solid rgba(201,168,76,.1);border-radius:10px;padding:16px;display:flex;align-items:flex-start;gap:10px;}
.about-feat .afi{font-size:1.4rem;flex-shrink:0;}
.about-feat h4{color:var(--white);font-size:.86rem;margin-bottom:3px;}
.about-feat p{color:var(--gray);font-size:.76rem;line-height:1.5;}
.owner-card{display:flex;align-items:center;gap:14px;background:var(--dark2);border:1px solid rgba(201,168,76,.15);border-radius:10px;padding:16px;margin-top:20px;}
.owner-av{width:52px;height:52px;background:var(--gold);border-radius:50%;display:flex;align-items:center;justify-content:center;color:var(--black);font-family:"Bebas Neue";font-size:1.3rem;flex-shrink:0;}
.owner-info h4{color:var(--white);font-size:.9rem;}
.owner-info p{color:var(--gold);font-size:.76rem;}
.owner-info small{color:var(--gray);font-size:.72rem;}
.apoints{display:flex;flex-direction:column;gap:9px;margin-top:18px;}
.apoint{display:flex;align-items:center;gap:10px;color:var(--gray-l);font-size:.86rem;}
.apoint::before{content:"✓";color:var(--gold);font-weight:700;flex-shrink:0;}
#services{background:var(--black);}
.svc-header{display:flex;justify-content:space-between;align-items:flex-end;flex-wrap:wrap;gap:20px;margin-bottom:48px;}
.svc-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(270px,1fr));gap:22px;}
.svc-card{background:var(--dark2);border:1px solid rgba(201,168,76,.08);border-radius:14px;padding:28px;transition:all .3s;cursor:pointer;position:relative;overflow:hidden;}
.svc-card::before{content:"";position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,var(--gold-d),var(--gold),var(--gold-d));transform:scaleX(0);transition:transform .3s;}
.svc-card:hover{border-color:rgba(201,168,76,.35);transform:translateY(-5px);box-shadow:0 12px 40px rgba(0,0,0,.5);}
.svc-card:hover::before{transform:scaleX(1);}
.svc-card .si{font-size:2.4rem;margin-bottom:16px;}
.svc-card h3{font-family:"Oswald";font-size:1.15rem;color:var(--white);margin-bottom:8px;font-weight:600;}
.svc-card p{color:var(--gray);font-size:.82rem;line-height:1.7;}
.svc-card .sp{color:var(--gold);font-size:.78rem;font-weight:600;margin-top:14px;display:flex;align-items:center;gap:5px;}
.svc-card .tap-hint{color:#444;font-size:.7rem;margin-top:8px;}
#why{background:var(--dark);}
.why-intro{display:flex;justify-content:space-between;align-items:flex-end;flex-wrap:wrap;gap:20px;margin-bottom:48px;}
.why-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:26px;}
.why-card{text-align:center;padding:30px 20px;background:var(--dark2);border:1px solid rgba(201,168,76,.07);border-radius:14px;transition:all .3s;}
.why-card:hover{border-color:rgba(201,168,76,.25);transform:translateY(-3px);}
.why-icon{width:68px;height:68px;border-radius:14px;background:rgba(201,168,76,.08);border:1px solid rgba(201,168,76,.18);display:flex;align-items:center;justify-content:center;font-size:1.9rem;margin:0 auto 18px;transition:all .3s;}
.why-card:hover .why-icon{background:var(--gold);border-color:var(--gold);}
.why-card h3{font-family:"Oswald";font-size:1.1rem;color:var(--white);margin-bottom:8px;}
.why-card p{color:var(--gray);font-size:.82rem;line-height:1.7;}
#process{background:var(--black);}
.process-steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:0;margin-top:48px;position:relative;}
.process-steps::before{content:"";position:absolute;top:36px;left:0;right:0;height:2px;background:linear-gradient(90deg,transparent,var(--gold),transparent);z-index:0;}
.p-step{text-align:center;padding:0 20px;position:relative;z-index:1;}
.p-num{width:72px;height:72px;border-radius:50%;background:var(--gold);color:var(--black);font-family:"Bebas Neue";font-size:2rem;display:flex;align-items:center;justify-content:center;margin:0 auto 18px;box-shadow:0 0 0 6px rgba(201,168,76,.12);}
.p-step h3{font-family:"Oswald";font-size:1.1rem;color:var(--white);margin-bottom:8px;}
.p-step p{color:var(--gray);font-size:.82rem;line-height:1.6;}
#testimonials{background:var(--dark);}
.testi-header{margin-bottom:48px;}
.testi-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:20px;}
.testi-card{background:var(--dark2);border:1px solid rgba(201,168,76,.08);border-radius:14px;padding:26px;transition:all .3s;position:relative;}
.testi-card:hover{border-color:rgba(201,168,76,.28);transform:translateY(-3px);}
.testi-card .quote{font-size:3rem;color:rgba(201,168,76,.15);font-family:"Bebas Neue";line-height:1;margin-bottom:8px;}
.stars{color:var(--gold);font-size:.95rem;margin-bottom:12px;letter-spacing:1px;}
.testi-txt{color:var(--gray-l);font-size:.86rem;line-height:1.8;margin-bottom:18px;}
.testi-author{display:flex;align-items:center;gap:10px;border-top:1px solid #1e1e1e;padding-top:14px;}
.tav{width:40px;height:40px;border-radius:50%;background:linear-gradient(135deg,var(--gold-d),var(--gold));display:flex;align-items:center;justify-content:center;color:var(--black);font-weight:700;font-size:.88rem;flex-shrink:0;}
.tinfo h5{color:var(--white);font-size:.86rem;}
.tinfo p{color:var(--gray);font-size:.74rem;}
.verified{display:inline-flex;align-items:center;gap:4px;background:rgba(39,174,96,.1);color:#27ae60;font-size:.68rem;padding:2px 7px;border-radius:10px;margin-top:3px;}
#contact{background:var(--black);}
.contact-grid{display:grid;grid-template-columns:1fr 1fr;gap:60px;margin-top:44px;}
.cinfo-items{display:flex;flex-direction:column;gap:18px;}
.citem{display:flex;align-items:flex-start;gap:13px;}
.cicon{width:46px;height:46px;border-radius:9px;background:rgba(201,168,76,.08);border:1px solid rgba(201,168,76,.18);display:flex;align-items:center;justify-content:center;font-size:1.1rem;flex-shrink:0;}
.citem h4{color:var(--gold);font-size:.72rem;text-transform:uppercase;letter-spacing:1px;margin-bottom:3px;}
.citem p,.citem a{color:var(--gray-l);font-size:.88rem;text-decoration:none;line-height:1.5;}
.citem a:hover{color:var(--gold);}
.map-box{background:var(--dark2);border:1px solid rgba(201,168,76,.12);border-radius:10px;height:210px;display:flex;align-items:center;justify-content:center;flex-direction:column;gap:10px;color:var(--gray);font-size:.86rem;margin-top:20px;text-align:center;}
.map-box a{color:var(--gold);font-size:.82rem;text-decoration:none;margin-top:6px;}
.cform{display:flex;flex-direction:column;gap:13px;}
.fg{display:flex;flex-direction:column;gap:5px;}
.fg label{color:var(--gray);font-size:.74rem;text-transform:uppercase;letter-spacing:.5px;}
.fg input,.fg select,.fg textarea{padding:12px 14px;background:var(--dark2);border:1px solid rgba(255,255,255,.07);border-radius:7px;color:var(--white);font-size:.88rem;font-family:inherit;outline:none;transition:border-color .3s;}
.fg input:focus,.fg select:focus,.fg textarea:focus{border-color:var(--gold);}
.fg select option{background:var(--dark2);}
.fg textarea{resize:vertical;min-height:90px;}
.fr2{display:grid;grid-template-columns:1fr 1fr;gap:13px;}
.form-note{color:var(--gray);font-size:.72rem;text-align:center;}
footer{background:var(--dark2);border-top:1px solid rgba(201,168,76,.12);padding:56px 5% 28px;}
.footer-grid{display:grid;grid-template-columns:1.6fr 1fr 1fr;gap:50px;margin-bottom:40px;}
.fb-logo{display:flex;align-items:center;gap:10px;margin-bottom:14px;}
.fb-logo img{width:46px;height:46px;border-radius:50%;object-fit:contain;background:#000;border:2px solid var(--gold);}
.fb-logo h3{font-family:"Bebas Neue";font-size:1.6rem;color:var(--gold);}
.fb-desc{color:var(--gray);font-size:.82rem;line-height:1.7;max-width:260px;margin-bottom:18px;}
.fsocial{display:flex;gap:9px;}
.soc{width:38px;height:38px;border-radius:7px;background:var(--dark3);border:1px solid #2a2a2a;display:flex;align-items:center;justify-content:center;color:var(--gray);text-decoration:none;font-size:.88rem;transition:all .3s;}
.soc:hover{background:var(--gold);border-color:var(--gold);color:var(--black);}
.fcol h4{color:var(--white);font-weight:600;margin-bottom:14px;font-size:.86rem;letter-spacing:.3px;}
.fcol ul{list-style:none;display:flex;flex-direction:column;gap:8px;}
.fcol ul li a{color:var(--gray);text-decoration:none;font-size:.8rem;transition:color .3s;display:flex;align-items:center;gap:6px;}
.fcol ul li a:hover{color:var(--gold);}
.footer-btm{border-top:1px solid #1e1e1e;padding-top:22px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:10px;}
.footer-btm p{color:var(--gray);font-size:.76rem;}
.admin-btn{background:none;border:none;color:#1e1e1e;cursor:pointer;font-size:.7rem;padding:4px;transition:color .3s;}
.admin-btn:hover{color:var(--gold);}
.floats{position:fixed;bottom:24px;right:20px;z-index:500;display:flex;flex-direction:column;gap:10px;align-items:flex-end;}
.fbtn{width:54px;height:54px;border-radius:50%;display:flex;align-items:center;justify-content:center;text-decoration:none;font-size:1.3rem;border:none;cursor:pointer;transition:all .3s;box-shadow:0 4px 18px rgba(0,0,0,.4);}
.fbtn-wa{background:#25D366;color:#fff;}
.fbtn-wa:hover{transform:scale(1.1);box-shadow:0 8px 24px rgba(37,211,102,.5);}
.fbtn-call{background:var(--gold);color:var(--black);}
.fbtn-call:hover{transform:scale(1.1);box-shadow:0 8px 24px rgba(201,168,76,.5);}
#svc-modal{display:none;position:fixed;inset:0;background:rgba(0,0,0,.88);z-index:5000;align-items:center;justify-content:center;padding:20px;}
#svc-modal.open{display:flex;}
.modal-box{background:var(--dark2);border:1px solid rgba(201,168,76,.25);border-radius:14px;padding:36px;max-width:460px;width:100%;position:relative;max-height:90vh;overflow-y:auto;}
.mclose{position:absolute;top:14px;right:14px;background:none;border:none;color:var(--gray);font-size:1.4rem;cursor:pointer;width:30px;height:30px;display:flex;align-items:center;justify-content:center;border-radius:50%;transition:all .3s;}
.mclose:hover{background:#333;color:var(--white);}
.micon{font-size:2.8rem;margin-bottom:12px;}
.modal-box h3{font-family:"Oswald";font-size:1.5rem;color:var(--gold);margin-bottom:10px;}
.modal-box .mdesc{color:var(--gray-l);line-height:1.8;font-size:.87rem;margin-bottom:8px;}
.modal-box .mdetail{background:var(--dark3);border-radius:8px;padding:14px;margin:14px 0;font-size:.82rem;color:var(--gray);}
.modal-box .mdetail li{margin-bottom:5px;padding-left:4px;}
.modal-box .mdetail li::before{content:"✓ ";color:var(--gold);}
.mprice{color:var(--gold);font-size:.9rem;font-weight:700;margin-bottom:16px;}
.mactions{display:flex;gap:10px;flex-wrap:wrap;}
.mactions a{flex:1;text-align:center;text-decoration:none;display:inline-flex;align-items:center;justify-content:center;gap:6px;min-width:120px;}
@media(max-width:900px){
  .nav-links{display:none;}
  .hamburger{display:flex;}
  .about-grid,.contact-grid{grid-template-columns:1fr;gap:40px;}
  .about-vis{max-width:260px;margin:0 auto;}
  .footer-grid{grid-template-columns:1fr 1fr;gap:32px;}
  .about-features{grid-template-columns:1fr;}
  section{padding:70px 5%;}
  .hero-logo-side{display:none;}
  .fr2{grid-template-columns:1fr;}
  .af .fr2{grid-template-columns:1fr;}
  .process-steps::before{display:none;}
  .why-intro{flex-direction:column;align-items:flex-start;}
}
@media(max-width:600px){
  .footer-grid{grid-template-columns:1fr;}
  .a-stats{grid-template-columns:1fr 1fr;}
  .a-body{padding:14px;}
  .atab{padding:10px 11px;font-size:.8rem;}
  .hero-stats{gap:20px;}
  .svc-header{flex-direction:column;align-items:flex-start;}
}


"""
