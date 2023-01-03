#!/usr/bin/env python

from setuptools import setup


setup(
    setup_requires=["setuptools_scm"],
    use_scm_version={
        "root": ".",
        "relative_to": __file__,
        # "local_scheme": "node-and-timestamp"
    },
)
