#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Colin Brislawn'
SITENAME = u'Camerata Musica'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
	('Facebook', 'https://www.facebook.com/pages/Camerata-Musica-Richland/226889204035616'),
	('Origional site','http:///www.cameratamusica.com'),
	('GitHub', 'https://github.com/colinbrislawn'),
	)

NEWEST_FIRST_ARCHIVES = True
DEFAULT_PAGINATION = 10
ARTICLE_ORDER_BY = 'date'
PAGE_ORDER_BY = 'date'
#ARTICLE_ORDER_REVERSED = True
#REVERSE_CATEGORY_ORDER = False
#LOAD_CONTENT_CACHE = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
THEME = "./pelican-bootstrap3"
#THEME = "../pelican-themes/bootstrap"
#THEME = "../pelican-themes/bootstrap2"
#THEME = "../pelican-themes/bootstrap2-dark"

PLUGIN_PATHS = ['../pelican-plugins']
#PLUGINS=['sitemap',]
