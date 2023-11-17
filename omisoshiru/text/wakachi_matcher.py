from ..algorithm import partial_match
from .join_str import join_str
from .wakachi import Wakachi


class WakachiMatcher:
    def __init__(self):
        self.__wakachi = Wakachi()

    def match(self, patterns: str, string: str):
        p = [self.__wakachi.parse(pattern) for pattern in patterns]
        s = self.__wakachi.parse(string)
        matches = partial_match(p, s)

        s_lengths = list(map(len, s))
        return [
            (
                (sum(s_lengths[:m_pos]), sum(s_lengths[: m_pos + len(m_pat)])),
                join_str(m_pat),
            )
            for m_pos, m_pat in matches
        ]
