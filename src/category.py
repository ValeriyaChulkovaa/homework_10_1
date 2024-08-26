from src.product import Product


class Category:
    name: str
    description: str
    list_product: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__list_product = products
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product):
        self.__list_product.append(product)
        Category.product_count += 1

    @property
    def products(self):
        product_str = ''
        for product in self.__list_product:
            product_str += f'\n{product.name}, {product.price} руб. Остаток: {product.quantity} шт.'
        return product_str

    @property
    def products_in_list(self):
        return self.__list_product
    