def filter_by_state(list_of_dist: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция принимает на вход список словарей и значение для ключа state
    (опциональный параметр со значением по умолчанию EXECUTED)
    и возвращает новый список, содержащий только те словари,
    у которых ключ state содержит переданное в функцию значение."""
    filtered_list = []
    for el in list_of_dist:
        if el.get("state") == state:
            filtered_list.append(el)
    return filtered_list


def sort_by_date(list_of_dist: list[dict], is_reverse: bool = True) -> list[dict]:
    """Функция которая принимает на вход список словарей и возвращает новый список,
    в котором исходные словари отсортированы по убыванию даты (ключ date).
    Функция принимает два аргумента, второй необязательный задает порядок сортировки (убывание, возрастание)."""
    sort_date = sorted(list_of_dist, key=lambda dict: dict["date"], reverse=is_reverse)
    return sort_date
