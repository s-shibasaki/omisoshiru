from typing import List


def partial_match(pat: list, tgt: list):
    matches = []

    i = 0
    while i <= len(tgt) - len(pat):
        if tgt[i : i + len(pat)] == pat:
            matches.append(i)
            i += len(pat)
        else:
            i += 1

    return matches


def partial_match_multi(patterns: List[list], tgt: list):
    # 長さの降順にソート
    patterns = sorted(patterns, key=len, reverse=True)

    matches = []

    i = 0
    while i < len(tgt):
        for pat in patterns:
            if tgt[i : i + len(pat)] == pat:
                matches.append((i, pat))
                i += len(pat)
                break
        else:
            i += 1

    return matches
