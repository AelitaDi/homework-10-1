from typing import List
from collections import Counter
import re


def filter_by_state(operation_list: list[dict], state: str) -> list[dict]:
    """Function filter operations by state."""

    operations: list = [operation for operation in operation_list if operation.get('state') == state.upper()]
    return operations


def sort_by_date(operation_list: list[dict], sort_flag: bool = True) -> list[dict]:
    """Function sort operations by date."""

    date_list: List[str] = [operation.get("date") for operation in operation_list]
    for operation_date in date_list:
        new_date: list = operation_date[:10].split("-")
        if not "".join(new_date).isdigit() or len(new_date) != 3:
            print("Некорректный формат даты: ", new_date)
            return []
        elif 1900 > int(new_date[0]) or int(new_date[0]) > 2024 or int(new_date[1]) > 12 or int(new_date[2]) > 31:
            print("Некорректный формат даты: ", new_date)
            return []

    return sorted(operation_list, key=lambda date: date["date"], reverse=sort_flag)


def filter_by_request(transaction_list: list[dict], user_request: str) -> list[dict]:
    """Function filter transactions by user request. """

    target_list = []
    lower_user_request = user_request.lower()
    for transaction in transaction_list:
        if re.search(lower_user_request, transaction.get('description', ''), flags=re.IGNORECASE):
            target_list.append(transaction)
        else:
            continue
    print(target_list)
    return target_list


def count_transaction_categories(transactions: list[dict]) -> dict:
    """Function count transactions by type of category. """

    categories = []
    for transaction in transactions:
        categories.append(transaction['description'])
    counted = dict(Counter(categories))
    print(counted)
    return counted


if __name__ == "__main__":
    filter_by_request([
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ], 'счет')
