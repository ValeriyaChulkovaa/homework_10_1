import pytest

from src.product import Product


def test_category_init(category_fruit, apple, pineapple):
    assert category_fruit.name == "Fruits"
    assert category_fruit.description == "Сбор урожая - 2024"
    assert category_fruit.products == "Green apple, 115.2 руб. Остаток: 30 шт.\nPineapple, 460 руб. Остаток: 10 шт.\n"

    assert category_fruit.category_count == 1
    assert category_fruit.product_count == 2


@pytest.mark.parametrize(
    "product",
    [
        (Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)),
        (Product(name="Pineapple", description="Страна-поставщик Коста-Рика", price=460, quantity=10)),
    ],
)
def test_add_product_setter(category_fruit, product):
    assert category_fruit.add_product(product) == None


def test_category_str(category_fruit):
    assert str(category_fruit) == "Fruits, количество продуктов: 40 шт."


def test_products_in_list(category_fruit):
    assert str(category_fruit.products_in_list[0]) == "Green apple, 115.2 руб. Остаток: 30 шт.\n"


def test_product_add_error(apple):
    with pytest.raises(TypeError):
        result = apple + "string"
        