#!/usr/bin/env python

"""
Try out pydata-sphinx-theme and its version switcher dropdown.

.. autosummary::
   ~main
   ~about
   ~get_version
"""


def about():
    """
    Print something.
    """
    from .another import talkative

    print(f"Here we are in '{__file__}:about()', calling talkative()")
    talkative()


def get_version():
    """
    Get the current project version string or ``"undefined"``.
    """
    try:
        from ._version import __version__

        return __version__
    except ImportError:
        return "undefined"


def main():
    """
    The ``main()`` function in this module.

    Calls ``about()``.
    """
    print(f"{__package__=}")
    # print(f"{demo2301.__package__=}  {demo2301.__version__=}")
    print(f"Here we are in '{__file__}:main()', calling about()")
    about()


if __name__ == "__main__":
    main()
