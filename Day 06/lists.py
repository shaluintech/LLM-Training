"""
Lists - ordered , changables collections.
Your everyday container
"""

cart = ["milk","bread","banana"]
print("Cart :    ",cart)
print("First item of Cart", cart[0])
print("Last item of Cart", cart[-1])
print("Length", len(cart))
print("Slice" , cart[0:2])
print("'Milk in cart'","milk" in cart)


#Mutating a List
cart[0] = "coffee"
print(cart)
cart.append("rice")
cart.insert(0,"tea")
shopping_list = ["jam","oil"]
cart.extend(shopping_list)
print(cart)


demo = [1,2]
demo.append([3,4])
print("Demo after append",demo)
demo = [1,2]
demo.extend([3,4])
print("Demo after extend",demo)


#Removing Items 

removed_item = cart.pop()
print(cart)
print(removed_item)
cart.remove("tea")
print("Cart after removing tea", cart)
print("")
del cart[0]
print_queue = []
print_queue.append("Report.pdf")
print_queue.append("invoice.pdf")
print_queue.append("photo.png")
print(f"{len(print_queue)} jobs waiting")
while print_queue:
    job = print_queue.pop(0)
    print(f"  printing {job}....({len(print_queue)} jobs remaining)")




