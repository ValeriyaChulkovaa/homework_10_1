def mask_account_card(text: str) -> str:
    """Функция принимает строку с информацией — тип карты/счета и номер карты/счета
    Возвращать исходную строку с замаскированным номером карты/счета."""
    info_card_str = text.split()
    name_cards = []
    card_number = []
    for el in info_card_str:
        if el.isalpha():
            name_cards.append(el)

    for el in info_card_str:
        if el.isdigit():
            card_number.append(el)

    card_number_new = ""

    if name_cards[0] in ["Visa", "Maestro", "MasterCard"]:
        if len(name_cards) >= 2 and name_cards[1] in ["Platinum", "Classic"]:
            for el in card_number:
                card_number_new += el
            mask_card_num = f"{card_number_new[:4]} {card_number_new[4:6]}** **** {card_number_new[-4:]}"
            return f"{name_cards[0]} {name_cards[1]} {mask_card_num}"
        else:
            for el in card_number:
                card_number_new += el
            mask_card_num = f"{card_number_new[:4]} {card_number_new[4:6]}** **** {card_number_new[-4:]}"
            return f"{name_cards[0]} {mask_card_num}"
    elif name_cards[0] in ["Счет"]:
        account_num = ""
        for el in card_number:
            account_num += el
        mask_account = f"**{account_num[-4:]}"
        return name_cards[0] + " " + mask_account
    return ""


def get_data(text: str) -> str:
    """Функция прнимает зашифрованню строку(2018-07-11T02:26:18.671407) и возвращает дату"""
    new_string = text.split("-")
    data_string = new_string[2][0:2] + "." + new_string[1] + "." + new_string[0]
    return data_string
