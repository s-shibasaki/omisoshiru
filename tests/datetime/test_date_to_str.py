from datetime import datetime

import pytest
from pandas import NaT

from omisoshiru.datetime import date_to_str


def test_valid_date_formatting():
    valid_date = datetime(2023, 11, 16)
    formatted_date = date_to_str(valid_date)
    assert formatted_date == "20231116"


def test_invalid_date_formatting():
    invalid_date = NaT
    with pytest.raises(ValueError, match="Invalid 'date' parameter"):
        date_to_str(invalid_date)


def test_invalid_type_formatting():
    invalid_date = "2023-11-16"  # 文字列は無効な型
    with pytest.raises(ValueError, match="Invalid 'date' parameter"):
        date_to_str(invalid_date)


def test_invalid_date_formatting_return_none():
    invalid_date = NaT
    formatted_date = date_to_str(invalid_date, "return_none")
    assert formatted_date is None


def test_invalid_date_formatting_return_empty():
    invalid_date = NaT
    formatted_date = date_to_str(invalid_date, "return_empty")
    assert formatted_date == ""


def test_invalid_error_handling_type():
    invalid_date = NaT
    with pytest.raises(ValueError, match="Invalid error handling type"):
        date_to_str(invalid_date, "invalid_type")
