"""Does ``intersphinx`` do its thing?"""

from __future__ import annotations
from typing import Any

import polars as pl

type Hello = str
"""This is a type alias."""


def make_df(
    greeting: Hello, some_datatype: pl.DataType, some_stuff: Any
) -> pl.DataFrame:
    print(greeting)
    return pl.DataFrame()
