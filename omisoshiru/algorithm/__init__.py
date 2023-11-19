"""
Module providing various algorithms for pattern matching.

This module includes functions for finding partial matches in a target list.

Available functions:
    - partial_match: Find partial matches of patterns in a target list.

Example:
    >>> from omisoshiru.algorithm import partial_match
    >>> patterns = [['a', 'b'], ['b', 'c'], ['d']]
    >>> target = ['a', 'b', 'c', 'd', 'e']
    >>> partial_match(patterns, target)
    [(0, ['a', 'b']), (2, ['b', 'c']), (3, ['d'])]
"""

from .partial_match import partial_match

__all__ = [
    "partial_match",
]
