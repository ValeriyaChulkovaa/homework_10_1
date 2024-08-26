from src.decorators import decorator_search


@decorator_search
def simple_search(my_list: list, string_search: str) -> list:
    """Функция поиска по переданной строке"""
    result = [

    ]
    for i in my_list:
        if i['Описание'] == "nan" or type(i['Описание']) == float or i['Категория'] == "nan" or type(
                i['Категория']) == float:
            continue
        elif string_search in i['Описание'] or string_search in i['Категория']:
            result.append(i)
    return result
