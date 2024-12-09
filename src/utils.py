import json
import logging
import requests
import pandas as pd
from datetime import datetime, timedelta
from typing import List, Dict, Any

# Настройка логирования
logger = logging.getLogger("utils")
file_handler = logging.FileHandler("utils.log", "w", encoding='utf-8')
file_formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def greetings() -> str:
    """Функция приветствия"""
    time_obj = datetime.now()
    if 6 <= time_obj.hour < 12:
        return "Доброе утро"
    elif 12 <= time_obj.hour < 18:
        return "Добрый день"
    elif 18 <= time_obj.hour < 24:
        return "Добрый вечер"
    else:
        return "Доброй ночи"


def for_each_card(my_list: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Функция создания информации по каждой карте"""
    logger.info("Начало работы функции (for_each_card)")
    cards = {}
    result = []

    logger.info("Перебор транзакций")
    for item in my_list:
        if pd.isna(item["Номер карты"]) or pd.isna(item["Сумма платежа"]):
            continue

        card_number = item["Номер карты"][1:]  # Убираем первый символ
        amount = float(str(item["Сумма платежа"]).replace(',', '.')[1:])  # Убираем знак и заменяем запятую на точку

        if card_number in cards:
            cards[card_number] += amount
        else:
            cards[card_number] = amount

    for k, v in cards.items():
        result.append({"last_digits": k, "total_spent": round(v, 2), "cashback": round(v / 100, 2)})

    logger.info("Завершение работы функции (for_each_card)")
    return result


def currency_rates(currencies: List[str]) -> List[Dict[str, Any]]:
    """Функция запроса курса валют"""
    logger.info("Начало работы функции (currency_rates)")
    result = []

    for currency in currencies:
        url = f"https://v6.exchangerate-api.com/v6/{API_KEY_CUR}/latest/{currency}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            result.append({"currency": currency, "rate": round(data["conversion_rates"]["RUB"], 2)})
        else:
            logger.error(f"Ошибка при запросе курса валют для {currency}: {response.status_code}")

    logger.info("Окончание работы функции - currency_rates")
    return result


def top_five_transaction(my_list: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Функция для получения топ-5 транзакций по сумме платежа"""
    logger.info("Начало работы функции (top_five_transaction)")

    all_transactions = {}

    for item in my_list:
        if pd.isna(item["Категория"]) or pd.isna(item["Сумма платежа"]):
            continue

        category = item["Категория"]
        amount = float(str(item["Сумма платежа"]).replace(',', '.')[1:])  # Убираем знак и заменяем запятую на точку

        if category not in all_transactions or amount > all_transactions[category]:
            all_transactions[category] = amount

    result = [
        {"date": item["Дата платежа"], "amount": amount, "category": category, "description": item["Описание"]}
        for item in my_list
        for category, amount in all_transactions.items()
        if item["Категория"] == category and amount == float(str(item["Сумма платежа"]).replace(',', '.')[1:])
    ]

    logger.info("Окончание работы функции (top_five_transaction)")
    return result


def get_price_stock(stocks: List[str]) -> List[Dict[str, Any]]:
    """Функция для получения данных об акциях из списка S&P500"""
    logger.info("Начало работы функции (get_price_stock)")

    stock_prices = []

    for stock in stocks:
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock}&apikey={SP_500_API_KEY}"
        response = requests.get(url)

        if response.status_code == 200:
            result = response.json()
            stock_prices.append({"stock": stock, "price": round(float(result["Global Quote"]["05. price"]), 2)})
        else:
            logger.error(f"Ошибка при запросе данных для акции {stock}: {response.status_code}")

    logger.info("Функция get_price_stock успешно завершила свою работу")
    return stock_prices


def filter_by_date(date: str, my_list: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Функция фильтрующая данные по заданной дате"""
    list_by_date = []

    if date == "":
        return list_by_date

    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d")  # Ожидаем формат YYYY-MM-DD
    except ValueError as e:
        logger.error(f"Ошибка формата даты: {e}")
        return list_by_date

    for item in my_list:
        if pd.isna(item["Дата платежа"]) or isinstance(item["Дата платежа"], float):
            continue

        try:
            payment_date = datetime.strptime(str(item["Дата платежа"]), "%d.%m.%Y")
        except ValueError as e:
            logger.error(f"Ошибка преобразования даты платежа: {e}")
            continue

        if date_obj >= payment_date >= (date_obj - timedelta(days=date_obj.day - 1)):
            list_by_date.append(item)

    return list_by_date