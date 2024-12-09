import json
import os

from src.category import Category
from src.products import Product


def read_json(path: str) -> dict:
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)

    return data


def create_objects(data: dict):
    prod = []
    for i in data:
        desc = []
        for j in i["products"]:
            desc.append(Product(**j))
        i["products"] = desc
        prod.append(Category(**i))
    return prod


if __name__ == "__main__":
    info = read_json("/Users/maksbolomoznov/PycharmProjects/OOP/data/products.json")
    new = create_objects(info)
    print(new[0].name)
    print((new[0].description))