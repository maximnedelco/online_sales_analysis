class Cart:
    def __init__(self):
        self.cart_items = []

    def add_product(self, product):
        self.cart_items.append(product)

    def total(self):
        return sum(p.price for p in self.cart_items)

    def display_cart(self):
        for p in self.cart_items:
            print(f"{p.name} - Price: {p.price}")
