"""
Custom datetime utilities.

This module provides custom utilities for handling datetime objects.

Available functions:
    - date_to_str: Convert a datetime object to a string in the format '%Y%m%d'.

Example:
    >>> from omisoshiru.datetime import date_to_str
    >>> from datetime import datetime
    >>> my_date = datetime(2023, 1, 1)
    >>> date_string = date_to_str(my_date)
    >>> print(date_string)
    '20230101'
"""

from .date_to_str import date_to_str

__all__ = ["date_to_str"]
