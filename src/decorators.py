import logging
import json
import pandas as pd
import datetime
from typing import Any, Callable, Optional

# Настройка логирования
logger = logging.getLogger("report")
file_handler = logging.FileHandler("report.log", "w")
file_formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def log_spending_by_category(filename: str) -> Callable:
    """Логирует результат функции в указанный файл"""

    def decorator(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            result = func(*args, **kwargs)
            with open(filename, "w") as f:
                json.dump(result, f, indent=4)
            return result

        return wrapper

    return decorator


@log_spending_by_category("spending_report.json")
def spending_by_category(transactions: pd.DataFrame, category: str, date: Optional[str] = None) -> list[Any]:
    """Функция возвращающая траты за последние 3 месяца по заданной категории"""
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
        # Проверка на NaN и float
        if pd.isna(i["Дата платежа"]) or isinstance(i["Дата платежа"], float):
            continue

        # Преобразуем дату платежа в объект datetime
        try:
            day_, month_, year_ = map(int, i["Дата платежа"].split("."))
            date_obj_ = datetime.datetime(year_, month_, day_)
        except ValueError as e:
            logger.error(f"Ошибка при преобразовании даты: {e}")
            continue

        if date_start <= date_obj_ <= date_start + datetime.timedelta(days=90):
            final_list.append(i["Сумма платежа"])

    logger.info("Формирование списка по тратам завершено")
    return final_list