from typing import List, Union

import pandas as pd
import rapidfuzz

from .unify_hz import unify_hz


class FuzzyReplacer:
    """
    A FuzzyReplacer class that replaces input text with the most similar string from a reference list.

    Args:
        reference (List[str]): List of reference strings.

    Attributes:
        reference (List[str]): List of reference strings.
        unified_reference (List[str]): List of unified reference strings.

    Methods:
        replace(text: Union[str, List[str]]) -> Union[str, List[str]]:
            Replaces the input text with the most similar string from the reference list.

        _unify_text(text: str) -> str:
            Unifies the input text by converting it to lowercase after applying full-width and half-width character conversion.

    Example:
        >>> replacer = FuzzyReplacer(["apple", "orange", "banana"])
        >>> replacer.replace("applle")
        "apple"
        >>> replacer.replace(["applle", "bannaana"])
        ["apple", "banana"]
    """

    def __init__(self, reference: List[str]):
        """
        Initializes a FuzzyReplacer instance with a reference list.

        Args:
            reference (List[str]): List of reference strings.

        Returns:
            None
        """
        self.reference = reference
        self.unified_reference = [self._unify_text(text) for text in reference]

    def replace(self, text: Union[str, List[str]]) -> Union[str, List[str]]:
        """
        Replaces the input text with the most similar string from the reference list.

        Args:
            text (Union[str, List[str]]): Input text or list of texts to be replaced.

        Returns:
            Union[str, List[str]]: Replaced text or list of replaced texts.

        Example:
            >>> replacer = FuzzyReplacer(["apple", "orange", "banana"])
            >>> replacer.replace("applle")
            "apple"
            >>> replacer.replace(["applle", "bannaana"])
            ["apple", "banana"]
        """
        if isinstance(text, str):
            unified_text = self._unify_text(text)
            unified_result = rapidfuzz.process.extract(
                unified_text, self.unified_reference
            )
            most_similar_idx = (
                pd.DataFrame(unified_result, columns=["choice", "similarity", "idx"])
                .set_index("idx")
                .similarity.idxmax()
            )
            return self.reference[most_similar_idx]

        elif isinstance(text, list):
            return [self.replace(item) for item in text]

        else:
            raise TypeError("Input must be str or list")

    def _unify_text(self, text: str) -> str:
        """
        Unifies the input text by converting it to lowercase after applying full-width and half-width character conversion.

        Args:
            text (str): Input text to be unified.

        Returns:
            str: Unified text.

        Example:
            >>> replacer = FuzzyReplacer([])
            >>> replacer._unify_text("Ａｐｐｌｅ")
            "apple"
        """
        return unify_hz(text).lower()
