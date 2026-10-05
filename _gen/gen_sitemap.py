#!/usr/bin/env python3
"""Regenerate sitemap.xml with <lastmod> dates.

lastmod reflects real content freshness: file mtime of each page's index.htm.
Google uses lastmod to prioritise recrawling, so keeping it truthful and
present measurably speeds up reindexing of new/updated pages.

Usage:  python3 _gen/gen_sitemap.py
"""
import os
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAIN = "https://wheeloflist.com"

# (url_path, priority, fs_path_of_source_file)
# url_path is the public path with trailing slash; source is the file on disk.
PAGES = [
    ("/", 1.0, "index.htm"),
    ("/coin-flip/", 0.9, "coin-flip/index.htm"),
    ("/random-number/", 0.9, "random-number/index.htm"),
    ("/dice-roller/", 0.9, "dice-roller/index.htm"),
    ("/yes-no-wheel/", 0.9, "yes-no-wheel/index.htm"),
    ("/team-generator/", 0.9, "team-generator/index.htm"),
    ("/random-letter/", 0.9, "random-letter/index.htm"),
    ("/raffle-picker/", 0.9, "raffle-picker/index.htm"),
    ("/tournament/", 0.9, "tournament/index.htm"),
    ("/tools/", 0.8, "tools/index.htm"),
    ("/wheels/", 0.8, "wheels/index.htm"),
    ("/blog/", 0.8, "blog/index.htm"),
    ("/privacy-policy/", 0.3, "privacy-policy/index.htm"),
    ("/terms/", 0.3, "terms/index.htm"),
]

# Auto-discover blog articles, wheels, and any other */index.htm not listed.
for sub, prio in (("blog", 0.7), ("wheels", 0.8)):
    base = os.path.join(ROOT, sub)
    if not os.path.isdir(base):
        continue
    for name in sorted(os.listdir(base)):
        src = os.path.join(base, name, "index.htm")
        if os.path.isfile(src):
            url = f"/{sub}/{name}/"
            if not any(p[0] == url for p in PAGES):
                PAGES.append((url, prio, f"{sub}/{name}/index.htm"))


def lastmod_for(rel_path):
    full = os.path.join(ROOT, rel_path)
    if not os.path.isfile(full):
        return None
    ts = os.path.getmtime(full)
    return datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%d")


def build():
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for url, prio, src in PAGES:
        lm = lastmod_for(src)
        lines.append("  <url>")
        lines.append(f"    <loc>{DOMAIN}{url}</loc>")
        if lm:
            lines.append(f"    <lastmod>{lm}</lastmod>")
        lines.append(f"    <priority>{prio}</priority>")
        lines.append("  </url>")
    lines.append("</urlset>")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    out = os.path.join(ROOT, "sitemap.xml")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(build())
    print(f"Wrote {out} ({len(PAGES)} urls)")
