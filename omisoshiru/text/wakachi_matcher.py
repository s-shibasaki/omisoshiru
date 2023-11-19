from typing import List

from ..algorithm import partial_match
from .join_str import join_str
from .wakachi import Wakachi


class WakachiMatcher:
    """
    A class for matching patterns in Japanese text using MeCab.

    Attributes:
        None

    Methods:
        match(patterns: List[str], string: str) -> list:
            Matches patterns in the input string and returns the positions and matched patterns.

    Examples:
        >>> wakachi_matcher = WakachiMatcher()
        >>> pattern_list = ["桜の花"]
        >>> input_text = "桜の花が風に舞い、春の訪れを感じる。桜の花の美しさと儚さが心を打つ。"
        >>> matches = wakachi_matcher.match(pattern_list, input_text)
        >>> print(matches)
        [((0, 3), "桜の花"), ((18, 21), "桜の花")]
    """

    def __init__(self):
        """
        Initializes a WakachiMatcher instance.

        Args:
            None

        Returns:
            None
        """
        self.__wakachi = Wakachi()

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
