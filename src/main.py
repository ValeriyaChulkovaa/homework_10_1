import json
import logging
import pandas as pd
from read_excel import read_excel  # Предполагается, что эта функция возвращает DataFrame
from utils import (
    currency_rates,
    for_each_card,
    get_price_stock,
    greetings,
    top_five_transaction,
    filter_by_date
)

# Настройка логирования
logger = logging.getLogger("main")
file_handler = logging.FileHandler("main.log", "w", encoding='utf-8')
file_formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def main(transactions: pd.DataFrame, date: str, stocks: list) -> str:
    """Функция создающая JSON ответ для страницы главная"""
    logger.info("Начало работы главной функции (main)")

    # Фильтрация транзакций по дате
    final_list = filter_by_date(date, transactions)

    # Получение приветствия
    greeting = greetings()

    # Получение информации по картам
    cards = for_each_card(final_list)

    # Получение топ-5 транзакций
    top_trans = top_five_transaction(final_list)

    # Получение цен акций
    try:
        stocks_prices = get_price_stock(stocks)
    except Exception as e:
        logger.error(f"Ошибка при получении цен акций: {e}")
        stocks_prices = []

    # Получение курсов валют
    currency_r = currency_rates()

    logger.info("Создание JSON ответа")

    # Формирование JSON-ответа
    date_json = json.dumps(
        {
            "greeting": greeting,
            "cards": cards,
            "top_transactions": top_trans,
            "currency_rates": currency_r,
            "stock_prices": stocks_prices,
        },
        indent=4,
        ensure_ascii=False,
    )

    logger.info("Завершение работы главной функции (main)")
    return date_json


# Пример вызова функции
if __name__ == "__main__":
    file_path = "../data/operations.xlsx"

    try:
        transactions = read_excel(file_path)  # Предполагается, что read_excel возвращает DataFrame
        print(main(transactions, "2021-11-12", ["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"]))
    except Exception as e:
        logger.error(f"Ошибка при чтении файла Excel: {e}")