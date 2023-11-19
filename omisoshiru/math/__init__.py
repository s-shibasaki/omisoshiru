"""
Mathematical utilities.

This module provides mathematical utilities, including functions for calculating cosine similarity.

Available functions:
    - cosine_similarity: Calculate cosine similarity between two sets of vectors.

Example:
    >>> from omisoshiru.math import cosine_similarity
    >>> import numpy as np
    >>> a = np.array([[1, 2, 3], [4, 5, 6]])
    >>> b = np.array([[7, 8, 9], [10, 11, 12]])
    >>> cosine_similarity(a, b)
    array([0.95941195, 0.99614986])
"""

from .cosine_similarity import cosine_similarity

__all__ = ["cosine_similarity"]
