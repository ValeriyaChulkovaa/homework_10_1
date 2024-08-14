import json
import logging
from pathlib import Path
from typing import Any

from src.config import utils_log

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(utils_log, "w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_info(file_json: Path) -> Any:
    """
    Функция, которая принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях.

    """

    with open(file_json, encoding="utf-8") as f:
        try:
            logger.info("Открываем файл для просмотра содержимого")
            trans = json.load(f)
            return trans

        except Exception as ex:
            logger.error(f"Произошла ошибка: {ex}")
            return []
