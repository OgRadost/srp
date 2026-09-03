# Ekosystem automatyzacji SRP Polska — plan rozbudowy

Wersja: 2026-07-18. Strategia: **małe, niezależne klocki spięte przez n8n** — żaden element
nie jest wpisany na stałe w kod strony, więc każdy da się wymienić bez przebudowy całości.
Rynek (przetargi, kanały social, ceny narzędzi AI) zmienia się szybko — architektura ma to
przetrwać.

---

## Zasady architektury (dlaczego tak, a nie inaczej)

1. **Strona = front, nie system.** Statyczne HTML na GitHub Pages: zero serwera do
   utrzymania, zero kosztów, brak powierzchni ataku. Cała logika żyje w n8n.
2. **n8n = kręgosłup i Wasza własność.** Integracje wchodzą i wychodzą (HubSpot dziś,
   coś innego za rok) — przepływy zostają.
3. **Dane oddzielone od kodu** (`data/site.json`): automat może zmienić treść strony
   (np. dopisać meldunek) bez dotykania szablonów.
4. **Buduj tylko to, co Was wyróżnia** (konfigurator doboru, meldunek, baza wiedzy).
   CRM, mailing, agregator przetargów — wynajmować, nie pisać.
5. **Człowiek domyka sprzedaż.** Automat dowozi ciepłe leady i nie gubi żadnego;
   pokazu i rozmowy z komendantem nie automatyzujemy.
6. **Każdy automat ma bramkę akceptacji** tam, gdzie publikuje w imieniu firmy
   (posty, maile, artykuły) — patrz „Zasady bezpieczeństwa marki".

---

## ETAP 0 — MVP (to budujemy teraz, bez dostępów zewnętrznych)

| # | Element | Status |
|---|---------|--------|
| 0.1 | GitHub Actions: auto-build i deploy po każdej zmianie | ✅ w tym commicie |
| 0.2 | Dane strony w `data/site.json` (meldunek, kontakt, opinie) | ✅ w tym commicie |
| 0.3 | Formularze gotowe pod webhook (jeden przełącznik `FORM_ENDPOINT`) | ✅ w tym commicie |
| 0.4 | Endpoint dla automatu: dopisanie meldunku = edycja JSON → strona sama się przebuduje | ✅ w tym commicie |

Efekt: n8n (albo Ty z telefonu) zmienia jeden plik JSON w repo → strona publikuje się sama.

---

## ETAP 1 — Lead nie ginie (tydzień 1)

- **1.1 Formularze → n8n → CRM.** Kontakt, zapytanie ofertowe, newsletter, konfigurator.
  n8n: walidacja → scoring (przetarg/pokaz = wysoki) → CRM + powiadomienie push/Slack.
- **1.2 Autoresponder < 5 min** z katalogiem PDF i linkiem do kalendarza.
- **1.3 Samoobsługowe umawianie pokazów** (cal.com) zamiast „oddzwonimy".
- **1.4 CRM.** Start: HubSpot Free lub ClickUp (już używany). Spinany przez n8n, nie wprost.

**Potrzebne od Was:** adres e-mail na leady, instancja n8n, decyzja CRM.

---

## ETAP 2 — Popyt sam się zgłasza (tydzień 1–2)

- **2.1 Monitoring przetargów (własny, ~0 zł):** n8n odpytuje ezamowienia.gov.pl i TED
  po frazach: manekin ratowniczy, fantom, symulator ran, pozoracja, szkolenie RKO,
  Stop the Bleed, sprzęt do ćwiczeń ratowniczych → codzienny alert + wpis do CRM.
- **2.2 Test agregatora komercyjnego** (1 miesiąc, ~150–300 zł): łapie zapytania poniżej
  progów z platform zakupowych, których BZP nie pokazuje. **Decyzja po liczbach:**
  ile ogłoszeń ponad to, co złapał własny robot.
- **2.3 Konfigurator doboru manekina** na stronie (quiz → rekomendacja + lead).
- **2.4 Gated content:** wzory OPZ i karty katalogowe za e-mail.

