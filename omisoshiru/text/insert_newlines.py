from .join_str import join_str
from .wakachi import Wakachi

# TODO: Wakachiを使って単語区切りにする


def insert_newlines(input_string, max_length):
    remaining = input_string
    lines = []
    while remaining:
        line = remaining[:max_length]
        remaining = remaining[max_length:]
        while remaining.startswith("\\"):
            line += remaining[:1]
            remaining = remaining[1:]
        lines.append(line)
    return join_str(lines, "\n")
