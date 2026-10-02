# -*- coding: utf-8 -*-
"""Treści podstron obszarów prawa, O kancelarii i Kontakt.

Zasady: § 23 Kodeksu Etyki Adwokackiej (bez obietnic wyniku, ocen skuteczności, porównań, straszenia).
Przepisy zweryfikowane 01.10.2026 (agent weryfikujący, źródła: arslege.pl, komentarzpzp.pl, dlajurysty.pl, MS).
Edytuj tutaj, potem: python3 scripts/build_podstrony.py
"""

# term: (wartość, jednostka, czego dotyczy, przepis)
OBSZARY = [
  {
    "slug": "prawo-cywilne", "n": "01", "name": "Prawo cywilne", "h1": ("prawo", "cywilne"),
    "lead": "Spory o zapłatę, odszkodowania, spadki i zachowek, prawo rzeczowe, umowy i prawo pracy. Dla osób prywatnych i firm.",
    "desc": "Prawo cywilne w Opolu i online: sprawy o zapłatę, odszkodowania, spadki i zachowek, umowy, prawo pracy. Terminy, przebieg współpracy, konsultacja z adwokatem.",
    "chips": ["Zapłata", "Odszkodowania", "Spadki", "Prawo pracy"],
    "topics": [
      ("Sprawy o zapłatę", "Najem, dzierżawa, sprzedaż, dostawa, roboty budowlane, dzieło, zlecenie, pożyczka, poręczenie."),
      ("Odszkodowania i zadośćuczynienie", "Szkody majątkowe i krzywdy, ochrona dóbr osobowych, spory z ubezpieczycielem."),
      ("Spadki i zachowek", "Dziedziczenie, dział spadku, zachowek, ochrona praw spadkobiercy."),
      ("Prawo rzeczowe", "Własność, zasiedzenie, służebności, użytkowanie, zastaw."),
      ("Umowy", "Analiza, projekty i negocjacje umów, spory powstałe przy ich wykonaniu."),
      ("Prawo pracy", "Dokumentacja pracownicza, umowy i kontrakty menedżerskie, rozwiązanie umowy, spory przed sądem pracy."),
    ],
    "terms_title": "Terminy, które warto znać",
    "terms": [
      ("6", "lat", "Ogólny termin przedawnienia roszczeń. Dla działalności gospodarczej i świadczeń okresowych: 3 lata.", "art. 118 k.c."),
      ("5", "lat", "Przedawnienie roszczenia o zachowek, liczone od ogłoszenia testamentu.", "art. 1007 § 1 k.c."),
      ("1", "tydzień", "Wniosek o doręczenie wyroku z uzasadnieniem, liczony od ogłoszenia wyroku.", "art. 328 § 1 k.p.c."),
      ("2", "tygodnie", "Apelacja od wyroku, liczona od doręczenia wyroku z uzasadnieniem.", "art. 369 § 1 k.p.c."),
    ],
    "blog": ["sprzeciw-od-nakazu-zaplaty"],
    "faq": [
      ("Roszczenie jest stare. Czy mogę go jeszcze dochodzić?", "To zależy od terminu przedawnienia. Ogólny termin to 6 lat, a dla działalności gospodarczej i świadczeń okresowych 3 lata (art. 118 k.c.). Koniec terminu przypada na ostatni dzień roku kalendarzowego, chyba że termin jest krótszy niż dwa lata."),
      ("Czy warto wysłać wezwanie do zapłaty przed pozwem?", "Często tak: porządkuje sprawę i bywa, że kończy ją bez sądu. Przygotujemy wezwanie i ocenimy, jaki krok będzie następny."),
      ("Pomagacie pracownikom czy pracodawcom?", "Obu stronom: przy umowach, rozwiązaniu stosunku pracy i w sporach przed sądem pracy."),
    ],
  },
  {
    "slug": "prawo-karne", "n": "02", "name": "Prawo karne", "h1": ("prawo", "karne"),
    "lead": "Obrona i reprezentacja na każdym etapie: od wezwania na policję, przez proces, po wykonanie kary. Także sprawy karne skarbowe i gospodarcze.",
    "desc": "Adwokat karny w Opolu i online: obrona podejrzanego i oskarżonego, pokrzywdzeni, sprawy kierowców, karne skarbowe. Terminy k.p.k. i przebieg współpracy.",
    "chips": ["Obrona", "Pokrzywdzeni", "Kierowcy", "Karne skarbowe"],
    "topics": [
      ("Obrona podejrzanego i oskarżonego", "Postępowanie przygotowawcze, sądowe i odwoławcze."),
      ("Pokrzywdzeni", "Zawiadomienie o przestępstwie, udział w procesie, oskarżyciel posiłkowy i prywatny."),
      ("Sprawy kierowców", "Jazda po alkoholu, wypadki drogowe, zatrzymanie prawa jazdy."),
      ("Przestępstwa gospodarcze", "Oszustwa, wyłudzenia, działanie na szkodę wierzyciela, pranie pieniędzy."),
      ("Mienie i zdrowie", "Kradzież, przywłaszczenie, rozbój, pobicie, udział w bójce."),
      ("Narkotyki", "Sprawy z ustawy o przeciwdziałaniu narkomanii: posiadanie, udzielanie, obrót."),
      ("Karne skarbowe", "Zarzuty z k.k.s., kontrole skarbowe, czynny żal."),
      ("Wykonanie kary", "Odroczenie wykonania kary, przerwa w karze, warunkowe przedterminowe zwolnienie."),
    ],
    "terms_title": "Terminy w procesie karnym",
    "terms": [
      ("7", "dni", "Sprzeciw od wyroku nakazowego, liczony od doręczenia.", "art. 506 § 1 k.p.k."),
      ("7", "dni", "Wniosek o uzasadnienie wyroku, liczony od ogłoszenia.", "art. 422 § 1 k.p.k."),
      ("14", "dni", "Apelacja, liczona od doręczenia wyroku z uzasadnieniem.", "art. 445 § 1 k.p.k."),
      ("7", "dni", "Zażalenie na postanowienie, od ogłoszenia lub doręczenia.", "art. 460 k.p.k."),
    ],
    "terms_note": "Termin zachowasz, gdy nadasz pismo w placówce pocztowej operatora w Unii Europejskiej (art. 124 k.p.k.).",
    "blog": ["wyrok-nakazowy-co-to-jest", "sprzeciw-od-wyroku-nakazowego", "wezwanie-na-policje-jako-podejrzany", "jazda-po-alkoholu-pierwszy-raz", "zatrzymanie-prawa-jazdy", "czynny-zal-art-16-kks"],
    "faq": [
      ("Dostałem wezwanie na policję jako podejrzany. Co robić?", "Już na tym etapie możesz mieć obrońcę i możesz odmówić składania wyjaśnień. Skontaktuj się z adwokatem przed przesłuchaniem."),
      ("Jestem pokrzywdzonym. Czy mogę mieć pełnomocnika?", "Tak. Pełnomocnik pomoże złożyć zawiadomienie i wnioski dowodowe oraz dochodzić roszczeń w procesie."),
      ("Czy bronicie w sądach poza Opolem?", "Tak. Na rozprawy jeździmy do sądów w całej Polsce, a konsultacja może odbyć się online."),
    ],
  },
  {
    "slug": "prawo-administracyjne", "n": "03", "name": "Prawo administracyjne", "h1": ("prawo", "administracyjne"),
    "lead": "Odwołania, zażalenia i skargi na decyzje urzędów. Reprezentacja przed organami administracji, SKO, WSA i NSA.",
    "desc": "Prawo administracyjne w Opolu i online: odwołania od decyzji, prawo budowlane, skargi do WSA i NSA. Terminy k.p.a. i p.p.s.a., przebieg współpracy.",
    "chips": ["Odwołania", "Prawo budowlane", "WSA", "NSA"],
    "topics": [
      ("Odwołania od decyzji", "Analiza decyzji, odwołanie i zażalenie, udział w postępowaniu."),
      ("Prawo budowlane", "Pozwolenia na budowę, warunki zabudowy, nakazy rozbiórki, samowola budowlana."),
      ("Skargi do WSA i NSA", "Skarga do wojewódzkiego sądu administracyjnego i skarga kasacyjna do NSA."),
      ("Wnioski do urzędów", "Wnioski wszczynające postępowanie i pisma w jego toku."),
      ("Uprawnienia i zezwolenia", "Prawo jazdy, koncesje, zezwolenia, pobyt cudzoziemców."),
      ("Kary administracyjne", "Kary pieniężne nakładane przez organy i ich zaskarżanie."),
    ],
    "terms_title": "Terminy w sprawach administracyjnych",
    "terms": [
      ("14", "dni", "Odwołanie od decyzji, liczone od doręczenia lub ustnego ogłoszenia.", "art. 129 § 2 k.p.a."),
      ("7", "dni", "Zażalenie na postanowienie organu.", "art. 141 § 2 k.p.a."),
      ("30", "dni", "Skarga do WSA, liczona od doręczenia rozstrzygnięcia.", "art. 53 § 1 p.p.s.a."),
      ("30", "dni", "Skarga kasacyjna do NSA, od doręczenia wyroku z uzasadnieniem.", "art. 177 § 1 p.p.s.a."),
    ],
    "blog": ["odwolanie-od-decyzji-administracyjnej", "skarga-do-wsa", "zatrzymanie-prawa-jazdy"],
    "faq": [
      ("Od kiedy liczy się termin na odwołanie?", "Od doręczenia decyzji, a gdy decyzję ogłoszono ustnie, od jej ogłoszenia (art. 129 § 2 k.p.a.)."),
      ("Czy odwołanie musi mieć szczegółowe uzasadnienie?", "Nie. Wystarczy, że z odwołania wynika niezadowolenie z decyzji (art. 128 k.p.a.). Warto jednak wskazać zarzuty i dowody."),
      ("Organ drugiej instancji utrzymał decyzję. Co dalej?", "Można wnieść skargę do WSA w ciągu 30 dni od doręczenia rozstrzygnięcia (art. 53 § 1 p.p.s.a.)."),
    ],
  },
  {
    "slug": "prawo-rodzinne", "n": "04", "name": "Prawo rodzinne", "h1": ("prawo", "rodzinne"),
    "lead": "Rozwód i separacja, alimenty, kontakty z dziećmi, władza rodzicielska, ojcostwo i przysposobienie, sprawy nieletnich. Rzeczowo i poufnie.",
    "desc": "Prawo rodzinne w Opolu i online: rozwód, alimenty, kontakty z dziećmi, władza rodzicielska, podział majątku. Podstawy prawne i przebieg współpracy.",
    "chips": ["Rozwód", "Alimenty", "Kontakty", "Władza rodzicielska", "Nieletni"],
    "topics": [
      ("Rozwód i separacja", "Z orzekaniem o winie i bez, unieważnienie małżeństwa."),
      ("Alimenty", "Ustalenie, zabezpieczenie na czas sprawy, podwyższenie i obniżenie."),
      ("Kontakty z dziećmi", "Ustalenie i zmiana kontaktów, ich wykonywanie."),
      ("Władza rodzicielska", "Zawieszenie, ograniczenie, pozbawienie i przywrócenie."),
      ("Ojcostwo", "Ustalenie i zaprzeczenie ojcostwa."),
      ("Przysposobienie, opieka, kuratela", "Sprawy opiekuńcze przed sądem rodzinnym."),
      ("Podział majątku", "Podział majątku wspólnego i zniesienie współwłasności."),
      ("Demoralizacja nieletnich, czyny karalne", "Reprezentowanie rodziców i opiekunów w postępowaniu sądowym, obrona nieletnich w sprawach przed sądem."),
    ],
    "terms_title": "Przepisy, od których zaczyna się sprawa",
    "terms": [
      ("art. 56", "k.r.o.", "Rozwód: sąd orzeka go przy zupełnym i trwałym rozkładzie pożycia.", "art. 56 § 1 k.r.o."),
      ("art. 58", "k.r.o.", "W wyroku rozwodowym sąd rozstrzyga o władzy rodzicielskiej, kontaktach i kosztach utrzymania dziecka.", "art. 58 § 1 k.r.o."),
      ("art. 133", "k.r.o.", "Alimenty na dziecko, które nie jest w stanie utrzymać się samodzielnie.", "art. 133 § 1 k.r.o."),
      ("art. 753", "k.p.c.", "Zabezpieczenie alimentów na czas trwania sprawy.", "art. 753 § 1 k.p.c."),
    ],
    "blog": ["pozew-o-rozwod", "ile-trwa-rozwod", "alimenty-na-dziecko"],
    "faq": [
      ("Czy alimenty można dostać jeszcze w trakcie sprawy?", "Tak. Sąd może zabezpieczyć alimenty na czas trwania sprawy; wystarczy uprawdopodobnienie roszczenia (art. 753 § 1 k.p.c.)."),
      ("Czy rozwód bez orzekania o winie trwa krócej?", "Zwykle tak, bo sąd nie bada winy. Czas zależy jednak od sądu i od tego, czy trzeba ustalić sprawy dzieci."),
      ("Czy pierwsza rozmowa może być online?", "Tak. Konsultacja odbywa się przez telefon lub wideo, a dokumenty możesz wysłać wcześniej."),
    ],
  },
  {
    "slug": "prawo-rolne-i-przetworstwa-rolnego", "n": "05", "name": "Prawo rolne i przetwórstwa rolnego", "h1": ("prawo", "rolne"),
    "lead": "Rolnicy indywidualni, grupy producenckie i firmy przetwórstwa rolnego: umowy, nieruchomości rolne, dopłaty i postępowania przed urzędami.",
    "desc": "Prawo rolne w Opolu i online: obrót nieruchomościami rolnymi, kontraktacja, dopłaty, grupy producenckie, prawo ochrony środowiska.",
    "chips": ["Ziemia rolna", "Kontraktacja", "Dopłaty", "Grupy producenckie"],
    "topics": [
      ("Nieruchomości rolne", "Nabycie, dzierżawa i najem gruntów rolnych."),
      ("Kontraktacja i umowy", "Umowy kontraktacji i dostawy, połączenia przedsiębiorstw."),
      ("Produkcja i obrót żywnością", "Obsługa produkcji i obrotu produktami rolnymi i spożywczymi."),
      ("Dopłaty i dofinansowania", "Wnioski, odwołania i spory o środki."),
      ("Ochrona środowiska", "Postępowania przed organami ochrony środowiska i sądami administracyjnymi."),
      ("Opinie i analizy", "Analizy prawne dla przedsiębiorstw produkcji rolnej."),
    ],
    "terms_title": "Przepisy przy obrocie ziemią",
    "terms": [
      ("art. 3", "ust. 1", "Przy sprzedaży nieruchomości rolnej prawo pierwokupu ma dzierżawca.", "art. 3 ust. 1 u.k.u.r."),
      ("art. 3", "ust. 4", "Gdy dzierżawcy nie ma albo nie skorzysta z pierwokupu, prawo to ma KOWR.", "art. 3 ust. 4 u.k.u.r."),
      ("art. 158", "k.c.", "Przeniesienie własności nieruchomości wymaga aktu notarialnego.", "art. 158 k.c."),
    ],
    "blog": [],
    "faq": [
      ("Kupuję ziemię rolną. Kto ma prawo pierwokupu?", "Najpierw dzierżawca (art. 3 ust. 1 u.k.u.r.). Gdy go nie ma albo nie skorzysta z prawa, pierwokup przysługuje KOWR (art. 3 ust. 4)."),
      ("Czy pomagacie przy odwołaniach w sprawie dopłat?", "Tak. Przygotujemy odwołanie i poprowadzimy sprawę, także przed sądem administracyjnym."),
      ("Czy obsługujecie grupy producenckie?", "Tak. Przygotowujemy i opiniujemy umowy oraz dokumenty grup producenckich i spółek."),
    ],
  },
  {
    "slug": "prawo-egzekucyjne-i-windykacja-naleznosc", "n": "06", "name": "Prawo egzekucyjne i windykacja należności", "h1": ("windykacja", "i egzekucja"),
    "lead": "Od wezwania do zapłaty, przez klauzulę wykonalności, po nadzór nad działaniami komornika.",
    "desc": "Windykacja i egzekucja w Opolu i online: wezwania do zapłaty, zabezpieczenie, klauzula wykonalności, wnioski egzekucyjne, skarga na czynności komornika.",
    "chips": ["Windykacja", "Egzekucja", "Komornik", "Zabezpieczenie"],
    "topics": [
      ("Windykacja przedsądowa", "Monity, wezwania do zapłaty, mediacja."),
      ("Zabezpieczenie roszczeń", "Zastępstwo w postępowaniu zabezpieczającym."),
      ("Klauzula wykonalności", "Reprezentacja w postępowaniu klauzulowym."),
      ("Wnioski egzekucyjne", "Egzekucja z nieruchomości, zajęcie ksiąg wieczystych, opis i oszacowanie."),
      ("Nadzór nad komornikiem", "Stały monitoring działań komorniczych i skargi na czynności."),
      ("Egzekucja z nieruchomości", "Zastępstwo przed organem egzekucyjnym i sądem."),
    ],
    "terms_title": "Terminy w windykacji i egzekucji",
    "terms": [
      ("6", "lat", "Przedawnienie roszczenia stwierdzonego prawomocnym wyrokiem.", "art. 125 § 1 k.c."),
      ("1", "tydzień", "Skarga na czynności komornika, od dnia czynności lub zawiadomienia o niej.", "art. 767 § 4 k.p.c."),
      ("3", "lata", "Przedawnienie roszczeń związanych z działalnością gospodarczą.", "art. 118 k.c."),
    ],
    "blog": ["sprzeciw-od-nakazu-zaplaty"],
    "faq": [
      ("Dłużnik nie płaci mimo wyroku. Co dalej?", "Potrzebny jest tytuł wykonawczy, czyli wyrok z klauzulą wykonalności. Z nim składamy wniosek do komornika i pilnujemy przebiegu egzekucji."),
      ("Komornik dokonał czynności niezgodnie z prawem. Co mogę zrobić?", "Złożyć skargę na czynność komornika w ciągu tygodnia (art. 767 § 4 k.p.c.). Termin liczy się od dnia czynności albo od zawiadomienia o niej."),
      ("Komu pomagacie w tych sprawach?", "Przede wszystkim wierzycielom: od wezwania do zapłaty po zakończenie egzekucji."),
    ],
  },
  {
    "slug": "prawo-obrotu-nieruchomosciami", "n": "07", "name": "Prawo obrotu nieruchomościami", "h1": ("prawo", "nieruchomości"),
    "lead": "Zakup, sprzedaż, najem i dzierżawa: analiza stanu prawnego, projekty umów, negocjacje i spory dotyczące nieruchomości.",
    "desc": "Prawo nieruchomości w Opolu i online: analiza stanu prawnego, umowy sprzedaży, najmu i dzierżawy, negocjacje, spory o nieruchomości.",
    "chips": ["Stan prawny", "Umowy", "Najem i dzierżawa", "Spory", "Księga wieczysta"],
    "topics": [
      ("Analiza stanu prawnego", "Księga wieczysta, obciążenia, roszczenia osób trzecich."),
      ("Zakup i sprzedaż", "Umowy przedwstępne, negocjacje, reprezentacja przy transakcji."),
      ("Obciążenia", "Hipoteka, służebność, użytkowanie."),
      ("Najem i dzierżawa", "Projekty i opinie umów, ich wykonanie, roszczenia stron."),
      ("Spory o nieruchomości", "Postępowania sądowe, administracyjne i sądowoadministracyjne."),
      ("Uzgodnienie treści księgi wieczystej", "Powództwo o uzgodnienie treści księgi wieczystej z rzeczywistym stanem prawnym."),
    ],
    "terms_title": "Warto wiedzieć przed transakcją",
    "terms": [
      ("art. 158", "k.c.", "Umowa przeniesienia własności nieruchomości wymaga aktu notarialnego.", "art. 158 k.c."),
      ("art. 390", "§ 2 k.c.", "Umowa przedwstępna w formie aktu notarialnego pozwala żądać zawarcia umowy przyrzeczonej.", "art. 390 § 2 k.c."),
      ("art. 3", "u.k.u.r.", "Przy ziemi rolnej sprawdź prawo pierwokupu dzierżawcy i KOWR.", "art. 3 ust. 1 i 4 u.k.u.r."),
    ],
    "blog": [],
    "faq": [
      ("Na co patrzeć w księdze wieczystej przed zakupem?", "Na właściciela w dziale II, prawa i roszczenia osób trzecich w dziale III oraz hipoteki w dziale IV. Księgę sprawdzisz bezpłatnie w systemie EKW Ministerstwa Sprawiedliwości."),
      ("Czy umowa przedwstępna musi być u notariusza?", "Nie musi, ale forma aktu notarialnego pozwala żądać zawarcia umowy przyrzeczonej (art. 390 § 2 k.c.)."),
      ("Czy pomożecie w sporze z najemcą?", "Tak: od wezwań i rozwiązania umowy po sprawę w sądzie."),
    ],
  },
  {
    "slug": "prawo-zamowien-publicznych-i-pomocy-publicznej", "n": "08", "name": "Prawo zamówień publicznych i pomocy publicznej", "h1": ("zamówienia", "publiczne"),
    "lead": "Dla zamawiających i wykonawców: dokumentacja przetargowa, oferty, odwołania do KIO i roszczenia przy realizacji zamówienia.",
    "desc": "Zamówienia publiczne w Opolu i online: dokumentacja przetargowa, oferty, odwołania do KIO, wadium, realizacja umów, pomoc publiczna.",
    "chips": ["Przetargi", "Oferty", "KIO", "Pomoc publiczna"],
    "topics": [
      ("Dla zamawiających", "Formularze, regulaminy, wzory pism i dokumenty do wszczęcia postępowania."),
      ("Dla wykonawców", "Analiza dokumentacji przetargowej pod kątem ryzyka prawnego."),
      ("Odwołania do KIO", "Odwołania od czynności i zaniechań zamawiającego."),
      ("Wadium i roszczenia", "Zatrzymanie wadium i szkody związane z udziałem w postępowaniu."),
      ("Realizacja umowy", "Doradztwo na etapie wykonania zamówienia."),
      ("Pomoc publiczna", "Opinie i analizy prawne."),
    ],
    "terms_title": "Terminy na odwołanie do KIO",
    "terms": [
      ("10", "dni", "Zamówienia od progów unijnych, gdy informację przekazano elektronicznie.", "art. 515 ust. 1 pkt 1 lit. a Pzp"),
      ("5", "dni", "Zamówienia poniżej progów unijnych, gdy informację przekazano elektronicznie.", "art. 515 ust. 1 pkt 2 lit. a Pzp"),
    ],
    "blog": [],
    "faq": [
      ("Od kiedy liczy się termin na odwołanie do KIO?", "Od przekazania informacji o czynności zamawiającego, która jest podstawą odwołania. Przy zamówieniach od progów unijnych to 10 dni, poniżej progów 5 dni (art. 515 Pzp)."),
      ("Odrzucono naszą ofertę. Co możemy zrobić?", "Przeanalizujemy uzasadnienie zamawiającego i, jeśli są podstawy, przygotujemy odwołanie w terminie."),
      ("Czy doradzacie też zamawiającym?", "Tak: od przygotowania dokumentacji po postępowanie przed KIO."),
    ],
  },
  {
    "slug": "prawo-gospodarcze-i-handlowe", "n": "09", "name": "Prawo gospodarcze i handlowe", "h1": ("prawo", "gospodarcze"),
    "lead": "Spółki i przedsiębiorcy: zakładanie i likwidacja spółek, umowy wspólników, organy spółek, KRS, restrukturyzacja i upadłość.",
    "desc": "Prawo gospodarcze i handlowe w Opolu i online: spółki, umowy wspólników, KRS, zgromadzenia, likwidacja, upadłość i restrukturyzacja.",
    "chips": ["Spółki", "KRS", "Wspólnicy", "Upadłość"],
    "topics": [
      ("Zakładanie spółek", "Spółki, oddziały i przedstawicielstwa."),
      ("Umowy wspólników", "Umowy między wspólnikami i akcjonariuszami."),
      ("Spory wspólników", "Spory między wspólnikami i akcjonariuszami."),
      ("Organy spółek", "Obsługa zarządu, rady nadzorczej i zgromadzeń."),
      ("KRS", "Reprezentacja w postępowaniach rejestrowych."),
      ("Likwidacja", "Likwidacja spółek i działalności gospodarczej."),
      ("Upadłość i restrukturyzacja", "Postępowania upadłościowe i naprawcze."),
    ],
    "terms_title": "Przepisy ważne dla zarządu",
    "terms": [
      ("30", "dni", "Wniosek o ogłoszenie upadłości, od dnia wystąpienia podstawy.", "art. 21 ust. 1 Prawa upadłościowego"),
      ("art. 299", "k.s.h.", "Odpowiedzialność członków zarządu sp. z o.o., gdy egzekucja przeciwko spółce okaże się bezskuteczna.", "art. 299 § 1 k.s.h."),
      ("3", "lata", "Przedawnienie roszczeń związanych z działalnością gospodarczą.", "art. 118 k.c."),
    ],
    "blog": ["kontrola-skarbowa-co-robic", "czynny-zal-art-16-kks"],
    "faq": [
      ("Spółka przestała płacić. Na co uważać w zarządzie?", "Na termin wniosku o upadłość: 30 dni od wystąpienia podstawy (art. 21 ust. 1 Prawa upadłościowego). Od tego zależy też odpowiedzialność z art. 299 k.s.h."),
      ("Czy obsługujecie spółki na stałe?", "Tak, stale albo przy konkretnej sprawie. Zasady i koszt (stała kwota lub stawka godzinowa) zapisujemy w umowie."),
      ("Czy doradzacie po angielsku i niemiecku?", "Tak, doradztwo prowadzimy także w językach angielskim i niemieckim."),
    ],
  },
]

