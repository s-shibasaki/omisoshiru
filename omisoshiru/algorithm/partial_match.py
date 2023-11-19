from typing import Any, List, Tuple


def partial_match(
    patterns: List[List[Any]], tgt: List[Any]
) -> List[Tuple[int, List[Any]]]:
    """
    Find partial matches of patterns in a target list.

    Args:
        patterns (List[List[Any]]): A list of patterns to search for in the target list.
        tgt (List[Any]): The target list to search within.

    Returns:
        List[Tuple[int, List[Any]]]: A list of tuples representing partial matches.
            Each tuple contains the starting index of the match in the target list and the matching pattern.

    Example:
        >>> patterns = [['a', 'b'], ['b', 'c'], ['d']]
        >>> target = ['a', 'b', 'c', 'd', 'e']
        >>> partial_match(patterns, target)
        [(0, ['a', 'b']), (2, ['b', 'c']), (3, ['d'])]
    """
    patterns = sorted(patterns, key=len, reverse=True)

    matches: List[Tuple[int, List[Any]]] = []

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
