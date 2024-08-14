import json
import re

from src.config import file_transaction_json


def filtered_by_descriptions(list_dict: list[dict], search: str) -> list[dict]:
    """
    Функция, которая будет принимать список словарей с данными о банковских операциях и строку поиска,
    а возвращать список словарей, у которых в описании есть данная строка.
    """
    operations_ = []
    for i in list_dict:
        if i.get('description'):
            operations_.append(i)
    return [trans for trans in operations_ if re.search(search, trans['description'])]


path = file_transaction_json
with open(path, encoding='utf-8') as f:
    data_ = json.load(f)
    search_string = 'Перевод организации'
    