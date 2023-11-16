def replace_text_ranges(text, replace_to, ranges):
    offset = 0
    for start, stop in ranges:
        text = text[: start + offset] + replace_to + text[stop + offset :]
        offset += len(replace_to) - (stop - start)
    return text
