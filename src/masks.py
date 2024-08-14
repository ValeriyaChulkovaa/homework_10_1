import logging
from typing import Any

from src.config import masks_log

logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(masks_log, "w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_account(number: str) -> Any:
    """Функция, маскирующая номер счета или карты"""
    try:
        logger.info("Проверяем корректность полученных данных и маскируем их")
        if str(number).isdigit() and len(number) == 16:
            return f"{number[:4]} {number[4:6]}** **** {number[12:]}"
        elif str(number).isdigit() and len(number) == 20:
            return f"**{number[-4::]}"
        else:
            logger.info("Выводим сообщение, что данные некорректны")
            return "Введены некорректные данные"
    except Exception as ex:
        logger.error(f"Произошла ошибка: {ex}")
