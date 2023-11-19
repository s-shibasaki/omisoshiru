from .fuzzy_replacer import FuzzyReplacer
from .join_str import join_str
from .replace_text_ranges import replace_text_ranges
from .unify_hz import unify_hz
from .wakachi import Wakachi
from .wakachi_matcher import WakachiMatcher
from .wakachi_replacer import WakachiReplacer

__all__ = [
    "FuzzyReplacer",
    "join_str",
    "replace_text_ranges",
    "unify_hz",
    "Wakachi",
    "WakachiMatcher",
    "WakachiReplacer",
]

"""
Text Processing Module

This module provides several text processing classes and functions.

Classes:
    - FuzzyReplacer: A class for fuzzy text replacement based on a reference list.
    - Wakachi: A class for tokenizing Japanese text using MeCab.
    - WakachiMatcher: A class for matching patterns in Japanese text.
    - WakachiReplacer: A class for replacing patterns in Japanese text.
    
Functions:
    - join_str: Concatenates a list of strings into a single string using a separator.
    - replace_text_ranges: Replaces specified text ranges in a string.
    - unify_hz: Unifies half-width and full-width characters in a string.

Example:
    ```
    from omisoshiru.text import FuzzyReplacer, Wakachi

    # Create a FuzzyReplacer instance with a reference list
    replacer = FuzzyReplacer(["apple", "banana", "orange"])

    # Replace a text with the most similar item from the reference list
    result = replacer.replace("appl")
    print(result)  # Output: "apple"

    # Create a Wakachi instance for tokenization
    tokenizer = Wakachi()

    # Tokenize a Japanese text
    tokens = tokenizer.parse("日本語のテキスト")
    print(tokens)  # Output: ["日本語", "の", "テキスト"]
    ```
"""
