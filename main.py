from product import Product
from product_manager import ProductManager

manager = ProductManager()
manager.add_product(Product("Gaming Laptop", 1200, 8))
manager.add_product(Product("Wireless Mouse", 25, 40))
manager.add_product(Product("Keyboard", 70, 30))
manager.add_product(Product("Monitor", 300, 10))

