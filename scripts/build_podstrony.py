#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Buduje podstrony: /obszar-dzialania/<slug>/ (9), /o-kancelarii/, /kontakt/.

Styl i układ jak /konsultacje-online/: style bazowe z co-sie-stalo/index.html
+ style podstrony z konsultacje-online/index.html + style poniżej.
Treści: scripts/podstrony_dane.py.  Uruchom: python3 scripts/build_podstrony.py
"""
import os, re, json, html, sys
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(__file__))
from podstrony_dane import OBSZARY, ZESPOL

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://lawyerai.pl"
E = html.escape

def rd(p): return open(os.path.join(ROOT, p), encoding="utf-8").read()

CSS_BASE = re.search(r"<style>(.*?)</style>", rd("co-sie-stalo/index.html"), re.S).group(1)
CSS_KO = re.search(r"<style>\s*(/\* ===== Konsultacje online.*?)</style>", rd("konsultacje-online/index.html"), re.S).group(1)
CSS_KO = CSS_KO.split("@media (max-width:1100px)")[0]  # bez reguł @media strony online (dodane niżej, na końcu)
KO_MEDIA = re.search(r"(@media \(max-width:1100px\).*)", re.search(r"<style>\s*/\* ===== Konsultacje online.*?</style>", rd("konsultacje-online/index.html"), re.S).group(0), re.S).group(1).replace("</style>", "")

CSS_NEW = r"""
/* ===== Podstrony (build_podstrony.py) ===== */
.ko-hero h1.long{font-size:clamp(40px,5.4vw,84px)}
/* teczka akt w nagłówku */
.case{position:relative;max-width:440px;width:100%;justify-self:end;padding-top:34px}
.case-tab{position:absolute;left:0;top:0;height:34px;width:44%;background:#1b201e;border:1px solid rgba(255,255,255,.14);border-bottom:0;display:flex;align-items:center;padding:0 16px;font-family:var(--mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:rgba(255,255,255,.7)}
.case-body{background:#121614;border:1px solid rgba(255,255,255,.14);box-shadow:0 40px 80px -30px rgba(0,0,0,.8);padding:26px 24px 22px;position:relative;overflow:hidden}
.case-body::after{content:"";position:absolute;right:-70px;bottom:-70px;width:220px;height:220px;border-radius:50%;background:rgba(173,255,35,.16);filter:blur(40px)}
.case-n{font-family:var(--display);font-stretch:125%;font-weight:800;font-size:96px;line-height:.8;color:transparent;-webkit-text-stroke:1px rgba(173,255,35,.8);letter-spacing:-.04em}
.case-name{font-family:var(--display);font-stretch:112%;font-weight:700;font-size:22px;margin-top:14px;color:#fff;line-height:1.15}
.case-rows{list-style:none;margin:18px 0 0;padding:0;border-top:1px solid rgba(255,255,255,.12);position:relative;z-index:1}
.case-rows li{display:flex;justify-content:space-between;gap:16px;padding:10px 0;border-bottom:1px solid rgba(255,255,255,.12);font-size:13px;color:rgba(255,255,255,.75);animation:in .5s both}
.case-rows li:nth-child(2){animation-delay:.1s}.case-rows li:nth-child(3){animation-delay:.2s}.case-rows li:nth-child(4){animation-delay:.3s}
.case-rows b{font-family:var(--mono);font-weight:500;font-size:11px;letter-spacing:.04em;color:var(--green);white-space:nowrap}
.stamp{position:absolute;right:18px;top:52px;width:86px;height:86px;border-radius:50%;border:1.5px solid var(--green);display:grid;place-items:center;text-align:center;font-family:var(--mono);font-size:9px;letter-spacing:.1em;text-transform:uppercase;color:var(--green);transform:rotate(-12deg);line-height:1.4;z-index:2}
@keyframes in{from{opacity:0;transform:translateY(10px)}}

/* kafelki tematów */
.topics{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));border-left:1px solid var(--line);border-top:1px solid var(--line)}
.topics.c4{grid-template-columns:repeat(4,minmax(0,1fr))}
.topic{border-right:1px solid var(--line);border-bottom:1px solid var(--line);padding:26px 24px;display:grid;gap:10px;align-content:start;position:relative;background:var(--paper);transition:background .25s;text-decoration:none;color:inherit;min-width:0}
.topic::before{content:"";position:absolute;left:0;top:0;height:3px;width:0;background:var(--green);transition:width .35s}
.topic:hover{background:var(--paper-2)}.topic:hover::before{width:100%}
.topic .tn{font-family:var(--mono);font-size:12px;color:var(--green-ink)}
.topic h3{font-size:21px;font-stretch:112%}
.topic p{color:var(--ink-2);font-size:15px}
a.topic .more{font-size:14px;font-weight:600;display:inline-flex;gap:8px;margin-top:4px}
a.topic .more .arr{transition:transform .2s;color:var(--green-ink)}
a.topic:hover .more .arr{transform:translateX(4px)}

/* terminy / przepisy (ciemny pas) */
.terms{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:1px;background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.14)}
.terms.c3{grid-template-columns:repeat(3,minmax(0,1fr))}
.terms.c2{grid-template-columns:repeat(2,minmax(0,1fr))}
.term{background:var(--night);padding:28px 24px;display:grid;gap:12px;align-content:start;position:relative;transition:background .3s}
.term:hover{background:var(--night-2)}
.term .tv{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap}
.term .tv b{font-family:var(--display);font-stretch:125%;font-weight:800;font-size:clamp(48px,5vw,72px);line-height:.9;letter-spacing:-.03em;color:var(--green)}
.term .tv span{font-family:var(--display);font-stretch:112%;font-weight:700;font-size:20px;color:#fff}
.term p{color:rgba(255,255,255,.78);font-size:15px}
.term .law{font-family:var(--mono);font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:rgba(255,255,255,.55);border-top:1px solid rgba(255,255,255,.14);padding-top:12px;margin-top:auto}
.terms-note{margin-top:22px;font-size:14px;color:rgba(255,255,255,.72);border-left:3px solid var(--green);padding:4px 0 4px 14px;max-width:70ch}

/* jak pracujemy (jasne) */
.steps4{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));list-style:none;margin:0;padding:0;position:relative}
.steps4::before{content:"";position:absolute;left:0;right:0;top:26px;height:2px;background:repeating-linear-gradient(90deg,var(--green-ink) 0 8px,transparent 8px 14px)}
.steps4 li{position:relative;padding-right:24px;display:grid;gap:10px;align-content:start}
.steps4 .rn{width:54px;height:54px;border-radius:50%;background:var(--paper);border:2px solid var(--ink);display:grid;place-items:center;font-family:var(--mono);font-size:13px;position:relative;z-index:1}
.steps4 li:last-child .rn{background:var(--green);border-color:var(--green)}
.steps4 b{font-family:var(--display);font-stretch:112%;font-size:19px}
.steps4 span{color:var(--ink-2);font-size:15px}

