"""
Parameters (names in def) - arguments (values you pass)
"""
def greet(name):
    """Greet one person by name"""
    print(f"Hello {name}")

greet("Ben")
# arguments can be expressions
raw = "   chetan    "
greet(raw.strip().title())

#Multiple paraments -> matched by postions
def book_ticket(name,seat,price):
    """Print a booking line"""
    print(f"{name} -> Seat : {seat} (Rs {price})")

book_ticket("Arjit","3B",9000)

orders = [101,102,103]

def confirm_order(order_id):
    print(f"Order #{order_id} confirment.Out for Delivery")

for oid in orders:
    confirm_order(oid)
