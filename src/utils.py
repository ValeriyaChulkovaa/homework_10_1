import csv
import json
import logging
import os
import re
from collections import Counter

import pandas as pd

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/utils.log")
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s", "%d.%m.%Y %H:%M:%S"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_financial_transactions(file_name: str) -> list:
    """Функция принимает на вход путь до файла формата(JSON/csv/xlsx) и возвращает список словарей
    с данными о финансовых транзакциях"""
    try:
        logger.info(f"Попытка открыть файл {file_name}")
        with open(os.path.join("data/", file_name), "r", encoding="utf-8") as f:
            logger.info(f"Файл {file_name} успешно открыт")
            if file_name.endswith(".json"):
                try:
                    data = json.load(f)
                    if isinstance(data, list):
                        logger.info(f"Файл {file_name} успешно десериализован")
                        return data
                    else:
                        logger.error(f"Файл {file_name} не содержит список")
                        return []
                except json.JSONDecodeError:
                    logger.error(f"Файл {file_name} не содержит JSON-строки")
                    return []
            elif file_name.endswith(".csv"):
                logger.info(f"Файл {file_name} формата .csv")
                transaction_for_dict = csv.DictReader(f, delimiter=";")
                logger.info(f"Файл {file_name} прочитан и преобразуется в список с вложенными словарями")
                list_of_transaction = list(transaction_for_dict)
                return list_of_transaction
            elif file_name.endswith(".xlsx"):
                logger.info(f"Файл {file_name} формата .xlsx")
                transaction = pd.read_excel(os.path.join("data/", file_name))
                list_id_name = transaction.columns.to_list()  # преобразовали в список
                list_for_transaction = []
                for idx, row in transaction.iterrows():
                    transaction_dict = {}
                    for i, el in enumerate(row):
                        transaction_dict[list_id_name[i]] = el
                        # print(transaction_dict)
                    list_for_transaction.append(transaction_dict)
                logger.info(f"Файл {file_name} прочитан и преобразуется в список с вложенными словарями")
                return list_for_transaction
            else:
                print(f"Неверный формат файла {file_name}")
                return []

    except FileNotFoundError:
        logger.error(f"Файл {file_name} не найден")
        return []


def search_transaction_data(transactions: list, search_string: str) -> list:
    """Функция принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка."""
    result = []
    for transaction in transactions:
        if "description" in transaction and re.search(search_string.lower(), str(transaction["description"]).lower()):
            result.append(transaction)
    return result


def sorting_operations_category_and_count(transactions: list, categories: list) -> dict:
    """
    Функция принимает список словарей с данными о банковских операциях и список категорий операций,
    и возвращает словарь - категория: количество операций.
    """
    list_result = []
    for transaction in transactions:
        list_result.append(transaction.get("description"))
    dict_result = {}
    count = Counter(list_result)
    for el in count:
        if el is None or el == "":
            continue
        else:
            dict_result[el] = count[el]
    return dict_result
