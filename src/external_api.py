import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = 'WAbEGULfdVkp1lvalHnIwuAnCDFJSKMh'


def get_transaction_amount_in_rubles(transaction: dict) -> float:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях."""

    amount = float(transaction["amount"])
    currency = transaction["currency"]

    if currency == "RUB":
        return float(amount)

    elif currency == "USD" or currency == "EUR":
        api_key = os.getenv("API_KEY")
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"

        headers = {"apikey": api_key}
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()
        return float(data["result"])

    else:
        raise ValueError(f"Неизвестная валюта {currency}.")


if __name__ == "__main__":
    transaction1 = {"amount": 100, "currency": "RUB"}
    transaction2 = {"amount": 50, "currency": "USD"}
    transaction3 = {"amount": 150, "currency": "EUR"}

    amount_in_rubles1 = get_transaction_amount_in_rubles(transaction1)
    amount_in_rubles2 = get_transaction_amount_in_rubles(transaction2)
    amount_in_rubles3 = get_transaction_amount_in_rubles(transaction3)

    print(f"Сумма в рублях (RUB): {amount_in_rubles1}")
    print(f"Сумма в рублях (USD): {amount_in_rubles2}")
    print(f"Сумма в рублях (EUR): {amount_in_rubles3}")


def get_exchange_rate(target_currency):
    """Получаем текущий обменный курс для заданной валюты"""
    headres = {'apikey': API_KEY}
    params = {'symbol': 'RUB', 'base': target_currency}

    response = requests.get(BASE_URL, headres=headres, params=params)

    if response.status_code != 200:
        raise Exception('Error fetching exchange rates')

    data = response.json()
    return data['rates']['RUB']
