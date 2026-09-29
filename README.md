# PK Adwokaci – strona www

Strona kancelarii Polański Konofalski i Wspólnicy Sp.p. Adwokatów (Opole), stylistycznie wzorowana na lark.de: biało-czarna, zielone akcenty, wideo z lotem przez labirynt wieżowców w nagłówku.

Jeden plik `index.html` (bez budowania) + materiały w `assets/`.

## Materiały z Higgsfield („instaluj”)

1. Dopisz pozycję do `assets.json`: `file` (np. `assets/nowe.mp4`), `type` (`video` / `image`) i `url` z Higgsfield.
2. Wyślij zmianę na `main`.
3. Automat **Materiały z Higgsfield** pobierze plik, zmniejszy go (wideo: H.264 bez dźwięku; obraz: JPG) i zapisze w `assets/`.

Pliki, które już są w repozytorium, są pomijane. Żeby podmienić plik, dodaj `"force": true`.

## Publikacja na Seohost („zapisz na hostingu”)

Wyślij `main` na gałąź `produkcja`. Automat **Publikacja na Seohost** pobierze brakujące materiały i wgra stronę przez FTPS.

Wymagane sekrety repozytorium (Settings → Secrets and variables → Actions): `FTP_SERVER`, `FTP_USERNAME`, `FTP_PASSWORD`, `FTP_DIR` (np. `/public_html/`).

## Stara wersja

Poprzednia strona jest oznaczona tagiem `stara-strona`.
