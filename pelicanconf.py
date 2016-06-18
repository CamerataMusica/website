#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Camerata Musica'
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
DISPLAY_CATEGORIES_ON_MENU = False
CATEGORY_URL = 'seasons/{slug}.html'
CATEGORY_SAVE_AS = 'seasons/{slug}.html'
CATEGORIES_SAVE_AS = 'seasons/index.html'
# We could also have this save over the archive, which could be quite elegant.

MENUITEMS = (
    #('Current Season', 'https://colinbrislawn.github.io/CamerataMusica/seasons/current-season.html'),
)


# Blogroll
LINKS = (
# Absolute paths seem to work best
	('Facebook', 'https://www.facebook.com/pages/Camerata-Musica-Richland/226889204035616'),
	('Past Seasons', 'https://colinbrislawn.github.io/CamerataMusica/seasons/'),
	('Origional Site','http:///www.cameratamusica.com'),
	)

# Social widget
#SOCIAL = (
#	('Facebook', 'https://www.facebook.com/pages/Camerata-Musica-Richland/226889204035616'),
#	('Past Seasons', 'https://colinbrislawn.github.io/CamerataMusica/seasons/'),
#	('Origional Site','http:///www.cameratamusica.com'),
#	)

DISPLAY_TAGS_ON_SIDEBAR = False
#SIDEBAR_IMAGES = ["http://127.0.0.1:8000/images/2015-2016/StephenBeus200.jpg"]
#SIDEBAR_CONSTANT_CONTACT = 'asdf'

NEWEST_FIRST_ARCHIVES = True
DEFAULT_PAGINATION = 10
#ARTICLE_ORDER_BY = 'date'
#ARTICLE_ORDER_BY = 'reversed-date'

PAGE_ORDER_BY = 'reversed-date'
#LOAD_CONTENT_CACHE = False


STATIC_PATHS = ['images', 'pages', 'favicon.png', 'CamerataMusica/images']


SUMMARY_MAX_LENGTH = 20

BANNER_ALL_PAGES = True
BANNER_SUBTITLE = 'A Tradition of Chamber Music in the Tri-Cities'
BANNER = 'images/background3crop1.jpg'
BANNER_LOGO = 'images/Logo-white-500-t.png'

RELATIVE_URLS = True
THEME = "./pelican-bootstrap3"

PLUGIN_PATHS = ['../pelican-plugins']
