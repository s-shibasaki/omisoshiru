from typing import List, Optional

import pandas as pd


def join_str(strings: List[str], sep: Optional[str] = None):
    if sep is None:
        sep = ""

    return sep.join([s if pd.notna(s) else "" for s in strings])
