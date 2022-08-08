#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'Daniel M. Sullivan'
SITENAME = 'Daniel M. Sullivan'
SITEURL = 'https://www.danielmsullivan.com'

PATH = 'content'

TIMEZONE = 'America/New_York'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_LANG = 'en'

INDEX_SAVE_AS = 'blog.html'

HOMEDIR = os.path.expanduser('~')
# THEME = os.path.join(HOMEDIR, 'proj', 'pelican-themes', 'pelican-bootstrap3')
THEME = os.path.join(HOMEDIR, 'proj', 'pelican-digistrap3')

PLUGIN_PATHS = [HOMEDIR + '/proj/pelican-plugins', ]
PLUGINS = ['i18n_subsites', 'series', 'html_rst_directive']
JINJA_ENVIRONMENT = {
    "extensions": ['jinja2.ext.i18n'],
}

I18N_TEMPLATES_LANG = 'en'

BOOTSTRAP_THEME = 'flatly'
# PYGMENTS_STYLE = 'default'

FEED_DOMAIN = SITEURL

# Blogroll
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
    ('CV', '/pdf/Sullivan_CV.pdf'),
    ('Research', '/pages/research.html'),
    ('Code', '/pages/code.html'),
    ('Tutorials', (
        ('Stata-to-Python Equivalents', '/pages/tutorial_stata_to_python.html'),
        ('Writing Code in Social Science', '/pages/tutorial_workflow_0overview.html'),
        ('Python', '/pages/tutorial_intro_to_python.html'),
        ('Git', '/pages/tutorial_git_0overview.html'),
        ('Vim', '/pages/tutorial_vim.html'),
        ('All tutorials', '/pages/tutorials.html'),
    )
    ),
)

# Social widget
# GITHUB_USER = 'dmsul'
# GITHUB_SKIP_FORK = True
SOCIAL_WIDGET_NAME = 'Contact'
SOCIAL = (
    ('Github', 'http://github.com/dmsul'),
    ('LinkedIn', 'https://www.linkedin.com/in/daniel-sullivan-42134687'),
    ('Twitter', 'https://twitter.com/Dan_M_Sullivan'),
    ('Google Scholar',
     'https://scholar.google.com/citations?user=naLX3CIAAAAJ',
     'graduation-cap'),
    ('Email', 'mailto:sullivan.dm3@gmail.com', 'envelope'),
    ('Work Email', 'mailto:daniel.m.sullivan@jpmchase.com', 'inbox'),
    # ('ORCID', 'http://orcid.org/0000-0002-0380-7681', 'orcid'),
    # ('RePEc', 'https://ideas.repec.org/f/psu490.html'),
)

DEFAULT_PAGINATION = False
DEFAULT_ORPHANS = 0
SUMMARY_MAX_LENGTH = 65

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
# XXX must be commented out when live

# AVATAR = 'images/dms_med.jpg'

# CUSTOM_CSS = 'static/css/custom.css'  # XXX Can't get it to work

STATIC_PATHS = ['images', 'static', 'pdf', 'extra/CNAME', ' extra/custom.css']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/custom.css': {'path': 'static/css/custom.css'}
}

GOOGLE_ANALYTICS = 'UA-88761020-1'

# Series plugin stuff
DISPLAY_SERIES_ON_SIDEBAR = True
SHOW_SERIES = True
