from .date_to_str import date_to_str

__all__ = ["date_to_str"]

"""
Datetime Utilities Package

This package provides utility functions for working with datetime objects.

Modules:
- date_to_str: Function to convert a datetime object to a string in the format '%Y%m%d'.

Example:
    >>> from omisoshiru.datetime import date_to_str
    >>> date = datetime(2023, 11, 1)
    >>> date_to_str(date)
    '20231101'
"""
