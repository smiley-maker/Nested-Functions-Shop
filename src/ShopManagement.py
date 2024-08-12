import random
from Customer import Customer

class ShopKeep: 
  def __init__(self, items : list[str], costs: list[float], user : Customer): 
    # Create a mapping from items to quantity and costs. 
    self.shop = {
                  # Creates a random quantity for each item. 
                  items[i] : (costs[i], random.randint(0, 100)) for i in range(len(items))
                }
    self.user = user
   
  def parse_input(self):
    # Display the current state of the shop
    self.display_shop()
    # Ask the user for an action
    action = input("Please specify an action to take. Select a for add to cart, c for checkout, and r for removing an item.")
    
    if action == "a":
      # Call add to cart
      self.add_to_cart()
    elif action == "r":
      # Call remove from cart
      self.remove_from_cart()
    elif action == "c": 
      self.checkout()
      print("Thanks for shopping!")
      return False
    else:
      print("Unsupported action request, please try again...")
    
    return True

  def display_shop(self, flag = True):
    # Welcome message
    if flag:
      print("Hello! Welcome to the tutorial shop!")
    # prints shop inventory. 
    for k,v in self.shop.items():
      # k -> item name
      # v -> tuple containing cost and quantity
      print(f"{k} -- ${v[0]} -- {v[1]} left")
  
  def add_to_cart(self, shop_item): 
    # Queries the user for which item they want. 
#    shop_item = input("Which item would you like to add?")

  
    # checks if the item is in the shop. 
    if shop_item in self.shop.keys():
      # checks if the item is still in stock. 
        if self.shop[shop_item][1] > 0:
            # Add the item name to the users cart. 
            self.user.add_to_cart(shop_item)
#            self.cart.append(shop_item)
            # Reduce the quantity of the item.
            self.shop[shop_item] = (self.shop[shop_item][0], self.shop[shop_item][1] - 1)
        else:
            print("Item out of stock.")
    else:
      print("You selected an item that doesn't exist in the shop, please pick something else")

  def remove_from_cart(self, item_to_remove):
    # Gets the item to remove from the user
#    item_to_remove = input("Please specify an item to remove.")
    # If it is in the cart, proceed with removing. 
    if item_to_remove in self.user.cart:
      # Remove the item from the user's cart. 
      self.user.remove_from_cart(item_to_remove)
#      self.cart.remove(item_to_remove)
      # print the updated cart
      print(f"Removed {item_to_remove}")
      print(self.user.cart)
      # Increment the quantity in the shop
      self.shop[item_to_remove] = (self.shop[item_to_remove][0], self.shop[item_to_remove][1] + 1)
    else:
      print("Specified item not in cart, please try again.")

  def checkout(self):
    # calculate total
    total = 0
    for k in self.user.cart:
      total += self.shop[k][1][0]
    
    # send total to checkout user
    self.user.checkout(total)

    # print
    print(f"Your total is {total}")

    return total


def test_functions(test_cases : dict):
  for k,v in test_cases.items():
    # call the function
    k(v[0])
    if shop.shop["Moana"][1] == v[1][0] and shop.cart == v[1][1]:
      print(f"{k} passed ✅")
    else:
      print(f"{k} failed ⛔️")

if __name__ == "__main__":
    # Create shop items. 
    # Let's make a movie shop! 
    items = ["Moana", "Princess Diaries", "X-Men", "Fantastic Beasts"]
    costs = [30, 20, 10, 15]
    shop = ShopKeep(items, costs)

    original_amount = shop.shop["Moana"][1]

    tests = {
               # input, expected outputs (i.e. shop, cart)
               shop.add_to_cart : ["Moana", (original_amount - 1, ["Moana"])],
               shop.remove_from_cart : ["Moana", (original_amount, [])],
             }
    
    test_functions(tests)