"""
Japanese text processing utilities using MeCab.

This module provides classes and functions for tokenizing Japanese text, matching patterns, and performing replacements.

Available classes and functions:
    - Wakachi: A class for tokenizing Japanese text using MeCab.
    - WakachiMatcher: A class for matching patterns in Japanese text using MeCab.
    - WakachiReplacer: A class for performing replacements in Japanese text based on a predefined dictionary.

Examples:
    # Using Wakachi to tokenize Japanese text
    >>> from omisoshiru.text.wakachi import Wakachi
    >>> wakachi = Wakachi(allow_whitespace=True)
    >>> input_text = "これはテストです。"
    >>> tokens = wakachi.parse(input_text)
    >>> print(tokens)
    ['これ', 'は', 'テスト', 'です', '。']

    # Using WakachiMatcher to find patterns in Japanese text
    >>> from omisoshiru.text.wakachi import WakachiMatcher
    >>> wakachi_matcher = WakachiMatcher()
    >>> pattern_list = ["桜の花"]
    >>> input_text = "桜の花が風に舞い、春の訪れを感じる。桜の花の美しさと儚さが心を打つ。"
    >>> matches = wakachi_matcher.match(pattern_list, input_text)
    >>> print(matches)
    [((0, 3), "桜の花"), ((18, 21), "桜の花")]

    # Using WakachiReplacer to replace patterns in Japanese text
    >>> from omisoshiru.text.wakachi import WakachiReplacer
    >>> replacer = WakachiReplacer({"りんご": "フルーツ", "ばなな": "フルーツ"})
    >>> text = "りんごとばななが好きです。"
    >>> result = replacer.replace(text)
    >>> print(result)
    "フルーツとフルーツが好きです。"
"""
from .wakachi import Wakachi
from .wakachi_matcher import WakachiMatcher
from .wakachi_replacer import WakachiReplacer

__all__ = ["Wakachi", "WakachiMatcher", "WakachiReplacer"]
