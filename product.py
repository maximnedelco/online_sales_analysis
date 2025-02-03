class Product:
    def __init__(self,name, price , quantity):
        self.name = name 
        self.price = price
        self.quantity = quantity
        
        
        
    def display_info(self):
        print(f"Numele: {self.name} , Pretul: {self.price} , Cantitatea: {self.quantity}")
        
        
    def update(self,new_quantity):
        self.quantity = new_quantity
        