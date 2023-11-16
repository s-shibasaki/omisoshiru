from omisoshiru.algorithm import partial_match


def test_single_match():
    pat = [list("cde")]
    tgt = list("abcdefg")
    excepted_result = [(2, list("cde"))]
    assert partial_match(pat, tgt) == excepted_result


def test_multiple_matches():
    pat = [list("cde")]
    tgt = list("abcdefgabcdefg")
    excepted_result = [(2, list("cde")), (9, list("cde"))]
    assert partial_match(pat, tgt) == excepted_result


def test_overlapped_matches():
    pat = [list("aba")]
    tgt = list("xxxababaxxx")
    excepted_result = [(3, list("aba"))]
    assert partial_match(pat, tgt) == excepted_result


def test_multiple_patterns_single_match():
    patterns = [list("cde"), list("cdefg")]
    tgt = list("abcdefg")
    excepted_result = [(2, list("cdefg"))]
    assert partial_match(patterns, tgt) == excepted_result


def test_multiple_patterns_multiple_matches():
    patterns = [list("cde"), list("cdefg")]
    tgt = list("abcdefgabcde")
    excepted_result = [(2, list("cdefg")), (9, list("cde"))]
    assert partial_match(patterns, tgt) == excepted_result