---

## ETAP 3 — Research i obecność w społecznościach (tydzień 2–4)

> Cel: wiedzieć, o czym mówi rynek, i być tam, gdzie zapadają decyzje — **bez spamu**.

- **3.1 Nasłuch (w pełni automatyczny, bezpieczny):**
  - RSS/API: portale pożarnicze i ratownicze, komunikaty PSP/KG PSP, MON, NFZ,
    branżowe newsy o szkoleniach i symulacji medycznej;
  - Reddit API (r/ems, r/firefighting, r/tacticalmedicine), YouTube, publiczne fora
    branżowe — pobieranie tylko tego, co udostępniają API/RSS i regulamin serwisu;
  - Google Alerts + Search Console: o co ludzie realnie pytają w wyszukiwarce.
  - Wyjście: **cotygodniowy briefing tematyczny** (co boli rynek, jakie pytania wracają,
    jakie przetargi/wydarzenia na horyzoncie) → wsad do artykułów i newslettera.
- **3.2 Wykrywanie okazji:** alert, gdy w monitorowanych źródłach pada pytanie
  o dobór fantomów/scenariusze ćwiczeń → trafia do kolejki „warto odpowiedzieć”.
- **3.3 Odpowiedzi na forach/grupach — PÓŁautomat (świadoma decyzja):**
  automat przygotowuje szkic merytorycznej odpowiedzi + link do naszego poradnika,
  **człowiek publikuje z własnego, imiennego konta.** Uzasadnienie w sekcji
  „Zasady bezpieczeństwa marki”.
- **3.4 LinkedIn (firmowy):** publikacja przez oficjalne API, z akceptacją jednym
  kliknięciem. Źródła postów: nowy artykuł, nowy meldunek, nowe szkolenie.

---

## ETAP 4 — Treść, która pisze się sama (tydzień 3–6)

- **4.1 Redakcja artykułów (AI + akceptacja):** briefing z etapu 3 → szkic artykułu
  do strefy wiedzy (struktura, SEO, CTA) → **Twoja akceptacja** → publikacja
  (commit do repo → auto-deploy) → post na LinkedIn → wzmianka w newsletterze.
  Kadencja startowa: 1 artykuł/tydzień.
- **4.2 Newsletter (AI redaguje, człowiek zatwierdza):** miesięczny numer składany
  automatycznie z: nowych artykułów, meldunków, terminów szkoleń, jednej porady
  praktycznej. Narzędzie: MailerLite/Brevo (darmowe do ~1000 kontaktów).
- **4.3 Sekwencja powitalna (raz napisana, działa latami):** 5–7 maili
  segmentowanych po typie organizacji z formularza (straż ≠ szpital ≠ wojsko).
- **4.4 Repurposing:** artykuł → karuzela na LinkedIn → skrypt na short → grafika.

---

## ETAP 5 — Sprzedaż bez przepisywania danych (miesiąc 2)

- **5.1 Generator ofert PDF** z konfiguracji klienta (n8n + szablon).
- **5.2 E-podpis** (Autenti) na umowach i protokołach odbioru.
- **5.3 Fakturowanie** (Fakturownia/inFakt) + automatyczne monity o płatność.
- **5.4 Pipeline w CRM** z automatycznymi follow-upami (3/7/21 dni po ofercie).

---

## ETAP 6 — Przychód powtarzalny (miesiąc 2–3) ⭐ największy potencjał

- **6.1 Rejestracja sprzętu** na stronie (nr seryjny) → automatyczne: przegląd po 12 mies.,
  koniec gwarancji, instrukcje konserwacji.
- **6.2 Cykliczne uzupełnianie eksploatacji** (krew symulacyjna, gaza, części) —
  model „maszynka i żyletki”: mail w cyklu do każdego posiadacza fantomu.
