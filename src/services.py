from src.decorators import decorator_search


@decorator_search
def simple_search(my_list: list, string_search: str) -> list:
    """Функция поиска по переданной строке"""
    result = []
    for i in my_list:
        if string_search == '':
            return result
        elif (
                i["Описание"] == "nan"
                or type(i["Описание"]) is float
                or i["Категория"] == "nan"
                or type(i["Категория"]) is float
        ):
            continue
        elif string_search in i["Описание"] or string_search in i["Категория"]:
            result.append(i)

    return result
