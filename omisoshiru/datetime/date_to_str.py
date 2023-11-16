from datetime import datetime
from typing import Optional

import pandas as pd


def date_to_str(date: datetime, raise_error: Optional[bool] = True):
    if isinstance(date, datetime) and not pd.isna(date):
        return date.strftime("%Y%m%d")
    elif raise_error:
        raise ValueError(
            "Invalid 'date' parameter. It must be a valid datetime object."
        )
    else:
        return ""
