# Zasady budowy bloga PKW Adwokaci (lawyerai.pl/blog)

Stałe polecenie właściciela strony. Stosuj przy KAŻDYM nowym wpisie, bez ponownego pytania.
Źródło planu tematów i fraz: dokument „PKW Adwokaci – słowa kluczowe, plan bloga i teksty strony”.

## 1. Tempo i kolejność
- Publikacja: **2 wpisy tygodniowo** (poniedziałek i czwartek) przez pierwsze 3 miesiące, potem **1 tygodniowo + aktualizacja starszych tekstów**.
- Regularność ważniejsza niż ilość. Nigdy kilku wpisów jednego dnia. Zapas tekstów planujemy datami (`"status": "zaplanowany"`, `date_published` w przyszłości); automat publikuje je sam w dniu daty.
- Kolejność tematów według planu z raportu (najpierw priorytet A, krótkie terminy).

## 2. Jeden temat = jedna fraza = jeden wpis (bez kanibalizacji)
- Każdy wpis ma **jedną frazę główną** (`keyword` w meta.json). Przed napisaniem sprawdź listę fraz istniejących wpisów w `content/blog/*/meta.json`.
- Nie twórz wpisu, którego fraza jest odmianą frazy już użytej (np. „sprzeciw od wyroku nakazowego” i „jak złożyć sprzeciw od wyroku nakazowego”). Zamiast tego rozbuduj istniejący wpis.
- Tematy pokrewne rozdzielaj wyraźnie po intencji: „co to jest / skutki” ≠ „jak napisać / krok po kroku” ≠ „ile trwa / ile kosztuje”.

## 3. Jakość treści
- Wpis odpowiada na **jedno konkretne pytanie czytelnika** lepiej niż konkurencja w top 10 Google.
- Długość: zwykle 700–1800 słów razem z „W skrócie” i FAQ. Długość wynika z pytania czytelnika, nie z liczby słów; bez waty i powtórzeń.
- Budowa: tytuł z frazą → lead z odpowiedzią w 2–3 zdaniach → „W skrócie” (3–5 punktów) → 5–8 sekcji H2 → ramka z terminem lub liczbą (`b-box`) → lista kroków (`b-steps`) lub tabela (`b-table`) → FAQ (3–5 pytań) → CTA → autor.
- Każde twierdzenie prawne z numerem przepisu. **Każdy wpis przed publikacją przechodzi niezależną weryfikację przepisów** (osobny agent sprawdzający z aktualnym tekstem ustawy, np. arslege.pl, isap.sejm.gov.pl). Kwot, progów i statystyk bez źródła nie podajemy.
- Stan prawny: data aktualizacji w `date_modified`; przy zmianie przepisów aktualizuj wpis, nie pisz nowego.
- Wzory pism (`b-tpl`) tam, gdzie ludzie szukają „wzór”.

## 4. Etyka i język (§ 23 Kodeksu Etyki Adwokackiej)
- Tylko informacja: bez obietnic wyniku, bez ocen własnej skuteczności („najlepsi”, „wygrywamy”), bez straszenia, bez porównań z innymi kancelariami.
- Prosty język, zdania do ~25 słów, forma „Ty”. Po polsku.
- Nota na dole: charakter informacyjny, nie zastępuje porady; przygotowane z pomocą AI i sprawdzone.

## 5. Linkowanie
- Każdy wpis linkuje do: 1–3 innych wpisów bloga (w treści, naturalnym tekstem kotwicy), strony **Co się stało?** z właściwą kategorią (`../../co-sie-stalo/#karne` itd.) i formularza kontaktu (CTA).
- Linki tylko do wpisów już opublikowanych albo publikowanych wcześniej; generator i tak usuwa link do wpisu, który jeszcze się nie ukazał.
- „Przeczytaj też”: `related` w meta.json; generator dopełnia z tej samej kategorii.
- Po publikacji nowego wpisu dodaj link do niego w 1–2 starszych, pokrewnych wpisach.

## 6. SEO techniczne (automat w `scripts/build_blog.py`)
- `seo_title` do ~60 znaków z frazą na początku; `description` 140–160 znaków z frazą.
- Adres: `/blog/<fraza-bez-polskich-znakow>/`, krótki, bez dat.
- Automatycznie: canonical, Open Graph, dane strukturalne BlogPosting + BreadcrumbList + FAQPage, sitemap.xml, robots.txt, noindex dla szkiców.
- Obrazy: okładka 16:9 z Higgsfield (styl: czarno-białe zdjęcie noir, jeden zielony akcent #ADFF23, bez tekstu i twarzy), `cover_alt` opisuje obraz, podpis „Ilustracja poglądowa”, szerokość 1600 px, plik w `assets/blog/<slug>.jpg`, dodany przez `assets.json`.
- Po każdej publikacji: sprawdzenie strony (zrzut desktop/telefon, brak błędów JS, poprawny JSON-LD).

## 7. E-E-A-T (wiarygodność)
- Autor: prawdziwy adwokat z imieniem, zdjęciem i bio, gdy właściciel poda dane (`author.person: true`, `reviewer`). Do tego czasu „Zespół PKW Adwokaci”.
- Data publikacji i aktualizacji przy każdym wpisie.

## 8. Poza blogiem (do zrobienia i pilnowania)
- Google Search Console z sitemap.xml; co miesiąc przegląd fraz i wejść → nowe tematy lub rozbudowa wpisów.
- Profil Firmy w Google połączony ze stroną.
- Jedna domena główna kancelarii (lawyerai.pl vs pkwadwokaci.pl) — decyzja właściciela.
- Brak treści skopiowanych z innych stron (zduplikowana treść).

## 9. Jak dodać wpis (technicznie)
1. `content/blog/<slug>/meta.json` + `body.html` (wzór: istniejące wpisy).
2. Okładka: Higgsfield → pozycja w `assets.json` (`assets/blog/<slug>.jpg`, width 1600) → push na main (automat pobiera plik).
3. Weryfikacja przepisów (agent), poprawki.
4. `python3 scripts/build_blog.py`, test, commit, `git push origin main` i `git push origin main:produkcja`.
