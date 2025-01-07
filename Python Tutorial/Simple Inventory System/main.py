class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Name: {self.name}, Price: ${self.price:.2f}, Quantity: {self.quantity}")

    def update_quantity(self, amount):
        self.quantity += amount
        print(f"Updated quantity of {self.name}: {self.quantity}")

    def calculate_value(self):
        return self.price * self.quantity


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, quantity):
        new_product = Product(name, price, quantity)
        self.products.append(new_product)
        print(f"Product {name} added to inventory.")

    def display_inventory(self):
        print("\nInventory Details:")
        for product in self.products:
            product.display_info()

    def calculate_total_value(self):
        total_value = sum(product.calculate_value() for product in self.products)
        print(f"\nTotal value of inventory: ${total_value:.2f}")


def main():
    store_inventory = Inventory()

    store_inventory.add_product("Laptop", 1200.99, 10)
    store_inventory.add_product("Headphones", 199.99, 50)
    store_inventory.add_product("Keyboard", 49.99, 30)

    store_inventory.display_inventory()

    store_inventory.products[0].update_quantity(-2)  # Sold 2 laptops
    store_inventory.products[1].update_quantity(20)  # Restocked 20 headphones

    store_inventory.display_inventory()

    store_inventory.calculate_total_value()

main()
