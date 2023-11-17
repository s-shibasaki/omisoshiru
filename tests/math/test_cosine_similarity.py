import numpy as np
import pytest

from omisoshiru.math import cosine_similarity


def test_cosine_similarity_pairwise():
    a = np.array([[1, 2, 3], [4, 5, 6]])
    b = np.array([[7, 8, 9], [10, 11, 12]])
    expected_result = np.array([[0.95941195, 0.95125831], [0.99819089, 0.99614986]])
    assert np.allclose(cosine_similarity(a, b, pairwise=True), expected_result)


def test_cosine_similarity_non_pairwise():
    a = np.array([[1, 2, 3], [4, 5, 6]])
    b = np.array([[7, 8, 9], [10, 11, 12]])
    expected_result = np.array([0.95941195, 0.99614986])
    assert np.allclose(cosine_similarity(a, b, pairwise=False), expected_result)


def test_cosine_similarity_invalid_input():
    a = np.array([1, 2, 3])
    b = np.array([[7, 8, 9], [10, 11, 12]])
    with pytest.raises(ValueError):
        cosine_similarity(a, b)