ZESPOL = [
  ("adw. Bartosz Polański", "Partner", "BP", "team-portrait-1.jpg"),
  ("adw. Marcin Konofalski", "Partner", "MK", "team-portrait-2.jpg"),
  ("adw. Jolanta Konofalska", "Adwokat", "JK", "team-portrait-3.jpg"),
]

# ---------- /co-sie-stalo/ ----------
# f: filtr; area: indeks pola „Czego dotyczy sprawa?” w formularzu na stronie głównej (0–14, kolejność jak w index.html)
SYTUACJE = [
  {"f": "karne", "law": "art. 178a k.k.", "t": "Jazda po alkoholu, zatrzymane prawo jazdy", "d": "Zakaz prowadzenia pojazdów, konfiskata auta, warunkowe umorzenie.", "v": "7", "u": "dni", "em": "na zażalenie na zatrzymanie prawa jazdy", "area": 3, "blog": ["jazda-po-alkoholu-pierwszy-raz", "zatrzymanie-prawa-jazdy"], "ob": "prawo-karne"},
  {"f": "karne", "law": "k.p.k.", "t": "Dostałem wezwanie na policję", "d": "Jako podejrzany lub świadek. Możesz mieć obrońcę już przed przesłuchaniem.", "v": "1.", "u": "przesłuchanie", "em": "przed nim warto porozmawiać z adwokatem", "area": 3, "blog": ["wezwanie-na-policje-jako-podejrzany"], "ob": "prawo-karne"},
  {"f": "karne", "law": "art. 506 § 1 k.p.k.", "t": "Dostałem wyrok nakazowy bez rozprawy", "d": "Wyrok staje się prawomocny, jeśli nikt nie wniesie sprzeciwu.", "v": "7", "u": "dni", "em": "na sprzeciw, od doręczenia", "area": 3, "blog": ["wyrok-nakazowy-co-to-jest", "sprzeciw-od-wyroku-nakazowego"], "ob": "prawo-karne"},
  {"f": "podatkowe", "law": "Ordynacja podatkowa", "t": "Urząd skarbowy wszczął kontrolę", "d": "Kontrola podatkowa lub celno-skarbowa, wezwania, niezgodności w JPK.", "v": "1.", "u": "pismo", "em": "już wtedy warto mieć pełnomocnika", "area": 2, "blog": ["kontrola-skarbowa-co-robic"], "ob": "prawo-karne"},
  {"f": "podatkowe", "law": "art. 16 k.k.s.", "t": "Zarzuty karne skarbowe, czynny żal", "d": "Faktury, VAT, nierzetelne księgi. Czynny żal działa przed wszczęciem sprawy.", "v": "—", "u": "", "em": "przed wszczęciem postępowania", "area": 3, "blog": ["czynny-zal-art-16-kks"], "ob": "prawo-karne"},
  {"f": "admin", "law": "art. 129 § 2 k.p.a.", "t": "Odmowa pozwolenia, nakaz rozbiórki", "d": "Decyzje budowlane, warunki zabudowy, samowola budowlana.", "v": "14", "u": "dni", "em": "na odwołanie, od doręczenia", "area": 2, "blog": ["odwolanie-od-decyzji-administracyjnej"], "ob": "prawo-administracyjne"},
  {"f": "admin", "law": "art. 53 § 1 p.p.s.a.", "t": "Chcę zaskarżyć decyzję do WSA", "d": "Pobyt cudzoziemców, prawo jazdy, koncesje, kary administracyjne.", "v": "30", "u": "dni", "em": "na skargę do WSA", "area": 2, "blog": ["skarga-do-wsa"], "ob": "prawo-administracyjne"},
  {"f": "rodzinne", "law": "art. 56 k.r.o.", "t": "Rozwód i podział majątku", "d": "Z orzekaniem o winie i bez, mieszkanie, kredyt, firma.", "v": "1", "u": "konsultacja", "em": "by poznać koszt i czas trwania", "area": 10, "blog": ["pozew-o-rozwod", "ile-trwa-rozwod"], "ob": "prawo-rodzinne"},
  {"f": "rodzinne", "law": "art. 133 k.r.o.", "t": "Alimenty i kontakty z dziećmi", "d": "Ustalenie, podwyższenie, obniżenie, zabezpieczenie na czas sprawy.", "v": "1", "u": "konsultacja", "em": "by ocenić sytuację i dowody", "area": 11, "blog": ["alimenty-na-dziecko"], "ob": "prawo-rodzinne"},
  {"f": "cywilne", "law": "k.p.c.", "t": "Dostałem nakaz zapłaty z sądu", "d": "Nakaz się uprawomocni, jeśli nie wniesiesz sprzeciwu w terminie.", "v": "2", "u": "tygodnie", "em": "na sprzeciw w postępowaniu upominawczym", "area": 4, "blog": ["sprzeciw-od-nakazu-zaplaty"], "ob": "prawo-cywilne"},
  {"f": "cywilne", "law": "art. 767 § 4 k.p.c.", "t": "Komornik zajął konto lub wynagrodzenie", "d": "Skarga na czynność komornika, sprawdzenie tytułu wykonawczego.", "v": "1", "u": "tydzień", "em": "na skargę na czynność komornika", "area": 7, "blog": [], "ob": "prawo-egzekucyjne-i-windykacja-naleznosc"},
]
FILTRY = [("all", "Wszystkie"), ("karne", "Karne"), ("podatkowe", "Podatkowe"), ("admin", "Administracyjne"), ("rodzinne", "Rodzinne"), ("cywilne", "Cywilne")]

