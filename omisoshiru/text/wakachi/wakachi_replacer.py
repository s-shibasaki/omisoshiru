from typing import Dict, Optional

from ..replace_text_ranges import replace_text_ranges
from .wakachi_matcher import WakachiMatcher


class WakachiReplacer:
    def __init__(
        self,
        replace_dict: Dict[str, str],
        unify_hz: Optional[bool] = None,
        unify_hl: Optional[bool] = None,
    ):
        """
        A WakachiReplacer performs replacements in a given text based on a predefined dictionary.

        Args:
            replace_dict (Dict[str, str]): A dictionary where keys are patterns to be replaced,
                and values are the replacement strings.
            unify_hz (bool, optional): Whether to unify half-width characters. Defaults to None.
            unify_hl (bool, optional): Whether to unify characters to lowercase. Defaults to None.

        Example:
            >>> replacer = WakachiReplacer({"りんご": "フルーツ", "ばなな": "フルーツ"})
            >>> text = "りんごとばななが好きです。"
            >>> result = replacer.replace(text)
            >>> print(result)
            "フルーツとフルーツが好きです。"
        """
        self._matcher = WakachiMatcher(unify_hz=unify_hz, unify_hl=unify_hl)
        self.replace_dict = replace_dict

    def replace(self, text: str) -> str:
        """
        Replaces patterns in the input text based on the defined replacement dictionary.

        Args:
            text (str): The input text to perform replacements on.

        Returns:
            str: The text with replacements applied.
        """
        matches = self._matcher.match(list(self.replace_dict.keys()), text)
        text = replace_text_ranges(
            text, [(m_pos, self.replace_dict[m_pat]) for m_pos, m_pat in matches]
        )
        return text

    def __str__(self) -> str:
        """
        Returns a string representation of the WakachiReplacer instance.

        Returns:
            str: String representation of the WakachiReplacer instance.
        """
        return f"WakachiReplacer(replace_dict={self.replace_dict})"
