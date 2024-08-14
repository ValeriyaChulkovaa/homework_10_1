import os

import requests
from dotenv import load_dotenv

load_dotenv()


def return_amount_trans(transactions: dict) -> float:
    """
    Функция, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях
    """
    amount = transactions["operationAmount"]["amount"]
    currency = transactions["operationAmount"]["currency"]["code"]
    if currency == "RUB":
        return float(amount)
    else:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        API_KEY = os.getenv("API_KEY")
        headers = {"apikey": f"{API_KEY}"}

        response = requests.get(url, headers=headers)
        data = response.json()
        return float(data["result"])
    