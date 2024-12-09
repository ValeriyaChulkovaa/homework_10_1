import json
import logging
import pandas as pd

# Настройка логирования
logger = logging.getLogger("search_module")
file_handler = logging.FileHandler("search_module.log", "w", encoding='utf-8')
file_formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def simple_search(my_list: pd.DataFrame, string_search: str) -> str:
    """Функция поиска по переданной строке в описании и категории"""
    logger.info("Начало работы функции simple_search")

    result = []

    # Проверка на пустую строку
    if string_search == '':
        logger.warning("Поисковая строка пуста.")
        return json.dumps(result, ensure_ascii=False)

    # Поиск по описанию и категории
    for item in my_list.to_dict("records"):
        if pd.isna(item['Описание']) or pd.isna(item['Категория']):
            continue

        if string_search.lower() in item['Описание'].lower() or string_search.lower() in item['Категория'].lower():
            result.append(item)

    logger.info(f"Завершение работы функции simple_search, найдено {len(result)} результатов.")

    return json.dumps(result, ensure_ascii=False)


def search_by_phone(my_list: pd.DataFrame, phone_number: str) -> str:
    """Функция поиска по телефонным номерам"""
    logger.info("Начало работы функции search_by_phone")

    result = [item for item in my_list.to_dict("records") if item.get("Номер телефона") == phone_number]

    logger.info(f"Завершение работы функции search_by_phone, найдено {len(result)} результатов.")

    return json.dumps(result, ensure_ascii=False)


# Пример использования функций
if __name__ == "__main__":
    # Пример DataFrame для тестирования
    data = {
        "Описание": ["Перевод на карту", "Оплата услуг", "Покупка в магазине"],
        "Категория": ["Переводы", "Коммунальные услуги", "Шопинг"],
        "Сумма платежа": [1000, 500, 1500],
        "Дата платежа": ["01.11.2021", "02.11.2021", "03.11.2021"],
        "Номер карты": ["1234-5678-9012-3456", "2345-6789-0123-4567", "3456-7890-1234-5678"],
        "Номер телефона": ["+1234567890", "+0987654321", "+1234567890"]
    }

    df = pd.DataFrame(data)

    # Выполнение поиска по строке
    search_string = "перевод"
    json_result_search = simple_search(df, search_string)
    print("Результат поиска по строке:", json_result_search)  # Вывод результата в формате JSON

    # Выполнение поиска по номеру телефона
    phone_number = "+1234567890"
    json_result_phone = search_by_phone(df, phone_number)
    print("Результат поиска по номеру телефона:", json_result_phone)  # Вывод результата в формате JSON