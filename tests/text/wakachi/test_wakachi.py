import pytest

from omisoshiru.text.wakachi import Wakachi


@pytest.fixture
def wakachi():
    return Wakachi()


@pytest.fixture
def wakachi_preserve_space():
    return Wakachi(allow_whitespace=True)


# 正常系のテストケース
def test_parse_no_space(wakachi):
    string = "桜が咲く季節です"
    expected_result = ["桜", "が", "咲く", "季節", "です"]
    assert wakachi.parse(string) == expected_result


def test_parse_with_space_preserve(wakachi_preserve_space):
    string = "桜が咲く季 節です"
    expected_result = ["桜", "が", "咲く", "季", "節", "です"]
    assert wakachi_preserve_space.parse(string) == expected_result


# エラーのテストケース
def test_parse_with_space_error(wakachi):
    string = "桜が咲く季 節です"
    with pytest.raises(ValueError):
        wakachi.parse(string)
