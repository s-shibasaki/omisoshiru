"""
Text processing utilities for various tasks, including Japanese text processing, fuzzy replacements, string manipulation, and more.

Modules:
    - wakachi: Japanese text processing utilities using MeCab.
    - FuzzyReplacer: A class for fuzzy replacements in text.
    - join_str: Function for joining a list of strings using a specified separator.
    - replace_text_ranges: Function for replacing specified text ranges in a string.
    - unify_hz: Function for unifying character width in text.

Examples:
    >>> from omisoshiru.text import wakachi, FuzzyReplacer, join_str, replace_text_ranges, unify_hz

    # Japanese text processing with Wakachi
    >>> wakachi_instance = wakachi.Wakachi(allow_whitespace=True)
    >>> input_text = "これはテストです。"
    >>> tokens = wakachi_instance.parse(input_text)
    >>> print(f"Japanese Tokenization Result: {tokens}")

    # Fuzzy replacements with FuzzyReplacer
    >>> fuzzy_replacer = FuzzyReplacer(["apple", "orange", "banana"])
    >>> fuzzy_result = fuzzy_replacer.replace("applle")
    >>> print(f"Fuzzy Replacement Result: {fuzzy_result}")

    # Joining strings with join_str
    >>> string_list = ["apple", "orange", "banana"]
    >>> joined_string = join_str(string_list, "-")
    >>> print(f"Joined String Result: {joined_string}")

    # Replacing text ranges with replace_text_ranges
    >>> original_text = "The quick brown fox jumps over the lazy dog."
    >>> replacement_ranges = [((4, 9), "swift"), ((20, 25), "leaps"), ((35, 39), "sleepy")]
    >>> modified_text = replace_text_ranges(original_text, replacement_ranges)
    >>> print(f"Text Replacement Result: {modified_text}")

    # Unifying character width with unify_hz
    >>> text_to_unify = "Ｈｅｌｌｏ, １２３."
    >>> unified_text = unify_hz(text_to_unify)
    >>> print(f"Character Width Unification Result: {unified_text}")
"""


from . import wakachi
from .fuzzy_replacer import FuzzyReplacer
from .join_str import join_str
from .replace_text_ranges import replace_text_ranges
from .unify_hz import unify_hz

__all__ = ["wakachi", "FuzzyReplacer", "join_str", "replace_text_ranges", "unify_hz"]
