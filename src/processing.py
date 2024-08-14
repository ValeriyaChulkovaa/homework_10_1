from typing import Any


def filter_by_state(dictionary_list: list, state: str = "EXECUTED") -> list:
    """Принимает список словарей, и возвращает новый список
    у которых ключ state содержит переданное в функцию значение."""
    new_list_ = []

    for i in dictionary_list:
        if i.get("state") == state:
            new_list_.append(i)
    return new_list_


def sort_by_date(dictionary_list: list, reverse_dictionary_list: bool = False) -> Any:
    """
    Функция сортировки операций по дате (по возрастанию)
    """
    dictionary_list.sort(key=lambda d: d.get("date"), reverse=reverse_dictionary_list)