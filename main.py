from product import Product
from product_manager import ProductManager
from cart import Cart
import random

def main():
    manager = ProductManager()
    manager.add_product(Product("Laptop", 1200.0, 5))
    manager.add_product(Product("Smartphone", 800.0, 10))
    manager.add_product(Product("Headphones", 150.0, 15))
    manager.add_product(Product("Mouse", 50.0, 20))
    manager.add_product(Product("Keyboard", 70.0, 10))

    print("Lista proizvoda:")
    manager.display_products()
    print(f"Ukupna vrednost inventara: ${manager.total_value():.2f}")

    cart = Cart()
    # Dodajemo tri slučajna proizvoda iz inventara u korpu
    random_products = random.sample(manager.products, 3)
    for prod in random_products:
        cart.add_product(prod)

    cart.display_cart()
    print(f"Ukupna vrednost za naplatu: ${cart.total_amount():.2f}")

if __name__ == "__main__":
    main()
