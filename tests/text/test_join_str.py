import pandas as pd

from omisoshiru.text import join_str


def test_join_str_empty_list():
    result = join_str([], "-")
    assert result == ""


def test_join_str_with_sep():
    result = join_str(["apple", "banana", "orange"], "-")
    assert result == "apple-banana-orange"


def test_join_str_without_sep():
    result = join_str(["apple", "banana", "orange"])
    assert result == "applebananaorange"


def test_join_str_with_nan_values():
    result = join_str(["apple", pd.NA, "orange"], "-")
    assert result == "apple--orange"


def test_join_str_with_different_sep():
    result = join_str(["apple", "banana", "orange"], ",")
    assert result == "apple,banana,orange"
