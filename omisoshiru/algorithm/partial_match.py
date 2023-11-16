from typing import List


def partial_match(patterns: List[list], tgt: list):
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
