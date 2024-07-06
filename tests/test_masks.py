import pytest


@pytest.mark.parametrize("x", [7000792289606361, 8000522289606361, 700792289606361, ()])
def test_get_mask_card_number(x):
    card_number_str = str(x)
    return f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"


assert test_get_mask_card_number(7000792289606361) == "7000 79** **** 6361"
assert test_get_mask_card_number(8000522289606361) == "8000 79** **** 6361"
assert test_get_mask_card_number(700792289606361) == "7007 79** **** 6361"


@pytest.mark.parametrize("x", [73654108430135874305, 773654108430135874305, 3373654108430135874305, ()])
def test_get_mask_account(x):
    account_number_str = str(x)
    return f"**{account_number_str[-4:]}"


assert test_get_mask_account(73654108430135874305) == "**4305"
assert test_get_mask_account(773654108430135874305) == "**4305"
assert test_get_mask_account(3373654108430135874305) == "**4305"
