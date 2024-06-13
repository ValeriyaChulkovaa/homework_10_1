from typing import Any


def get_data(data_today: str) -> Any:
    """Реализация функции, которая возвращает измененную дату"""
    if str(len(data_today)) == '26':
        return f"{data_today[8:10]}.{data_today[5:7]}.{data_today[:4]}"
    else:
        return None


print(get_data('2018-07-11T02:26:18.671407'))
