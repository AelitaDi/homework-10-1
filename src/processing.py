import re
from collections import Counter
from typing import List


def filter_by_state(operation_list: list[dict], state: str) -> list[dict]:
    """Function filter operations by state."""

    operations: list = [operation for operation in operation_list if operation.get("state") == state.upper()]
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
    """Function filter transactions by user request."""

    target_list = []
    lower_user_request = user_request.lower()
    for transaction in transaction_list:
        if re.search(lower_user_request, transaction.get("description", ""), flags=re.IGNORECASE):
            target_list.append(transaction)
        else:
            continue
    print(target_list)
    return target_list


def count_transaction_categories(transactions: list[dict]) -> dict:
    """Function count transactions by type of category."""

    categories = []
    for transaction in transactions:
        categories.append(transaction["description"])
    counted = dict(Counter(categories))
    print(counted)
    return counted
