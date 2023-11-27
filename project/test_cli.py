import re
from unittest.mock import patch
from cli import log


@patch('builtins.print')
def test_log_decorator_without_args(mock_print):
    @log
    def test_function():
        return "test"

    test_function()

    # Проверяем, что print был вызван
    # с сообщением соответствующего формата
    args, _ = mock_print.call_args

    assert re.match(r"test_function - [1-5]с", args[0]), "Неправильный вывод!"


@patch('builtins.print')
def test_log_decorator_with_args(mock_print):
    @log("Привет, как дела: {}с")
    def test_function():
        return "test"

    test_function()

    # Проверяем, что print был вызван
    # с сообщением соответствующего формата
    args, _ = mock_print.call_args
    assert re.match(
        r"Привет, как дела: [1-5]с",
        args[0]
    ), "Неправильный вывод!"
