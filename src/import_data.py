import csv

import pandas as pd


def get_data_from_csv(csv_path: str) -> list[dict]:
    """Function get data from csv file."""

    transaction_list = []
    with open(csv_path, encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file, delimiter=";")
        for row in reader:
            transaction_list.append(row)

    return transaction_list


def get_data_from_excel(excel_path: str) -> list[dict]:
    """Function get data from excel file."""

    transaction_list = []
    excel_data = pd.read_excel(excel_path)
    len_, b = excel_data.shape
    for i in range(len_ - 1):
        if excel_data["id"][i]:
            transaction_list.append(
                {
                    "id": str(excel_data["id"][i]),
                    "state": excel_data["state"][i],
                    "date": excel_data["date"][i],
                    "amount": float(excel_data["amount"][i]),
                    "currency_name": excel_data["currency_name"][i],
                    "currency_code": excel_data["currency_code"][i],
                    "from": excel_data["from"][i],
                    "to": excel_data["to"][i],
                    "description": excel_data["description"][i],
                }
            )
        else:
            continue

    print(transaction_list[-5:])
    return transaction_list


if __name__ == '__main__':
    get_data_from_excel('data/transactions_excel.xlsx')
