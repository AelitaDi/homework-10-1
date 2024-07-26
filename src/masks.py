import logging
import os


logging.basicConfig(
    filename=os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs", "masks.log"),
    filemode='w',
    format='%(asctime)s: %(name)s: %(levelname)s: %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)


def get_mask_card_number(card_number: str) -> str:
    """ Function masking card number."""

    logger.info(f'Запуск функции {get_mask_card_number.__name__}.')

    if len(card_number) == 16 and card_number.isdigit():
        logger.info(f'Успешное завершении работы функции {get_mask_card_number.__name__}.')
        return card_number[0:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
    else:
        logger.error('Ошибка. Некорректный номер карты.')
        return ""


def get_mask_account(user_account: str) -> str:
    """ Function masking user account."""

    logger.info(f'Запуск функции {get_mask_account.__name__}.')

    if len(user_account) == 20 and user_account.isdigit():
        logger.info(f'Успешное завершение работы функции {get_mask_account.__name__}.')
        return "**" + user_account[-4:]
    else:
        logger.error(f'Ошибка. Некорректный номер счета.')
        return ""
