from typing import List, Union

import pandas as pd
import rapidfuzz

from .unify_hz import unify_hz


def unify_text(text):
    return unify_hz(text).lower()


class FuzzyReplacer:
    def __init__(self, reference: List[str]):
        self.reference = reference
        self.unified_reference = [unify_text(text) for text in reference]

    def replace(self, text: Union[str, List[str]]):
        if isinstance(text, str):
            unified_text = unify_text(text)
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
            raise TypeError("must be str or list")
