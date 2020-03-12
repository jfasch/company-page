# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

import os
import sys
sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Jörg Faschingbauer'
copyright = '2020, Jörg Faschingbauer'
author = 'Jörg Faschingbauer'

# The full version, including alpha/beta/rc tags
release = '0.0.0'


# -- General configuration ---------------------------------------------------
master_doc = 'index'
templates_path = []

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.autodoc',
    'sphinx_rtd_theme',
    'ablog',
    'nbsphinx',
    'sphinxcontrib.fulltoc',
]
todo_include_todos = True

# ablog
if True:
    import ablog
    templates_path.append(ablog.get_html_templates_path())
    post_date_format = '%Y-%m-%d'

    blog_title = u'Jörg Faschingbauer'
    blog_path = 'blog'

    # a side effect of setting blog_baseurl is that atom.axml feeds
    # are generated altogether
    blog_baseurl = 'https://www.faschingbauer.me'

    blog_authors = {
        'jfasch': ('Jörg Faschingbauer', 'https://www.faschingbauer.me'),
    }
    blog_default_author = 'jfasch'
    
    blog_locations = {
        'daham': ('Graz, Austria', 'https://de.wikipedia.org/wiki/Graz'),
    }
    blog_default_location = 'daham'
    fontawesome_link_cdn = 'https://netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.min.css'
    blog_feed_fulltext = True
    blog_feed_length = 10
    blog_feed_archives = True

    # feed is http://feeds.feedburner.com/JoergFaschingbauer


templates_path.append('_templates')

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    '_build',
    '**.ipynb_checkpoints',
]
html_context = {}
html_static_path = ['_static']

_BASIC = 'basic'
_RTD = 'sphinx_rtd_theme'
_PYRAMID = 'pyramid'
_PRESS = 'press'
_NATURE = 'nature'
_ALABASTER = 'alabaster'
_BOOTSTRAP = 'bootstrap'

html_theme = _ALABASTER
html_theme_path = []
html_theme_options = {}

if html_theme == _ALABASTER:
    import alabaster

    html_theme_path.append(alabaster.get_path())

    html_theme_options['fixed_sidebar'] = True
    html_theme_options['logo'] = 'logo.jpg'
    # html_theme_options['show_powered_by'] = False
    html_theme_options['page_width'] = '90%'
    html_theme_options['sidebar_width'] = '20%'

    html_sidebars = {
        '**': [
            'about.html',
            'searchbox.html',
            'navigation.html',
        ],
    }

    def setup(app):
        app.add_stylesheet('css/jf.css')

if html_theme == _RTD:
    # nav and location feedback really great
    
    # looks good on mobile
    
    # on wider screen a lot of screen real estate to the right is wasted
    
    # html_sidebars disregarded

    # RTD css unreadable (uglified?)
    
    html_theme_options['collapse_navigation'] = False
    html_theme_options['navigation_depth'] = -1
    
    # context that jinja (and rst, via the rstjinja extension) sees.
    html_context.update({
        # experimental: this is how we can get settings into templates
        'READTHEDOCS': False, # {en,dis}able versions.html
        'versions': [('blah', 'https://www.google.com'),],
    
        # reading the RTD theme sources, I see that this is the RTD way of
        # adding my own css.
        'extra_css_files': ['_static/css/jf.css'],
    })
    
if html_theme == _PYRAMID:
    import pyramid_sphinx_themes
    html_theme_path += pyramid_sphinx_themes.get_html_themes_path()

if html_theme == _PRESS:
    # html_sidebars as set above won't work. emptying it does,
    # somehow.

    # nav is buggy.
    pass

if html_theme == _NATURE:
    pass

if html_theme == _BASIC:
    pass

if html_theme == _BOOTSTRAP:
    # just a try, no navigation with location feedback

    import sphinx_bootstrap_theme
    html_theme_path += sphinx_bootstrap_theme.get_html_theme_path()
