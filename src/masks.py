def get_mask_card_number(card_number: str) -> str:
    """Function masking card number."""

    if len(card_number) == 16 and card_number.isdigit():
        return card_number[0:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
    else:
        print("Некорректный номер карты")
        return ""


def get_mask_account(user_account: str) -> str:
    """Function masking user account."""

    if len(user_account) == 20 and user_account.isdigit():
        return "**" + user_account[-4:]
    else:
        print("Некорректный номер счета")
        return ""
