import json
import logging

from read_excel import read_excel
from utils import currency_rates, for_each_card, get_price_stock, greetings, top_five_transaction
from views import filter_by_date

logger = logging.getLogger("utils.log")
file_handler = logging.FileHandler("main.log", "w")
file_formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def main(date: str, file_path: str, stocks: list):
    """Функция создающая JSON ответ для страницы главная"""
    logger.info("Начало работы главной функции (main)")

    my_list_trans = read_excel(file_path)
    final_list = filter_by_date(date, my_list_trans)
    greeting = greetings()
    cards = for_each_card(final_list)
    top_trans = top_five_transaction(final_list)
    stocks_prices = get_price_stock(stocks)
    currency_r = currency_rates()
    logger.info("Создание JSON ответа")
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


# print(main("2021.11.12", "../data/operations.xlsx", ["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"]))
