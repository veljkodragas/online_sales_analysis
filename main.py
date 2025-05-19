from product import Product
from product_manager import ProductManager

def main():
    manager = ProductManager()
    # Dodajemo proizvoljne proizvode
    manager.add_product(Product("Laptop", 1200.0, 5))
    manager.add_product(Product("Smartphone", 800.0, 10))
    manager.add_product(Product("Headphones", 150.0, 15))

    print("Lista proizvoda:")
    manager.display_products()

    ukupna_vrednost = manager.total_value()
    print(f"Ukupna vrednost inventara: ${ukupna_vrednost:.2f}")

if __name__ == "__main__":
    main()