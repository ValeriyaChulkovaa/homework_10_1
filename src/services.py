import json
import logging
import pandas as pd
from src.decorators import decorator_search

# Настройка логирования
logger = logging.getLogger("search_service")
file_handler = logging.FileHandler("search_service.log", "w", encoding='utf-8')
file_formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

@decorator_search
def simple_search(my_list: pd.DataFrame, string_search: str) -> str:
    """Функция поиска по переданной строке в описании и категории"""
    logger.info("Начало работы функции simple_search")
    result = []

    # Проверка на пустую строку
    if string_search == '':
        logger.warning("Поисковая строка пуста.")
        return json.dumps(result, ensure_ascii=False)

    for item in my_list.to_dict("records"):
        # Проверка на NaN с использованием pandas
        if pd.isna(item["Описание"]) or pd.isna(item["Категория"]):
            continue

        # Поиск строки в 'Описание' и 'Категория'
        if string_search.lower() in item["Описание"].lower() or string_search.lower() in item["Категория"].lower():
            result.append(item)

    logger.info(f"Завершение работы функции simple_search, найдено {len(result)} результатов.")
    return json.dumps(result, ensure_ascii=False)