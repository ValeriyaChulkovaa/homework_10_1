import pandas as pd
from typing import List, Dict


def read_excel(path_file: str) -> List[Dict[str, Any]]:
    """Функция читает .xlsx файл и возвращает список словарей"""
    try:
        df = pd.read_excel(path_file)
    except FileNotFoundError:
        print(f"Ошибка: Файл '{path_file}' не найден.")
        return []
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return []

    # Проверка наличия необходимых столбцов
    required_columns = [
        "Дата платежа", "Статус", "Сумма платежа",
        "Валюта платежа", "Категория", "Описание", "Номер карты"
    ]

    for column in required_columns:
        if column not in df.columns:
            print(f"Ошибка: Столбец '{column}' отсутствует в файле.")
            return []

    result = df.apply(
        lambda row: {
            "Дата платежа": row["Дата платежа"],
            "Статус": row["Статус"],
            "Сумма платежа": row["Сумма платежа"],
            "Валюта платежа": row["Валюта платежа"],
            "Категория": row["Категория"],
            "Описание": row["Описание"],
            "Номер карты": row["Номер карты"],
        },
        axis=1,
    ).tolist()

    return result