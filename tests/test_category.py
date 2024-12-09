import pytest

from src.category import Category


def test_category(first_category, first_product, third_product, second_product, second_category, third_category):

    assert first_category.name == "Смартфоны"

    assert (
        first_category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )

    assert (
        first_category.get_product_list == "Samsung, 180000.0 руб. Остаток: 5 шт..\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт..\n"
        "55 QLED 4K, 123000.0 руб. Остаток: 7 шт..\n"
    )

    assert first_category.product_count == 5

    assert second_category.product_count == 5

    assert first_category.category_count == 3

    assert second_category.category_count == 3

    assert first_category.product_count == 5

    assert second_category.product_count == 5


def test_category_str(first_category):
    assert str(first_category) == "Смартфоны, количество продуктов: 20 шт."


def test_get_product_list(first_category, second_category):
    with pytest.raises(AttributeError):
        print(first_category.__products)
    assert (
        first_category.get_product_list == "Samsung, 180000.0 руб. Остаток: 5 шт..\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт..\n"
        "55 QLED 4K, 123000.0 руб. Остаток: 7 шт..\n"
    )


def test_add_error(first_category):
    with pytest.raises(TypeError):
        first_category.add_product(1)


def test_add_smartphone(first_category, smartphone1):
    first_category.add_product = smartphone1


def test_TaskIterator(taskiterator):
    iter(taskiterator)
    assert taskiterator.index == 0
    assert next(taskiterator).name == "Samsung"
    assert next(taskiterator).name == "Iphone 15"
    assert next(taskiterator).name == "55 QLED 4K"

    with pytest.raises(StopIteration):
        next(taskiterator)


def test_middle_price(without_product):

    category1 = Category(name="test", description="test", products=[])
    result = category1.middle_price()
    assert result == 0

    category2 = Category(name="test", description="test", products=without_product)
    assert category2.middle_price() == 111629.63


# def test_custom_exception(capsys, first_product):
#
#     assert len(first_product.quantity) == 8