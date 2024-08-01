from unittest.mock import patch
from src.import_data import get_data_from_csv, get_data_from_excel

@patch('src.import_data.get_data_from_excel')
def test_get_data_from_excel(mock_get):
    mock_get.return_value = [{
                    "id": "7897654.0",
                    "state": "EXECUTED",
                    "date": "2020-10-06T23:30:05Z",
                    "amount": '13642.0',
                    "currency_name": 'Somoni',
                    "currency_code": 'TJS',
                    "from": "Discover 3233958335206913",
                    "to": "American Express 0522499169905654",
                    "description": "Открытие вклада",
                }]
    assert get_data_from_excel('..data/transactions_excel.xlsx') == [{
                    "id": "7897654.0",
                    "state": "EXECUTED",
                    "date": "2020-10-06T23:30:05Z",
                    "amount": '13642.0',
                    "currency_name": 'Somoni',
                    "currency_code": 'TJS',
                    "from": "Discover 3233958335206913",
                    "to": "American Express 0522499169905654",
                    "description": "Открытие вклада",
                }]
