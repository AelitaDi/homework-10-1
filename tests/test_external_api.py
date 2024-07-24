import os
from unittest.mock import patch

from dotenv import load_dotenv

from src.external_api import get_currency_conversion_to_rubles

load_dotenv()

API_KEY = os.getenv("API_KEY")
headers = {"apikey": API_KEY}


@patch("requests.get")
def test_get_currency_conversion_to_rubles(mock_get):
    mock_get.return_value.json.return_value = {"result": 25.5}
    assert get_currency_conversion_to_rubles("EUR", 3) == 25.5
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount=3", headers=headers
    )
