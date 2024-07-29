import os
from typing import Any

import requests
from dotenv import load_dotenv


def sum_transaction_amount(user_transaction: dict) -> Any:
    """Функция принимает транзакцию и возвращает возвращает ее сумму в рублях, если  транзакция была в USD или EUR,
    происходит конвертация с помощью Exchange Rates Data API
    """
    currency = user_transaction["operationAmount"]["currency"]["code"]
    amount = user_transaction["operationAmount"]["amount"]
    if currency in ["USD", "EUR"]:
        load_dotenv(".env")
        api_key = os.getenv("API_KEY")
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={'RUB'}&from={currency}&amount={amount}"
        headers = {"apikey": api_key}
        response = requests.get(url, headers=headers)
        result = response.json()["result"]
        return round(result, 2)
    else:
        return amount
    