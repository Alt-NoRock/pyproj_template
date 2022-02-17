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
sys.path.insert(0, os.path.abspath('../../src'))

from pyproj_template import VERSION

# -- Project information -----------------------------------------------------

project = 'pyproject_template'
copyright = '2022, Alt'
author = 'Alt'

# The short X.Y version
version = VERSION

# The full version, including alpha/beta/rc tags
release = VERSION

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',   # ソースコード読み込み用
    'sphinx.ext.napoleon',  # docstring パース用
    'sphinx_rtd_theme',     # Read the Docs テーマ (今回は不要*1)
    'sphinx_multiversion',  # マルチバージョン用
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'  # 変更

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

smv_tag_whitelist = r'^v\d+\.\d+\.\d+$'   # これにマッチしたタグを抽出
smv_branch_whitelist = r'^(main|develop)$'  # これにマッチしたブランチを抽出