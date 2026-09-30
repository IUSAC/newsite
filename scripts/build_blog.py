#!/usr/bin/env python3
"""Buduje blog (lawyerai.pl/blog) z plików w content/blog/<slug>/ (meta.json + body.html).

- blog/index.html            lista artykułów
- blog/<slug>/index.html      artykuł
- sitemap.xml, robots.txt     dla Google
Nagłówek, stopka, style i skrypty są brane z obszar-dzialania/index.html, więc blog wygląda jak reszta strony.
Artykuły ze statusem "szkic" mają noindex, oznaczenie „Szkic” i nie trafiają do sitemap.xml.
Uruchom: python3 scripts/build_blog.py
"""
import html, json, math, os, re, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://lawyerai.pl"
FIRM = "Polański Konofalski i Wspólnicy Sp.p. Adwokatów"
BRAND = "PKW Adwokaci"
PHONE = "+48774143669"
PHONE_TXT = "77 414 36 69"
ADDRESS = {"streetAddress": "ul. Kołłątaja 11 lok. 27", "postalCode": "45-064", "addressLocality": "Opole", "addressCountry": "PL"}
CATS = [("prawo-karne", "Prawo karne"), ("karne-skarbowe-i-podatkowe", "Karne skarbowe i podatkowe"),
        ("prawo-administracyjne", "Administracyjne"), ("prawo-rodzinne", "Rodzinne"), ("prawo-cywilne", "Cywilne")]
MONTHS = ["stycznia", "lutego", "marca", "kwietnia", "maja", "czerwca", "lipca", "sierpnia", "września", "października", "listopada", "grudnia"]

def esc(s): return html.escape(s, quote=True)
def pl_date(d):
    y, m, dd = map(int, d.split("-")); return f"{dd} {MONTHS[m-1]} {y}"
def slugify(t):
    t = t.lower()
    for a, b in zip("ąćęłńóśźż", "acelnoszz"): t = t.replace(a, b)
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")

# ---------- szkielet strony z podstrony „Obszar działania” ----------
base = open(os.path.join(ROOT, "obszar-dzialania", "index.html"), encoding="utf-8").read()
HEAD, rest = base.split("</head>", 1)
BODY_TOP = rest.split("<main id=\"start\">", 1)[0]
BODY_END = rest.split("</main>", 1)[1]
HEAD = re.sub(r"<title>.*?</title>\s*", "", HEAD, flags=re.S)
HEAD = re.sub(r'<meta name="description"[^>]*>\s*', "", HEAD)
# skrypt podstrony otwiera <details> z kotwicy – na blogu niepotrzebny, ale nieszkodliwy

BLOG_CSS = open(os.path.join(ROOT, "scripts", "blog.css"), encoding="utf-8").read()

def menu_with_blog(top, pre):
    top = top.replace('href="../', f'href="{pre}')
    if f'href="{pre}blog/">Blog' not in top:
        top = top.replace(f'<a href="{pre}#kontakt">Kontakt</a>', f'<a href="{pre}blog/">Blog</a>\n      <a href="{pre}#kontakt">Kontakt</a>', 1)
    return top

def page(pre, title, desc, canonical, body, jsonld, og_img=None, noindex=False, extra_js=""):
    head = HEAD.replace('href="../', f'href="{pre}').replace('src="../', f'src="{pre}')
    meta = [f"<title>{esc(title)}</title>", f'<meta name="description" content="{esc(desc)}">',
            f'<link rel="canonical" href="{canonical}">',
            f'<meta property="og:type" content="{"article" if "/blog/" in canonical and canonical.count("/") > 4 else "website"}">',
            f'<meta property="og:title" content="{esc(title)}">', f'<meta property="og:description" content="{esc(desc)}">',
            f'<meta property="og:url" content="{canonical}">', '<meta property="og:locale" content="pl_PL">',
            f'<meta property="og:site_name" content="{BRAND}">']
    if og_img: meta += [f'<meta property="og:image" content="{SITE}/{og_img}">', '<meta name="twitter:card" content="summary_large_image">']
    if noindex: meta.append('<meta name="robots" content="noindex, follow">')
    for j in jsonld: meta.append('<script type="application/ld+json">' + json.dumps(j, ensure_ascii=False) + "</script>")
    top = menu_with_blog(BODY_TOP, pre)
    end = BODY_END.replace('href="../', f'href="{pre}').replace('src="../', f'src="{pre}')
    end = end.replace("</body>", extra_js + "\n</body>", 1)
    return (head + "\n".join(meta) + f"\n<style>\n{BLOG_CSS}\n</style>\n</head>" + top +
            '<main id="start">\n' + body + "\n</main>" + end)