# kalkulator terminu: (id, nazwa, dni, ustawa, przepis o terminie)
KALKULATOR = [
  ("wn", "Sprzeciw od wyroku nakazowego", 7, "kpk", "art. 506 § 1 k.p.k."),
  ("zk", "Zażalenie w sprawie karnej", 7, "kpk", "art. 460 k.p.k."),
  ("ak", "Apelacja w sprawie karnej", 14, "kpk", "art. 445 § 1 k.p.k."),
  ("od", "Odwołanie od decyzji", 14, "kpa", "art. 129 § 2 k.p.a."),
  ("zp", "Zażalenie na postanowienie urzędu", 7, "kpa", "art. 141 § 2 k.p.a."),
  ("ws", "Skarga do WSA", 30, "ppsa", "art. 53 § 1 p.p.s.a."),
]

# ---------- /obszar-dzialania/ ----------
DLA = {  # o = osoby prywatne, f = firmy
  "prawo-cywilne": "o f", "prawo-karne": "o f", "prawo-administracyjne": "o f", "prawo-rodzinne": "o",
  "prawo-rolne-i-przetworstwa-rolnego": "f", "prawo-egzekucyjne-i-windykacja-naleznosc": "o f",
  "prawo-obrotu-nieruchomosciami": "o f", "prawo-zamowien-publicznych-i-pomocy-publicznej": "f", "prawo-gospodarcze-i-handlowe": "f",
}
# terminy na stronie zbiorczej: (slug obszaru, indeks terminu w OBSZARY[...]["terms"])
TERMINY_ZBIORCZE = [("prawo-karne", 0), ("prawo-administracyjne", 0), ("prawo-administracyjne", 2), ("prawo-cywilne", 1), ("prawo-gospodarcze-i-handlowe", 0), ("prawo-zamowien-publicznych-i-pomocy-publicznej", 0)]
