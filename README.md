# SRP Polska — strona dystrybutora

Polska wersja serwisu wzorowana na strukturze i stylu srp.se (Svenska Räddningsprodukter AB),
przygotowana pod wprowadzenie produktów SRP na rynek polski.

## Struktura

- `index.html` — strona główna (hero, pasek zaufania, kategorie, katalog, branże, proces zakupu B2B, FAQ, newsletter)
- `produkty/index.html` — katalog + 13 podstron kategorii produktów (specyfikacje na bazie danych producenta, dane strukturalne schema.org)
- `dla-kogo.html` — ścieżki branżowe (straż, wojsko, medycyna, WOPR, przemysł, edukacja) z rekomendacjami produktów
- `porownanie-manekinow.html` — tabela porównawcza 6 modeli manekinów
- `zamowienia-publiczne.html` — wsparcie przetargów (OPZ, certyfikaty, kryteria)
- `do-pobrania.html` — karty katalogowe i certyfikaty (placeholdery na PDF-y)
- `faq.html` — pytania i odpowiedzi B2B (ze schema FAQPage)
- `wiedza/` — strefa wiedzy: 3 poradniki startowe (dobór manekina, scenariusze ćwiczeń, kontrola krwotoków)
- `szkolenia.html`, `warunki-zakupu.html`, `zapytanie-ofertowe.html` (rozbudowany formularz RFQ: wiele produktów, przetarg, leasing, pokaz), `o-nas.html`, `aktualnosci.html`, `kontakt.html`
- `sitemap.xml`, `robots.txt` — podmień domenę w `write_seo_files()` w `build.py`
- `css/style.css` — wspólne style (ciemna nawigacja, żółte akcenty, pochyłe nagłówki — jak w oryginale)
- `build.py` — generator: **treści edytuj w tym pliku** (dane produktów w `PRODUCTS`, szkolenia w `COURSES`,
  dane firmy na górze pliku), potem `python3 build.py` żeby przebudować wszystkie strony.

## Podgląd lokalny

```
python3 -m http.server 8123
# → http://localhost:8123
```

## Grafiki i filmy (`img/`)

Katalog `img/` zawiera ok. 190 grafik i 2 filmy mp4 pobrane z www.srp.se skryptem
`scrape_assets.py` (nazwy plików = slug podstrony + numer). Generator (`build.py`)
automatycznie ich używa: największe zdjęcie dla danego produktu trafia jako główne,
reszta (>40 KB, bez miniatur) do galerii, pliki mp4 jako wideo na karcie produktu.
Gdy dla sekcji nie ma pliku, pojawia się placeholder.

**WAŻNE:** to materiały, do których prawa autorskie ma Svenska Räddningsprodukter AB.
Przed publikacją strony potwierdź pisemnie (mail wystarczy) prawo do ich wykorzystania —
to standardowy element umowy o wyłącznej dystrybucji. Najlepiej poproś SRP o oryginalną
paczkę zdjęć w pełnej rozdzielczości i logo w wektorze — wersje ze strony są skompresowane.

**Filmy są bardzo duże** (96 MB i 64 MB) — przed wrzuceniem na serwer skompresuj:

```
brew install ffmpeg
ffmpeg -i img/manekin-pro-elite-02.mp4 -vcodec libx264 -crf 28 -preset slow -vf scale=1280:-2 -acodec aac -b:a 96k img/manekin-pro-elite-02-web.mp4
```

(analogicznie dla drugiego pliku; potem podmień nazwy albo nadpisz oryginały).

## Do uzupełnienia przed startem

1. **Dane firmy** — nazwa, adres, NIP, telefon, e-maile (stałe `BRAND`, `DISTRIBUTOR`, `PHONE`, `EMAIL` w `build.py`).
2. **Zgoda producenta** — potwierdź pisemnie z SRP prawo do używania logo, zdjęć, filmów i treści
   marketingowych na polskiej stronie (standardowy element umowy dystrybucyjnej).
4. **Formularze** — kontakt i zapytanie ofertowe trzeba podpiąć pod backend/skrzynkę
   (np. Formspree, własny endpoint albo wtyczka przy przenosinach na WordPress).
5. **Warunki zakupu** — szkic dostosowany do rynku PL; wymaga weryfikacji prawnej
   (prawo konsumenckie, RODO, polityka prywatności i cookies).
6. **Domena i hosting** — pliki są statyczne, wgrasz je na dowolny hosting.
