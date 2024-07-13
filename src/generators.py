from typing import Generator, Union


def filter_by_currency(transactions: list[dict], currency: str) -> Union[Generator, str]:
    """Function filter operations by currency."""

    if not transactions:
        yield "Отсутствуют заданные параметры"
    for trans in transactions:
        if trans["operationAmount"]["currency"]["code"] == currency:
            yield trans
    yield "Отсутствуют заданные параметры"


def transaction_descriptions(transactions: list[dict]) -> Union[Generator, str]:
    """Function return description of transaction."""

    if not transactions:
        yield "Пустой список"

    for trans in transactions:
        yield trans["description"]


def card_number_generator(start: int, stop: int) -> Union[Generator, str]:
    """Function generate card numbers."""

    card_number = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]

    if len(str(start)) > 16 or len(str(stop)) > 16:
        yield "Too long number"
    if start > stop:
        start, stop = stop, start
    for j in range(start, stop + 1):
        for i in range(1, len(str(j)) + 1):
            card_number[-i] = str(j)[-i]
        card_number_str = "".join(card_number)
        yield " ".join([card_number_str[x : x + 4] for x in range(0, len(card_number_str), 4)])
