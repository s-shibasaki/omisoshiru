from .cosine_similarity import cosine_similarity

__all__ = ["cosine_similarity"]

"""
Math Utilities Package

This package provides utility functions for mathematical operations.

Modules:
- cosine_similarity: Function to calculate cosine similarity between two sets of vectors.

Example:
    >>> from omisoshiru.math import cosine_similarity
    >>> a = np.array([[1, 2, 3], [4, 5, 6]])
    >>> b = np.array([[7, 8, 9], [10, 11, 12]])
    >>> cosine_similarity(a, b)
    array([0.95941195, 0.99614986])
"""
