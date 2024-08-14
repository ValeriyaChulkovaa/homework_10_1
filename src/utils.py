import json
import os
from typing import Any

from src.category import Category
from src.product import Product


def get_data_by_products(file_path: str = "../data/products.json") -> Any:
    full_path = os.path.abspath(file_path)
    result = []
    try:
        with open(full_path, "r", encoding="utf-8") as f_obj:
            result = json.load(f_obj)
    except FileNotFoundError:
        print("Файл не найден")
        return result
    else:
        return result


def create_object_products(data_products: list[dict]) -> list[Category]:
    categories = []
    for data_product in data_products:
        products = []
        for product in data_product["products"]:
            products.append(Product(**product))
        data_product["products"] = products
        categories.append(Category(**data_product))

    return categories
