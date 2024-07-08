import pytest

from src.masks import mask_account_card


@pytest.mark.parametrize("cards", ['Visa Platinum 7000 7922 8960 6361'])
def test_mask_account_card(cards):
    assert mask_account_card(cards)
