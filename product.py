class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Product: {self.name}, Price: ${self.price:.2f}, Quantity: {self.quantity}")

    def update_quantity(self, new_quantity: int):
        self.quantity = new_quantity
