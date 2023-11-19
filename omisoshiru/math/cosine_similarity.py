from typing import Optional

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity as pairwise_cosine_similarity


def cosine_similarity(
    a: np.ndarray, b: np.ndarray, pairwise: Optional[bool] = None
) -> np.ndarray:
    """
    Calculate cosine similarity between two sets of vectors.

    Args:
        a (np.ndarray): The first set of vectors.
        b (np.ndarray): The second set of vectors.
        pairwise (Optional[bool]): If True, compute the pairwise cosine similarity matrix.
            If False or None, compute the cosine similarity for each corresponding pair of vectors. Defaults to None.

    Returns:
        np.ndarray: The cosine similarity values. If 'pairwise' is True, a matrix is returned.

    Raises:
        ValueError: If 'a' or 'b' is not a 2D numpy array.

    Example:
        >>> a = np.array([[1, 2, 3], [4, 5, 6]])
        >>> b = np.array([[7, 8, 9], [10, 11, 12]])
        >>> cosine_similarity(a, b)
        array([0.95941195, 0.99614986])
    """
    if not (isinstance(a, np.ndarray) and a.ndim == 2):
        raise ValueError("Argument 'a' must be a 2D numpy array.")
    if not (isinstance(b, np.ndarray) and b.ndim == 2):
        raise ValueError("Argument 'b' must be a 2D numpy array.")

    pairwise = pairwise if pairwise is not None else False

    if pairwise:
        return pairwise_cosine_similarity(a, b)

    else:
        dot_product = np.einsum("ij,ij->i", a, b)
        norm_a = np.linalg.norm(a, axis=1)
        norm_b = np.linalg.norm(b, axis=1)

        cosine_sim = dot_product / (norm_a * norm_b)

        return cosine_sim
