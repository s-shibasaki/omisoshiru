def replace_text_ranges(text, replace_to, ranges):
    offset = 0
    for start, stop in ranges:
        text = text[: start + offset] + replace_to + text[stop + offset :]
        offset += len(replace_to) - (stop - start)
    return text


def replace_text_ranges_multi(text, replace):
    offset = 0
    for (start, stop), replace_to in replace:
        text = text[: start + offset] + replace_to + text[stop + offset :]
        offset += len(replace_to) - (stop - start)
    return text
