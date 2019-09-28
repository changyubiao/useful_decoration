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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import os
from os.path import abspath, dirname, join
import sys

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

print(f"root_path:{root_path}")
# sys.path.insert(0, root_path)

# Make sure we get the version of this copy of useful-decoration
print("Make sure we get the version of this copy of useful-decoration ")

namespace_package = dirname(dirname(dirname(abspath(__file__))))
package_dir = namespace_package + '/src'
print(f'package_dir: {package_dir}')

sys.path.insert(0, package_dir)

import useful_decoration

print("import useful_decoration successfully !")

# ----end path setup -----------------------------------------


# -- Project information -----------------------------------------------------

project = 'useful-decoration'
copyright = '2019, frank.chang'
author = 'frank.chang'

# The full version, including alpha/beta/rc tags
# release = 'y'
# The short X.Y version.
version = useful_decoration.__version__
# The full version, including alpha/beta/rc tags.
release = version

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# extensions = [
# ]


# The master toctree document.
master_doc = 'index'

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinxcontrib.log_cabinet",
    "pallets_sphinx_themes",
    "sphinx_issues",
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
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
