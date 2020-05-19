#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Sam Lavigne"
SITENAME = "Scrapism"
SITEURL = ""
THEME = "./theme"
DISPLAY_PAGES_ON_MENU = True
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"
PAGE_ORDER_BY = "sortorder"

PATH = "content"

TIMEZONE = "US/Eastern"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = False

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "codehilite"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
    },
    "output_format": "html5",
}


# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
