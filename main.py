from product import Product
from product_manager import ProductManager

manager = ProductManager()
manager.add_product(Product("Laptop", 1200, 5))
manager.add_product(Product("Mouse", 25, 50))
manager.add_product(Product("Keyboard", 70, 30))
manager.add_product(Product("Monitor", 300, 10))

manager.display_products()
print(f"Total inventory value: {manager.total_value()}")

import random
from cart import Cart

cart = Cart()
for product in random.sample(manager.products, 3):
    cart.add_product(product)

print("Cart contents:")
cart.display_cart()
print(f"Cart total: {cart.total()}")
