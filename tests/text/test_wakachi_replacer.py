import pytest

from omisoshiru.text import WakachiReplacer


@pytest.fixture
def replacer():
    replace_dict = {
        "りんご": "果物",
        "ばなな": "果物",
        "オレンジ": "果物",
        "車": "乗り物",
        "自転車": "乗り物",
        "犬": "動物",
        "猫": "動物",
    }
    return WakachiReplacer(replace_dict)


def test_replace_single_word(replacer):
    text = "私はりんごが好きです"
    result = replacer.replace(text)
    assert result == "私は果物が好きです"


def test_replace_multiple_words(replacer):
    text = "私はりんごとばななとオレンジを持っています"
    result = replacer.replace(text)
    assert result == "私は果物と果物と果物を持っています"


def test_replace_non_matching_words(replacer):
    text = "私は車を運転し、自転車に乗ります"
    result = replacer.replace(text)
    assert result == "私は乗り物を運転し、乗り物に乗ります"


def test_replace_japanese_words(replacer):
    text = "犬と猫がいます"
    result = replacer.replace(text)
    assert result == "動物と動物がいます"
