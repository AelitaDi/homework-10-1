import os

from src.generators import filter_by_currency
from src.import_data import get_data_from_csv, get_data_from_excel
from src.processing import filter_by_state, sort_by_date, filter_by_request
from src.utils import get_transactions_from_json
from src.widget import get_date, mask_account_card

PATH_TO_FILE_JSON = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")
PATH_TO_FILE_CSV = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions.csv")
PATH_TO_FILE_EXCEL = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions_excel.xlsx")


def main():
    """ Main function of the Project. """

    while True:
        menu_item = input('''Привет! Добро пожаловать в программу работы 
с банковскими транзакциями. 
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
''')
        if menu_item == '1':
            print('Для обработки выбран JSON-файл.')
            transactions = get_transactions_from_json(PATH_TO_FILE_JSON)
            break
        elif menu_item == '2':
            print('Для обработки выбран CSV-файл.')
            transactions = get_data_from_csv(PATH_TO_FILE_CSV)
            break
        elif menu_item == '3':
            print('Для обработки выбран XLSX-файл.')
            transactions = get_data_from_excel(PATH_TO_FILE_EXCEL)
            break
        else:
            print('Такого пункта в меню нет, попробуйте еще раз.')

    state_list = ['executed', 'canceled', 'pending']

    while True:
        state = input('''Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING.
''').lower()

        if state not in state_list:
            print(f'Статус операции "{state}" недоступен.')
        else:
            break

    filtered_transactions = filter_by_state(transactions, state)

    date_sort = input('Отсортировать операции по дате? Да/Нет. ').lower()
    if date_sort == 'да':
        if input('Отсортировать по возрастанию или по убыванию? ').lower() == 'по возрастанию':
            date_flag = False
        else:
            date_flag = True
        filtered_transactions = sort_by_date(filtered_transactions, date_flag)

    filter_by_rub = input('Выводить только рублевые транзакции? Да/Нет ')
    if filter_by_rub.lower() == 'да':
        rub_transactions = filter_by_currency(filtered_transactions, 'RUB')
        filtered_transactions = list(rub_transactions)[:-1]

    filter_by_word = input('Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет ')
    if filter_by_word.lower() == 'да':
        word = input('Введите слово: ')
        filtered_transactions = filter_by_request(filtered_transactions, word)

    print('Распечатываю итоговый список транзакций...')
    if len(filtered_transactions) == 0:
        print('Не найдено ни одной транзакции, подходящей под ваши условия фильтрации')
    else:
        print(f'Всего банковских операций в выборке: {len(filtered_transactions)}')
        for tr in filtered_transactions:
            tr_date = get_date(tr['date'])
            currency = tr['operationAmount']['currency']['name']
            if tr['description'] == 'Открытие вклада':
                from_to = mask_account_card(tr['to'])
            else:
                from_to = mask_account_card(tr['from']) + ' -> ' + mask_account_card(tr['to'])

            amount = tr['operationAmount']['amount']
            print(f'''{tr_date} {tr['description']}
{from_to}
Сумма: {round(float(amount))} {currency}
''')


if __name__ == "__main__":
    main()
