from src.product import Product


class Order:
    """класс Заказ, в котором будет ссылка на то какой товар был куплен, количество купленного товара,
    а также итоговая стоимость. В заказе может быть указан только один товар."""
    product: Product
    byu_count: int
    total_price: float

    def __init__(self, product: Product, buy_count: int, name, description, price, quantity) -> None:
        super().__init__(name, description, price, quantity)
        self.product = product
        self.buy_count = buy_count
        self.total_price += self.product.price * buy_count

    def __str__(self):
        return f'Куплен: {self.product.name}, колличество: {self.buy_count} шт, сумма покупки:{self.total_price}'
    