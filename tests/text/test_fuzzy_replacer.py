import numpy as np
import pytest

from omisoshiru.text import FuzzyReplacer


# 1件の置換
def test_replace_single_text():
    reference = ["abc", "def"]
    text = "ab"
    excepted_result = "abc"

    replacer = FuzzyReplacer(reference)
    result = replacer.replace(text)

    assert result == excepted_result


# リストの置換
def test_replace_text_list():
    reference = ["abc", "def"]
    text_list = ["ab", "de"]
    excepted_result = ["abc", "def"]

    replacer = FuzzyReplacer(reference)
    result = replacer.replace(text_list)

    assert result == excepted_result


# NaNはTypeError
def test_type_error():
    reference = ["abc", "def"]
    text = np.nan

    replacer = FuzzyReplacer(reference)

    with pytest.raises(TypeError):
        replacer.replace(text)


# 半角と全角
def test_replace_hz():
    reference = ["ABC", "ＤＥＦ", "ｱｲｳ", "カキク"]
    text_list = ["ＡＢ", "DE", "アイ", "ｶｷ"]
    excepted_result = ["ABC", "ＤＥＦ", "ｱｲｳ", "カキク"]

    replacer = FuzzyReplacer(reference)
    result = replacer.replace(text_list)

    assert result == excepted_result


# 小文字と大文字
def test_replace_uncased():
    reference = ["ABC", "ＤＥＦ", "ghi", "ｊｋｌ"]
    text_list = ["ab", "ｄｅ", "GH", "ＪＫＬ"]
    excepted_result = ["ABC", "ＤＥＦ", "ghi", "ｊｋｌ"]

    replacer = FuzzyReplacer(reference)
    result = replacer.replace(text_list)

    assert result == excepted_result
