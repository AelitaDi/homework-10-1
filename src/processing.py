def filter_by_state(operation_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Function filter operations by state."""

    operations: list = [operation for operation in operation_list if operation["state"] == state]
    return operations


def sort_by_date(operation_list: list[dict], sort_flag: bool = True) -> list[dict]:
    """Function sort operations by date."""

    date_list: list[str] = [operation.get("date") for operation in operation_list]
    for operation_date in date_list:
        new_date: list = operation_date[:10].split("-")
        if not "".join(new_date).isdigit() or len(new_date) != 3:
            print("Некорректный формат даты: ", new_date)
            return []
        elif 1900 > int(new_date[0]) or int(new_date[0]) > 2024 or int(new_date[1]) > 12 or int(new_date[2]) > 31:
            print("Некорректный формат даты: ", new_date)
            return []

    return sorted(operation_list, key=lambda date: date["date"], reverse=sort_flag)