- **6.3 Mini-sklep na akcesoria** (linki płatności Stripe/Przelewy24 — działa
  ze statycznej strony, bez backendu). Fantomy sprzedaje pokaz; akcesoria mają
  sprzedawać się same.
- **6.4 Certyfikaty szkoleń PDF** + automatyczne przypomnienie o recertyfikacji
  (szkolenie staje się przychodem cyklicznym).
- **6.5 Automat opinii:** 2 tyg. po dostawie ankieta → zgoda na cytat → sekcja opinii.

---

## ETAP 7 — Koło zamachowe i pomiar (ciągłe)

- **7.1 Pętla:** dostawa w CRM → wpis do meldunku na stronie → post → ruch → leady → pokaz
  → dostawa. Bez ręcznej publikacji.
- **7.2 Analityka:** Plausible (bez bannera cookies) + Search Console; miesięczny raport
  automatyczny: ruch, źródła, leady, pokazy, koszt leada.
- **7.3 AI-czat na stronie** (na treściach serwisu): odpowiada 24/7, kwalifikuje, umawia pokaz.
- **7.4 Monitoring dostępności** strony + backup leadów.

---

## Zasady bezpieczeństwa marki (nienegocjowalne)

1. **Żadnych automatycznych postów na forach i grupach z kont firmowych.**
   Regulaminy Facebooka, LinkedIna i większości forów branżowych zakazują automatycznego
   publikowania i masowych wiadomości — realne ryzyko to blokada konta i (gorzej)
   spalenie reputacji w środowisku, które jest małe i pamiętliwe. Strażacy i ratownicy
   wyczuwają automat natychmiast. Dlatego: **automat researchuje i pisze szkic,
   człowiek publikuje.**
2. **Zero fikcji w treściach:** opinie, referencje, meldunki — wyłącznie prawdziwe
   (dyrektywa Omnibus, kary UOKiK, a przede wszystkim wiarygodność wobec instytucji).
3. **Artykuły i newsletter przed publikacją akceptuje człowiek** — AI myli się
   w szczegółach technicznych (wymiary, normy, procedury medyczne), a tu błąd
   merytoryczny kosztuje zaufanie klienta, którego zdobycie zajęło miesiące.
4. **RODO:** zgody marketingowe zbierane osobno, polityka prywatności aktualizowana
   przy każdej nowej integracji, dane leadów tylko w CRM (nie w repo).
5. **Prawa do materiałów SRP** (zdjęcia, filmy, logo) — potwierdzenie od producenta.

---

## Odporność na zmienność rynku

- **Wymienne klocki:** CRM, mailing, agregator przetargów i model AI da się wymienić
  w godzinę (zmiana węzła w n8n), bo nic z tego nie jest wpisane w kod strony.
- **Dane u Was:** kontakty w CRM z regularnym eksportem, treści w repo (Git = historia),
  przepływy w n8n (self-hosted) — żaden dostawca nie trzyma Was zakładnikiem.
- **Start na darmowych planach**, płatne dopiero, gdy licznik pokaże zwrot.
- **Kwartalny przegląd:** co działa, co wyłączamy, gdzie rynek się przesunął.

---

## Kolejność wdrożenia (rekomendacja)

1. **ETAP 0** (teraz) — fundament, bez niego nic dalej nie zadziała.
2. **ETAP 1 + 2** — leady i przetargi = najkrótsza droga do gotówki.
3. **ETAP 3 + 4** — research, artykuły, newsletter = budowa pozycji eksperta.
4. **ETAP 6** — przychód powtarzalny.
5. **ETAP 5 + 7** — usprawnienia i pomiar.

## Blokery po stronie klienta (bez tego stoimy)

- [ ] e-mail na leady i alerty
- [ ] instancja n8n (istniejąca czy stawiamy nową?)
- [ ] wybór CRM (HubSpot Free / ClickUp)
- [ ] dane firmy: nazwa, telefon, adres, NIP
- [ ] prawdziwe dostawy do meldunku
- [ ] logotypy certyfikatów (STB / ERC / TECC)
