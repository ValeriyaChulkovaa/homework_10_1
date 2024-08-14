from src.product import Product


def test_product_init(apple, pineapple):
    assert apple.name == "Green apple"
    assert apple.description == "Сезонные 2024 года"
    assert apple.price == 115.20
    assert apple.quantity == 30

    assert pineapple.name == "Pineapple"
    assert pineapple.description == "Страна-поставщик Коста-Рика"
    assert pineapple.price == 460
    assert pineapple.quantity == 10


def test_new_product():
    name_product = Product.new_product({"name": "apple", "description": "green apple", "price": 13, "quantity": 12})
    assert name_product.name == "apple"
    assert name_product.description == "green apple"
    assert name_product.price == 13
    assert name_product.quantity == 12


def test_new_price(capsys, apple):
    apple.price = -100
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
    apple.price = 1000
    assert apple.price == 1000
    apple.price = 1
    assert apple.price == 1
    