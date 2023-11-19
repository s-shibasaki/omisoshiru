from typing import List, Optional

import pandas as pd


def join_str(strings: List[str], sep: Optional[str] = None) -> str:
    """
    Joins a list of strings using the specified separator.

    Args:
        strings (List[str]): List of strings to be joined.
        sep (Optional[str]): Separator for joining strings. Defaults to None.

    Returns:
        str: Joined string.

    Example:
        >>> strings = ["apple", "orange", "banana"]
        >>> join_str(strings, "-")
        "apple-orange-banana"
    """
    if sep is None:
        sep = ""

    return sep.join([s if pd.notna(s) else "" for s in strings])
