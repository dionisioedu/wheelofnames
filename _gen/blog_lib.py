#!/usr/bin/env python3
"""Shared template + builders for the wheeloflist.com blog."""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATE = "2026-07-17"

NAV = '''  <nav class="navbar navbar-expand-lg navbar-light navbar-custom">
    <div class="container-fluid">
      <a class="navbar-brand" href="/">🎡 Wheel Of List</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarContent">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarContent">
        <ul class="navbar-nav ms-auto">
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="toolsDropdown" role="button" data-bs-toggle="dropdown">Tools</a>
            <ul class="dropdown-menu" aria-labelledby="toolsDropdown">
              <li><a class="dropdown-item" href="/">🎡 Wheel Spinner</a></li>
              <li><a class="dropdown-item" href="/coin-flip/">🪙 Coin Flip</a></li>
              <li><a class="dropdown-item" href="/random-number/">🎲 Random Number Generator</a></li>
              <li><a class="dropdown-item" href="/dice-roller/">🎰 Dice Roller</a></li>
              <li><a class="dropdown-item" href="/yes-no-wheel/">❓ Yes or No Wheel</a></li>
              <li><a class="dropdown-item" href="/team-generator/">👥 Team Generator</a></li>
              <li><a class="dropdown-item" href="/random-letter/">🔤 Random Letter</a></li>
              <li><a class="dropdown-item" href="/raffle-picker/">🏆 Raffle Picker</a></li>
              <li><a class="dropdown-item" href="/tournament/">🏟️ Tournament Bracket</a></li>
              <li><a class="dropdown-item" href="/wheels/">🎯 Wheel Templates</a></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item" href="/tools/">🧰 All Tools</a></li>
            </ul>
          </li>
          <li class="nav-item"><a class="nav-link" href="/blog/">Blog</a></li>
          <li class="nav-item"><a class="nav-link" href="/#about">About</a></li>
          <li class="nav-item"><a class="nav-link" href="mailto:dionisiosoftware@gmail.com?subject=Wheel%20of%20List">Contact</a></li>
        </ul>
      </div>
    </div>
  </nav>'''

FOOTER = '''  <footer class="bg-light text-center mt-3 p-4">
    <div class="mb-2">
      <a href="/" class="text-decoration-none mx-2">Wheel Spinner</a>
      <a href="/coin-flip/" class="text-decoration-none mx-2">Coin Flip</a>
      <a href="/random-number/" class="text-decoration-none mx-2">Random Number</a>
      <a href="/dice-roller/" class="text-decoration-none mx-2">Dice Roller</a>
      <a href="/yes-no-wheel/" class="text-decoration-none mx-2">Yes or No Wheel</a>
      <a href="/team-generator/" class="text-decoration-none mx-2">Team Generator</a>
      <a href="/random-letter/" class="text-decoration-none mx-2">Random Letter</a>
      <a href="/raffle-picker/" class="text-decoration-none mx-2">Raffle Picker</a>
      <a href="/tournament/" class="text-decoration-none mx-2">Tournament Bracket</a>
      <a href="/wheels/" class="text-decoration-none mx-2">Wheel Templates</a>
      <a href="/blog/" class="text-decoration-none mx-2">Blog</a>
      <a href="/tools/" class="text-decoration-none mx-2">All Tools</a>
    </div>
    <div class="mb-2">
      <a href="/privacy-policy/" class="text-decoration-none mx-2">Privacy Policy</a>
      <a href="/terms/" class="text-decoration-none mx-2">Terms of Use</a>
      <a href="mailto:dionisiosoftware@gmail.com?subject=Wheel%20of%20List" class="text-decoration-none mx-2">Contact</a>
    </div>
    <a href="https://dionisio.dev" class="text-decoration-none">Copyright © Dionisio Software</a>
  </footer>'''

HEAD_EXTRAS = '''  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Quicksand&display=swap" rel="stylesheet">
  <link href="/styles.css" rel="stylesheet">
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-XV614N2RLR"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-XV614N2RLR');
  </script>
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6858130394830057" crossorigin="anonymous"></script>'''

