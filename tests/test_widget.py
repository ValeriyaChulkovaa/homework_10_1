from src.masks import mask_account_card
import pytest


def test_get_data(data_today):
    assert test_get_data(data_today) == ['2018-07-11T02:26:18.671407']


@pytest.mark.parametrize("x",
                         ['Visa Platinum 8990922113665229', 'Счет 73654108430135874305', 'Maestro 1596837868705199', '']
                         )
def test_get_mask_card(x):
    number_card = str(x)
    if 'Visa Platinum' in str(number_card):
        return (f"{number_card[:4]} {number_card[5:13]} "
                f"{number_card[14:18]} {number_card[18:20]}** **** {number_card[26:]}")
    elif 'Счет' in str(number_card) or 'Счёт' in str(number_card):
        return f"{number_card[:4]} **{number_card[21:]}"
    elif 'Maestro' in str(number_card):
        return (f"{number_card[:7]} {number_card[8:12]} "
                f"{number_card[12:14]}** **** {number_card[20:]}")


assert test_get_mask_card('Visa Platinum 8990922113665229') == "8990 92** **** 5229"
assert test_get_mask_card('Счет 73654108430135874305') == "7365 41** **** 4305"
assert test_get_mask_card('Maestro 1596837868705199') == "1596 83** **** 5199"
