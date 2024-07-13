# import pytest

from src.decorators import log


@log(filename="")
def example_func(a, b):
    """Test function with Exception."""
    raise ValueError("Something went wrong!")


@log(filename="")
def example_func_1(a, b):
    """Test function ok"""
    return a + b


def test_log_decorator(capsys):
    example_func(2, 5)
    captured = capsys.readouterr()
    assert captured.out == "example_func error: ValueError. Inputs: (2, 5), {}\n"


def test_log_decorator_output(capsys):
    example_func_1(2, 5)
    captured = capsys.readouterr()
    assert captured.out == "example_func_1 ok\n"
