from masks import get_mask_card_number, get_mask_account  # type: ignore


def mask_account_card(input_data: str) -> str:
    """ " Функция общей маскировки счета"""

    cards: list = ["visa", "maestro", "mastercard"]
    data_list: list = input_data.split(" ")
    if data_list[0].lower() in cards:
        return str(" ".join(data_list[:-1]) + " " + get_mask_card_number(data_list[-1]))
    else:
        return str(" ".join(data_list[:-1]) + " " + get_mask_account(data_list[-1]))


def get_data(unfiltered_date: str) -> str:
    """ " Функция возвращает отформатированную дату"""

    new_date: list = unfiltered_date[:10].split("-")
    return ".".join(new_date[::-1])
