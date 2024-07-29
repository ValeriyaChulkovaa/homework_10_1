import pytest

from src.widget import get_data, mask_account_card


def test_mask_card_visa_platinum(visa_platinum_card: str, mask_visa_platinum_card: str) -> None:
    assert mask_account_card(visa_platinum_card) == mask_visa_platinum_card


def test_mask_card_maestro(maestro_card: str, mask_maestro_card: str) -> None:
    assert mask_account_card(maestro_card) == mask_maestro_card


def test_mask_card_master(master_card: str, mask_master_card: str) -> None:
    assert mask_account_card(master_card) == mask_master_card


def test_mask_card_visa_classic(visa_classic_card: str, mask_visa_classic_card: str) -> None:
    assert mask_account_card(visa_classic_card) == mask_visa_classic_card


def test_mask_account(account_num: str, mask_account_num: str) -> None:
    assert mask_account_card(account_num) == mask_account_num


@pytest.mark.parametrize(
    "card, mask_card",
    [
        ("Visa Classic 6831 9824 7673 7658", "Visa Classic 6831 98** **** 7658"),
        ("MasterCard 7158 3007 3472 6758", "MasterCard 7158 30** **** 6758"),
        ("Maestro 1596 8378 6870 5199", "Maestro 1596 83** **** 5199"),
        ("Visa Platinum 7000 7922 8960 6361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 35383033474447895560", "Счет **5560"),
    ],
)
def test_mask_cards(card: str, mask_card: str) -> None:
    assert mask_account_card(card) == mask_card


@pytest.mark.parametrize("coded_date, decoded_date", [("2018-07-11T02:26:18.671407", "11.07.2018")])
def test_get_data(coded_date: str, decoded_date: str) -> None:
    assert get_data(coded_date) == decoded_date
