from widget import mask_account_card, get_data  # type: ignore


if __name__ == "__main__":
    client_data: str = input("Введите данные клиента: ")
    print(mask_account_card(client_data))

    input_date: str = input("Введите дату: ")
    print(get_data(input_date))
