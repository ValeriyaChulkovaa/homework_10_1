from typing import Any


def mask_account_card(number_card: str) -> Any:
    """Реализация функций, которые возвращают маскированные номера карт и счетов"""
    if 'Maestro' in str(number_card):
        return f"{number_card[:7]} {number_card[8:12]} {number_card[12:14]}** **** {number_card[20:]}"
    elif 'MasterCard' in str(number_card):
        return f"{number_card[:10]} {number_card[11:15]} {number_card[15:17]}** **** {number_card[23:]}"
    elif 'Visa Classic' in str(number_card):
        return f"{number_card[:4]} {number_card[5:12]} {number_card[13:17]} {number_card[17:19]}** **** {number_card[25:]}"
    elif 'Visa Platinum' in str(number_card):
        return f"{number_card[:4]} {number_card[5:13]} {number_card[14:18]} {number_card[18:20]}** **** {number_card[26:]}"
    elif 'Visa Gold' in str(number_card):
        return f"{number_card[:4]} {number_card[5:9]} {number_card[10:14]} {number_card[14:16]}** **** {number_card[22:]}"
    elif 'Счет' in str(number_card) or 'Счёт' in str(number_card):
        return f"{number_card[:4]} **{number_card[21:]}"
    else:
        return None


print(mask_account_card('Maestro 1596837868705199'))
print(mask_account_card('MasterCard 7158300734726758'))
print(mask_account_card('Visa Classic 6831982476737658'))
print(mask_account_card('Visa Platinum 8990922113665229'))
print(mask_account_card('Visa Gold 5999414228426353'))
print(mask_account_card('Счет 64686473678894779589'))
print(mask_account_card('Счёт 64686473678894779589'))

