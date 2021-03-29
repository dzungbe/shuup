#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This file is part of Shuup.
#
# Copyright (c) 2012-2021, Shuup Commerce Inc. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
"""
Shuup documentation build configuration file
"""

import django
import os
import sys

# -- Python path ----------------------------------------------------------

DOC_PATH = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(DOC_PATH, "_ext"))
sys.path.insert(0, os.path.join(DOC_PATH, ".."))


# -- Initialize Django ----------------------------------------------------


def initialize_django():
    os.environ["DJANGO_SETTINGS_MODULE"] = "shuup_workbench.settings"
    from django.conf import settings

    # Set USE_I18N=False to avoid warnings from import-time ugettext calls
    settings.USE_I18N = False

    django.setup()


initialize_django()


# -- Monkey patch some property descriptors to allow introspection


def patch_for_introspection():
    import shuup_introspection_helper

    shuup_introspection_helper.enable_patches()


patch_for_introspection()

# -- General configuration ------------------------------------------------

project = "Shuup"
copyright = "2021, Shuup Commerce Inc."

extensions = [
    "djangodocs",
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "django_sphinx",
]

# templates_path = ['_templates']
source_suffix = ".rst"
source_encoding = "utf-8"
master_doc = "index"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

with open(os.path.join(os.path.dirname(__file__), "..", "setup.py")) as sf:
    for line in sf:
        if line.startswith("VERSION = "):
            version_string = line.split("VERSION = ", 1)[1].strip()[1:-1]
            version_suffix = "+" if ".dev" in version_string else ""

# The short X.Y version.
version = ".".join(version_string.split(".")[0:2]) + version_suffix
# The full version, including alpha/beta/rc tags.
release = ".".join(version_string.split(".")[0:3]) + version_suffix

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = "en"

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#   today = ''
# Else, today_fmt is used as the format for a strftime call.
today_fmt = "%Y-%m-%d"

# Default role for pure backticked references without interpreted text role
default_role = "obj"

# Insert both the class’ and the __init__ method’s docstring into the
# main body of an autoclass directive
autoclass_content = "both"

autodoc_member_order = "bysource"
autodoc_default_flags = [
    "members",
    "undoc-members",
    # 'special-members',
    # 'inherited-members',
    "show-inheritance",
]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["_build"]

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = False

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# A list of ignored prefixes for module index sorting.
modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
keep_warnings = True

todo_include_todos = True

intersphinx_mapping = {
    "python": ("http://docs.python.org/3", None),
    "django": ("http://docs.djangoproject.com/en/1.8/", "http://docs.djangoproject.com/en/1.8/_objects/"),
    "djpolymorph": ("http://django-polymorphic.readthedocs.org/en/latest/", None),
}

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "sphinx_shoop_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ["_theme"]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
# html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = "Shuupdoc"


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    ("index", "Shuup.tex", "Shuup Documentation", "Shuup Commerce Inc.", "manual"),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [("index", "shuup", "Shuup Documentation", ["Shuup Commerce Inc."], 1)]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        "index",
        "Shuup",
        "Shuup Documentation",
        "Shuup Commerce Inc.",
        "Shuup",
        "One line description of project.",
        "Miscellaneous",
    ),
]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
# texinfo_no_detailmenu = False
