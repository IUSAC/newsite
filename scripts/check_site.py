#!/usr/bin/env python3
"""Sprawdza stronę przed publikacją (automat uruchamia to w deploy.yml; lokalnie: python3 scripts/check_site.py).

Bez dodatkowych pakietów:
- każdy index.html: doctype, <meta charset>, viewport, <title>, <meta name="description">, canonical
- tytuły i opisy unikalne w całej stronie
- linki wewnętrzne (href/src) prowadzą do istniejących plików
- brak resztek roboczych w treści ("TODO", "lorem", "{{")
Z opcją --zrzuty (wymaga playwright + Chromium): zrzuty telefon (390 px) i komputer (1440 px) każdej strony
do folderu zrzuty/ oraz kontrola, czy strona nie przewija się w bok na telefonie.
Kod wyjścia 1 = są błędy (automat zatrzymuje publikację).
"""
import os, re, sys, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {".git", ".github", ".claude", "scripts", "content", "node_modules", "zrzuty"}
errors, warnings = [], []


def pages():
    out = []
    for d, dirs, files in os.walk(ROOT):
        dirs[:] = [x for x in dirs if x not in SKIP_DIRS]
        if "index.html" in files:
            out.append(os.path.join(d, "index.html"))
    return sorted(out)


def rel(p):
    return os.path.relpath(p, ROOT).replace(os.sep, "/")


def check_head(p, s):
    r = rel(p)
    if not s.lstrip().lower().startswith("<!doctype html"):
        errors.append(f"{r}: brak <!doctype html> na początku")
    if 'charset="utf-8"' not in s.lower().replace("'", '"'):
        errors.append(f"{r}: brak <meta charset=\"utf-8\">")
    if 'name="viewport"' not in s:
        errors.append(f"{r}: brak <meta name=\"viewport\">")
    t = re.search(r"<title>(.*?)</title>", s, re.S)
    d = re.search(r'<meta name="description" content="([^"]*)"', s)
    if not t or not t.group(1).strip():
        errors.append(f"{r}: brak <title>")
    elif len(t.group(1)) > 70:
        warnings.append(f"{r}: tytuł ma {len(t.group(1))} znaków (Google ucina ok. 60–70)")
    if not d or not d.group(1).strip():
        errors.append(f"{r}: brak meta description")
    elif len(d.group(1)) > 170:
        warnings.append(f"{r}: opis ma {len(d.group(1))} znaków (zalecane do ok. 160)")
    if 'rel="canonical"' not in s and r != "index.html":
        warnings.append(f"{r}: brak <link rel=\"canonical\">")
    body = re.sub(r"<(style|script)\b.*?</\1>", " ", s, flags=re.S | re.I)  # tylko treść, bez CSS i JS
    for bad in ("TODO", "lorem ipsum", "{{", "}}"):
        if bad.lower() in body.lower():
            warnings.append(f"{r}: w treści jest „{bad}”")
    return (t.group(1).strip() if t else ""), (d.group(1).strip() if d else "")


def check_links(p, s):
    r = rel(p)
    base = os.path.dirname(p)
    for m in re.finditer(r'(?:href|src|poster)="([^"#?]+)[^"]*"', s):
        u = html.unescape(m.group(1)).strip()
        if not u or u.startswith(("http://", "https://", "mailto:", "tel:", "data:", "//", "javascript:")):
            continue
        target = os.path.normpath(os.path.join(ROOT if u.startswith("/") else base, u.lstrip("/")))
        if os.path.isdir(target):
            target = os.path.join(target, "index.html")
        if not os.path.exists(target):
            errors.append(f"{r}: link do nieistniejącego pliku: {u}")


def screenshots(ps):
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        errors.append("--zrzuty: brak pakietu playwright (pip install playwright)")
        return
    out = os.path.join(ROOT, "zrzuty")
    os.makedirs(out, exist_ok=True)
    exe = None
    for cand in ("/opt/pw-browsers/chromium/chrome", "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"):
        if os.path.exists(cand):
            exe = cand
    import http.server, threading, functools, socketserver
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=ROOT)
    socketserver.TCPServer.allow_reuse_address = True
    srv = socketserver.TCPServer(("127.0.0.1", 0), handler)
    port = srv.server_address[1]
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path=exe) if exe else pw.chromium.launch()
        for p in ps:
            path = rel(p).replace("index.html", "")
            name = (path.strip("/").replace("/", "_") or "glowna")
            for tag, vp, mob in (("komputer", (1440, 900), False), ("telefon", (390, 844), True)):
                pg = b.new_page(viewport={"width": vp[0], "height": vp[1]}, is_mobile=mob, has_touch=mob, device_scale_factor=2 if mob else 1)
                pg.goto(f"http://127.0.0.1:{port}/{path}", wait_until="networkidle")
                pg.wait_for_timeout(600)
                pg.screenshot(path=os.path.join(out, f"{name}-{tag}.png"), full_page=True)
                if mob:
                    over = pg.evaluate("document.documentElement.scrollWidth - window.innerWidth")
                    if over > 2:
                        errors.append(f"{path or '/'}: strona przewija się w bok na telefonie o {over} px")
                    # cele dotyku: przyciski i linki samodzielne (nie linki w zdaniu); za niskie = poniżej 36 px, dla ikon bez tekstu także za wąskie
                    small = pg.evaluate("""() => { const bad=[]; document.querySelectorAll('a,button').forEach(el=>{
                        if(el.closest('p,li,h1,h2,h3,h4,summary,figcaption,td,dd')) return;
                        const r=el.getBoundingClientRect(); if(r.width<=0||r.height<=0) return;
                        const hasText=(el.textContent||'').trim().length>0;
                        if(r.height<36||(!hasText&&r.width<36)) bad.push((el.textContent||el.getAttribute('aria-label')||el.className||'?').trim().slice(0,30))}); return bad.slice(0,8) }""")
                    if small:
                        warnings.append(f"{path or '/'}: małe cele dotyku (< 36 px): {', '.join(small)}")
                pg.close()
        b.close()
    srv.shutdown()
    print(f"Zrzuty: {out}/ ({len(ps)} stron × telefon i komputer)")


def main():
    ps = pages()
    titles, descs = {}, {}
    for p in ps:
        s = open(p, encoding="utf-8").read()
        t, d = check_head(p, s)
        check_links(p, s)
        if t:
            titles.setdefault(t, []).append(rel(p))
        if d:
            descs.setdefault(d, []).append(rel(p))
    for t, where in titles.items():
        if len(where) > 1:
            errors.append(f"ten sam <title> na {len(where)} stronach: {t[:50]} → {', '.join(where)}")
    for d, where in descs.items():
        if len(where) > 1:
            warnings.append(f"ten sam opis na {len(where)} stronach: {', '.join(where)}")
    if "--zrzuty" in sys.argv:
        screenshots(ps)
    for w in warnings:
        print("UWAGA:", w)
    for e in errors:
        print("BŁĄD:", e)
    print(f"Sprawdzono {len(ps)} stron: {len(errors)} błędów, {len(warnings)} uwag")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
