"""Configuration of demo2023 package."""

package = "demo2023"

try:
    from setuptools_scm import get_version

    __version__ = get_version(root="..", relative_to=__file__)
    del get_version
except (LookupError, ModuleNotFoundError):
    from importlib.metadata import version

    __version__ = version(package)
    del version

del package
