#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'Daniel M. Sullivan'
SITENAME = 'Daniel M. Sullivan'
SITEURL = 'http://www.danielmsullivan.com'

PATH = 'content'

TIMEZONE = 'America/New_York'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_LANG = 'en'

# GITHUB_USER = 'dmsul'
# GITHUB_SKIP_FORK = True

INDEX_SAVE_AS = 'blog.html'

HOMEDIR = os.path.expanduser('~')
THEME = os.path.join(HOMEDIR, 'proj', 'pelican-themes', 'pelican-bootstrap3')

PLUGIN_PATHS = [HOMEDIR + '/proj/pelican-plugins', ]
PLUGINS = ['i18n_subsites']
JINJA_ENVIRONMENT = {
    "extensions": ['jinja2.ext.i18n'],
}

I18N_TEMPLATES_LANG = 'en'

BOOTSTRAP_THEME = 'cosmo'

FEED_DOMAIN = SITEURL

# Blogroll
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
    ('CV', '/pdf/cv.pdf'),
    ('Research', '/pages/research.html'),
    ('Code', '/pages/code.html'),
    ('Contact', '/pages/contact.html'),
)

if 0:
    LINKS = (('Pelican', 'http://getpelican.com/'),
             ('Python.org', 'http://python.org/'),
             ('Jinja2', 'http://jinja.pocoo.org/'),
             ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('Github', 'http://github.com/dmsul', 'github-alt'),
    ('Google Scholar',
     'https://scholar.google.com/citations?user=naLX3CIAAAAJ',
     'graduation-cap'),
    ('ORCID', 'http://orcid.org/0000-0002-0380-7681', 'id-card-alt')
)

DEFAULT_PAGINATION = False
DEFAULT_ORPHANS = 0
SUMMARY_MAX_LENGTH = 65

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
# DELETE_OUTPUT_DIRECTORY = True
# XXX must be commented out when live

AVATAR = 'images/dms_med.jpg'

STATIC_PATHS = ['images', 'static', 'pdf', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}
