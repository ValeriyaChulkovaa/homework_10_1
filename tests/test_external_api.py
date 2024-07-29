from typing import Any
from unittest.mock import patch

from src.external_api import sum_transaction_amount


@patch("requests.get")
def test_sum_transaction_amount_usd(mock_get: Any) -> None:
    mock_get.return_value.json.return_value = {"result": 100}
    assert sum_transaction_amount({"operationAmount": {"currency": {"code": "USD"}, "amount": 1}}) == 100
    mock_get.assert_called_once()


def test_sum_transaction_amount_rub() -> None:
    assert sum_transaction_amount({"operationAmount": {"currency": {"code": "RUB"}, "amount": 100}}) == 100
    