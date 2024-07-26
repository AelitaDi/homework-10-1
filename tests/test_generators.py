import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_base(transactions_):
    generator = filter_by_currency(transactions_, "USD")
    assert next(generator) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(generator) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }


def test_filter_by_currency_none():
    generator = filter_by_currency([], "USD")
    assert next(generator) == "Отсутствуют заданные параметры"


def test_filter_by_currency_none_1(transactions_):
    generator = filter_by_currency(transactions_, "EUR")
    assert next(generator) == "Отсутствуют заданные параметры"


@pytest.mark.parametrize(
    "input_data, expected",
    [
        (
            [
                {
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
                {
                    "description": "Перевод со счета на счет",
                    "from": "Счет 44812258784861134719",
                    "to": "Счет 74489636417521191160",
                },
                {
                    "description": "Перевод с карты на карту",
                    "from": "Visa Classic 6831982476737658",
                    "to": "Visa Platinum 8990922113665229",
                },
                {
                    "description": "Перевод организации",
                    "from": "Visa Platinum 1246377376343588",
                    "to": "Счет 14211924144426031657",
                },
            ],
            [
                "Перевод организации",
                "Перевод со счета на счет",
                "Перевод со счета на счет",
                "Перевод с карты на карту",
                "Перевод организации",
            ],
        ),
        (
            [
                {
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
                {
                    "description": "Перевод со счета на счет",
                    "from": "Счет 44812258784861134719",
                    "to": "Счет 74489636417521191160",
                },
                {
                    "description": "Перевод с карты на карту",
                    "from": "Visa Classic 6831982476737658",
                    "to": "Visa Platinum 8990922113665229",
                },
            ],
            [
                "Перевод организации",
                "Перевод со счета на счет",
                "Перевод со счета на счет",
                "Перевод с карты на карту",
            ],
        ),
    ],
)
def test_transaction_descriptions(input_data, expected):
    result = list(transaction_descriptions(input_data))
    assert result == expected


def test_transaction_descriptions_none():
    generator = transaction_descriptions([])
    assert next(generator) == "Пустой список"


@pytest.mark.parametrize(
    "start, end, expected",
    [
        (
            5,
            9,
            [
                "0000 0000 0000 0005",
                "0000 0000 0000 0006",
                "0000 0000 0000 0007",
                "0000 0000 0000 0008",
                "0000 0000 0000 0009",
            ],
        ),
        (
            123456,
            123459,
            ["0000 0000 0012 3456", "0000 0000 0012 3457", "0000 0000 0012 3458", "0000 0000 0012 3459"],
        ),
        (
            123459,
            123456,
            ["0000 0000 0012 3456", "0000 0000 0012 3457", "0000 0000 0012 3458", "0000 0000 0012 3459"],
        ),
    ],
)
def test_card_number_generator(start, end, expected):
    result = list(card_number_generator(start, end))
    assert result == expected


def test_card_number_generator_too_long():
    generator = card_number_generator(123456789123456789, 456)
    assert next(generator) == "Too long number"


def test_card_number_generator_equal():
    generator = card_number_generator(9, 9)
    assert next(generator) == "0000 0000 0000 0009"
