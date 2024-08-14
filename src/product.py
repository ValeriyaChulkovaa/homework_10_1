from typing import Any


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, dict_product: dict) -> Any:

        return Product(**dict_product)

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price_product: int) -> Any:
        if price_product <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            if price_product < self.__price:
                answer = input("Вы действительно хотите понизить цену? y-да/n-нет ")
                if answer == "y":
                    self.__price = price_product
                self.__price = self.__price
            self.__price = price_product
            