/* poradniki */
.reads{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px}
.read{display:grid;gap:12px;text-decoration:none;color:inherit;align-content:start}
.read .im{aspect-ratio:16/9;background:var(--night) center/cover no-repeat;filter:grayscale(1);transition:filter .4s;position:relative;overflow:hidden}
.read .im::after{content:"";position:absolute;left:0;bottom:0;height:3px;width:0;background:var(--green);transition:width .35s}
.read:hover .im{filter:grayscale(.2)}.read:hover .im::after{width:100%}
.read .tag{font-family:var(--mono);font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:var(--green-ink)}
.read h3{font-size:19px;font-stretch:100%;line-height:1.25}
.read .more{font-size:14px;font-weight:600;display:inline-flex;gap:8px}
.read .more .arr{transition:transform .2s}.read:hover .more .arr{transform:translateX(4px)}

/* inne obszary */
.others{display:flex;flex-wrap:wrap;gap:8px}
.others a{font:500 14px var(--body);border:1px solid var(--line);padding:10px 16px;min-height:44px;display:inline-flex;align-items:center;text-decoration:none;color:var(--ink);white-space:nowrap;transition:border-color .2s,background .2s}
.others a:hover{border-color:var(--ink)}
.others a[aria-current="page"]{background:var(--ink);color:#fff;border-color:var(--ink)}

/* o kancelarii */
.stats{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:1px;background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.14);max-width:460px;width:100%;justify-self:end}
.stat{background:rgba(18,22,20,.92);padding:24px 22px;display:grid;gap:6px}
.stat b{font-family:var(--display);font-stretch:125%;font-weight:800;font-size:clamp(44px,4.6vw,64px);line-height:.9;letter-spacing:-.03em;color:var(--green)}
.stat span{font-size:14px;color:rgba(255,255,255,.75)}
.princ{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:0;border-top:1px solid rgba(255,255,255,.2)}
.princ div{padding:28px 24px 28px 0;display:grid;gap:10px;align-content:start}
.princ svg{width:44px;height:44px;padding:10px;background:var(--green);color:var(--ink)}
.princ h3{font-size:21px;font-stretch:112%}
.princ p{color:rgba(255,255,255,.72);font-size:15px}
.statement.big{max-width:30ch}

