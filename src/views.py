from datetime import datetime, timedelta
import pandas as pd


def filter_by_date(date: str, my_list: list) -> list:
    """Функция фильтрующая данные по заданной дате"""
    list_by_date = []

    if date == "":
        return list_by_date

    # Преобразование строки даты в объект datetime
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d")  # Ожидаем формат YYYY-MM-DD
    except ValueError as e:
        print(f"Ошибка формата даты: {e}")
        return list_by_date

    for item in my_list:
        # Проверка на NaN с использованием pandas
        if pd.isna(item["Дата платежа"]) or isinstance(item["Дата платежа"], float):
            continue

        # Преобразование даты из строки в объект datetime
        try:
            payment_date = datetime.strptime(str(item["Дата платежа"]), "%d.%m.%Y")
        except ValueError as e:
            print(f"Ошибка преобразования даты платежа: {e}")
            continue

        # Проверка, попадает ли дата в диапазон
        if date_obj >= payment_date >= (date_obj - timedelta(days=date_obj.day - 1)):
            list_by_date.append(item)

    return list_by_date