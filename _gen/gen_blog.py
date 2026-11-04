#!/usr/bin/env python3
"""Generate every blog article batch, then build the blog index."""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from blog_lib import build_article, build_index, word_count

# Register article batches (each defines an ARTICLES list)
import blog_batch1
import blog_batch2
import blog_batch3
import blog_batch4
import blog_batch5

all_articles = (blog_batch1.ARTICLES + blog_batch2.ARTICLES +
                blog_batch3.ARTICLES + blog_batch4.ARTICLES +
                blog_batch5.ARTICLES)
total_words = 0

for a in all_articles:
    wc = build_article(a, all_articles)
    total_words += wc
    print('built /blog/%s/  (%d words)' % (a['slug'], wc))

build_index(all_articles)
print('built /blog/ index')
print('%d articles, %d total words (~%d min read at 220wpm)' % (
    len(all_articles), total_words, total_words // 220))
