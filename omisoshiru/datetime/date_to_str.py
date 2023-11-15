from datetime import datetime

import pandas as pd


def date_to_str(date: datetime):
    if isinstance(date, datetime) and not pd.isnat(date):
        return date.strftime("%Y%m%d")
    else:
        raise ValueError(
            "Invalid 'date' parameter. It must be a valid datetime object."
        )
