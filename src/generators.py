from typing import Generator


def filter_by_currency(transactions: list[dict], currency: str) -> Generator:
    """Function filter operations by currency."""

    for trans in transactions:
        if trans["operationAmount"]["currency"]["name"] == currency:
            yield trans


def transaction_descriptions(transactions: list[dict]) -> Generator:
    """Function return description of transaction."""

    for trans in transactions:
        yield trans["description"]


def card_number_generator(start: int, end: int) -> Generator:
    """Function generate card numbers."""

    card_number = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
    if start > end:
        start, end = end, start
    for j in range(start, end + 1):
        for i in range(1, len(str(j)) + 1):
            card_number[-i] = str(j)[-i]
        card_number_str = "".join(card_number)
        yield str(
            card_number_str[0:4]
            + " "
            + card_number_str[4:8]
            + " "
            + card_number_str[8:12]
            + " "
            + card_number_str[12:]
        )
