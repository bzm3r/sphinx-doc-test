"""Does ``intersphinx`` do its thing?"""

# based on: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#confval-autodoc_type_aliases
from __future__ import annotations

from typing import Any

import polars as pl

# see: https://stackoverflow.com/q/73223417/3486684
# see: https://stackoverflow.com/a/74520813/3486684
# see: https://github.com/google/jax/pull/20875
type Hello = str
"""This is a type alias."""
# see: https://github.com/readthedocs/sphinx-autoapi/issues/224#issuecomment-2031117665
# this suggests that we can use `type HelloWorld = str` (i.e. PEP 695 style
# annotation), but it does not work :(
# PEP 695: https://peps.python.org/pep-0695/


def make_df(
    greeting: Hello, some_datatype: pl.DataType, some_stuff: Any
) -> pl.DataFrame:
    print(greeting)
    return pl.DataFrame()