# ---------- artykuły ----------
src_dir = os.path.join(ROOT, "content", "blog")
posts = []
for slug in sorted(os.listdir(src_dir)):
    d = os.path.join(src_dir, slug)
    if not os.path.isdir(d): continue
    m = json.load(open(os.path.join(d, "meta.json"), encoding="utf-8"))
    m["slug"] = slug
    m["body"] = open(os.path.join(d, "body.html"), encoding="utf-8").read()
    words = len(re.sub(r"<[^>]+>", " ", m["body"]).split())
    m["minutes"] = max(1, math.ceil(words / 200))
    posts.append(m)
TODAY = os.environ.get("BLOG_TODAY") or datetime.date.today().isoformat()
# „zaplanowany” = ukazuje się sam w dniu date_published (automat publikacji uruchamia się codziennie)
for p in posts:
    if p["status"] == "zaplanowany":
        p["status"] = "opublikowany" if p["date_published"] <= TODAY else "przyszly"
future = {p["slug"] for p in posts if p["status"] == "przyszly"}
posts = [p for p in posts if p["status"] != "przyszly"]
posts.sort(key=lambda p: (p["date_published"], p.get("order", 0)), reverse=True)
by_slug = {p["slug"]: p for p in posts}
def unlink_future(html_):
    # link do wpisu, który jeszcze się nie ukazał → sam tekst
    return re.sub(r'<a href="\.\./([a-z0-9-]+)/">(.*?)</a>', lambda m: m.group(2) if m.group(1) in future else m.group(0), html_)
catname = dict(CATS)

def author_block(p):
    a = p.get("author", {})
    ini = "".join(w[0] for w in a.get("name", "PKW").replace("adw.", "").split()[:2]).upper()
    return a, ini

def card(p, pre, big=False):
    draft = '<span class="b-draft">Szkic</span>' if p["status"] != "opublikowany" else ""
    return (f'<a class="b-card{" b-card--big" if big else ""}" href="{pre}{p["slug"]}/" data-cat="{p["category"]}">'
            f'<span class="b-card__img"><img src="{pre}../{p["cover"]}" alt="{esc(p["cover_alt"])}" width="1600" height="900" loading="{"eager" if big else "lazy"}" decoding="async"></span>'
            f'<span class="b-card__txt"><span class="b-meta"><span class="b-cat">{esc(catname[p["category"]])}</span>{draft}<span>{p["minutes"]} min czytania</span></span>'
            f'<strong class="b-card__t">{esc(p["title"])}</strong><span class="b-card__d">{esc(p["excerpt"])}</span>'
            f'<span class="b-more">Czytaj <span class="arr">→</span></span></span></a>')

