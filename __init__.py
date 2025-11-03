"""Hindi LIWC package.

This package provides modules for building and using a Hindi linguistic
inquiry dictionary.  See ``README.md`` for an overview and
``analyzer.py`` for usage.
"""

from .analyzer import analyze  # noqa: F401

__all__ = ["analyze"]