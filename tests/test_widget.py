import pytest

from src.widget import get_data, mask_account_card


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
    ],
)
def test_mask_account_card_base(input_data, expected):
    assert mask_account_card(input_data) == expected


def test_mask_account_card_no_card_info(no_number_5):
    assert mask_account_card(no_number_5) == ""


def test_mask_account_card_no_number():
    assert mask_account_card("Visa 12345") == ""
    assert mask_account_card("Счет 12345") == ""


def test_get_data_base():
    assert get_data("2024-03-11T02:26:18.671407") == "11.03.2024"


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("20240311T02:26:18.671407", ""),
        ("1024-03-11T02:26:18.671407", ""),
        ("2024-34-88T02:26:18.671407", ""),
        ("abcd-03-11T02:26:18.671407", ""),
    ],
)
def test_get_data_incorrect(input_data, expected):
    assert get_data(input_data) == expected
