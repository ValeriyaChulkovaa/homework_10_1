from src.products import Product


class Smartphone(Product):

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    # def __add__(self, other):
    #     # return (self.__products * self.product_count) + (other.__products * other.product_count)
    #     if type(other) is Smartphone:
    #         return (self.__price * self.quantity) + (other.__price * other.quantity)