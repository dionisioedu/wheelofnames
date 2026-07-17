#!/usr/bin/env python3
"""Propagate updated nav dropdown + footer to existing pages."""
import re

NAV_UL = '''<ul class="dropdown-menu" aria-labelledby="toolsDropdown">
              <li><a class="dropdown-item" href="/">🎡 Wheel Spinner</a></li>
              <li><a class="dropdown-item" href="/coin-flip/">🪙 Coin Flip</a></li>
              <li><a class="dropdown-item" href="/random-number/">🎲 Random Number Generator</a></li>
              <li><a class="dropdown-item" href="/dice-roller/">🎰 Dice Roller</a></li>
              <li><a class="dropdown-item" href="/yes-no-wheel/">❓ Yes or No Wheel</a></li>
              <li><a class="dropdown-item" href="/team-generator/">👥 Team Generator</a></li>
              <li><a class="dropdown-item" href="/random-letter/">🔤 Random Letter</a></li>
              <li><a class="dropdown-item" href="/raffle-picker/">🏆 Raffle Picker</a></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item" href="/tools/">🧰 All Tools</a></li>
            </ul>'''

OLD_FOOTER_ROW = '''<div class="mb-2">
      <a href="/" class="text-decoration-none mx-2">Wheel Spinner</a>
      <a href="/random-number/" class="text-decoration-none mx-2">Random Number</a>
      <a href="/dice-roller/" class="text-decoration-none mx-2">Dice Roller</a>
      <a href="/tools/" class="text-decoration-none mx-2">All Tools</a>
    </div>'''

NEW_FOOTER_ROW = '''<div class="mb-2">
      <a href="/" class="text-decoration-none mx-2">Wheel Spinner</a>
      <a href="/coin-flip/" class="text-decoration-none mx-2">Coin Flip</a>
      <a href="/random-number/" class="text-decoration-none mx-2">Random Number</a>
      <a href="/dice-roller/" class="text-decoration-none mx-2">Dice Roller</a>
      <a href="/yes-no-wheel/" class="text-decoration-none mx-2">Yes or No Wheel</a>
      <a href="/team-generator/" class="text-decoration-none mx-2">Team Generator</a>
      <a href="/random-letter/" class="text-decoration-none mx-2">Random Letter</a>
      <a href="/raffle-picker/" class="text-decoration-none mx-2">Raffle Picker</a>
      <a href="/tools/" class="text-decoration-none mx-2">All Tools</a>
    </div>'''

FILES = ['index.htm', 'random-number/index.htm', 'dice-roller/index.htm',
         'tools/index.htm', 'privacy-policy/index.htm', 'terms/index.htm']

for f in FILES:
    with open(f, encoding='utf-8') as fh:
        html = fh.read()
    orig = html

    # Replace dropdown menu (if present)
    html, n_nav = re.subn(
        r'<ul class="dropdown-menu" aria-labelledby="toolsDropdown">.*?</ul>',
        lambda m: NAV_UL, html, count=1, flags=re.S)

    # Replace footer tools row
    n_foot = 0
    if OLD_FOOTER_ROW in html:
        html = html.replace(OLD_FOOTER_ROW, NEW_FOOTER_ROW)
        n_foot = 1

    if html != orig:
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(html)
    print(f'{f}: nav={n_nav} footer={n_foot}')
