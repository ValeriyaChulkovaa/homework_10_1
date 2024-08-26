from unittest.mock import mock_open, patch

from src.utils import create_object_products, get_data_by_products


def test_get_data_by_products():
    mock_data = (
        '[{"name": "Телевизоры", "description": "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",'
        '"products": [{"name": "55 QLED 4K","description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}]}]'
    )
    with patch("builtins.open", mock_open(read_data=mock_data)):
        data = get_data_by_products()
        assert data == [
            {
                "name": "Телевизоры",
                "description": "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                "products": [
                    {"name": "55 QLED 4K", "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
                ],
            }
        ]


def test_data(get_data):
    result = create_object_products(get_data)
    assert result[0].name == "Смартфоны"
