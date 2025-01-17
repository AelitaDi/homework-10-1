# from time import time


def log(filename):
    """Decorator create log about function operation."""

    def my_decorator(func):
        def wrapper(*args, **kwargs):
            try:
                # time_1 = time()
                result = func(*args, **kwargs)
                # time_2 = time()
                if filename:
                    with open(filename, "w") as file:
                        file.write(f"{func.__name__} ok")
                else:
                    print(f"{func.__name__} ok")
                return result
            except Exception as e:
                if filename:
                    with open(filename, "w") as file:
                        file.write(f"{func.__name__} error: {e.__class__.__name__}. Inputs: {args}, {kwargs}")
                else:
                    print(f"{func.__name__} error: {e.__class__.__name__}. Inputs: {args}, {kwargs}")

        return wrapper

    return my_decorator
