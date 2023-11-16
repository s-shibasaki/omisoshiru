from omisoshiru.text import replace_text_ranges


def test_replace_single_range():
    text = "Hello, world!"
    replace_to = "Python"
    ranges = [(7, 12)]
    result = replace_text_ranges(text, [(r, replace_to) for r in ranges])
    assert result == "Hello, Python!"


def test_replace_multiple_ranges():
    text = "Hello, world!"
    replace_to = "Python"
    ranges = [(0, 5), (7, 12)]
    result = replace_text_ranges(text, [(r, replace_to) for r in ranges])
    assert result == "Python, Python!"


def test_replace_empty_text():
    text = ""
    replace_to = "Python"
    ranges = [(0, 0)]
    result = replace_text_ranges(text, [(r, replace_to) for r in ranges])
    assert result == "Python"


def test_replace_empty_ranges():
    text = "Hello, world!"
    replace_to = "Python"
    ranges = []
    result = replace_text_ranges(text, [(r, replace_to) for r in ranges])
    assert result == "Hello, world!"
