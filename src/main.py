from Customer import Customer
from ShopManagement import ShopKeep

def test_functions(test_cases : dict, shop : ShopKeep):
  for k,v in test_cases.items():
    # call the function
    k(v[0])
    if shop.shop["Peach"][1] == v[1][0] and shop.user.cart == v[1][1]:
      print(f"{k} passed ✅")
    else:
      print(f"{k} failed ⛔️")

if __name__ == "__main__":
    print("Starting shop!")

    cmr = Customer(30)
    shop_keep = ShopKeep([
        "Tomato", "Onion", "Lettuce", "Peach", "Strawberry"
    ], 
    [
        3, 1, 5, 4, 2
    ], cmr)

    shop_keep.display_shop()

    original_amount = shop_keep.shop["Peach"][1]

    tests = {
               # input, expected outputs (i.e. shop, cart)
               shop_keep.add_to_cart : ["Peach", (original_amount - 1, ["Peach"])],
               shop_keep.remove_from_cart : ["Peach", (original_amount, [])],
               shop_keep.checkout : []
             }
    
    test_functions(tests, shop_keep)
