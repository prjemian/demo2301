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

gh_org = "prjemian"
project = "demo2301"
copyright = "2023, Pete Jemian"
author = "Pete Jemian"
release = demo2301.__version__
version = ".".join(release.split(".")[:2])

# fmt: off
switcher_file = "_static/switcher.json"
switcher_json_url = (
    "https://raw.githubusercontent.com/"
    f"{gh_org}/{project}/"
    "main/docs/source"
    f"/{switcher_file}"
)
switcher_version_list = [
    v["version"]
    for v in json.load(open(switcher_file))
]
# fmt: on

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

html_static_path = ["_static"]
html_theme = "pydata_sphinx_theme"
# fmt: off
html_theme_options = {
    "navbar_start": ["navbar-logo", "version-switcher"],
    "switcher": {
        "json_url": switcher_json_url,
        "version_match": release if release in switcher_version_list else "dev"
    }
}
# fmt: on