for p in posts:
    pre = "../../"
    body = unlink_future(p["body"])
    toc = []
    def add_id(mo):
        t = re.sub(r"<[^>]+>", "", mo.group(1)); i = slugify(t); toc.append((i, t))
        return f'<h2 id="{i}">{mo.group(1)}</h2>'
    body = re.sub(r"<h2>(.*?)</h2>", add_id, body)
    a, ini = author_block(p)
    toc_html = "".join(f'<li><a href="#{i}">{esc(t)}</a></li>' for i, t in toc + ([("faq", "Najczęstsze pytania")] if p.get("faq") else []))
    tldr = "".join(f"<li>{x}</li>" for x in p.get("tldr", []))
    faq = "".join(f'<details class="b-faq__i"><summary>{esc(q)}</summary><div>{unlink_future(ans)}</div></details>' for q, ans in p.get("faq", []))
    rel = [by_slug[s] for s in p.get("related", []) if s in by_slug and s != p["slug"]]
    for q in posts:  # dopełnij z tej samej kategorii, potem najnowszymi
        if len(rel) >= 2: break
        if q["slug"] != p["slug"] and q not in rel and q["category"] == p["category"]: rel.append(q)
    for q in posts:
        if len(rel) >= 2: break
        if q["slug"] != p["slug"] and q not in rel: rel.append(q)
    rel_html = "".join(card(r, "../") for r in rel)
    draft_bar = ('<div class="b-draftbar">Szkic do akceptacji adwokata · niewidoczny dla Google</div>' if p["status"] != "opublikowany" else "")
    reviewer = p.get("reviewer")
    rev_html = f'<span>Weryfikacja: {esc(reviewer)}</span>' if reviewer else ('' if p["status"] == "opublikowany" else '<span class="b-todo">Weryfikacja: adwokat (do uzupełnienia)</span>')
    upd = f'<span>Aktualizacja: <time datetime="{p["date_modified"]}">{pl_date(p["date_modified"])}</time></span>' if p["date_modified"] != p["date_published"] else ""
    art = f'''{draft_bar}<div class="b-progress" aria-hidden="true"><i></i></div>
<article class="b-art">
  <header class="b-head wrap">
    <nav class="b-crumbs" aria-label="Okruszki"><a href="{pre}">Strona główna</a><span>/</span><a href="../">Blog</a><span>/</span><a href="../#{p["category"]}">{esc(catname[p["category"]])}</a></nav>
    <span class="label"><span class="dot"></span>{esc(catname[p["category"]])}</span>
    <h1 class="b-h1">{esc(p["title"])}</h1>
    <p class="b-lead">{p["lead"]}</p>
    <div class="b-byline"><span class="b-ava" aria-hidden="true">{ini}</span><span class="b-byline__t"><strong>{esc(a.get("name", BRAND))}</strong>
      <span class="b-byline__m"><span>Publikacja: <time datetime="{p["date_published"]}">{pl_date(p["date_published"])}</time></span>{upd}<span>{p["minutes"]} min czytania</span>{rev_html}</span></span></div>
  </header>
  <figure class="b-cover wrap"><img src="{pre}{p["cover"]}" alt="{esc(p["cover_alt"])}" width="1600" height="900" fetchpriority="high" decoding="async"><figcaption>Ilustracja poglądowa</figcaption></figure>
  <div class="b-grid wrap">
    <aside class="b-toc"><details open><summary>Spis treści</summary><ol>{toc_html}</ol></details></aside>
    <div class="b-body">
      <div class="b-tldr"><span class="b-tldr__h">W skrócie</span><ul>{tldr}</ul></div>
      {body}
      <section class="b-faq" id="faq"><h2>Najczęstsze pytania</h2>{faq}</section>
      <aside class="b-cta"><span class="label"><span class="dot"></span>{esc(p.get("cta_label", "Masz pismo z sądu?"))}</span>
        <p class="b-cta__t">{esc(p.get("cta_title", "Prześlij nam pismo. Sprawdzimy termin i powiemy, co możesz zrobić."))}</p>
        <div class="b-cta__b"><a class="btn green" href="{pre}#kontakt">Wyślij pismo do analizy <span class="arr">→</span></a><a class="btn ghost" href="tel:{PHONE}">Zadzwoń: {PHONE_TXT}</a></div></aside>
      <div class="b-author"><span class="b-ava b-ava--l" aria-hidden="true">{ini}</span><div><strong>{esc(a.get("name", BRAND))}</strong><p>{esc(a.get("bio", ""))}</p></div></div>
      <p class="b-note">Artykuł ma charakter informacyjny i opisuje stan prawny na dzień aktualizacji. Nie zastępuje porady prawnej w konkretnej sprawie. Tekst przygotowano z pomocą narzędzi AI i sprawdzono merytorycznie przed publikacją.</p>
    </div>
  </div>
  {f'<section class="b-rel wrap"><h2 class="b-rel__h">Przeczytaj też</h2><div class="b-list">{rel_html}</div></section>' if rel_html else ""}
</article>'''
    url = f"{SITE}/blog/{p['slug']}/"
    ld = [{"@context": "https://schema.org", "@type": "BlogPosting", "headline": p["title"], "description": p["description"],
           "image": [f"{SITE}/{p['cover']}"], "datePublished": p["date_published"], "dateModified": p["date_modified"],
           "inLanguage": "pl-PL", "mainEntityOfPage": url,
           "author": {"@type": "Person" if a.get("person") else "Organization", "name": a.get("name", BRAND), "url": SITE + "/#zespol"},
           "publisher": {"@type": "LegalService", "name": FIRM, "url": SITE + "/", "telephone": PHONE, "address": {"@type": "PostalAddress", **ADDRESS}}},
          {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
              {"@type": "ListItem", "position": 1, "name": "Strona główna", "item": SITE + "/"},
              {"@type": "ListItem", "position": 2, "name": "Blog", "item": SITE + "/blog/"},
              {"@type": "ListItem", "position": 3, "name": p["title"], "item": url}]}]
    if p.get("faq"):
        ld.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", ans)}} for q, ans in p["faq"]]})
    js = '''<script>(function(){var b=document.querySelector('.b-progress i'),a=document.querySelector('.b-art');if(!b||!a)return;
function u(){var r=a.getBoundingClientRect(),h=r.height-innerHeight;b.style.transform='scaleX('+Math.min(1,Math.max(0,-r.top/Math.max(1,h)))+')'}
addEventListener('scroll',u,{passive:true});u();
var links=[].slice.call(document.querySelectorAll('.b-toc a')),hs=links.map(function(l){return document.getElementById(l.getAttribute('href').slice(1))});
if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){var i=hs.indexOf(e.target);links.forEach(function(l,k){l.classList.toggle('is-on',k===i)})}})},{rootMargin:'0px 0px -70% 0px'});hs.forEach(function(h){h&&io.observe(h)})}
if(innerWidth<900){var d=document.querySelector('.b-toc details');if(d)d.open=false}
})();</script>'''
    out = page(pre, p["seo_title"], p["description"], url, art, ld, p["cover"], p["status"] != "opublikowany", js)
    os.makedirs(os.path.join(ROOT, "blog", p["slug"]), exist_ok=True)
    open(os.path.join(ROOT, "blog", p["slug"], "index.html"), "w", encoding="utf-8").write(out)

