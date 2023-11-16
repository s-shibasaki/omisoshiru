from datetime import datetime
from typing import Literal, Optional

import pandas as pd


def date_to_str(
    date: datetime,
    on_error: Optional[Literal["raise", "return_empty", "return_none"]] = "raise",
):
    if isinstance(date, datetime) and not pd.isna(date):
        return date.strftime("%Y%m%d")
    elif on_error == "raise":
        raise ValueError(
            "Invalid 'date' parameter. It must be a valid datetime object."
        )
    elif on_error == "return_empty":
        return ""
    elif on_error == "return_none":
        return None
    else:
        raise ValueError("Invalid error handling type")
