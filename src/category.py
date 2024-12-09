from typing import Any

from src.exceptions import ZeroProductError
from src.products import Product


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.product_count += len(products)
        Category.category_count += 1

    def middle_price(self):

        total_p = 0
        total_q = 0
        avg = 0

        try:
            for p in self.__products:
                total_p += p.price * p.quantity
                total_q += p.quantity
            avg = total_p / total_q

        except ZeroDivisionError:
            return 0

        else:
            return round(avg, 2)

    # def __str__(self):
    #     return f"{self.name}, количество продуктов: {len(self.__products)} шт.\n"
    def __str__(self):
        all_quantity = 0
        for j in self.__products:
            all_quantity += j.quantity
        return f"{self.name}, количество продуктов: {all_quantity} шт."

    # def add_product(self, product: Product):
    #     if isinstance(product, Product):
    #         for item in self.__products:
    #             if item.name == product.name:
    #                 item.quantity += product.quantity
    #                 if item.price < product.price:
    #                     item.price = product.price
    #                 return
    #     else:
    #         raise TypeError
    #     self.__products.append(product)
    #     Category.product_count += 1

    # def __add__(self, other):
    #     # return (self.__products * self.product_count) + (other.__products * other.product_count)
    #
    #     return (self.__products * self.quantity) + (other.__products * other.quantity)

    # def __add__(self, other):
    #     # return (self.__products * self.product_count) + (other.__products * other.product_count)
    #
    #     return (self.__products * self.quantity) + (other.__products * other.quantity)
    def add_product(self, product: Product) -> Any:
        if isinstance(product, Product):
            try:
                if product.quantity == 0:
                    raise ZeroProductError("Нет продуктов")
            except ZeroProductError as e:
                print(str(e))
            else:

                self.__products.append(product)
                Category.product_count += 1
                print("Продукт добавлен")
            finally:
                print("Обработка  с добавлением продукта завершена ")
        else:
            raise TypeError

    @property
    def list_prod(self):
        return self.__products

    @property
    def get_product_list(self) -> str:
        product_list = ""
        for i in self.__products:
            product_list += f"{str(i)}.\n"
        return product_list


if __name__ == "__main__":
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError :
        print(
            "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым количеством"
        )
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])

    print(category1.middle_price())

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(category_empty.middle_price())