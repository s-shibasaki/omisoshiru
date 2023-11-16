from typing import Dict

from .replace_text_ranges import replace_text_ranges_multi
from .wakachi_matcher import WakachiMatcher


class WakachiReplacer:
    def __init__(self, replace_dict: Dict[str, str]):
        self.__matcher = WakachiMatcher()
        self.replace_dict = replace_dict

    def replace(self, text):
        matches = self.__matcher.match_multi(list(self.replace_dict.keys()), text)
        text = replace_text_ranges_multi(
            text, [(m_pos, self.replace_dict[m_pat]) for m_pos, m_pat in matches]
        )
        return text
