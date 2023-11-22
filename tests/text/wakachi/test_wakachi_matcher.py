import pytest

from omisoshiru.text.wakachi import WakachiMatcher


@pytest.fixture
def matcher():
    matcher = WakachiMatcher()
    return matcher


def test_single_match(matcher):
    pattern = "春の訪れ"
    string = "桜の花が風に舞い、春の訪れを感じる。桜の花の美しさと儚さが心を打つ。"
    expected_result = [((9, 13), pattern)]
    assert matcher.match([pattern], string) == expected_result


def test_multiple_matches(matcher):
    pattern = "桜の花"
    string = "桜の花が風に舞い、春の訪れを感じる。桜の花の美しさと儚さが心を打つ。"
    expected_result = [((0, 3), pattern), ((18, 21), pattern)]
    assert matcher.match([pattern], string) == expected_result


def test_overlapped_matches(matcher):
    pattern = "おはようございます。おはよう"
    string = "おはようございます。おはようございます。おはようございます。"
    expected_result = [((0, 14), pattern)]
    assert matcher.match([pattern], string) == expected_result


def test_multiple_patterns_single_match(matcher):
    patterns = ["春の訪れ", "春の訪れを"]
    string = "桜の花が風に舞い、春の訪れを感じる。桜の花の美しさと儚さが心を打つ。"
    expected_result = [((9, 14), "春の訪れを")]
    assert matcher.match(patterns, string) == expected_result


def test_match_without_unification(matcher):
    patterns = [
        "ｵﾊﾖｳ",
        "ゴザイマス",
        "ＡＢＣ",
        "def",
        "ｈｉｊ",
        "KLM",
        "OPQ",
        "ｒｓｔ",
        "uvw",
        "ＸＹＺ",
    ]
    input_text = "オハヨウ,ｺﾞｻﾞｲﾏｽ,ABC,DEF,hij,klm,ＯＰＱ,ＲＳＴ,ｕｖｗ,ｘｙｚ"
    matches = matcher.match(patterns, input_text)
    assert len(matches) == 0


def test_match_with_unification_hz(matcher):
    matcher.unify_hz = True
    patterns = [
        "ｵﾊﾖｳ",
        "ゴザイマス",
        "ＡＢＣ",
        "def",
        "ｈｉｊ",
        "KLM",
        "OPQ",
        "ｒｓｔ",
        "uvw",
        "ＸＹＺ",
    ]
    input_text = "オハヨウ,ｺﾞｻﾞｲﾏｽ,ABC,DEF,hij,klm,ＯＰＱ,ＲＳＴ,ｕｖｗ,ｘｙｚ"
    matches = matcher.match(patterns, input_text)
    assert [m[1] for m in matches] == [
        "ｵﾊﾖｳ",
        "ゴザイマス",
        "ＡＢＣ",
        "ｈｉｊ",
        "OPQ",
        "uvw",
    ]


def test_match_with_unification_hl(matcher):
    matcher.unify_hl = True
    patterns = [
        "ｵﾊﾖｳ",
        "ゴザイマス",
        "ＡＢＣ",
        "def",
        "ｈｉｊ",
        "KLM",
        "OPQ",
        "ｒｓｔ",
        "uvw",
        "ＸＹＺ",
    ]
    input_text = "オハヨウ,ｺﾞｻﾞｲﾏｽ,ABC,DEF,hij,klm,ＯＰＱ,ＲＳＴ,ｕｖｗ,ｘｙｚ"
    matches = matcher.match(patterns, input_text)
    assert [m[1] for m in matches] == [
        "def",
        "KLM",
        "ｒｓｔ",
        "ＸＹＺ",
    ]


def test_match_with_unification_hz_and_hl(matcher):
    matcher.unify_hz = True
    matcher.unify_hl = True
    patterns = [
        "ｵﾊﾖｳ",
        "ゴザイマス",
        "ＡＢＣ",
        "def",
        "ｈｉｊ",
        "KLM",
        "OPQ",
        "ｒｓｔ",
        "uvw",
        "ＸＹＺ",
    ]
    input_text = "オハヨウ,ｺﾞｻﾞｲﾏｽ,ABC,DEF,hij,klm,ＯＰＱ,ＲＳＴ,ｕｖｗ,ｘｙｚ"
    matches = matcher.match(patterns, input_text)
    assert [m[1] for m in matches] == [
        "ｵﾊﾖｳ",
        "ゴザイマス",
        "ＡＢＣ",
        "def",
        "ｈｉｊ",
        "KLM",
        "OPQ",
        "ｒｓｔ",
        "uvw",
        "ＸＹＺ",
    ]