ARTICLE_CSS = '''  <style>
    .article-body { max-width: 760px; margin: 0 auto; font-size: 1.06rem; line-height: 1.75; }
    .article-body h1 { font-size: 2rem; line-height: 1.25; margin-bottom: 0.5rem; }
    .article-body h2 { font-size: 1.45rem; margin-top: 2.2rem; margin-bottom: 0.8rem; }
    .article-meta { color: #888; font-size: 0.9rem; margin-bottom: 1.8rem; }
    .article-body table { width: 100%; border-collapse: collapse; margin: 1rem 0; }
    .article-body th, .article-body td { border: 1px solid #ddd; padding: 8px 12px; text-align: left; }
    .article-body th { background: rgba(30,144,255,0.08); }
    .dark-theme .article-body th, .dark-theme .article-body td { border-color: #555; }
    .cta-box { background: linear-gradient(135deg, rgba(30,144,255,0.08), rgba(0,191,255,0.08)); border: 2px solid #1E90FF; border-radius: 14px; padding: 22px 26px; margin: 2.2rem 0; }
    .cta-box h3 { font-size: 1.2rem; margin-bottom: 0.4rem; }
    .cta-box p { margin-bottom: 0.9rem; }
    blockquote { border-left: 4px solid #1E90FF; padding-left: 16px; color: #666; font-style: italic; }
    .dark-theme blockquote { color: #aaa; }
  </style>'''

TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>@@TITLE@@</title>
  <meta name="description" content="@@DESC@@">
  <meta name="robots" content="index, follow">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="canonical" href="https://wheeloflist.com/blog/@@SLUG@@/">
  <meta name="theme-color" content="#3369e8">
  <link rel="icon" href="/favicon.ico">
  <meta property="og:title" content="@@OG_TITLE@@">
  <meta property="og:description" content="@@DESC@@">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://wheeloflist.com/blog/@@SLUG@@/">
  <meta property="og:site_name" content="Wheel Of List">
  <meta property="og:image" content="https://wheeloflist.com/og.jpg">
  <meta property="article:published_time" content="@@DATE@@">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:creator" content="@DionisioDev">
@@HEAD_EXTRAS@@
  <script type="application/ld+json">
@@ARTICLE_JSON@@
  </script>
  <script type="application/ld+json">
@@BREADCRUMB_JSON@@
  </script>
@@ARTICLE_CSS@@
</head>
<body>
  <script>try{if(localStorage.getItem('wheeloflist_theme')==='dark')document.body.classList.add('dark-theme');}catch(e){}</script>

@@NAV@@

  <main class="container" style="padding: 40px 20px;">
    <article class="article-body">
      <h1>@@H1@@</h1>
      <div class="article-meta">@@META_LINE@@</div>
@@BODY@@
    </article>

    <section class="quick-tools-section" style="margin-top:3.5rem; max-width: 1000px; margin-left:auto; margin-right:auto;">
      <h3 class="quick-tools-title">Keep Reading</h3>
      <div class="tools-grid">
@@RELATED@@
      </div>
    </section>
  </main>

@@FOOTER@@

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
  <script src="/consent.js" defer></script>
