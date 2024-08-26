import json


from src.product import Product
from src.category import Category
from src.config import file_json_product


def read_json(path: str) -> dict:
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def create_objects_from_json(data):
    categories = []
    for category in data:
        products = []
        for product in category['products']:
            products.append(Product(**product))
        category['products'] = products
        categories.append(Category(**category))

    return categories


if __name__ == '__main__':
    info = read_json(file_json_product)
    json_product = create_objects_from_json(info)
    print(json_product)
