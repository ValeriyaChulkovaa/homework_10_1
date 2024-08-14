from src.masks import get_mask_account


def test_get_mask_account_number_for_card(number_for_file_masks):
    assert get_mask_account('3234123412341234') == number_for_file_masks


def test_get_mask_account_for_account(number_for_account_for_file_masks):
    assert get_mask_account("53125674431399887757") == number_for_account_for_file_masks


def test_get_mask_account_letter(letter_for_file_masks):
    assert get_mask_account("fdgswe4252312653467547") == letter_for_file_masks
    