</body>
</html>
'''

def word_count(html):
    return len(re.sub(r'<[^>]+>', ' ', html).split())

def cta(title, text, href, button):
    return ('<div class="cta-box"><h3>%s</h3><p>%s</p>'
            '<a class="btn btn-primary" href="%s">%s</a></div>' % (title, text, href, button))

def build_article(article, all_articles):
    wc = word_count(article["body"])
    minutes = max(2, round(wc / 220))
    art_json = json.dumps({
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": article["h1"],
        "description": article["desc"],
        "author": {"@type": "Person", "name": "Eduardo Dionisio", "url": "https://dionisio.dev"},
        "publisher": {"@type": "Organization", "name": "Dionisio Software", "url": "https://dionisio.dev"},
        "datePublished": DATE,
        "dateModified": DATE,
        "mainEntityOfPage": "https://wheeloflist.com/blog/%s/" % article["slug"],
        "image": "https://wheeloflist.com/og.jpg",
    }, indent=2, ensure_ascii=False)
    bc_json = json.dumps({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://wheeloflist.com/"},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": "https://wheeloflist.com/blog/"},
            {"@type": "ListItem", "position": 3, "name": article["h1"],
             "item": "https://wheeloflist.com/blog/%s/" % article["slug"]},
        ],
    }, indent=2, ensure_ascii=False)

    others = [a for a in all_articles if a["slug"] != article["slug"]]
    idx = [a["slug"] for a in all_articles].index(article["slug"])
    picks = [others[i % len(others)] for i in range(idx, idx + 3)]
    related = '\n'.join(
        '        <a class="tool-card" href="/blog/%s/">\n'
        '          <div class="tool-card-icon">%s</div>\n'
        '          <h4>%s</h4>\n'
        '          <p>%s</p>\n'
        '          <div class="tool-card-arrow">→</div>\n'
        '        </a>' % (a["slug"], a["emoji"], a["h1"], a["desc"][:90] + '…')
        for a in picks)

    html = (TEMPLATE
            .replace('@@TITLE@@', article["title"])
            .replace('@@OG_TITLE@@', article["h1"])
            .replace('@@DESC@@', article["desc"])
            .replace('@@SLUG@@', article["slug"])
            .replace('@@DATE@@', DATE)
            .replace('@@H1@@', article["h1"])
            .replace('@@META_LINE@@', 'By Eduardo Dionisio · %s · %d min read' % ("July 17, 2026", minutes))
            .replace('@@ARTICLE_JSON@@', art_json)
            .replace('@@BREADCRUMB_JSON@@', bc_json)
            .replace('@@BODY@@', article["body"])
            .replace('@@RELATED@@', related)
            .replace('@@HEAD_EXTRAS@@', HEAD_EXTRAS)
            .replace('@@ARTICLE_CSS@@', ARTICLE_CSS)
            .replace('@@NAV@@', NAV)
            .replace('@@FOOTER@@', FOOTER))
    out = os.path.join(ROOT, 'blog', article["slug"])
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, 'index.htm'), 'w', encoding='utf-8') as f:
        f.write(html)
    return wc

INDEX_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Blog — Game Theory, Probability & Randomness | Wheel Of List</title>
  <meta name="description" content="Short, sharp reads on game theory, probability and the psychology of chance — from the makers of the Wheel of List random tools.">
  <meta name="robots" content="index, follow">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="canonical" href="https://wheeloflist.com/blog/">
  <meta name="theme-color" content="#3369e8">
  <link rel="icon" href="/favicon.ico">
  <meta property="og:title" content="Blog — Game Theory, Probability & Randomness">
  <meta property="og:description" content="Short, sharp reads on game theory, probability and the psychology of chance.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://wheeloflist.com/blog/">
  <meta property="og:site_name" content="Wheel Of List">
  <meta property="og:image" content="https://wheeloflist.com/og.jpg">
  <meta name="twitter:card" content="summary_large_image">
@@HEAD_EXTRAS@@
  <script type="application/ld+json">
@@BREADCRUMB_JSON@@
  </script>
  <script type="application/ld+json">
@@ITEMLIST_JSON@@
  </script>
</head>
<body>
  <script>try{if(localStorage.getItem('wheeloflist_theme')==='dark')document.body.classList.add('dark-theme');}catch(e){}</script>

@@NAV@@

  <main class="container" style="max-width: 1000px; padding: 40px 20px;">
    <h1 style="font-size:2rem; text-align:center;">The Wheel Of List Blog</h1>
    <p style="text-align:center; max-width:680px; margin: 0 auto 2rem;">Game theory, probability and the psychology of chance — the ideas behind fair decisions, good games and honest randomness. Written by the maker of the <a href="/tools/">Wheel of List tools</a>.</p>

    <section class="quick-tools-section">
      <div class="tools-grid">
@@CARDS@@
      </div>
    </section>
  </main>

@@FOOTER@@

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
  <script src="/consent.js" defer></script>
</body>
</html>
'''

def build_index(all_articles):
    cards = '\n'.join(
        '        <a class="tool-card" href="/blog/%s/">\n'
        '          <div class="tool-card-icon">%s</div>\n'
        '          <h4>%s</h4>\n'
        '          <p>%s</p>\n'
        '          <div class="tool-card-arrow">→</div>\n'
        '        </a>' % (a["slug"], a["emoji"], a["h1"], a["desc"])
        for a in all_articles)
    bc = json.dumps({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://wheeloflist.com/"},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": "https://wheeloflist.com/blog/"},
        ],
    }, indent=2, ensure_ascii=False)
    il = json.dumps({
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": "Wheel Of List Blog",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": a["h1"],
             "url": "https://wheeloflist.com/blog/%s/" % a["slug"]}
            for i, a in enumerate(all_articles)
        ],
    }, indent=2, ensure_ascii=False)
    html = (INDEX_TEMPLATE
            .replace('@@CARDS@@', cards)
            .replace('@@BREADCRUMB_JSON@@', bc)
            .replace('@@ITEMLIST_JSON@@', il)
            .replace('@@HEAD_EXTRAS@@', HEAD_EXTRAS)
            .replace('@@NAV@@', NAV)
            .replace('@@FOOTER@@', FOOTER))
    with open(os.path.join(ROOT, 'blog', 'index.htm'), 'w', encoding='utf-8') as f:
        f.write(html)
