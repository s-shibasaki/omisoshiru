import pandas as pd
import pytest

from omisoshiru.text import unify_hz


def test_text():
    assert unify_hz("AbＣｄ1２アｲ") == "AbCd12アイ"


def test_list():
    assert unify_hz(["AbＣｄ1２アｲ"]) == ["AbCd12アイ"]


def test_series():
    with pytest.raises(TypeError):
        unify_hz(pd.Series(["AbＣｄ1２アｲ"]))


def test_unify_hz_invalid_input():
    text = 12345
    with pytest.raises(TypeError):
        unify_hz(text)


def test_unify_hz_return_empty():
    text = 12345
    expected_result = ""
    assert unify_hz(text, on_error="return_empty") == expected_result


def test_unify_hz_return_none():
    text = 12345
    expected_result = None
    assert unify_hz(text, on_error="return_none") == expected_result


if __name__ == "__main__":
    pytest.main()
