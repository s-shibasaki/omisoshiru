from omisoshiru.algorithm import partial_match


def test_single_match():
    pat = list("cde")
    tgt = list("abcdefg")
    excepted_result = [2]
    assert partial_match(pat, tgt) == excepted_result


def test_multiple_matches():
    pat = list("cde")
    tgt = list("abcdefgabcdefg")
    excepted_result = [2, 9]
    assert partial_match(pat, tgt) == excepted_result


def test_overlapped_matches():
    pat = list("aba")
    tgt = list("xxxababaxxx")
    excepted_result = [3]
    assert partial_match(pat, tgt) == excepted_result
