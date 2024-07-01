def get_mask_card_number(card_number: str) -> str:
    """ Function masking client card number."""

    return card_number[0:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]


def get_mask_account(user_account: str) -> str:
    """ Function masking user account."""

    return "**" + user_account[-4:]
