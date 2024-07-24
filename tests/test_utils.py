import os

from src.utils import get_transaction_amount, get_transactions_from_json

PATH_1 = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations_.json")
PATH_2 = "test_operations_.json"


def test_get_transactions_from_json_empty_file():
    assert get_transactions_from_json("") == []
    assert get_transactions_from_json(PATH_1) == []
    assert get_transactions_from_json(PATH_2) == []


def test_get_transaction_amount(transaction_1, transaction_2):
    assert get_transaction_amount(transaction_1) == 31957.58
    assert get_transaction_amount(transaction_2) == 0.0
