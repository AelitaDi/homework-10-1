from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(input_data: str) -> str:
    """Base masking function."""

    # cards: list = ["visa", "maestro", "mastercard"]
    data_list: list = input_data.split(" ")
    # if data_list[0].lower() in cards and get_mask_card_number(data_list[-1]) != "":
    if len(data_list[-1]) == 16:
        return str(" ".join(data_list[:-1]) + " " + get_mask_card_number(data_list[-1]))
    # elif data_list[0].lower() == "счет" and get_mask_account(data_list[-1]) != "":
    elif len(data_list[-1]) == 20:
        return str(" ".join(data_list[:-1]) + " " + get_mask_account(data_list[-1]))
    else:
        # print("Некорректные данные")
        return ""


def get_date(unfiltered_date: str) -> str:
    """Data filtered function."""

    new_date: list = unfiltered_date[:10].split("-")
    if not "".join(new_date).isdigit() or len(new_date) != 3:
        print("Некорректный формат даты")
        return ""
    elif 1900 > int(new_date[0]) or int(new_date[0]) > 2024 or int(new_date[1]) > 12 or int(new_date[2]) > 31:
        print("Некорректный формат даты")
        return ""
    else:
        return ".".join(new_date[::-1])