/* kontakt */
.addr{background:#121614;border:1px solid rgba(255,255,255,.14);box-shadow:0 40px 80px -30px rgba(0,0,0,.8);max-width:440px;width:100%;justify-self:end;padding:28px;display:grid;gap:18px;position:relative;overflow:hidden}
.addr::after{content:"";position:absolute;right:-60px;top:-60px;width:200px;height:200px;border-radius:50%;background:rgba(173,255,35,.16);filter:blur(40px)}
.addr .pin{width:52px;height:52px;background:var(--green);display:grid;place-items:center;color:var(--ink)}
.addr .pin svg{width:26px;height:26px}
.addr b{font-family:var(--display);font-stretch:112%;font-size:26px;line-height:1.15;color:#fff}
.addr p{color:rgba(255,255,255,.75);font-size:15px}
.addr .lines{display:grid;border-top:1px solid rgba(255,255,255,.12)}
.addr .lines a{display:flex;justify-content:space-between;gap:12px;padding:12px 0;border-bottom:1px solid rgba(255,255,255,.12);text-decoration:none;color:#fff;font-size:15px;min-height:44px;align-items:center}
.addr .lines a span{font-family:var(--mono);font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:rgba(255,255,255,.55)}
.map{display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,1fr);gap:clamp(28px,5vw,72px);align-items:stretch}
.map-frame{position:relative;min-height:420px;background:var(--paper-2);border:1px solid var(--line)}
.map-frame::before{content:"Mapa: ul. Kołłątaja 11, Opole";position:absolute;inset:0;display:grid;place-items:center;font-family:var(--mono);font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-2)}
.map-frame iframe{position:absolute;inset:0;width:100%;height:100%;border:0;filter:grayscale(1) contrast(1.05)}
.how{list-style:none;margin:0;padding:0;border-top:1px solid var(--ink)}
.how li{display:grid;grid-template-columns:44px minmax(0,1fr);gap:16px;padding:18px 0;border-bottom:1px solid var(--line)}
.how svg{width:44px;height:44px;padding:10px;border:1px solid var(--ink)}
.how b{display:block;font-size:17px}
.how span{color:var(--ink-2);font-size:15px}
.map-cta{display:flex;flex-wrap:wrap;gap:10px;margin-top:24px}
.btn.line{background:transparent;color:var(--ink);box-shadow:inset 0 0 0 1px var(--ink)}
.btn.line:hover{background:var(--ink);color:#fff}
.firm{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.3fr);gap:clamp(28px,5vw,72px);align-items:start}
.firm .channels{margin-top:0}
.firm .channels div{align-items:center}
.copy{font:600 13px var(--body);background:transparent;color:var(--green);border:1px solid rgba(173,255,35,.5);padding:8px 12px;min-height:40px;cursor:pointer;white-space:nowrap}
.copy:hover{background:var(--green);color:var(--ink)}

/* stopka: nawigacja */
.fnav{display:flex;flex-wrap:wrap;gap:8px 24px;padding-top:28px;font-size:14px}
.fnav a{color:rgba(255,255,255,.8);text-decoration:none;min-height:40px;display:inline-flex;align-items:center}
.fnav a:hover{color:var(--green)}
"""

CSS_NEW_MEDIA = r"""
@media (max-width:1100px){
  .topics.c4{grid-template-columns:repeat(2,minmax(0,1fr))}
  .terms,.terms.c3{grid-template-columns:repeat(2,minmax(0,1fr))}
  .princ{grid-template-columns:repeat(2,minmax(0,1fr))}
}
@media (max-width:900px){
  .case,.stats,.addr{justify-self:start}
  .topics{grid-template-columns:repeat(2,minmax(0,1fr))}
  .reads{grid-template-columns:repeat(2,minmax(0,1fr))}
  .steps4{grid-template-columns:repeat(2,minmax(0,1fr));row-gap:28px}
  .steps4::before{display:none}
  .map,.firm{grid-template-columns:1fr}
}
@media (max-width:640px){
  .others{flex-wrap:nowrap;overflow-x:auto;scrollbar-width:none;margin-inline:-20px;padding-inline:20px;-webkit-mask-image:linear-gradient(90deg,#000 85%,transparent);mask-image:linear-gradient(90deg,#000 85%,transparent)}
  .others::-webkit-scrollbar{display:none}
  .others a{flex:0 0 auto}
}
@media (max-width:560px){
  .ko-hero h1.long{font-size:34px}
  .ko-hero h1.xlong{font-size:30px}
  .case{display:none}
  .stats{max-width:none}
  .stat{padding:18px 16px}
  .stat b{font-size:40px}
  .addr{padding:22px 18px;max-width:none}
  .topics,.topics.c4{grid-template-columns:1fr;border:0;gap:8px}
  .topic{border:1px solid var(--line);padding:18px 16px;gap:6px}
  .topic h3{font-size:18px}
  .terms,.terms.c3,.terms.c2{grid-template-columns:1fr}
  .term{padding:20px 18px;grid-template-columns:minmax(0,1fr);gap:8px}
  .term .tv b{font-size:48px}
  .steps4{grid-template-columns:1fr;row-gap:0}
  .steps4 li{grid-template-columns:54px minmax(0,1fr);column-gap:16px;row-gap:2px;padding:0 0 22px}
  .steps4 .rn{grid-row:span 2}
  .steps4 b{padding-top:6px;font-size:17px}
  .reads{grid-template-columns:1fr;gap:28px}
  .princ{grid-template-columns:1fr}
  .princ div{grid-template-columns:44px minmax(0,1fr);column-gap:16px;row-gap:4px;padding:18px 0;border-bottom:1px solid rgba(255,255,255,.14)}
  .princ svg{grid-row:span 2}
  .princ h3{font-size:18px;align-self:center}
  .map-frame{min-height:300px}
  .map-cta .btn{flex:1 1 100%;justify-content:center}
  .firm .channels div{flex-direction:row;flex-wrap:wrap;justify-content:space-between}
  .fnav{gap:4px 20px}
}
"""

ICON = {
 "phone": '<path fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" d="M6.62 10.79a15.05 15.05 0 0 0 6.59 6.59l2.2-2.2a1 1 0 0 1 1.02-.24c1.12.37 2.33.57 3.57.57a1 1 0 0 1 1 1V20a1 1 0 0 1-1 1C10.61 21 3 13.39 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1.02l-2.2 2.2z"/>',
 "mobile": '<path fill="none" stroke="currentColor" stroke-width="1.8" d="M7 2.8h10v18.4H7zM10.5 18h3"/>',
 "wa": '<path fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" d="M4 20l1.3-3.9A8 8 0 1 1 8 19z"/><path fill="none" stroke="currentColor" stroke-width="1.8" d="M9 9.5c0 3 2.5 5.5 5.5 5.5"/>',
 "mail": '<path fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" d="M3 5.5h18v13H3z"/><path fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" d="m3.5 6 8.5 7 8.5-7"/>',
 "pin": '<path fill="currentColor" d="M12 2a7 7 0 0 0-7 7c0 5.25 7 13 7 13s7-7.75 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5z"/>',
 "globe": '<circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="1.8"/><path fill="none" stroke="currentColor" stroke-width="1.8" d="M3 12h18M12 3c2.6 2.6 3.8 5.6 3.8 9s-1.2 6.4-3.8 9c-2.6-2.6-3.8-5.6-3.8-9S9.4 5.6 12 3z"/>',
 "shield": '<path fill="none" stroke="currentColor" stroke-width="1.8" d="M12 3l7 3v5.5c0 4.4-3 8.2-7 9.5-4-1.3-7-5.1-7-9.5V6z"/><path fill="none" stroke="currentColor" stroke-width="1.8" d="m8.8 12 2.2 2.2 4.2-4.4"/>',
 "doc": '<path fill="none" stroke="currentColor" stroke-width="1.8" d="M6 2.8h8l4 4v14.4H6z"/><path fill="none" stroke="currentColor" stroke-width="1.8" d="M14 2.8v4h4M9 12h6M9 15.5h6"/>',
 "coin": '<circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="1.8"/><path fill="none" stroke="currentColor" stroke-width="1.8" d="M14.8 9.2c-.5-.9-1.6-1.4-2.8-1.4-1.6 0-2.8.8-2.8 2.1 0 2.9 5.8 1.5 5.8 4.3 0 1.3-1.3 2.1-3 2.1-1.3 0-2.4-.5-3-1.5M12 6v1.8M12 16.3V18"/>',
 "court": '<path fill="none" stroke="currentColor" stroke-width="1.8" d="M4 20h16M6 20V10M10 20V10M14 20V10M18 20V10M3 10l9-6 9 6z"/>',
 "stairs": '<path fill="none" stroke="currentColor" stroke-width="1.8" d="M3 20h5v-4h4v-4h4V8h5"/>',
 "video": '<path fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" d="M3 7h12v10H3zM15 10.5l6-3.5v10l-6-3.5"/>',
 "clock": '<circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="1.8"/><path fill="none" stroke="currentColor" stroke-width="1.8" d="M12 7v5l3 2"/>',
}
def svg(k, cls=""): return f'<svg viewBox="0 0 24 24" aria-hidden="true"{(" class=%s" % cls) if cls else ""}>{ICON[k]}</svg>'

MAPS = "https://www.google.com/maps/search/?api=1&query=Pola%C5%84ski%20Konofalski%20i%20Wsp%C3%B3lnicy%2C%20ul.%20Ko%C5%82%C5%82%C4%85taja%2011%2C%2045-064%20Opole"
APPLE = "https://maps.apple.com/?q=PKW%20Adwokaci&amp;address=ul.%20Ko%C5%82%C5%82%C4%85taja%2011%2C%2045-064%20Opole"
PROVIDER = {"@type": "LegalService", "name": "Polański Konofalski i Wspólnicy Spółka Partnerska Adwokatów", "telephone": "+48774143669", "email": "biuro@pkwadwokaci.pl", "url": SITE + "/", "address": {"@type": "PostalAddress", "streetAddress": "ul. Ks. H. Kołłątaja 11 lok. 27", "postalCode": "45-064", "addressLocality": "Opole", "addressCountry": "PL"}}

def blog_meta(slug):
    p = os.path.join(ROOT, "content", "blog", slug, "meta.json")
    if not os.path.exists(os.path.join(ROOT, "blog", slug, "index.html")) or not os.path.exists(p): return None
    m = json.load(open(p, encoding="utf-8"))
    return m

# ---------- wspólny szkielet ----------
def page(pre, path, title, desc, body, ld, current=None, extra_js=""):
    css = CSS_BASE + CSS_KO.replace("../assets/", pre + "assets/") + CSS_NEW + KO_MEDIA + CSS_NEW_MEDIA
    def cur(name): return ' aria-current="page"' if current == name else ""
    kontakt_href = "./" if current == "kontakt" else pre + "#kontakt"
    return f"""<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#0b0d0c">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{SITE}/{path}">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{SITE}/{path}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..800&family=Instrument+Sans:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap">
<style>{css}</style>
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
<header class="top">
  <div class="wrap nav">
    <a class="logo" href="{pre}">PKW<b class="bar" aria-hidden="true"></b>ADWOKACI</a>
    <nav class="menu" id="menu" aria-label="Główne">
      <a href="{pre}co-sie-stalo/">Moja sytuacja</a>
      <a href="{pre}#wspolpraca">Współpraca</a>
      <a href="{pre}o-kancelarii/#zespol"{cur("o-kancelarii")}>Zespół</a>
      <a href="{pre}blog/">Blog</a>
      <a href="{kontakt_href}"{cur("kontakt")}>Kontakt</a>
    </nav>
    <a class="btn green top-cta" href="{pre}#kontakt">Umów konsultację <span class="arr">→</span></a>
    <button class="burger" id="burger" type="button" aria-expanded="false" aria-controls="menu" aria-label="Otwórz menu"><span></span><span></span></button>
  </div>
</header>
<main id="start">
{body}
</main>
<footer>
  <div class="wrap"><div class="big-mark"><svg viewBox="0 0 1000 132" role="img" aria-label="PKW Adwokaci"><text x="0" y="118" font-size="150" textLength="1000" lengthAdjust="spacingAndGlyphs">PKW<tspan> | </tspan>ADWOKACI</text></svg></div>
    <nav class="fnav" aria-label="Stopka">
      <a href="{pre}obszar-dzialania/">Obszar działania</a><a href="{pre}o-kancelarii/">O kancelarii</a><a href="{pre}konsultacje-online/">Konsultacje online</a><a href="{pre}co-sie-stalo/">Moja sytuacja</a><a href="{pre}blog/">Blog</a><a href="{pre}kontakt/">Kontakt</a>
    </nav>
  </div>
  <div class="wrap">
    <span>© 2026 Polański Konofalski i Wspólnicy Spółka Partnerska Adwokatów · ul. Ks. H. Kołłątaja 11 lok. 27 (II piętro), 45 - 064 Opole</span>
    <span>Polityka prywatności · Informacje zgodne z § 23 Kodeksu Etyki Adwokackiej</span>
  </div>
</footer>
<nav class="mbar" aria-label="Szybki kontakt">
  <a class="mb-call" href="tel:+48774143669"><svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M6.62 10.79a15.05 15.05 0 0 0 6.59 6.59l2.2-2.2a1 1 0 0 1 1.02-.24c1.12.37 2.33.57 3.57.57a1 1 0 0 1 1 1V20a1 1 0 0 1-1 1C10.61 21 3 13.39 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1.02l-2.2 2.2z"/></svg><span>Zadzwoń</span></a>
  <a class="mb-mail" href="mailto:biuro@pkwadwokaci.pl"><svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round" d="M3 5.5h18v13H3z"/><path fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round" d="m3.5 6 8.5 7 8.5-7"/></svg>E-mail</a>
  <a class="mb-map" href="{MAPS}" target="_blank" rel="noopener" data-apple="{APPLE}"><svg viewBox="0 0 24 24" aria-hidden="true">{ICON["pin"]}</svg><span>Mapa</span></a>
</nav>
<script>(function(){{var m=document.querySelector('.mbar .mb-map');if(m&&/iPhone|iPad|iPod|Macintosh/.test(navigator.userAgent)&&('ontouchend' in document)){{m.href=m.dataset.apple}};document.querySelectorAll('a[data-apple]:not(.mb-map)').forEach(function(a){{if(/iPhone|iPad|iPod|Macintosh/.test(navigator.userAgent)&&('ontouchend' in document))a.href=a.dataset.apple}})}})();
(function(){{var bg=document.getElementById('burger'),mn=document.getElementById('menu');if(!bg)return;bg.addEventListener('click',function(){{var o=mn.classList.toggle('open');bg.setAttribute('aria-expanded',o)}});mn.querySelectorAll('a').forEach(function(a){{a.addEventListener('click',function(){{mn.classList.remove('open');bg.setAttribute('aria-expanded','false')}})}})}})();
(function(){{var o=document.querySelector('.others a[aria-current]');if(o&&o.parentNode.scrollWidth>o.parentNode.clientWidth)o.parentNode.scrollLeft=o.offsetLeft-20}})();
{extra_js}</script>
</body>
</html>
"""

def facts():
    return f"""  <div class="wrap">
    <div class="ko-facts">
      <div>{svg("globe")}<b>Konsultacja online</b><span>Przez telefon lub wideo, z&nbsp;dowolnego miejsca w&nbsp;Polsce i&nbsp;za granicą.</span></div>
      <div>{svg("coin")}<b>Koszt przed rozmową</b><span>Cenę konsultacji podajemy na piśmie, zanim się spotkamy.</span></div>
      <div>{svg("shield")}<b>Tajemnica adwokacka</b><span>Obejmuje wszystko, co nam przekażesz, także przed podpisaniem umowy.</span></div>
    </div>
  </div>"""

def faq_html(items, title="Częste pytania"):
    d = "".join(f"<details><summary>{E(q)}</summary><p>{E(a)}</p></details>" for q, a in items)
    return f"""  <section class="s" id="pytania">
    <div class="wrap split">
      <div><span class="label"><span class="dot"></span>Pytania</span><h2 style="margin-top:18px">{title}</h2></div>
      <div class="faq">{d}</div>
    </div>
  </section>"""

def cta(pre, h="Umów konsultację", p="Napisz kilka zdań o&nbsp;sprawie i&nbsp;dołącz zdjęcie pisma. Odezwiemy się, żeby ustalić termin i&nbsp;formę rozmowy."):
    return f"""  <section class="ko-cta">
    <div class="wrap">
      <span class="label" style="color:rgba(255,255,255,.6)"><span class="dot"></span>Kontakt</span>
      <h2>{h}</h2>
      <p>{p}</p>
      <div class="od-cta" style="margin-top:0">
        <a class="btn green" href="{pre}#kontakt">Wypełnij formularz <span class="arr">→</span></a>
        <a class="btn ghost" href="tel:+48774143669">Zadzwoń: 77 414 36 69</a>
        <a class="btn ghost" href="{pre}konsultacje-online/">Konsultacja online</a>
      </div>
      <p class="ethics">Informacje na tej stronie mają charakter informacyjny i&nbsp;nie stanowią porady prawnej. Treść zgodna z&nbsp;§ 23 Kodeksu Etyki Adwokackiej.</p>
    </div>
  </section>"""

def h1_cls(words):
    longest = max(len(w) for part in words for w in part.split())
    return "long xlong" if longest >= 14 else ("long" if longest >= 11 else "")

def short(n):
    return {"Prawo egzekucyjne i windykacja należności": "Windykacja i egzekucja", "Prawo zamówień publicznych i pomocy publicznej": "Zamówienia publiczne", "Prawo rolne i przetwórstwa rolnego": "Prawo rolne", "Prawo obrotu nieruchomościami": "Nieruchomości", "Prawo gospodarcze i handlowe": "Prawo gospodarcze"}.get(n, n)

# ---------- obszar ----------
def build_area(a):
    pre = "../../"
    path = f"obszar-dzialania/{a['slug']}/"
    w1, w2 = a["h1"]
    cls = h1_cls(a["h1"])
    chips = "".join(f"<li>{E(c)}</li>" for c in a["chips"])
    rows = "".join(f"<li>{E(t[3])}<b>{E(t[0])} {E(t[1])}</b></li>" for t in a["terms"][:4])
    topics = "".join(f'<article class="topic"><span class="tn">{i+1:02d}</span><h3>{E(t)}</h3><p>{E(d)}</p></article>' for i, (t, d) in enumerate(a["topics"]))
    tc = "c4" if len(a["topics"]) in (4, 7, 8) else ""
    terms = "".join(f'<div class="term"><div class="tv"><b>{E(v)}</b><span>{E(u)}</span></div><p>{E(w)}</p><span class="law">{E(l)}</span></div>' for v, u, w, l in a["terms"])
    tcols = {2: "c2", 3: "c3"}.get(len(a["terms"]), "")
    note = f'<p class="terms-note">{E(a["terms_note"])}</p>' if a.get("terms_note") else ""
    reads = [(s, blog_meta(s)) for s in a["blog"]]
    reads = [(s, m) for s, m in reads if m][:3]
    reads_html = ""
    if reads:
        cards = "".join(f'<a class="read" href="{pre}blog/{s}/"><span class="im" style="background-image:url({pre}{m.get("cover", "assets/blog/blog-hero.jpg")})"></span><span class="tag">Poradnik</span><h3>{E(m["title"])}</h3><span class="more">Czytaj <span class="arr">→</span></span></a>' for s, m in reads)
        reads_html = f"""  <section class="s" id="poradniki">
    <div class="wrap">
      <div class="s-head">
        <div><span class="label"><span class="dot"></span>04 · Poradniki</span><h2 style="margin-top:18px">Przeczytaj, zanim zadzwonisz</h2></div>
        <p>Artykuły z&nbsp;naszego bloga, które wyjaśniają najczęstsze sytuacje w&nbsp;tej dziedzinie.</p>
      </div>
      <div class="reads">{cards}</div>
    </div>
  </section>"""
    CUR = ' aria-current="page"'
    others = "".join(f'<a href="../{o["slug"]}/"{CUR if o is a else ""}>{E(short(o["name"]))}</a>' for o in OBSZARY)
    nsec = "05" if reads else "04"
    body = f"""  <section class="ko-hero">
    <div class="wrap">
      <div>
        <span class="label"><span class="dot"></span>Obszar działania · {a["n"]}</span>
        <h1 class="{cls}">{E(w1)} <span>{E(w2)}</span></h1>
        <p class="lead">{E(a["lead"])}</p>
        <div class="hero-cta">
          <a class="btn green" href="{pre}#kontakt">Umów konsultację <span class="arr">→</span></a>
          <a class="btn ghost" href="tel:+48774143669">Zadzwoń: 77 414 36 69</a>
        </div>
        <ul class="ko-chips" aria-label="Najczęstsze sprawy">{chips}</ul>
      </div>
      <div class="case" aria-hidden="true">
        <div class="case-tab">Akta · {a["n"]}</div>
        <div class="case-body">
          <div class="stamp">PKW<br>Adwokaci<br>Opole</div>
          <div class="case-n">{a["n"]}</div>
          <div class="case-name">{E(a["name"])}</div>
          <ul class="case-rows">{rows}</ul>
        </div>
      </div>
    </div>
  </section>
{facts()}
  <section class="s" id="zakres">
    <div class="wrap">
      <div class="s-head">
        <div><span class="label"><span class="dot"></span>01 · Zakres</span><h2 style="margin-top:18px">W czym pomagamy</h2></div>
        <p>Najczęstsze sprawy, które prowadzimy w&nbsp;tej dziedzinie. Jeśli Twojej nie ma na liście, zadzwoń: powiemy, czy możemy pomóc.</p>
      </div>
      <div class="topics {tc}">{topics}</div>
    </div>
  </section>
  <section class="s dark" id="terminy">
    <div class="wrap">
      <div class="s-head">
        <div><span class="label"><span class="dot"></span>02 · Przepisy</span><h2 style="margin-top:18px">{E(a["terms_title"])}</h2></div>
        <p>Terminy liczą się od doręczenia lub ogłoszenia. Gdy masz pismo, sprawdź datę na kopercie albo potwierdzeniu odbioru.</p>
      </div>
      <div class="terms {tcols}">{terms}</div>
      {note}
    </div>
  </section>
  <section class="s" id="wspolpraca">
    <div class="wrap">
      <div class="s-head">
        <div><span class="label"><span class="dot"></span>03 · Współpraca</span><h2 style="margin-top:18px">Jak pracujemy</h2></div>
        <p>Zanim podpiszesz umowę, wiesz, ile to kosztuje i&nbsp;co będziemy robić.</p>
      </div>
      <ol class="steps4">
        <li><span class="rn">01</span><b>Kontakt</b><span>Formularz, telefon lub WhatsApp. Możesz od razu wysłać zdjęcie pisma.</span></li>
        <li><span class="rn">02</span><b>Konsultacja</b><span>W&nbsp;kancelarii lub <a href="{pre}konsultacje-online/">online</a>. Omawiamy sprawę, termin i&nbsp;możliwe kroki.</span></li>
        <li><span class="rn">03</span><b>Wycena</b><span>Stała kwota lub stawka godzinowa, spisana w&nbsp;umowie.</span></li>
        <li><span class="rn">04</span><b>Prowadzenie sprawy</b><span>Pisma, rozprawy, kontakt z&nbsp;urzędem. Informujemy o&nbsp;każdym etapie.</span></li>
      </ol>
    </div>
  </section>
{reads_html}
{faq_html(a["faq"])}
  <section class="s tint" style="background:var(--paper-2);padding-block:clamp(48px,6vw,80px)">
    <div class="wrap">
      <span class="label"><span class="dot"></span>{nsec} · Inne obszary</span>
      <div class="others" style="margin-top:20px">{others}</div>
      <p style="margin-top:20px"><a href="../" style="font-weight:600">Wszystkie obszary działania →</a></p>
    </div>
  </section>
{cta(pre)}"""
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "PKW Adwokaci", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Obszar działania", "item": SITE + "/obszar-dzialania/"},
            {"@type": "ListItem", "position": 3, "name": a["name"], "item": SITE + "/" + path}]},
        {"@type": "Service", "name": a["name"], "serviceType": a["name"], "areaServed": "PL", "description": a["lead"], "provider": PROVIDER},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": t}} for q, t in a["faq"]]}]}
    return path, page(pre, path, f"{a['name']} – adwokat Opole | PKW Adwokaci", a["desc"], body, ld)

# ---------- o kancelarii ----------
def build_about():
    pre = "../"; path = "o-kancelarii/"
    team = ""
    for name, role, ini, img in ZESPOL:
        team += f'<a class="person" href="tel:+48774143669" aria-label="Zadzwoń: {E(name)}, tel. 77 414 36 69"><div class="portrait has-photo" style="background-image:url({pre}assets/{img})"><span class="ini">{ini}</span><span class="pl">adwokat · Opole</span><span class="sample">Zdjęcie poglądowe</span></div><div class="meta"><div><h3>{E(name)}</h3><span>{E(role)}</span><span class="sample-note">Zdjęcie poglądowe</span></div></div><span class="call" aria-hidden="true">Zadzwoń <span class="arr">→</span></span></a>'
    areas = "".join(f'<a class="topic" href="{pre}obszar-dzialania/{o["slug"]}/"><span class="tn">{o["n"]}</span><h3>{E(o["name"])}</h3><p>{E(o["lead"].split(". ")[0].rstrip("."))}.</p><span class="more">Zobacz <span class="arr">→</span></span></a>' for o in OBSZARY)
    body = f"""  <section class="ko-hero">
    <div class="wrap">
      <div>
        <span class="label"><span class="dot"></span>O kancelarii</span>
        <h1>o <span>kancelarii</span></h1>
        <p class="lead">Polański Konofalski i&nbsp;Wspólnicy Spółka Partnerska Adwokatów. Kancelaria z&nbsp;Opola, działa od 2014 roku. Prowadzimy sprawy osób prywatnych i&nbsp;firm w&nbsp;całej Polsce.</p>
        <div class="hero-cta">
          <a class="btn green" href="#zespol">Poznaj zespół <span class="arr">→</span></a>
          <a class="btn ghost" href="{pre}#kontakt">Umów konsultację</a>
        </div>
      </div>
      <div class="stats">
        <div class="stat"><b>2014</b><span>rok założenia kancelarii</span></div>
        <div class="stat"><b>2</b><span>wspólników prowadzi zespół</span></div>
        <div class="stat"><b>9</b><span>obszarów prawa</span></div>
        <div class="stat"><b>3</b><span>języki: polski, angielski, niemiecki</span></div>
      </div>
    </div>
  </section>
  <section class="s" id="kancelaria">
    <div class="wrap split">
      <div><span class="label"><span class="dot"></span>01 · Kancelaria</span><h2 style="margin-top:18px">Kim jesteśmy</h2></div>
      <div>
        <p class="statement big">Usługi dopasowujemy do sprawy i&nbsp;potrzeb klienta. Pracujemy <b>w&nbsp;kancelarii</b>, <b>w&nbsp;siedzibie firmy klienta</b> i&nbsp;<b>online</b>.</p>
        <p style="margin-top:24px;color:var(--ink-2);font-size:17px;max-width:60ch">Zespół pracuje pod kierunkiem dwóch wspólników. Doradzamy osobom prywatnym i&nbsp;przedsiębiorcom, reprezentujemy klientów przed sądami powszechnymi, sądami administracyjnymi i&nbsp;urzędami. Odległość nie jest przeszkodą: na rozprawy jeździmy do sądów w&nbsp;całej Polsce, a&nbsp;konsultacje prowadzimy także przez telefon i&nbsp;wideo. Doradztwo prowadzimy po polsku, angielsku i&nbsp;niemiecku.</p>
      </div>
    </div>
  </section>
  <section class="s tint" id="zespol" style="background:var(--paper-2)">
    <div class="wrap">
      <div class="s-head">
        <div><span class="label"><span class="dot"></span>02 · Zespół</span><h2 style="margin-top:18px">Adwokaci</h2></div>
        <p>Kliknij kartę, żeby zadzwonić do kancelarii.</p>
      </div>
      <div class="team">{team}</div>
    </div>
  </section>
  <section class="s dark" id="zasady">
    <div class="wrap">
      <div class="s-head">
        <div><span class="label"><span class="dot"></span>03 · Zasady</span><h2 style="margin-top:18px">Jak pracujemy</h2></div>
        <p>Cztery zasady, które obowiązują w&nbsp;każdej sprawie.</p>
      </div>
      <div class="princ">
        <div>{svg("coin")}<h3>Koszt przed umową</h3><p>Wynagrodzenie ustalamy z&nbsp;góry: stała kwota lub stawka godzinowa, zapisana w&nbsp;umowie.</p></div>
        <div>{svg("doc")}<h3>Informacja na bieżąco</h3><p>Wiesz, co dzieje się w&nbsp;sprawie: o&nbsp;każdym piśmie i&nbsp;terminie informujemy na bieżąco.</p></div>
        <div>{svg("shield")}<h3>Tajemnica adwokacka</h3><p>Wszystko, co nam przekażesz, pozostaje poufne, także zanim podpiszesz umowę.</p></div>
        <div>{svg("globe")}<h3>Cała Polska i&nbsp;online</h3><p>Siedziba w&nbsp;Opolu, sprawy w&nbsp;sądach w&nbsp;całej Polsce, konsultacje przez telefon i&nbsp;wideo.</p></div>
      </div>
    </div>
  </section>
  <section class="s" id="obszary">
    <div class="wrap">
      <div class="s-head">
        <div><span class="label"><span class="dot"></span>04 · Obszary</span><h2 style="margin-top:18px">W czym pomagamy</h2></div>
        <p>Dziewięć dziedzin prawa. Każda ma swoją stronę z&nbsp;zakresem spraw, przepisami i&nbsp;odpowiedziami na częste pytania.</p>
      </div>
      <div class="topics">{areas}</div>
    </div>
  </section>
{cta(pre)}"""
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "PKW Adwokaci", "item": SITE + "/"}, {"@type": "ListItem", "position": 2, "name": "O kancelarii", "item": SITE + "/" + path}]},
        {"@type": "AboutPage", "name": "O kancelarii", "url": SITE + "/" + path, "about": dict(PROVIDER, foundingDate="2014", knowsLanguage=["pl", "en", "de"], employee=[{"@type": "Person", "name": n.replace("adw. ", ""), "jobTitle": r} for n, r, _, _ in ZESPOL])}]}
    return path, page(pre, path, "O kancelarii – PKW Adwokaci, Opole", "Polański Konofalski i Wspólnicy Spółka Partnerska Adwokatów: kancelaria z Opola od 2014 roku. Zespół, zasady współpracy i obszary prawa.", body, ld, current="o-kancelarii")

# ---------- kontakt ----------
def build_contact():
    pre = "../"; path = "kontakt/"
    iban = "PL 03 1140 2017 0000 4102 1306 6060"
    body = f"""  <section class="ko-hero">
    <div class="wrap">
      <div>
        <span class="label"><span class="dot"></span>Kontakt</span>
        <h1>kontakt <span>z kancelarią</span></h1>
        <p class="lead">Zadzwoń, napisz albo przyjdź do kancelarii w&nbsp;Opolu. Konsultację możesz też odbyć online, z&nbsp;dowolnego miejsca.</p>
        <div class="hero-cta">
          <a class="btn green" href="tel:+48774143669">Zadzwoń: 77 414 36 69 <span class="arr">→</span></a>
          <a class="btn ghost" href="{pre}#kontakt">Wyślij pismo do analizy</a>
        </div>
      </div>
      <div class="addr">
        <span class="pin">{svg("pin")}</span>
        <b>ul. Ks. H. Kołłątaja 11 lok. 27<br>45 - 064 Opole</b>
        <p>II piętro</p>
        <div class="lines">
          <a href="tel:+48774143669"><span>Biuro</span>+48 77 414 36 69</a>
          <a href="tel:+48608301225"><span>Komórka</span>+48 608 301 225</a>
          <a href="mailto:biuro@pkwadwokaci.pl"><span>E-mail</span>biuro@pkwadwokaci.pl</a>
        </div>
      </div>
    </div>
  </section>
  <section class="s" id="kanaly">
    <div class="wrap">
      <div class="s-head">
        <div><span class="label"><span class="dot"></span>01 · Kanały</span><h2 style="margin-top:18px">Jak się z&nbsp;nami skontaktować</h2></div>
        <p>Wybierz najwygodniejszy sposób. Pilną sprawę z&nbsp;terminem najlepiej zacząć od telefonu.</p>
      </div>
      <div class="modes">
        <article class="mode"><span class="mode-ic" aria-hidden="true">{svg("phone")}</span><h3>Biuro</h3><p>Telefon stacjonarny kancelarii.</p><p class="fit"><em>Dobre, gdy</em>chcesz umówić termin lub sprawa jest pilna.</p><a class="go" href="tel:+48774143669">77 414 36 69 <span class="arr">→</span></a></article>
        <article class="mode"><span class="mode-ic" aria-hidden="true">{svg("mobile")}</span><h3>Komórka</h3><p>Telefon komórkowy kancelarii.</p><p class="fit"><em>Dobre, gdy</em>nie możesz dodzwonić się do biura.</p><a class="go" href="tel:+48608301225">608 301 225 <span class="arr">→</span></a></article>
        <article class="mode"><span class="mode-ic" aria-hidden="true">{svg("wa")}</span><h3>WhatsApp</h3><p>Wiadomość i&nbsp;zdjęcie pisma.</p><p class="fit"><em>Dobre, gdy</em>masz pismo w&nbsp;ręku i&nbsp;chcesz je od razu pokazać.</p><a class="go" href="https://wa.me/48608301225" target="_blank" rel="noopener">Napisz na WhatsApp <span class="arr">→</span></a></article>
        <article class="mode"><span class="mode-ic" aria-hidden="true">{svg("mail")}</span><h3>E-mail</h3><p>Opis sprawy i&nbsp;dokumenty w&nbsp;załączniku.</p><p class="fit"><em>Dobre, gdy</em>dokumentów jest dużo albo wolisz napisać.</p><a class="go" href="mailto:biuro@pkwadwokaci.pl">biuro@pkwadwokaci.pl <span class="arr">→</span></a></article>
      </div>
    </div>
  </section>
  <section class="s tint" id="dojazd" style="background:var(--paper-2)">
    <div class="wrap">
      <div class="s-head">
        <div><span class="label"><span class="dot"></span>02 · Dojazd</span><h2 style="margin-top:18px">Kancelaria w&nbsp;Opolu</h2></div>
        <p>Centrum Opola, ul. Kołłątaja 11. Na spotkanie w&nbsp;kancelarii umów się wcześniej telefonicznie.</p>
      </div>
      <div class="map">
        <div class="map-frame"><iframe title="Mapa: PKW Adwokaci, ul. Kołłątaja 11, Opole" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://maps.google.com/maps?q=ul.%20Ko%C5%82%C5%82%C4%85taja%2011%2C%2045-064%20Opole&amp;z=16&amp;output=embed"></iframe></div>
        <div>
          <ul class="how">
            <li>{svg("pin")}<div><b>ul. Ks. H. Kołłątaja 11 lok. 27</b><span>45 - 064 Opole</span></div></li>
            <li>{svg("stairs")}<div><b>II piętro</b><span>Lokal nr 27.</span></div></li>
            <li>{svg("clock")}<div><b>Spotkanie po umówieniu</b><span>Zadzwoń lub napisz, żeby ustalić termin.</span></div></li>
            <li>{svg("video")}<div><b>Nie możesz przyjechać?</b><span><a href="{pre}konsultacje-online/">Konsultacja online</a> przez telefon lub wideo.</span></div></li>
          </ul>
          <div class="map-cta">
            <a class="btn" href="{MAPS}" target="_blank" rel="noopener" data-apple="{APPLE}">Wyznacz trasę <span class="arr">→</span></a>
            <a class="btn line" href="tel:+48774143669">Zadzwoń</a>
          </div>
        </div>
      </div>
    </div>
  </section>
  <section class="s dark" id="dane">
    <div class="wrap firm">
      <div><span class="label"><span class="dot"></span>03 · Dane</span><h2 style="margin-top:18px">Dane kancelarii</h2><p style="margin-top:20px;color:rgba(255,255,255,.72);max-width:40ch">Do faktur, umów i&nbsp;przelewów.</p></div>
      <div class="channels">
        <div><span>Nazwa</span><span>Polański Konofalski i&nbsp;Wspólnicy Spółka Partnerska Adwokatów</span></div>
        <div><span>Adres</span><span>ul. Ks. H. Kołłątaja 11 lok. 27 (II piętro), 45 - 064 Opole</span></div>
        <div><span>NIP</span><span>754-308-06-91</span></div>
        <div><span>REGON</span><span>1611572964</span></div>
        <div><span>Numer konta</span><span>IBAN {iban} <button class="copy" type="button" data-copy="PL03114020170000410213066060">Kopiuj</button></span></div>
        <div><span>BIC</span><span>BREXPLPWMUL</span></div>
      </div>
    </div>
  </section>
{faq_html([
    ("Ile kosztuje pierwsza rozmowa?", "Koszt konsultacji podajemy przed rozmową, na piśmie. Zadzwoń albo napisz, a otrzymasz wycenę dla swojej sprawy."),
    ("Termin już prawie minął. Co teraz?", "Wyślij zdjęcie pisma przez formularz i zadzwoń. Sprawy z terminem do 3 dni rozpatrujemy w pierwszej kolejności."),
    ("Czy rozmowa jest poufna?", "Tak. Wszystko, co przekażesz adwokatowi, objęte jest tajemnicą adwokacką, także zanim podpiszesz umowę."),
    ("Mieszkam w innym mieście. Czy muszę przyjechać?", "Nie. Konsultacja może odbyć się online, a dokumenty podpiszesz elektronicznie albo odeślesz kurierem."),
])}
{cta(pre, "Wyślij pismo <span>do analizy</span>")}"""
    js = "document.querySelectorAll('.copy').forEach(function(b){b.addEventListener('click',function(){var t=b.dataset.copy;(navigator.clipboard?navigator.clipboard.writeText(t):Promise.reject()).then(function(){b.textContent='Skopiowano'},function(){b.textContent=t});setTimeout(function(){b.textContent='Kopiuj'},2500)})});"
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "PKW Adwokaci", "item": SITE + "/"}, {"@type": "ListItem", "position": 2, "name": "Kontakt", "item": SITE + "/" + path}]},
        {"@type": "ContactPage", "name": "Kontakt", "url": SITE + "/" + path, "about": dict(PROVIDER, taxID="7543080691")}]}
    return path, page(pre, path, "Kontakt – PKW Adwokaci, Opole", "Kontakt z kancelarią PKW Adwokaci w Opolu: telefon 77 414 36 69, WhatsApp 608 301 225, e-mail, adres ul. Kołłątaja 11, dojazd i dane do faktur.", body, ld, current="kontakt", extra_js=js)

def main():
    out = [build_area(a) for a in OBSZARY] + [build_about(), build_contact()]
    for path, doc in out:
        d = os.path.join(ROOT, path); os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(doc)
    print("Zbudowano podstrony:", len(out))
    return [p for p, _ in out]

PATHS = ["obszar-dzialania/%s/" % a["slug"] for a in OBSZARY] + ["o-kancelarii/", "kontakt/"]

if __name__ == "__main__":
    main()
