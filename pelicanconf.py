#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import datetime

# {{{ Meta data
AUTHOR = 'outdex consortium'
SITENAME = 'outdex'

TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'
# }}}


# {{{ Path and url specs
PATH = 'content'
SITEURL = 'http://localhost:8000'
ABS_SITEURL = SITEURL
USE_FOLDER_AS_CATEGORY = True

ARTICLE_PATHS = ['News', 'Tutorials', 'Discussions']
ARTICLE_URL = '{date:%Y-%m-%d}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
PAGE_PATHS = ['pages']
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = PAGE_URL

STATIC_PATHS = ['img', 'extra/CNAME']
STATIC_EXCLUDE_SOURCES = False
IGNORE_FILES = ['extra']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'}
}
# }}}


# {{{ Plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = [
           'extract_toc',
           'pandoc_reader',
           'post_stats',
           'related_posts',
           'series',
           'share_post',
           ]
# pandoc-reader options
PANDOC_EXTENSIONS = [
  '+smart',
]
PANDOC_ARGS = [
  '--mathjax',
]
PANDOC_CSL = 'language.csl'
# }}}


# {{{ Math config
USE_MATHJAX = True
MATHJAX_BUNDLE = 'TeX-AMS_SVG'
# }}}

# {{{ Theme
THEME = 'themes/flex'
SITETITLE = SITENAME
SITESUBTITLE = 'language ⊗ computation'
SITEDESCRIPTION = SITESUBTITLE
SITELOGO = SITEURL + '/img/logo.svg'
FAVICON = SITEURL + 'img/favicon.ico'
CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}
COPYRIGHT_YEAR = datetime.datetime.now().year
MAIN_MENU = True
MENUITEMS = (('Tutorials', '/category/tutorials.html'),
             ('by author', '/authors.html'),
             ('by topic', '/tags.html'),)
ATOM_IN_MENU = False
RSS_IN_MENU = False
PYGMENTS_STYLE = 'friendly'

ROBOTS = 'index, follow'

DATE_FORMATS = {
    'en': '%B %d, %Y',
}
HOME_HIDE_TAGS = False
SHOW_POST_AUTHOR = True
# }}}


# {{{ Feed generation
# Feed generation is usually not desired when developing
FEED_URL = '/feeds/all.atom.xml'
FEED_DOMAIN = 'https://outde.xyz'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TAG_FEED_ATOM = None
FEED_MAX_ITEMS = 10
# }}}


# {{{ Sidebar links
# Blogroll
# LINKS = (('Subscribe', FEED_URL),)

# Search field
DISPLAY_SEARCH_FORM = True

# Social widget
SOCIAL = (('github', 'https://github.com/outde-xyz/website'),
          ('rss', FEED_DOMAIN + FEED_URL))
# }}}


# {{{ Misc
USE_UTTERANCES = False
USE_TALKYARD = False
DEFAULT_PAGINATION = 10
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = ['README.md', '.git', '.gitignore']
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
# Do not publish articles by default;
# only if they have the meta field
# Status: published
# DEFAULT_METADATA = {
#     'status': 'draft',
# }
# }}}
