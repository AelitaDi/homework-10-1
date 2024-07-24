import json
import os

from src.external_api import get_currency_conversion_to_rubles

PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")


def get_transactions_from_json(path_to_file: str) -> list[dict]:
    """Function get transactions from JSON file."""

    try:
        with open(path_to_file, encoding="utf-8") as file:
            data = json.load(file)
        return data
    except Exception:
        return []


def get_transaction_amount(transaction: dict) -> float:
    """Function get amount of transaction in Rubles."""

    try:
        if transaction["operationAmount"]["currency"]["code"] != "RUB":
            return get_currency_conversion_to_rubles(
                transaction["operationAmount"]["currency"]["code"], transaction["operationAmount"]["amount"]
            )
        else:
            return transaction["operationAmount"]["amount"]
    except Exception:
        print("Error operationAmount")
        return 0.0


# if __name__ == "__main__":
#     trans = get_transactions_from_json(PATH_TO_FILE)
#     for tr in trans:
#         print(get_transaction_amount(tr))
