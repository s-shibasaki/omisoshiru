"""
Text processing utilities for various tasks, including Japanese text processing, fuzzy replacements, string manipulation, and more.
"""


from . import wakachi
from .fuzzy_replacer import FuzzyReplacer
from .insert_newlines import insert_newlines
from .join_str import join_str
from .replace_text_ranges import replace_text_ranges
from .tfidf_cosine_similarity import tfidf_cosine_similarity
from .unify_hz import unify_hz

__all__ = [
    "FuzzyReplacer",
    "join_str",
    "replace_text_ranges",
    "unify_hz",
    "tfidf_cosine_similarity",
    "insert_newlines",
]
