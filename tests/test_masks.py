from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number_base():
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"


def test_get_mask_card_number_no_number_1(no_number_1):
    assert get_mask_card_number(no_number_1) == ""


def test_get_mask_card_number_no_number_2(no_number_2):
    assert get_mask_card_number(no_number_2) == ""


def test_get_mask_card_number_no_number_3(no_number_3):
    assert get_mask_card_number(no_number_3) == ""


def test_get_mask_card_number_no_number_4(no_number_4):
    assert get_mask_card_number(no_number_4) == ""


def test_get_mask_account_base():
    assert get_mask_account("73654108430135874305") == "**4305"


def test_get_mask_account_no_number_1(no_number_1):
    assert get_mask_account(no_number_1) == ""


def test_get_mask_account_no_number_2(no_number_2):
    assert get_mask_account(no_number_2) == ""


def test_get_mask_account_no_number_3(no_number_3):
    assert get_mask_account(no_number_3) == ""


def test_get_mask_account_no_number_4(no_number_4):
    assert get_mask_account(no_number_4) == ""
