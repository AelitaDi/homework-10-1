import json
import logging
import os

from src.external_api import get_currency_conversion_to_rubles

logging.basicConfig(
    filename=os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs", "utils.log"),
    filemode="w",
    format="%(asctime)s: %(name)s: %(levelname)s: %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)

PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")


def get_transactions_from_json(path_to_file: str) -> list[dict]:
    """Function get transactions from JSON file."""

    logger.info(f"Запуск функции {get_transactions_from_json.__name__}.")
    try:
        with open(path_to_file, encoding="utf-8") as file:
            data = json.load(file)
        logger.info(f"Успешное завершение работы функции {get_transactions_from_json.__name__}")
        return data
    except Exception as e:
        logger.error(f"Ошибка. {e}.")
        return []


def get_transaction_amount(transaction: dict) -> float:
    """Function get amount of transaction in Rubles."""

    logger.info(f"Запуск функции {get_transaction_amount.__name__}.")
    try:
        if transaction["operationAmount"]["currency"]["code"] != "RUB":
            logger.info(
                f"Успешное завершение работы функции {get_transaction_amount.__name__}, "
                f"обращение к функции {get_currency_conversion_to_rubles.__name__}."
            )
            return get_currency_conversion_to_rubles(
                transaction["operationAmount"]["currency"]["code"], float(transaction["operationAmount"]["amount"])
            )
        else:
            logger.info(f"Успешное завершение работы функции {get_transaction_amount.__name__}.")
            return float(transaction["operationAmount"]["amount"])
    except Exception as e:
        logger.error(f"Ошибка. {e}.")
        return 0.0
