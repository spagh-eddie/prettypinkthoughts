"""
Configuration file for the Sphinx documentation builder.

For the full list of built-in configuration values, see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "prettypinkthoughts"
project_copyright = "2022, Eddie Darling"
author = "Eddie Darling"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_rtd_theme",
    "sphinx_mdinclude",
    "sphinxcontrib.spelling",
]
templates_path = ["_templates"]
rst_epilog = """
.. |CC BY 3.0| replace:: CC BY 3.0
.. _CC BY 3.0: https://creativecommons.org/licenses/by/3.0/
"""

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
