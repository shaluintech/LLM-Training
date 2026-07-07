"""
Nested loop - a loop inside a loop
"""
# Mental model Rows X cols
for row in range(3):
    for col in range(4):
        print(f"({row}{col})",end=" ")
    print()


colors = ["Red","Blue"]
sizes = ["S","M","L"]
print("Generating Variants")
for color in colors:
    for size in sizes:
        # sku = f"Tshirt - {color[:3].upper()} - {size}"
        print(f"    {color} / {size}")
print()


for n in range(1,21):
    if n%3==0 and n%5==0:
        print("FizzBuzz")
    elif n%3==0:
        print("Fizz")
    elif n%5==0:
        print("Buzz")
    else:
        print(n)