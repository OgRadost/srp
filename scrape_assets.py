#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pobiera grafiki i filmy z www.srp.se do katalogu img/ (per podstrona).
UWAGA: to materiały, do których prawa ma Svenska Räddningsprodukter AB —
przed publikacją potwierdź pisemnie prawo do ich użycia (umowa dystrybucyjna).
Uruchom: python3 scrape_assets.py
"""
import os, re, html, urllib.request, urllib.parse

BASE = "https://www.srp.se"
ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "img")

# mapowanie: podstrona źródłowa -> prefiks nazwy pliku (nasz slug)
PAGES = {
    "/": "home",
    "/produkter/raddningsdocka-pro-elite-military": "manekin-pro-elite-military",
    "/produkter/raddningsdocka-pro-elite": "manekin-pro-elite",
    "/produkter/raddningsdocka-pro-military": "manekin-pro-military",
    "/produkter/raddningsdocka-pro": "manekin-pro",
    "/produkter/raddningsdocka-standard": "manekin-standard",
    "/produkter/sarskadesimulatorer": "symulatory-ran",
    "/produkter/raddningsdocka-med-hlr-funktion": "manekin-rko",
    "/produkter/vattenlivraddningsdocka-med-hlr-funktion": "manekin-wodny-rko",
    "/produkter/vattenlivraddningsdockor": "manekiny-ratownictwa-wodnego",
    "/produkter/Overviktsdocka": "manekin-bariatryczny",
    "/produkter/branddockor": "manekiny-pozarowe",
    "/produkter/medicinsk-simulering": "symulacja-medyczna",
    "/produkter/Ovriga-produkter": "pozostale-produkty",
    "/utbildningar": "szkolenia",
    "/om-oss": "o-nas",
    "/produkter": "produkty",
}

MEDIA_RE = re.compile(r"""["'\(](/files/[^"'\)\s]+?\.(?:jpe?g|png|webp|gif|mp4|webm))["'\)]""", re.I)
VIDEO_RE = re.compile(r"""(?:youtube\.com/embed/|youtu\.be/|player\.vimeo\.com/video/)([\w-]+)""", re.I)

UA = {"User-Agent": "Mozilla/5.0 (Macintosh) srp-pl-asset-fetch"}

def fetch(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()

def main():
    os.makedirs(OUT, exist_ok=True)
    seen = {}          # url -> local filename (nie pobieraj dwa razy)
    videos = []
    for page, prefix in PAGES.items():
        try:
            doc = fetch(BASE + page).decode("utf-8", "replace")
        except Exception as e:
            print(f"!! {page}: {e}")
            continue
        doc = html.unescape(doc)
        urls, n = [], 0
        for m in MEDIA_RE.finditer(doc):
            u = m.group(1)
            if u not in urls and "lang-" not in u and "placeholder" not in u:
                urls.append(u)
        for u in urls:
            full = BASE + urllib.parse.quote(u, safe="/:%")
            if full in seen:
                continue
            ext = os.path.splitext(u)[1].lower().replace(".jpeg", ".jpg")
            n += 1
            name = f"{prefix}-{n:02d}{ext}"
            try:
                data = fetch(full)
                if len(data) < 3000:   # pomiń ikonki/śmieci
                    n -= 1
                    continue
                with open(os.path.join(OUT, name), "wb") as f:
                    f.write(data)
                seen[full] = name
                print(f"✓ {name}  ({len(data)//1024} KB)  <- {u}")
            except Exception as e:
                print(f"!! {u}: {e}")
        for v in VIDEO_RE.finditer(doc):
            videos.append((page, v.group(0)))
    print(f"\nPobrano {len(seen)} plików do img/")
    if videos:
        print("Znalezione osadzone filmy (do wstawienia jako embed):")
        for p, v in videos:
            print(f"  {p}: {v}")
    else:
        print("Nie znaleziono osadzonych filmów (mp4/YouTube/Vimeo) na przeszukanych stronach.")

if __name__ == "__main__":
    main()
