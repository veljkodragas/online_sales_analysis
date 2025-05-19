from product import Product

class Cart:
    def __init__(self):
        self.cart_items = []

    def add_product(self, product: Product):
        self.cart_items.append(product)

    def total_amount(self):
        return sum(p.price * p.quantity for p in self.cart_items)

    def display_cart(self):
        print("Sadržaj korpe:")
        for product in self.cart_items:
            product.display_info()
