============================================
Version switcher
============================================

In many software packages used as libraries, it is useful to provide
documentation for both the current release of the software as well as for other
versions (such most recent development build or notable older versions).

There is now a Python package [#]_ which makes it easy to provide several
documentation versions, even for projects that do not [#]_ use *ReadTheDocs*
(*RTD*) [#]_ to host their documentation.

Versioning
============================================

This project uses *semantic versioning*. [#]_ Builds of the documentation should
include the current version, including build information if not a tagged
release. The most popular packages to automate this task are 
``setuptools-scm`` [#]_ (used in this package)
and the older ``python-versioneer``. [#]_

The version of the current documentation being built is defined in the Sphinx
configuration (``conf.py``).  First, the ``switcher.json`` file is read into a
Python dictionary:

.. code-block:: py

    switcher_version_list = [
        v["version"]  # to match with ``release`` (above)
        for v in json.load(open(switcher_file))
    ]

Then, the current version is compared against all ``"version"`` keys in ``switcher_version_list``.
If it matches a key, then use it.  (This would match a tag.)  If it does not match,
then name this version ``"dev"`` for the purposes of the version switcher dropdown.
These lines of code provide that configuration:

.. code-block:: py

    "switcher": {
        "json_url": switcher_json_url,
        "version_match": release if release in switcher_version_list else "dev"
    }


Cache of documentation versions
============================================

While the ``pydata-sphinx-theme`` [#dropdown]_ documentation provides detailed
instructions to add a dropdown menu to a project's html site to switch between
documentation versions, it does not describe where to keep the cache of prior
versions of the built documentation.  For many projects, this task is automated
by the *RTD* service.  Projects that do not use *RTD* should provide their own
scheme.

This project keeps the cache of previous documentation versions in the GitHub
repository's ``gh-pages`` branch. [#gh_pages]_  The documentation's continuous
integration (CI) workflow builds the current documentation into a temporary
directory, then downloads the ``gh-pages`` branch and copies only those
documentation versions listed now in the ``switcher.json`` file.  The workflow
also makes soft links to the development (``dev``) and latest (``latest``)
versions, then pushes that temporary directory back to the repository's
``gh-pages`` branch. [#]_

The cache will grow as each new tag creates a new version of the documentation.
While this is probably acceptable for small projects, larger projects (such as
those which include many graphics files) may require 100 MB or more for each
version. Quickly, the ``gh-pages`` branch can grow too large and the project
should identify other ways to capture and host the docs for each tagged version.
Suggestions are welcomed for other schemes to capture and serve the cache.

the ``switcher.json`` file
============================================

The project's ``switcher.json`` file [#]_ describes [#dropdown]_ the
documentation versions available.  Here is an example:

.. code-block:: json

    [
        {
            "name": "development (main branch)",
            "version": "dev",
            "url": "https://prjemian.github.io/demo2301/dev/"
        },
        {
            "name": "1.0.2 (latest)",
            "version": "1.0.2",
            "url": "https://prjemian.github.io/demo2301/1.0.2/"
        },
        {
            "name": "1.0.0",
            "version": "1.0.0",
            "url": "https://prjemian.github.io/demo2301/1.0.0/"
        }
    ]

Location
--------

Per the docs, [#dropdown]_ *The JSON file needs to be at a stable, persistent,
fully-resolved URL*.

A convenient place to keep this file is in the ``main`` branch of the project's
GitHub repository.  One logical place is in the Sphinx documentation's
``_static`` directory. We name this file ``switcher.json``, as suggested by the
docs. [#dropdown]_ Since this file will be read directly from the GitHub
repository ``main`` branch, we must use the raw content URL, to avoid all the
additional GitHub controls from the regular web page.  So, this file:
https://raw.githubusercontent.com/prjemian/demo2301/main/docs/source/_static/switcher.json

.. _json.content:

Content
------------

Each version to be published will have its own JSON dictionary in the list.
Here is an example:

.. code-block:: json

      {
          "version": "1.0.0",
          "url": "https://prjemian.github.io/demo2301/1.0.0/"
      }

Here are some of the conventions used by this project:

* If ``name`` will be same as ``version``, then omit ``name``.
* Append ``(latest)`` to the ``name`` of the most recent release.
* If size of the documentation *cache* is a concern (such as when hosting in the
  project's GitHub repository ``gh-pages`` branch) consider keeping this list
  between 5 to 10 versions, so the cache does not grow too large.

Editing
------------

For now, edit the ``switcher.json`` file manually just before making a new tag,
as described below in the :ref:`tagging_checklist` section.

Mark only one version as ``(latest)``

.. tip::

    After editing and pushing a revised ``switcher.json`` file, your web browser
    cache may still retain the old version.  You might need to clear the browser's
    cache, force a refresh, or wait a few minutes for the new revision to be used.

Styling
------------

Certain items in the version dropdown are styled (background color is changed to
advise selection) using custom CSS (file ``_static/css/custom.css``, as
suggested in the docs.  [#dropdown]_ The CSS matches text content in the JSON
file to apply custom styling. See the conventions described in the section
:ref:`json.content`. Here is an example:

.. code-block:: css

    /* Style the link marked: latest */
    .version-switcher__container a[data-version-name*="(latest)"] {
      background-color: lightgreen;
    }

    /* Style the link marked: dev */
    .version-switcher__container a[data-version="dev"] {
      background-color: var(--pst-color-secondary);
    }


``versions`` in docs CI workflow
============================================

For now, the list of versions (includes old versions and possible future
versions) is defined in ``.github/workflows/pages.yml`` (the docs CI workflow).
It makes sense to move this list to a separate file, making it easier to find
and update without disturbing the code in the CI workflow.  Here's an example
(bash code within the ``.yml`` file):

.. code-block:: bash

    # List of documentation versions to keep.
    # (should include all versions in switcher.json)
    # Adding future versions will capture that version
    # once it appears in the downloaded gh-pages branch.
    versions=
    versions+=" 0.0.4"
    versions+=" 0.0.5"
    versions+=" 0.0.6"
    versions+=" 1.0.0"
    versions+=" 1.0.2"
    versions+=" 1.0.3"
    versions+=" 1.0.4"

When a new tag appears that matches an item in this list, then the docs will be
built with the new tag, rather than ``"dev"``, indicating a development version.
By this technique, only tags matching in the list will be differentiated from
development versions, including release candidate tags.

.. _tagging_checklist:

Checklist for a new tag
============================================

* complete all issues related to the new tag
* merge all open pull requests
* update the ``CHANGES.rst`` file for the new tag
* ensure all CI workflows pass with no errors
* make sure the new version appears in the list in the docs CI workflow file ``pages.yml``
* consider using a release candidate sequence [#]_ to test before applying the new tag
* only update next version in the ``switcher.json`` file **just before creating the new tag**
* be certain to push that commit before the tag **and wait** until the docs CI finishes
* Once the docs CI finishes, tag and push the new tag; this will create the new version of the docs

----

Footnotes
============================================


.. [#] ``pydata-sphinx-theme``: https://github.com/pydata/pydata-sphinx-theme
.. [#] hosting outside *RTD*: https://github.com/pydata/pydata-sphinx-theme/discussions/1013#discussioncomment-4602335
.. [#] *RTD*: https://readthedocs.org/
.. [#] semantic versioning: https://semver.org
.. [#] ``setuptools-scm``: https://github.com/pypa/setuptools_scm
.. [#] ``versioneer``: https://github.com/python-versioneer/python-versioneer
.. [#dropdown] version dropdown: https://pydata-sphinx-theme.readthedocs.io/en/latest/user_guide/version-dropdown.html
.. [#gh_pages] ``gh-pages`` branch:  https://github.com/prjemian/demo2301/tree/gh-pages
.. [#] push to ``gh-pages``: https://github.com/peaceiris/actions-gh-pages
.. [#] ``switcher.json``: https://github.com/prjemian/demo2301/blob/main/docs/source/_static/switcher.json
.. [#] release candidate process: https://www.tutorialspoint.com/software_testing_dictionary/release_candidate.htm
