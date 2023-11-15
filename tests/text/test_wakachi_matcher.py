import pytest

from omisoshiru.text import WakachiMatcher


@pytest.fixture
def matcher():
    matcher = WakachiMatcher()
    return matcher


def test_single_match(matcher):
    pattern = "春の訪れ"
    string = "桜の花が風に舞い、春の訪れを感じる。桜の花の美しさと儚さが心を打つ。"
    expected_result = [(9, 13)]
    assert matcher.match(pattern, string) == expected_result


def test_multiple_matches(matcher):
    pattern = "桜の花"
    string = "桜の花が風に舞い、春の訪れを感じる。桜の花の美しさと儚さが心を打つ。"
    expected_result = [(0, 3), (18, 21)]
    assert matcher.match(pattern, string) == expected_result


def test_overlapped_matches(matcher):
    pattern = "おはようございます。おはよう"
    string = "おはようございます。おはようございます。おはようございます。"
    expected_result = [(0, 14)]
    assert matcher.match(pattern, string) == expected_result
