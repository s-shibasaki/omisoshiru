from typing import Optional

import MeCab
import unidic


class Wakachi:
    def __init__(self, preserve_space: Optional[bool] = None):
        dicdir = unidic.DICDIR.replace("\\", "/")
        self.__wakachi = MeCab.Tagger(f"-Owakati -d {dicdir}")
        self.preserve_space = preserve_space if preserve_space is not None else False

    def parse(self, string: str):
        if not self.preserve_space and len(string.split()) > 1:
            raise ValueError("input must not contain spaces")
        return self.__wakachi.parse(string).split()
