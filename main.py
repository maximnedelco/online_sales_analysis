from product_manager import ProductManager # type: ignore #type
from product import Product
from cart import Cart # type: ignore

manager = ProductManager()


manager.add_product(Product("Laptop", 2400, 5))
manager.add_product(Product("Tastatura", 700, 10))
manager.add_product(Product("Casti", 250, 7))

cart = Cart()
cart.add_products(manager.products[0])
cart.add_products(manager.products[1])
cart.add_products(manager.products[2])

print("Cosul de cumparaturi:")
cart.display_cart()
print(f"Total de plata: {cart.total_cart_value()} lei")


manager.display_product()
manager.total_value()
