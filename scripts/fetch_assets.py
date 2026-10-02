#!/usr/bin/env python3
"""Pobiera materiały wymienione w assets.json (np. z Higgsfield) i przygotowuje je pod stronę.

- wideo: H.264, bez dźwięku, max 1920 px szerokości, szybki start (faststart), opcjonalnie klatka-plakat
- obraz: JPG o zadanej szerokości

Pliki, które już istnieją, są pomijane, chyba że pozycja ma "force": true.
Wymaga ffmpeg. Użycie: python3 scripts/fetch_assets.py
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def run(cmd):
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)


def download(url, dest):
    req = urllib.request.Request(url, headers={"User-Agent": "pk-adwokaci-assets/1.0"})
    with urllib.request.urlopen(req, timeout=120) as r, open(dest, "wb") as f:
        shutil.copyfileobj(r, f)


def process(item, src):
    out = os.path.join(ROOT, item["file"])
    os.makedirs(os.path.dirname(out), exist_ok=True)
    kind = item.get("type") or ("video" if out.endswith((".mp4", ".webm")) else "image")
    if kind == "video":
        width = int(item.get("width", 1920))
        run(["ffmpeg", "-y", "-v", "error", "-i", src, "-an", "-c:v", "libx264", "-preset", "slow",
             "-crf", str(item.get("crf", 26)), "-pix_fmt", "yuv420p", "-movflags", "+faststart",
             "-vf", f"scale='min({width},iw)':-2", out])
        if item.get("poster"):
            poster = os.path.join(ROOT, item["poster"])
            run(["ffmpeg", "-y", "-v", "error", "-ss", "0", "-i", out, "-frames:v", "1",
                 "-vf", "scale=1280:-2", "-q:v", "5", poster])
    else:
        width = int(item.get("width", 1600))
        run(["ffmpeg", "-y", "-v", "error", "-i", src, "-vf", f"scale='min({width},iw)':-2",
             "-q:v", str(item.get("quality", 4)), out])
    return out


def pending(manifest):
    """Pozycje z adresem url, których pliku jeszcze nie ma (albo mają force)."""
    out = []
    for item in manifest.get("assets", []):
        target = os.path.join(ROOT, item["file"])
        if item.get("url") and (not os.path.exists(target) or item.get("force")):
            out.append(item["file"])
    return out


def main():
    with open(os.path.join(ROOT, "assets.json"), encoding="utf-8") as f:
        manifest = json.load(f)
    if "--pending" in sys.argv:
        # tylko liczba brakujących plików (automat instaluje ffmpeg wyłącznie, gdy > 0)
        print(len(pending(manifest)))
        return
    changed, failed = [], []
    for item in manifest.get("assets", []):
        target = os.path.join(ROOT, item["file"])
        if os.path.exists(target) and not item.get("force"):
            print(f"= jest już: {item['file']}")
            continue
        url = item.get("url")
        if not url:
            print(f"! brak adresu url: {item['file']}")
            failed.append(item["file"])
            continue
        with tempfile.TemporaryDirectory() as tmp:
            src = os.path.join(tmp, "source")
            try:
                download(url, src)
                process(item, src)
                print(f"+ pobrano: {item['file']}")
                changed.append(item["file"])
            except Exception as e:  # noqa: BLE001
                print(f"! błąd przy {item['file']}: {e}")
                failed.append(item["file"])
    print(f"Nowe pliki: {len(changed)}, błędy: {len(failed)}")
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
