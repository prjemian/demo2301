# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import json
import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).parent.parent.parent))
import demo2301

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "demo2301"
copyright = "2023, Pete Jemian"
author = "Pete Jemian"
release = demo2301.__version__
version = ".".join(release.split(".")[:2])

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = """
    sphinx.ext.autodoc
    sphinx.ext.autosummary
    sphinx.ext.coverage
    sphinx.ext.githubpages
    sphinx.ext.inheritance_diagram
    sphinx.ext.mathjax
    sphinx.ext.todo
    sphinx.ext.viewcode
""".split()

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

gh_raw_url = "https://raw.githubusercontent.com"
gh_repo = "prjemian/demo2301"
gh_path = "main/docs/source"
switcher_file = "_static/switcher.json"
v_match = {v["version"] : v for v in json.load(open(switcher_file))}.get(release, "dev")
# TODO: How can this _ever_ be anything but "dev"?
#   Just after a tag?  Yes, if switcher file was edited.

html_static_path = ["_static"]
html_theme = "pydata_sphinx_theme"
html_theme_options = {
    "navbar_start": ["navbar-logo", "version-switcher"],
    "switcher": {
        "json_url": f"{gh_raw_url}/{gh_repo}/{gh_path}/{switcher_file}",
        "version_match": v_match,
    }
}
