#!/usr/bin/env python3
"""Insert Tournament Bracket link into nav dropdown + footer of non-generated pages."""

NAV_ANCHOR = '<li><a class="dropdown-item" href="/raffle-picker/">🏆 Raffle Picker</a></li>'
NAV_NEW = NAV_ANCHOR + '\n              <li><a class="dropdown-item" href="/tournament/">🏟️ Tournament Bracket</a></li>'

FOOT_ANCHOR = '<a href="/raffle-picker/" class="text-decoration-none mx-2">Raffle Picker</a>'
FOOT_NEW = FOOT_ANCHOR + '\n      <a href="/tournament/" class="text-decoration-none mx-2">Tournament Bracket</a>'

FILES = ['index.htm', 'random-number/index.htm', 'dice-roller/index.htm',
         'coin-flip/index.htm', 'yes-no-wheel/index.htm', 'team-generator/index.htm',
         'random-letter/index.htm', 'raffle-picker/index.htm',
         'tools/index.htm', 'privacy-policy/index.htm', 'terms/index.htm']

for f in FILES:
    with open(f, encoding='utf-8') as fh:
        html = fh.read()
    nav = foot = 0
    if NAV_ANCHOR in html and 'Tournament Bracket</a></li>' not in html:
        html = html.replace(NAV_ANCHOR, NAV_NEW)
        nav = 1
    if FOOT_ANCHOR in html and '>Tournament Bracket</a>' not in html:
        html = html.replace(FOOT_ANCHOR, FOOT_NEW)
        foot = 1
    with open(f, 'w', encoding='utf-8') as fh:
        fh.write(html)
    print(f'{f}: nav={nav} footer={foot}')
