import json
from collections import Counter

from src.config import file_transaction_json


def grouping_operations(transactions: list[dict], category: list) -> dict:
    """
    Функция, которая будет принимать список словарей с данными о банковских операциях и список категорий операций,
    а возвращать словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой
    категории.
    """
    operations_ = []
    for i in transactions:
        if i.get('description'):
            operations_.append(i)
            result = [trans['description'] for trans in operations_ if trans['description'] in category]
            count_ = Counter(result)
            count_dict = dict(count_)
    return count_dict


path = file_transaction_json
with open(path, encoding='utf-8') as f:
    sentence = json.load(f)
    