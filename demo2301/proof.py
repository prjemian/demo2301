#!/usr/bin/env python

"""
Try out pydata-sphinx-theme and its version switcher dropdown.

.. autosummary::
   ~main
   ~about
"""


def about():
    """
    Print something.
    """
    print(f"Here we are in '{__file__}:main()'")


def main():
    """
    The ``main()`` function in this module.

    Calls ``about()``.
    """
    about()


if __name__ == "__main__":
    main()
