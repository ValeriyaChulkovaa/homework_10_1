import pytest

from src.widget import get_data


@pytest.mark.parametrize("coded_date, decoded_date", [("2018-07-11T02:26:18.671407", "11.07.2018")])
def test_get_data(coded_date: str, decoded_date: str) -> None:
    assert get_data(coded_date) == decoded_date
