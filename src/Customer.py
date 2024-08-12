class Customer: 
    def __init__(self, money : int):
        self.wallet = money
        self.cart = []
        self.inventory = []
    
    def add_to_cart(self, to_add):
        self.cart.append(to_add)
        print(f"Added {to_add}")
    
    def remove_from_cart(self, to_remove):
        self.cart.remove(to_remove)
        print(f"Removed {to_remove}")
    
    def checkout(self, total):
        self.inventory.extend(self.cart)
        print(f"Your total is: {total}")
        self.wallet -= total
        self.cart = []