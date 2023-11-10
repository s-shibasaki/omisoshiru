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
