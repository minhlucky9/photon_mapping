# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

sys.path.insert(0, os.path.abspath('../..'))

project = 'Photon Mapping Simulation'
copyright = '2024, Tuan-Minh NGUYEN, Aurélien BESNIER'
author = 'Tuan-Minh NGUYEN, Aurélien BESNIER'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.todo', 'sphinx.ext.viewcode', 'autoapi.extension', "sphinx_copybutton", "nbsphinx", "sphinx.ext.githubpages"]

templates_path = ['_templates']
exclude_patterns = []

autoapi_dirs = ['../../photonmap']
# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
