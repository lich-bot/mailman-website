#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'GNU Mailman Team'
SITENAME = u'GNU Mailman'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

STATIC_PATHS = ['images', 'css', 'fonts']

THEME = 'theme/pelicanchameleon'
BS3_THEME = '/css/bootstrap.min.css'
CSS_OVERWRITE = '/css/style.css'
DEFAULT_LANG = u'en'

URL_PREFIX = ''

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
    ('Documentation', [
        ('Mailman Suite', 'http://docs.mailman3.org'),
        ('Mailman Core', 'http://mailman.readthedocs.org'),
        ('Postorius', 'http://postorius.readthedocs.org'),
        ('Mailman Client', 'http://mailmanclient.rtfd.org'),
        ('Hyperkitty', 'http://hyperkitty.rtfd.org'),
    ]),
    ('Source Code', 'http://gitlab.com/mailman/'),
    ('Donate', 'https://my.fsf.org/civicrm/contribute/transact?reset=1&id=22'),
]

FAVICON = 'images/favicon.ico'
FAVICON_TYPE = u'jpeg'
LOGO_URL = 'images/logo2010-2.jpg'

SIDEBAR_LINKS = [
    ('Download', '/download.html'),
    ('Security', '/security.html'),
    ('Features', '/features.html'),
    ('Discussion Lists', '/lists.html'),
    ('Rants, Papers and Logos', '/rants.html'),
    ('Developers', '/devs.html'),
    ('Mirror', '/mirrors.html'),
    ('Barry Warsaw', 'http://barry.warsaw.us'),
]
