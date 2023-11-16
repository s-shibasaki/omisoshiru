import MeCab
import unidic

from ..algorithm import partial_match
from .join_str import join_str


class WakachiMatcher:
    def __init__(self):
        dicdir = unidic.DICDIR.replace("\\", "/")
        self.__wakachi = MeCab.Tagger(f"-Owakati -d {dicdir}")

    def __parse(self, string):
        if len(string.split()) > 1:
            raise ValueError("input must not contain spaces")
        return self.__wakachi.parse(string).split()

    def match(self, patterns: str, string: str):
        p = [self.__parse(pattern) for pattern in patterns]
        s = self.__parse(string)
        matches = partial_match(p, s)

        s_lengths = list(map(len, s))
        return [
            (
                (sum(s_lengths[:m_pos]), sum(s_lengths[: m_pos + len(m_pat)])),
                join_str(m_pat),
            )
            for m_pos, m_pat in matches
        ]
