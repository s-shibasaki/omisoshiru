from typing import List

from ...algorithm import partial_match
from ..join_str import join_str
from ..unify_hz import unify_hz
from .wakachi import Wakachi


class WakachiMatcher:
    def __init__(self, unify_hz=False, unify_hl=False):
        """
        A class for matching patterns in Japanese text using MeCab.

        Examples:
            >>> wakachi_matcher = WakachiMatcher()
            >>> pattern_list = ["桜の花"]
            >>> input_text = "桜の花が風に舞い、春の訪れを感じる。桜の花の美しさと儚さが心を打つ。"
            >>> matches = wakachi_matcher.match(pattern_list, input_text)
            >>> print(matches)
            [((0, 3), "桜の花"), ((18, 21), "桜の花")]
        """
        self.wakachi = Wakachi()
        self.unify_hz = unify_hz
        self.unify_hl = unify_hl

    def _preprocess_string(self, string):
        string = unify_hz(string) if self.unify_hz else string
        string = string.lower() if self.unify_hl else string
        return string

    def match(self, patterns: List[str], string: str) -> list:
        """
        Matches patterns in the input string and returns the positions and matched patterns.

        Args:
            patterns (List[str]): A list of patterns to match in the input string.
            string (str): The input text to be searched for matches.

        Returns:
            list: A list of tuples containing the positions and matched patterns.

        Notes:
            The positions in the returned tuples represent the start and end positions of the matched patterns.
        """
        unified_patterns = [self._preprocess_string(pattern) for pattern in patterns]
        unified_string = self._preprocess_string(string)

        p = [self.wakachi.parse(pattern) for pattern in unified_patterns]
        s = self.wakachi.parse(unified_string)
        matches = partial_match(p, s)

        s_lengths = [len(segment) for segment in s]
        return [
            (
                (sum(s_lengths[:m_pos]), sum(s_lengths[: m_pos + len(m_pat)])),
                patterns[unified_patterns.index(join_str(m_pat))],
            )
            for m_pos, m_pat in matches
        ]
