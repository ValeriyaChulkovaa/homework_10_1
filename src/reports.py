import datetime
import json
import logging
from typing import Any, Callable, Optional, List, Dict

import pandas as pd

# Настройка логирования
logger = logging.getLogger("report")
file_handler = logging.FileHandler("report.log", "w", encoding='utf-8')
file_formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def log_spending_by_category(filename: str) -> Callable:
    """Логирует результат функции в указанный файл"""

    def decorator(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            result = func(*args, **kwargs)
            with open(filename, "w", encoding='utf-8') as f:
                json.dump(result, f, indent=4, ensure_ascii=False)
            return result

        return wrapper

    return decorator


@log_spending_by_category("spending_report.json")
def spending_by_category(transactions: pd.DataFrame, category: str, date: Optional[str] = None) -> str:
    """Функция возвращающая траты за последние 3 месяца по заданной категории в формате JSON"""
    logger.info("Начало работы")
    list_by_category = []
    final_list = []

    if date is None:
        logger.info("Вариант обработки с настоящей датой")
        date_start = datetime.datetime.now() - datetime.timedelta(days=90)
    else:
        logger.info("Вариант обработки с введенной датой")
        day, month, year = date.split(".")
        date_obj = datetime.datetime(int(year), int(month), int(day))
        date_start = date_obj - datetime.timedelta(days=90)

    logger.info("Формирование списка по категории")
    for i in transactions.to_dict("records"):
        if i["Категория"] == category:
            list_by_category.append(i)

    logger.info("Фильтрация на пропущенные даты")
    for i in list_by_category:
        if pd.isna(i["Дата платежа"]) or isinstance(i["Дата платежа"], float):
            continue

        # Преобразуем дату платежа в объект datetime
        day_, month_, year_ = map(int, i["Дата платежа"].split("."))
        date_obj_ = datetime.datetime(year_, month_, day_)

        if date_start <= date_obj_ <= date_start + datetime.timedelta(days=90):
            final_list.append({
                "Дата платежа": i["Дата платежа"],
                "Сумма платежа": i["Сумма платежа"],
                "Описание": i["Описание"],
                "Номер карты": i["Номер карты"]
            })

    logger.info("Формирование списка по тратам завершено")

    # Возврат результата в формате JSON
    return json.dumps(final_list, ensure_ascii=False)


# Пример использования функции
if __name__ == "__main__":
    # Пример DataFrame для тестирования
    data = {
        "Описание": ["Перевод на карту", "Оплата услуг", "Покупка в магазине"],
        "Категория": ["Переводы", "Коммунальные услуги", "Шопинг"],
        "Сумма платежа": [1000, 500, 1500],
        "Дата платежа": ["01.11.2021", "02.11.2021", "03.11.2021"],
        "Номер карты": ["1234-5678-9012-3456", "2345-6789-0123-4567", "3456-7890-1234-5678"]
    }

    df = pd.DataFrame(data)

    # Выполнение поиска по категории
    category_to_search = "Переводы"
    json_result = spending_by_category(df, category_to_search)

    print("Результат поиска по категории:", json_result)  # Вывод результата в формате JSON