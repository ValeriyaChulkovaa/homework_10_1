from typing import Any

from src.decorators import log


def test_log_terminal_ok(capsys: Any) -> None:
    @log()
    def example(x: list) -> Any:
        return x[0]

    example([1])
    capture = capsys.readouterr()
    assert capture.out == "my_function ok \n\n"


def test_log_terminal_error(capsys: Any) -> None:
    @log()
    def example_2(x: list) -> Any:
        return x[0]

    example_2(0)
    capture = capsys.readouterr()
    assert capture.out == "my_function error: 'int' object is not subscriptable. Inputs: (0,), {} \n\n"
