from product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        self.products.append(product)

    def display_products(self):
        for product in self.products:
            product.display_info()

    def total_value(self):
        return sum(p.price * p.quantity for p in self.products)