from typing import Dict

from ..replace_text_ranges import replace_text_ranges
from .wakachi_matcher import WakachiMatcher


class WakachiReplacer:
    """
    A WakachiReplacer performs replacements in a given text based on a predefined dictionary.

    Attributes:
        replace_dict (Dict[str, str]): A dictionary where keys are patterns to be replaced,
            and values are the replacement strings.

    Methods:
        replace(text: str) -> str: Replaces patterns in the input text based on the defined replacement dictionary.

    Example:
        >>> replacer = WakachiReplacer({"りんご": "フルーツ", "ばなな": "フルーツ"})
        >>> text = "りんごとばななが好きです。"
        >>> result = replacer.replace(text)
        >>> print(result)
        "フルーツとフルーツが好きです。"
    """

    def __init__(self, replace_dict: Dict[str, str]):
        """
        Initializes a WakachiReplacer instance.

        Args:
            replace_dict (Dict[str, str]): A dictionary where keys are patterns to be replaced,
                and values are the replacement strings.

        Returns:
            None
        """
        self.__matcher = WakachiMatcher()
        self.replace_dict = replace_dict

    def replace(self, text: str) -> str:
        """
        Replaces patterns in the input text based on the defined replacement dictionary.

        Args:
            text (str): The input text to perform replacements on.

        Returns:
            str: The text with replacements applied.
        """
        matches = self.__matcher.match(list(self.replace_dict.keys()), text)
        text = replace_text_ranges(
            text, [(m_pos, self.replace_dict[m_pat]) for m_pos, m_pat in matches]
        )
        return text

    def __str__(self):
        """
        Returns a string representation of the WakachiReplacer instance.

        Returns:
            str: String representation of the WakachiReplacer instance.
        """
        return f"WakachiReplacer(replace_dict={self.replace_dict})"