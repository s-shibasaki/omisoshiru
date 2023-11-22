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
        self.__wakachi = Wakachi()
        self._unify_hz = unify_hz
        self._unify_hl = unify_hl

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
        unified_patterns = unify_hz(patterns) if self._unify_hz else patterns
        unified_patterns = (
            [pattern.lower() for pattern in patterns]
            if self._unify_hl
            else unified_patterns
        )

        p = [self.__wakachi.parse(pattern) for pattern in unified_patterns]
        s = self.__wakachi.parse(string)
        matches = partial_match(p, s)

        s_lengths = list(map(len, s))
        return [
            (
                (sum(s_lengths[:m_pos]), sum(s_lengths[: m_pos + len(m_pat)])),
                patterns[unified_patterns.index(join_str(m_pat))],
            )
            for m_pos, m_pat in matches
        ]
