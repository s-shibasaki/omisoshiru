from datetime import datetime
from typing import Literal, Optional

import pandas as pd


def date_to_str(
    date: datetime,
    on_error: Optional[Literal["raise", "return_empty", "return_none"]] = "raise",
) -> Optional[str]:
    """
    Convert a datetime object to a string in the format '%Y%m%d'.

    Args:
        date (datetime): The datetime object to be converted.
        on_error (Optional[Literal["raise", "return_empty", "return_none"]]):
            Specifies the behavior when encountering an error.
            - 'raise': Raise a ValueError if the 'date' parameter is not a valid datetime object.
            - 'return_empty': Return an empty string if an error occurs.
            - 'return_none': Return None if an error occurs. Defaults to 'raise'.

    Returns:
        Optional[str]: The formatted date string or None if an error occurs and 'on_error' is set to 'return_none'.

    Raises:
        ValueError: If 'on_error' is set to 'raise' and the 'date' parameter is not a valid datetime object,
            or if an invalid value is provided for 'on_error'.
    """
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
