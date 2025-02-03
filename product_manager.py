from product import Product
class ProductManager:
    def __init__(self):
        self.products = []
        
        
    def add_product(self,product):
        self.products.append(product)
        
        
        
    def display_product(self):
        if not self.products:
            print("Nu exista acest produs!")
            for product in self.products:
                product.display_info()
            
            
    def total_value(self):
        total_val = sum(product.price * product.quantity for product in self.products)
        print(f"Valoarea totala a tuturor produselor {total_val} lei")
        
        
    def remove_product(self, name):
        self.products = [p for p in self.products if p.name != name]

        
        
    