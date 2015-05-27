#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'GNU Mailman Team'
SITENAME = u'GNU Mailman'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

STATIC_PATHS = ['images', 'css']

THEME = 'theme/pelican-chameleon'
BS3_THEME = 'https://bootswatch.com/flatly/bootstrap.min.css'
CSS_OVERWRITE = '/css/style.css'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MENUITEMS = [
    ('Home', '/'),
    ('Wiki', 'http://wiki.list.org'),
    ('Documentation', 'http://docs.mailman3.org'),
    ('Source Code', 'http://gitlab.com/mailman/'),
]

FAVICON = ''
FAVICON_TYPE = u'jpeg'
LOGO_URL = 'images/logo2010.png'

SIDEBAR_LINKS = [
    ('Security', '/security.html'),
    ('Features', '/features.html'),
    ('Discussion Lists', '/lists.html'),
    ('Rants, Papers and Logos', '/otherstuff.html'),
    ('Bugs', '/bugs.html'),
    ('Mirror', '/mirrors.html'),
    ('Barry Warsaw', 'http://barry.warsaw.us'),
]
