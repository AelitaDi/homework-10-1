def filter_by_state(operation_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """ Function filter operations by state."""

    return [operation for operation in operation_list if operation["state"] == state]
