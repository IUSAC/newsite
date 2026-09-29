# Instrukcje dla Claude: strona PK Adwokaci

- Strona: jeden plik `index.html`, materiały w `assets/`. Styl: biało-czarny, zielony akcent `#00b86b`, wzór lark.de. Treści zgodne z § 23 Kodeksu Etyki Adwokackiej (bez obietnic wyniku, ocen, straszenia).
- „instaluj” (film/obraz z Higgsfield na stronę): dopisz pozycję do `assets.json` z adresem `url` z Higgsfield, podepnij plik w `index.html`, wyślij na `main`. Automat `.github/workflows/assets.yml` pobiera i zapisuje plik. Sesja Claude nie pobiera plików z cloudfront.net sama (blokada sieci) – nie próbuj, używaj automatu.
- „zapisz na hostingu”: wyślij `main` na gałąź `produkcja` (`git push origin main:produkcja`). Automat `.github/workflows/deploy.yml` publikuje na Seohost przez FTPS.
- Podgląd w Claude: artefakt „PK Adwokaci”; publikuj `index.html` z plikami z `assets/`.
