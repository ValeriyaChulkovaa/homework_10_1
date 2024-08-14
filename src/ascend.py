import csv
from pathlib import Path


def reader_csv_file(file: Path) -> list:
    """
    Функция, считывающая информацию из csv файла
    """
    with open(file, encoding='utf-8') as f:
        csv.DictReader(f, delimiter=";")
        reader = csv.DictReader(f, delimiter=";")
        return list(reader)
