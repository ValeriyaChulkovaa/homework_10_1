import pytest

from src.product import Product


def test_category_init(first_category, second_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == ("Смартфоны, как средство не только коммуникации,"
                                          " но и получения дополнительных функций для удобства жизни")
    assert len(first_category.products_in_list) == 3

    assert first_category.category_count == 2
    assert second_category.product_count == 4


def test_category_products_property(first_category):
    assert (first_category.products == '\nSamsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'
                                       'Iphone 15, 210000.0 руб. Остаток: 8 шт.\n'
                                       'Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.')


def test_category_str(first_category):
    assert str(first_category) == "Смартфоны, количество продуктов: 10 шт."


def test_product_iterator(product_iterator):
    iter(product_iterator)
    assert product_iterator.index == 0
    assert next(product_iterator).name == "Samsung Galaxy S23 Ultra"
    assert next(product_iterator).name == "Iphone 15"
    assert next(product_iterator).name == "Xiaomi Redmi Note 11"

    with pytest.raises(StopIteration):
        next(product_iterator)


def test_category_product_list_smartphone(first_category, product_smartphone1):
    first_category.list_product = product_smartphone1
    assert first_category.products_in_list[-1].name == "Xiaomi Redmi Note 11"


def test_middle_price(first_category, category_without_product):
    assert first_category.middle_price() == 140333.33333333334
    assert category_without_product.middle_price() == 0


# def test_custom_exception_add_product(capsys):
#     Product("Бракованный товар", "Неверное количество", 1000.0, 2)
#     # assert invalid_product.add_product() ==
#     message = capsys.readouterr()
#     assert message.out.strip().split('\n')[-2] == 'Нельзя добавить товар с нулевым количеством'
#     assert message.out.strip().split('\n')[-1] == 'Обработка добавления продукты прошла успешно'
