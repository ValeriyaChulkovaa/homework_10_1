import pytest
from src.decorators import my_function, log


def test_log_good():
    @log(filename="mylog.txt")
    def my_function(x, y):
        return x + y

    result = my_function(1, 2)
    assert result == 3


def test_log_exception():
    with pytest.raises(Exception):
        my_function()
        