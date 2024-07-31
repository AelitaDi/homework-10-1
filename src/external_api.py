import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
headers = {"apikey": API_KEY}


def get_currency_conversion_to_rubles(currency: str, amount: float) -> float:
    """Get currency conversion to rubles."""

    response = requests.get(
        f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}", headers=headers
    )
    # print(response.status_code)
    amount_rub = response.json()["result"]
    return amount_rub
