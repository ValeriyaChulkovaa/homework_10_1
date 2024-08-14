import json
import os

import pytest

from src.category import Category
from src.product import Product


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