# ---------- lista artykułów ----------
pre = "../"
# Filtr: krótkie, równoległe nazwy + liczba wpisów; kategorie bez wpisów są ukryte (UX: brak pustych wyników)
SHORT = {"prawo-karne": "Karne", "karne-skarbowe-i-podatkowe": "Podatkowe", "prawo-administracyjne": "Administracyjne",
         "prawo-rodzinne": "Rodzinne", "prawo-cywilne": "Cywilne"}
cnt = {c: sum(1 for p in posts if p["category"] == c) for c, _ in CATS}
chips = f'<button type="button" data-f="all" aria-pressed="true">Wszystkie<span class="n">{len(posts)}</span></button>' + "".join(
    f'<button type="button" data-f="{c}" aria-pressed="false" title="{esc(n)}">{SHORT[c]}<span class="n">{cnt[c]}</span></button>'
    for c, n in CATS if cnt[c])
feat = card(posts[0], "", True) if posts else ""
grid = "".join(card(p, "") for p in posts[1:])
hero_img = "assets/blog/blog-hero.jpg"
body = f'''<section class="b-hero" style="--hero:url({pre}{hero_img})">
  <div class="wrap"><span class="label"><span class="dot"></span>Blog · prawo w praktyce</span>
    <h1 class="b-hero__h">Pismo z sądu lub urzędu?<br><span>Wyjaśniamy krok po kroku.</span></h1>
    <p class="b-hero__p">Terminy, procedury i Twoje prawa w sprawach karnych, skarbowych, administracyjnych, rodzinnych i cywilnych. Każdy tekst sprawdza adwokat.</p></div>
</section>
<section class="s b-index"><div class="wrap">
  <div class="filters b-filters" role="group" aria-label="Kategorie">{chips}</div>
  {feat}
  <div class="b-list">{grid}</div>
  <p class="b-empty" hidden>W tej kategorii artykuły pojawią się wkrótce.</p>
</div></section>'''
js = '''<script>(function(){var bs=document.querySelectorAll('.b-filters button'),cs=document.querySelectorAll('.b-index .b-card'),em=document.querySelector('.b-empty');
function set(f){bs.forEach(function(b){b.setAttribute('aria-pressed',b.dataset.f===f?'true':'false')});var n=0;cs.forEach(function(c){var on=f==='all'||c.dataset.cat===f;c.hidden=!on;if(on)n++});em.hidden=n>0}
bs.forEach(function(b){b.addEventListener('click',function(){set(b.dataset.f);history.replaceState(null,'',b.dataset.f==='all'?location.pathname:'#'+b.dataset.f)})});
var h=location.hash.slice(1);if(h&&document.querySelector('.b-filters button[data-f="'+h+'"]'))set(h);
var fb=document.querySelector('.b-filters');function edge(){fb.classList.toggle('is-end',fb.scrollLeft+fb.clientWidth>=fb.scrollWidth-4)}fb.addEventListener('scroll',edge,{passive:true});addEventListener('resize',edge);edge();
bs.forEach(function(b){b.addEventListener('click',function(){b.scrollIntoView({block:'nearest',inline:'center',behavior:'smooth'})})})})();</script>'''
ld = [{"@context": "https://schema.org", "@type": "Blog", "name": f"Blog {BRAND}", "url": SITE + "/blog/", "inLanguage": "pl-PL",
       "publisher": {"@type": "LegalService", "name": FIRM, "url": SITE + "/"},
       "blogPost": [{"@type": "BlogPosting", "headline": p["title"], "url": f"{SITE}/blog/{p['slug']}/", "datePublished": p["date_published"]} for p in posts if p["status"] == "opublikowany"]}]
