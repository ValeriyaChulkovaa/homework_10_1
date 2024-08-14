from src.product import Product


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list) -> None:

        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    @property
    def products(self) -> str:
        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"

        return product_str

    def add_product(self, product: Product) -> Product:
        name_products = []
        for product_class in self.__products:
            name_products.append(product_class.name)
        if product.name not in name_products:
            self.__products.append(product)
            Category.product_count += 1
            return product
        else:
            for product_class in self.__products:
                if product.name == product_class.name:
                    product_class.quantity += product.quantity
                    if product_class.price < product.price:
                        product_class.price = product.price
                return product
            