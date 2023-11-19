def replace_text_ranges(text: str, replace: list) -> str:
    """
    Replace specified ranges in the input text with the given replacement strings.

    Args:
        text (str): The input text to be processed.
        replace (list): A list of tuples where each tuple represents a text range to be replaced
            and the corresponding replacement string.

    Returns:
        str: The text with specified ranges replaced by the provided replacement strings.

    Examples:
        >>> original_text = "The quick brown fox jumps over the lazy dog."
        >>> replacement_ranges = [((4, 9), "swift"), ((20, 25), "leaps"), ((35, 39), "sleepy")]
        >>> modified_text = replace_text_ranges(original_text, replacement_ranges)
        >>> print(modified_text)
        "The swift brown fox leaps the sleepy dog."
    """
    offset = 0
    for (start, stop), replace_to in replace:
        text = text[: start + offset] + replace_to + text[stop + offset :]
        offset += len(replace_to) - (stop - start)
    return text
