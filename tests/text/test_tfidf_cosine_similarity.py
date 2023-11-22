import numpy as np

from omisoshiru.text import tfidf_cosine_similarity
from omisoshiru.text.wakachi import Wakachi


def test_tfidf_cosine_similarity_basic():
    # Test with basic input where documents are identical
    documents_a = ["This is the first document.", "Another document."]
    documents_b = ["This is the first document.", "Another document."]

    result = tfidf_cosine_similarity(documents_a, documents_b, tokenizer=str.split)

    # Assert that cosine similarity between identical documents is 1.0
    assert np.allclose(result, np.array([1.0, 1.0]))


def test_tfidf_cosine_similarity_custom_tokenizer():
    # Test with a custom tokenizer (e.g., using Janome's wakachi.parse)
    tokenizer = Wakachi()

    documents_a = ["これは最初のドキュメントです。", "別のドキュメント。"]
    documents_b = ["このドキュメントは2番目のドキュメントです。", "まだ別のドキュメント。"]

    result = tfidf_cosine_similarity(
        documents_a, documents_b, tokenizer=tokenizer.parse
    )

    # Add your specific assertions based on the expected results
    assert np.allclose(result, np.array([0.44140881, 0.76806246]))


def test_tfidf_cosine_similarity_pairwise():
    # Test with pairwise=True
    documents_a = ["This is the first document.", "Another document."]
    documents_b = ["This document is the second document.", "Yet another document."]

    result = tfidf_cosine_similarity(
        documents_a, documents_b, tokenizer=str.split, pairwise=True
    )

    # Add your specific assertions based on the expected results for pairwise cosine similarity
    expected_result = np.array([[0.59321534, 0.11172065], [0.14160617, 0.68701684]])
    assert np.allclose(result, expected_result)
