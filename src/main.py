from masks import get_mask_account, get_mask_card_number  # type: ignore


if __name__ == "__main__":
    client_card_number: str = input("Введите номер карты без пробелов: ")
    print(get_mask_card_number(client_card_number))

    client_account: str = input("Введите номер лицевого счета без пробелов: ")
    print(get_mask_account(client_account))
