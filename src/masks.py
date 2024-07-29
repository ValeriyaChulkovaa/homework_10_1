import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/masks.log")
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s", "%d.%m.%Y %H:%M:%S"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_info: list) -> str:
    """
    Функция принимает на вход информацию о карте и возвращает зашифрованную информацию
    """
    # Шифруем номер карты
    logger.info(f"Карта {" ".join(card_info)} передана для зашифрованния")
    card_info[-1] = f"{card_info[-1][:6]}******{card_info[-1][-4:]}"

    # Оборачиваем номер карты в список для перебора и вставки пробелов
    list_card_number = list(card_info[-1])
    counter = 0
    for index in range(1, len(list_card_number)):
        if index % 4 == 0:
            list_card_number.insert(index + counter, " ")
            counter += 1
    # Заменяем исходную строку с номером карты на зашифрованную с пробелами
    else:
        card_info[-1] = "".join(list_card_number)
        logger.info(f"Зашифрованная карта {" ".join(card_info)}")

    return " ".join(card_info)


def get_mask_account(account: list) -> str:
    """
    Функция принимает на вход информацию о счете и возвращает зашифрованную информацию
    """
    logger.info(f"{" ".join(account)} передан для шифровки номера")
    account[-1] = f"**{account[-1][-2:]}"
    logger.info(f"Зашифрованный {" ".join(account)}")

    return " ".join(account)
