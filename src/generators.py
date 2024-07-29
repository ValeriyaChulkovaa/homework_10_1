from typing import Generator


def filter_by_currency(transactions: list, is_open_file: str, currency: str) -> Generator:
    """
    Функция которая принимает список словарей с банковскими операциями
    (или объект-генератор, который выдает по одной банковской операции)
     и возвращает итератор, который выдает по очереди операции, в которых указана заданная валюта.
    """
    if is_open_file == "json":
        for transaction in transactions:
            if transaction["operationAmount"]["currency"]["code"] == currency:
                yield transaction
    elif is_open_file == "csv":
        for transaction in transactions:
            if transaction["currency_name"] == currency:
                yield transaction
    elif is_open_file == "xlsx":
        for transaction in transactions:
            if transaction["currency_name"] == currency:
                yield transaction


def transaction_descriptions(transactions: list) -> Generator:
    """Функция который принимает список словарей и
    возвращает описание каждой операции по очереди
    """
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Generator:
    """
    Функция генерирует номер карт в формате XXXX XXXX XXXX XXXX
    """
    if end < start:
        cash = start
        start = end
        end = cash

    for num in range(start, end + 1):
        if len(str(num)) < 16:
            numbers = "0" * (16 - len(str(num))) + str(num)
        else:
            numbers = str(num)

        block_number = f"{numbers[:4]} {numbers[4:8]} {numbers[8:12]} {numbers[12:16]}"
        yield block_number
