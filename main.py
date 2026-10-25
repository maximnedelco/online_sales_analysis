import random
from product import Product
from product_manager import ProductManager
from cart import Cart

manager = ProductManager()
manager.add_product(Product("Gaming Laptop", 1200, 8))
manager.add_product(Product("Wireless Mouse", 25, 40))
manager.add_product(Product("Keyboard", 70, 30))
manager.add_product(Product("Monitor", 300, 10))

cart = Cart()
for product in random.sample(manager.products, 3):
    cart.add_product(product)

print("Cart contents:")
cart.display_cart()
print(f"Cart total: {cart.total()}")
