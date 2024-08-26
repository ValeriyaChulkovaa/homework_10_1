from src.product import Product


def test_product(product):
    assert product.name == "55\" QLED 4K"
    assert product.description == "Фоновая подсветка"
    assert product.price == 123000.0
    assert product.quantity == 7


def test_new_product():
    product = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    product.name = "55\" QLED 4K"
    product.description = "Фоновая подсветка"
    product.price = 123000.0
    product.quantity = 7


def test_price_update(capsys, product):
    product.price = -100
    message = capsys.readouterr()
    assert message.out.strip() == 'Цена не должна быть нулевая или отрицательная'
