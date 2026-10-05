#!/usr/bin/env python3
"""
Inject a complete, consistent favicon/apple-touch-icon link block into every
page, idempotently.

- Replaces any existing `<link rel="icon" ...>` line.
- Ensures the block exists right after the manifest link (or charset if none).
- Skips re-adding if already present.

Usage:  python3 _gen/inject_icon_links.py            # apply
        python3 _gen/inject_icon_links.py --check     # verify only
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BLOCK = """  <link rel="icon" href="/favicon.ico" sizes="any">
  <link rel="icon" type="image/png" sizes="32x32" href="/icons/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="/icons/favicon-16x16.png">
  <link rel="apple-touch-icon" sizes="180x180" href="/icons/favicon-180x180.png">"""

ICON_LINE_RE = re.compile(r'[ \t]*<link[^>]*rel="icon"[^>]*>\s*\n?')
APPLE_LINE_RE = re.compile(r'[ \t]*<link[^>]*rel="apple-touch-icon"[^>]*>\s*\n?')
MANIFEST_RE = re.compile(r'([ \t]*<link[^>]*rel="manifest"[^>]*>\n)')


def process(path, check=False):
    with open(path, "r", encoding="utf-8") as f:
        src = f.read()

    has_complete = ('/icons/favicon-32x32.png' in src and
                    'apple-touch-icon" sizes="180x180" href="/icons/favicon-180x180.png"' in src and
                    'rel="icon" href="/favicon.ico"' in src)
    if has_complete:
        return "ok"

    if check:
        return "MISSING"

    # strip any existing icon / apple-touch lines
    out = ICON_LINE_RE.sub("", src)
    out = APPLE_LINE_RE.sub("", out)

    # insert the block after the manifest link if present, else after charset
    m = MANIFEST_RE.search(out)
    if m:
        out = out[:m.end()] + BLOCK + "\n" + out[m.end():]
    else:
        cm = re.search(r'(<meta charset[^>]*>\n)', out)
        if cm:
            out = out[:cm.end()] + BLOCK + "\n" + out[cm.end():]
        else:
            out = out.replace("<head>", "<head>\n" + BLOCK, 1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(out)
    return "fixed"


def main():
    check = "--check" in sys.argv
    changed = missing = total = 0
    for dirpath, _dirs, files in os.walk(ROOT):
        if "_gen" in dirpath or "/.git" in dirpath:
            continue
        for name in files:
            if not name.endswith(".htm"):
                continue
            total += 1
            p = os.path.join(dirpath, name)
            r = process(p, check=check)
            if r == "fixed":
                changed += 1
            elif r == "MISSING":
                missing += 1
                print("MISSING:", os.path.relpath(p, ROOT))
    if check:
        print(f"check: {total} pages, {missing} missing icon block")
    else:
        print(f"done: {changed} pages updated, {total} total")


if __name__ == "__main__":
    main()
