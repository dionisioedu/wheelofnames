#!/usr/bin/env python3
"""Add Blog link to nav (as top-level, not in the Tools dropdown) and footer of non-generated pages."""
import re

# For nav: insert <li class="nav-item"><a class="nav-link" href="/blog/">Blog</a></li> after Tools/About/Contact group.
NAV_PATTERN = r'(<li class="nav-item"><a class="nav-link" href="/#about">About</a></li>)'
NAV_REPLACE = r'<li class="nav-item"><a class="nav-link" href="/blog/">Blog</a></li>\n          \1'

# For footer: insert before All Tools
FOOT_ANCHOR = '<a href="/tools/" class="text-decoration-none mx-2">All Tools</a>'
FOOT_NEW = '<a href="/blog/" class="text-decoration-none mx-2">Blog</a>\n      ' + FOOT_ANCHOR

FILES = ['index.htm', 'random-number/index.htm', 'dice-roller/index.htm',
         'coin-flip/index.htm', 'yes-no-wheel/index.htm', 'team-generator/index.htm',
         'random-letter/index.htm', 'raffle-picker/index.htm', 'tournament/index.htm',
         'tools/index.htm', 'privacy-policy/index.htm', 'terms/index.htm']

for f in FILES:
    with open(f, encoding='utf-8') as fh:
        html = fh.read()
    nav = foot = 0
    # Only add if not already present
    if '/blog/' not in html:
        pass  # already has it from previous batch? check specific
    if 'nav-link" href="/blog/"' not in html:
        html = re.sub(NAV_PATTERN, NAV_REPLACE, html, count=1)
        nav = 1
    if '>Blog</a>' not in html and FOOT_ANCHOR in html:
        html = html.replace(FOOT_ANCHOR, FOOT_NEW)
        foot = 1
    with open(f, 'w', encoding='utf-8') as fh:
        fh.write(html)
    print(f'{f}: nav={nav} footer={foot}')
