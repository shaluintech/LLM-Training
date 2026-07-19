"""
While Loops
"""

# Anatomy => init -> test ->update

count = 1
while count <= 5:
    print(f"Rep {count} of 5")
    count += 1
print("Done Counting \n")


second = 10
while second > 0:
    print(f"Launchin in {second} seconds")
    second -=1
print("Take Off")


pending_order = ["ORD-101","ORD-102","ORD-103"]
while pending_order:
    order = pending_order.pop(0)
    print(f"Processing {order}..shipped")
print("All Orders Processed!!.\n")


print("Tiny menu - type 'quit' to leave")
while True:
    choice = input("Pick (status/help/quit)").strip().lower()
    if choice == "quit":
        print("Bye")
        break
    elif choice == "status":
        print("All systems Up")
    elif choice == "help":
        print("Commands : status,help , quit")
    else:
        print(f"Unknown command : {choice}")
