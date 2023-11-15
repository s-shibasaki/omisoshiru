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
