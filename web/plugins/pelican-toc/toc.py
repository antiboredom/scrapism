"""
toc
===================================

This plugin generates tocs for pages and articles.
"""

from __future__ import unicode_literals

import logging
import re

from bs4 import BeautifulSoup, Comment

from pelican import contents, signals
from pelican.utils import python_2_unicode_compatible, slugify


logger = logging.getLogger(__name__)
TOC_DEFAULT = {
    "TOC_HEADERS": "^h[1-6]",
    "TOC_RUN": "true",
    "TOC_INCLUDE_TITLE": "true",
}
TOC_KEY = "TOC"


"""
https://github.com/waylan/Python-Markdown/blob/master/markdown/extensions/headerid.py
"""
IDCOUNT_RE = re.compile(r"^(.*)_([0-9]+)$")


def unique(id, ids):
    """ Ensure id is unique in set of ids. Append '_1', '_2'... if not """
    while id in ids or not id:
        m = IDCOUNT_RE.match(id)
        if m:
            id = "%s_%d" % (m.group(1), int(m.group(2)) + 1)
        else:
            id = "%s_%d" % (id, 1)
    ids.add(id)
    return id


@python_2_unicode_compatible
class HtmlTreeNode(object):
    def __init__(self, parent, header, level, id, include_title):
        self.children = []
        self.parent = parent
        self.header = header
        self.level = level
        self.id = id
        self.include_title = include_title

    def add(self, new_header, ids):
        new_level = new_header.name
        new_string = new_header.string
        new_id = new_header.attrs.get("id")

        if not new_string:
            new_string = new_header.find_all(
                text=lambda t: not isinstance(t, Comment), recursive=True
            )
            new_string = "".join(new_string)

        if not new_id:
            new_id = slugify(new_string, ())

        new_id = unique(new_id, ids)  # make sure id is unique
        new_header.attrs["id"] = new_id
        if self.level < new_level:
            new_node = HtmlTreeNode(
                self, new_string, new_level, new_id, self.include_title
            )
            self.children += [new_node]
            return new_node, new_header
        elif self.level == new_level:
            new_node = HtmlTreeNode(
                self.parent, new_string, new_level, new_id, self.include_title
            )
            self.parent.children += [new_node]
            return new_node, new_header
        elif self.level > new_level:
            return self.parent.add(new_header, ids)

    def __str__(self):
        ret = ""
        if self.parent or self.include_title:
            ret = "<a class='toc-href' href='#{0}' title='{1}'>{1}</a>".format(
                self.id, self.header
            )

        if self.children:
            ret += "<ul>{}</ul>".format("{}" * len(self.children)).format(
                *self.children
            )

        # each list
        if self.parent or self.include_title:
            ret = "<li>{}</li>".format(ret)

        # end wrapper
        if not self.parent:
            if self.include_title:
                ret = "<div id='toc'><ul>{}</ul></div>".format(ret)
            else:
                ret = "<div id='toc'>{}</div>".format(ret)

        return ret


def init_default_config(pelican):
    from pelican.settings import DEFAULT_CONFIG

    def update_settings(settings):
        temp = TOC_DEFAULT.copy()
        if TOC_KEY in settings:
            temp.update(settings[TOC_KEY])
        settings[TOC_KEY] = temp
        return settings

    DEFAULT_CONFIG = update_settings(DEFAULT_CONFIG)
    if pelican:
        pelican.settings = update_settings(pelican.settings)


def generate_toc(content):
    if isinstance(content, contents.Static):
        return

    _toc_run = content.metadata.get("toc_run", content.settings[TOC_KEY]["TOC_RUN"])
    if not _toc_run == "true":
        return

    _toc_include_title = (
        content.metadata.get(
            "toc_include_title", content.settings[TOC_KEY]["TOC_INCLUDE_TITLE"]
        )
        == "true"
    )

    all_ids = set()
    title = content.metadata.get("title", "Title")
    tree = node = HtmlTreeNode(None, title, "h0", "", _toc_include_title)
    soup = BeautifulSoup(content._content, "html.parser")
    settoc = False

    try:
        header_re = re.compile(
            content.metadata.get(
                "toc_headers", content.settings[TOC_KEY]["TOC_HEADERS"]
            )
        )
    except re.error as e:
        logger.error(
            "TOC_HEADERS '%s' is not a valid re\n%s",
            content.settings[TOC_KEY]["TOC_HEADERS"],
        )
        raise e

    for header in soup.findAll(header_re):
        settoc = True
        node, new_header = node.add(header, all_ids)
        header.replaceWith(new_header)  # to get our ids back into soup

    if settoc:
        tree_string = "{}".format(tree)
        tree_soup = BeautifulSoup(tree_string, "html.parser")
        content.toc = tree_soup.decode(formatter="html")
    content._content = soup.decode(formatter="html")


def register():
    signals.initialized.connect(init_default_config)
    signals.content_object_init.connect(generate_toc)
