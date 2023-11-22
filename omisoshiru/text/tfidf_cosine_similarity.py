from typing import List, Optional

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

from omisoshiru.math import cosine_similarity


def tfidf_cosine_similarity(
    a: List[str],
    b: List[str],
    tokenizer: Optional[callable] = None,
    pairwise: Optional[bool] = None,
) -> np.ndarray:
    """
    Calculate TF-IDF cosine similarity between two lists of documents.

    Args:
        a (List[str]): List of documents as strings for the first set.
        b (List[str]): List of documents as strings for the second set.
        tokenizer (Optional[callable]): A callable tokenizer function. Defaults to None.
        pairwise (Optional[bool]): If True, compute the pairwise cosine similarity matrix.
            If False or None, compute the cosine similarity for each corresponding pair of vectors. Defaults to None.

    Returns:
        np.ndarray: The TF-IDF cosine similarity values. If 'pairwise' is True, a matrix is returned.

    Example:
        >>> documents_a = ["This is the first document.", "Another document."]
        >>> documents_b = ["This document is the second document.", "Yet another document."]
        >>> tfidf_cosine_similarity(documents_a, documents_b)
        array([0.2753838, 0.])
    """
    # Convert documents to TF-IDF vectors
    vectorizer = TfidfVectorizer(tokenizer=tokenizer)
    vectorizer.fit(a + b)
    matrix_a = vectorizer.transform(a).toarray()
    matrix_b = vectorizer.transform(b).toarray()

    # Calculate cosine similarity using the provided cosine_similarity function
    return cosine_similarity(matrix_a, matrix_b, pairwise=pairwise)
