#PROBLEM-3. Fake Cart & Bill

cart = {}
while True:
    print("\n1. ADD ITEM")
    print("2.VIEW CART")
    print("3. CHECKOUT")
    
    choice = input("choice:")
    
    if choice =="1":
        item = input("item name:")
        price = float(input("price: "))
        qty = int(input("quantity:"))
        
        if item in cart:
            cart[item][1] += qty
        else:
            cart[item]=[price,qty]
                       
    elif choice == "2":
        subtotal =0
        
        for item in cart:
            price = cart[item][0]
            qty = cart[item][1]

            total = price * qty

            subtotal += total

            print(item, "x", qty, "= ₹", total)

        print("Subtotal =", subtotal)

    elif choice == "3":
        break