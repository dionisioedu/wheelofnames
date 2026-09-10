#!/usr/bin/env python3
"""Reproducible integrity checks for the static GitHub Pages site."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse
import json
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.ids = []
        self.jsonld = []
        self._jsonld_parts = None

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if values.get("id"):
            self.ids.append(values["id"])
        for key in ("href", "src"):
            if values.get(key):
                self.links.append(values[key])
        if tag == "script" and values.get("type", "").lower() == "application/ld+json":
            self._jsonld_parts = []

    def handle_data(self, data):
        if self._jsonld_parts is not None:
            self._jsonld_parts.append(data)

    def handle_endtag(self, tag):
        if tag == "script" and self._jsonld_parts is not None:
            self.jsonld.append("".join(self._jsonld_parts).strip())
            self._jsonld_parts = None


def local_target(page, raw):
    if not raw or raw.startswith(("#", "mailto:", "tel:", "data:", "javascript:")):
        return None
    parsed = urlparse(raw)
    if parsed.scheme or parsed.netloc:
        return None
    path = unquote(parsed.path)
    if not path:
        return None
    target = ROOT / path.lstrip("/") if path.startswith("/") else page.parent / path
    if path.endswith("/") or target.is_dir():
        target /= "index.htm"
    return target.resolve()


def main():
    errors = []
    pages = sorted(ROOT.rglob("*.htm"))
    for page in pages:
        parser = PageParser()
        try:
            parser.feed(page.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"{page.relative_to(ROOT)}: HTML parse failed: {exc}")
            continue

        duplicates = sorted({item for item in parser.ids if parser.ids.count(item) > 1})
        if duplicates:
            errors.append(f"{page.relative_to(ROOT)}: duplicate ids: {', '.join(duplicates)}")

        if "/engagement.js" not in parser.links:
            errors.append(f"{page.relative_to(ROOT)}: missing shared analytics.js")

        for index, payload in enumerate(parser.jsonld, 1):
            if not payload:
                errors.append(f"{page.relative_to(ROOT)}: empty JSON-LD block {index}")
                continue
            try:
                json.loads(payload)
            except json.JSONDecodeError as exc:
                errors.append(f"{page.relative_to(ROOT)}: invalid JSON-LD block {index}: {exc}")

        for raw in parser.links:
            target = local_target(page, raw)
            if target and ROOT not in target.parents and target != ROOT:
                errors.append(f"{page.relative_to(ROOT)}: link escapes site root: {raw}")
            elif target and not target.exists():
                errors.append(f"{page.relative_to(ROOT)}: missing local target: {raw}")

    try:
        manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
        for icon in manifest.get("icons", []):
            target = local_target(ROOT / "index.htm", icon.get("src", ""))
            if target and not target.exists():
                errors.append(f"manifest.json: missing icon: {icon.get('src')}")
    except Exception as exc:
        errors.append(f"manifest.json: {exc}")

    try:
        sitemap_root = ET.parse(ROOT / "sitemap.xml").getroot()
        locations = [node.text.strip() for node in sitemap_root.iter() if node.tag.endswith("loc") and node.text]
        html_routes = {
            "/" if page == ROOT / "index.htm" else "/" + page.parent.relative_to(ROOT).as_posix() + "/"
            for page in pages
        }
        sitemap_routes = {urlparse(url).path for url in locations}
        missing = sorted(html_routes - sitemap_routes)
        stale = sorted(sitemap_routes - html_routes)
        if missing:
            errors.append("sitemap.xml: missing routes: " + ", ".join(missing))
        if stale:
            errors.append("sitemap.xml: routes without pages: " + ", ".join(stale))
    except Exception as exc:
        errors.append(f"sitemap.xml: {exc}")

    if errors:
        print(f"Static validation failed with {len(errors)} issue(s):")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Static validation passed: {len(pages)} pages, local assets, JSON-LD, manifest and sitemap.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
