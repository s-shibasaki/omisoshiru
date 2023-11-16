def replace_text_ranges(text, replace):
    offset = 0
    for (start, stop), replace_to in replace:
        text = text[: start + offset] + replace_to + text[stop + offset :]
        offset += len(replace_to) - (stop - start)
    return text
