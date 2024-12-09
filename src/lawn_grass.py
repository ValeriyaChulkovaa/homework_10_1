from src.products import Product


class LawnGrass(Product):

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    # def __add__(self, other):
    #     # return (self.__products * self.product_count) + (other.__products * other.product_count)
    #     if type(other) is LawnGrass:
    #         return (self.__price * self.quantity) + (other.__price * other.quantity)