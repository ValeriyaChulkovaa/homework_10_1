from functools import wraps
from typing import Any, Callable


def log(filename: Any = None) -> Callable:
    """Декоратор который логирует результат вызова функции в консоль если аргумент не задан или в файл.
    Пример: @log() -> без аргумента, вывод будет в консоль.
    Пример: @log(filename='test_log.txt') -> аргумент передан, вывод будет записан в файл test_log.txt
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: list, **kwargs: dict) -> Any:
            try:
                result = func(*args, **kwargs)
                message_log = "my_function ok \n"
            except Exception as e:
                result = None
                message_log = f"my_function error: {e}. Inputs: {args}, {kwargs} \n"
            if filename:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(message_log)
            else:
                print(message_log)

            return result

        return wrapper

    return decorator
