import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def number_for_file_masks():
    return '3234 12** **** 1234'


@pytest.fixture
def number_for_account_for_file_masks():
    return "**7757"


@pytest.fixture
def letter_for_file_masks():
    return 'Введены некорректные данные'


@pytest.fixture
def number_for_file_widget():
    return 'Visa 1245 23** **** 1234'


@pytest.fixture
def number_account_for_file_widget():
    return 'Счет **4356'


@pytest.fixture
def data():
    return "11.07.2018"


@pytest.fixture
def filter_():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


@pytest.fixture
def sort_():
    return [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]


@pytest.fixture
def first_category():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        list_product=[
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
            Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
        ]
    )


@pytest.fixture
def second_category():
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        list_product=[
            Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
        ]
    )


@pytest.fixture
def product():
    return Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
