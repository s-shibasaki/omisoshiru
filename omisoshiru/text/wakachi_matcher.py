import MeCab
import unidic

from ..algorithm import partial_match


class WakachiMatcher:
    def __init__(self):
        dicdir = unidic.DICDIR.replace("\\", "/")
        self.__wakachi = MeCab.Tagger(f"-Owakati -d {dicdir}")

    def __parse(self, string):
        return self.__wakachi.parse(string).split()

    def match(self, pattern: str, string: str):
        if len(pattern.split()) != 1 or len(string.split()) != 1:
            raise ValueError("input must not contain spaces")

        p = self.__parse(pattern)
        s = self.__parse(string)
        matches = partial_match(p, s)

        s_lengths = list(map(len, s))
        return [(sum(s_lengths[:m]), sum(s_lengths[: m + len(p)])) for m in matches]
