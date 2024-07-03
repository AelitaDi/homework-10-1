def filter_by_state(operation_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """ Function filter operations by state."""

    return [operation for operation in operation_list if operation["state"] == state]


def sort_by_date(operation_list: list[dict], sort_flag: bool = True) -> list[dict]:
    """ Function sort operations by date."""

    return sorted(operation_list, key=lambda date: date["date"], reverse=sort_flag)
