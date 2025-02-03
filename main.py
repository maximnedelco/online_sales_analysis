from product_manager import ProductManager # type: ignore #type
from product import Product


manager = ProductManager()


manager.add_product(Product("Laptop", 2400, 5))
manager.add_product(Product("Tastatura", 700, 10))
manager.add_product(Product("Casti", 250, 7))


manager.display_product()
manager.total_value()
