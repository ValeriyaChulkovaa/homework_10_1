import json
import os

import pytest

from src.category import Category
from src.category_iterator import CategoryIterator
from src.product import Product
from src.subclass_product import LawnGrass, Smartphone


@pytest.fixture
def apple():
    return Product(name="Green apple", description="Сезонные 2024 года", price=115.20, quantity=30)


@pytest.fixture
def pineapple():
    return Product(name="Pineapple", description="Страна-поставщик Коста-Рика", price=460, quantity=10)


@pytest.fixture
def category_fruit(apple, pineapple):
    return Category(name="Fruits", description="Сбор урожая - 2024", products=[apple, pineapple])


@pytest.fixture
def get_data(file_path="../object_orient_programming/data/products.json"):
    full_path = os.path.abspath(file_path)
    with open(full_path, "r", encoding="utf-8") as f_obj:
        result = json.load(f_obj)
    return result


@pytest.fixture
def category_iter(category_fruit):
    return CategoryIterator(category_fruit)


@pytest.fixture
def smartphone():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def grass():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
