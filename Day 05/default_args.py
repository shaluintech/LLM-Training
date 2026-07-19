"""
Default values 
"""

def greet(name,greeting = "Hi"):
    print(f"{greeting} , {name}")

greet("Arjit")
greet("Arjit","Welcome")

#Keyword arguments
def book_tickets(name,seat,price):
    print(f"{name} --> seat {seat} (Rs {price})")

book_tickets("Arjit","3b",8999)
book_tickets(name="Arjit",price=8999,seat="3B")
book_tickets("Chetan",price=2323,seat="4F")



def add_cart_item(item,cart=[]):
    cart.append(item)
    return cart

print(" ", add_cart_item("Apple"))
print(" ", add_cart_item("Banana"))
print(" ", add_cart_item("Bread"))

def add_cart(item,cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart
print(" ", add_cart("Apple"))
print(" ", add_cart("Banana"))
print(" ", add_cart("Milk"))