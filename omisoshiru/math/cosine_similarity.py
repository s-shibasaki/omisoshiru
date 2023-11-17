from typing import Optional

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity as pairwise_cosine_similarity


def cosine_similarity(a: np.ndarray, b: np.ndarray, pairwise: Optional[bool] = None):
    if not (isinstance(a, np.ndarray) and a.ndim == 2):
        raise ValueError("Argument 'a' must be a 2D numpy array.")
    if not (isinstance(b, np.ndarray) and b.ndim == 2):
        raise ValueError("Argument 'b' must be a 2D numpy array.")

    pairwise = pairwise if pairwise is not None else False

    if pairwise:
        return pairwise_cosine_similarity(a, b)

    else:
        dot_product = np.diagonal(np.dot(a, b.T))
        norm_a = np.linalg.norm(a, axis=1)
        norm_b = np.linalg.norm(b, axis=1)
        cosine_sim = dot_product / (norm_a * norm_b)

        return cosine_sim