out = page(pre, f"Blog prawniczy – poradniki adwokatów | {BRAND}",
           "Poradniki adwokatów z Opola: wyrok nakazowy, kontrola skarbowa, odwołanie od decyzji, rozwód, alimenty. Terminy i procedury krok po kroku.",
           SITE + "/blog/", body, ld, hero_img, not any(p["status"] == "opublikowany" for p in posts), js)
os.makedirs(os.path.join(ROOT, "blog"), exist_ok=True)
open(os.path.join(ROOT, "blog", "index.html"), "w", encoding="utf-8").write(out)

# ---------- sitemap.xml i robots.txt ----------
today = datetime.date.today().isoformat()
urls = [(SITE + "/", today), (SITE + "/co-sie-stalo/", today), (SITE + "/obszar-dzialania/", today)]
pub = [p for p in posts if p["status"] == "opublikowany"]
if pub: urls.append((SITE + "/blog/", max(p["date_modified"] for p in pub)))
urls += [(f"{SITE}/blog/{p['slug']}/", p["date_modified"]) for p in pub]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
    f"  <url><loc>{u}</loc><lastmod>{d}</lastmod></url>\n" for u, d in urls) + "</urlset>\n"
open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write(sm)
open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
print(f"Zbudowano ({TODAY}): {len(posts)} artykułów ({len(pub)} opublikowanych), zaplanowane na później: {len(future)}, sitemap: {len(urls)} adresów")
