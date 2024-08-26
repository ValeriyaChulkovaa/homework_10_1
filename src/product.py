class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        if type(other) is Product:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError

    @property
    def price(self):
        return self.__price

    @classmethod
    def new_product(cls, dict_product):
        return cls(dict_product['name'], dict_product['description'], dict_product['price'], dict_product['quantity'])

    @price.setter
    def price(self, new_price: int):
        if new_price <= 0:
            print('Цена не должна быть нулевая или отрицательная')
            return
        self.__price = new_price
        