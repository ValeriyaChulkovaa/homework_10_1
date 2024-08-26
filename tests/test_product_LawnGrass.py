import pytest


def test_lawngrass(product_lawngrass1):
    assert product_lawngrass1.name == "Газонная трава"
    assert product_lawngrass1.description == "Элитная трава для газона"
    assert product_lawngrass1.price == 500.0
    assert product_lawngrass1.quantity == 20
    assert product_lawngrass1.country == "Россия"
    assert product_lawngrass1.germination_period == "7 дней"
    assert product_lawngrass1.color == "Зеленый"


def test_lawngrass_test_add(product_lawngrass1, product_lawngrass2):
    assert product_lawngrass1 + product_lawngrass2 == 16750.0


def test_lawngrass_test_add_error(product_lawngrass1):
    with pytest.raises(TypeError):
        result = product_lawngrass1 + 1
        