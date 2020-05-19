#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Sam Lavigne"
SITENAME = "Scrapism"
SITEURL = "https://scrapism.lav.io"
THEME = "./theme"
DISPLAY_PAGES_ON_MENU = True
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"
PAGE_ORDER_BY = "sortorder"
STATIC_PATHS = ["images"]

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

CATEGORY_SAVE_AS = False
AUTHOR_SAVE_AS = False
AUTHORS_SAVE_AS = False
ARCHIVES_SAVE_AS = False
TAG_SAVE_AS = False
TAGS_SAVE_AS = False
CATEGORY_SAVE_AS = False


# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
