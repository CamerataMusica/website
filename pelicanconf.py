#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

AUTHOR = u'Camerata Musica'
SITENAME = u'Camerata Musica'
SITEURL = ''
PATH = 'content'
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = u'en'
DCOPY_DATE = date.today().year

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
USE_FOLDER_AS_CATEGORY = True
CATEGORY_URL = 'seasons/{slug}.html'
CATEGORY_SAVE_AS = 'seasons/{slug}.html'
CATEGORIES_SAVE_AS = 'seasons/index.html'
# We could also have this save over the archive, which could be quite elegant.
# ^^ Nope; Overwriting an existing page throws an error. Maybe better to chage the theme

# Set the current season (global variable for template)
CURRENT_SEASON_CATEGORY = '2023-2024'

# Change to output articles into subfolders by category (season)
ARTICLE_URL = 'seasons/{category}/{slug}.html'
ARTICLE_SAVE_AS = 'seasons/{category}/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

#MENUITEMS = ( )

# A mapping containing template pages that will be rendered with the blog entries.
# This should auto-generate the current season list page and place in the menu
#TEMPLATE_PAGES = { 'pelican-bootstrap3/templates/current_season.html' : 'current_season.html', }
DIRECT_TEMPLATES = ['index', 'current_season', 'categories', 'archives']

DISPLAY_BREADCRUMBS = False
DISPLAY_CATEGORY_IN_BREADCRUMBS = False
HIDE_SIDEBAR = True

# Blogroll
#LINKS = ( )

SIDEBAR_EMAIL_SIGNUP_URL = 'http://eepurl.com/cD1Zvv'

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
ARTICLE_ORDER_BY = 'date'
#ARTICLE_ORDER_BY = 'reversed-date'

PAGE_ORDER_BY = 'basename'
#PAGE_ORDER_BY = 'reversed-date'

# caching options 
CACHE_CONTENT = True
CHECK_MODIFIED_METHOD = 'mtime'
LOAD_CONTENT_CACHE = True
GZIP_CACHE = False


STATIC_PATHS = ['images', 'pages', 'root']
EXTRA_PATH_METADATA = {'root': {'path': ''}} # Put root in root of output
ARTICLE_EXCLUDES = ['root'] # Don't try to render root files

SUMMARY_MAX_LENGTH = 20

BANNER_ALL_PAGES = True
BANNER_TITLE = 'Camerata Musica'
BANNER_SUBTITLE = 'A Tradition of Chamber Music in the Tri-Cities'
BANNER = 'images/background3crop1.jpg'
BANNER_LOGO = 'images/Logo-white-500-t.png'

# Small logo for top menubar
SITELOGO = 'images/CM_icon.png'
SITELOGO_SIZE = '25px'

RELATIVE_URLS = True
THEME = "./pelican-bootstrap3"

# Email newsletter
SENDER_ID = 'd2f76d4df99251'
# SENDER_FORM_ID = ''

PLUGIN_PATHS = ['../pelican-plugins']
