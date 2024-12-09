def tests_products(capsys, first_product, second_product, third_product, fourth_product):
    assert first_product.name == "Samsung"
    assert first_product.description == "256GB, Серый цвет, 200MP камера"
    assert first_product.price == 180000.0
    assert first_product.quantity == 5

    assert second_product.name == "Iphone 15"
    assert second_product.description == "512GB, Gray space"
    assert second_product.price == 210000.0
    assert second_product.quantity == 8

    assert third_product.name == "55 QLED 4K"
    assert third_product.description == "Фоновая подсветка"
    assert third_product.price == 123000.0
    assert third_product.quantity == 7

    assert fourth_product.name == "Xiaomi Redmi Note 11"
    assert fourth_product.description == "1024GB, Синий"
    assert fourth_product.price == 31000.0
    assert fourth_product.quantity == 14


def test_Product_str(capsys, first_product, second_product, third_product, fourth_product):
    assert str(first_product) == "Samsung, 180000.0 руб. Остаток: 5 шт."
    assert str(second_product) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    assert str(third_product) == "55 QLED 4K, 123000.0 руб. Остаток: 7 шт."
    assert str(fourth_product) == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."


def test_Product_add(first_product, second_product, all_sum1, all_sum2):
    assert all_sum1 == 2580000.0
    assert all_sum2 == 1334000.0


def test_product_price(first_product, capsys):
    first_product.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"

    first_product.price = 100000
    assert first_product.price == 100000