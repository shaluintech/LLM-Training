"""
Variables — named boxes that hold values.

Run:
    python variables.py
"""

# Assign values to names with '='
age = 25
name = "Tushar"
price = 199.99

# Use the names anywhere you'd use the value
print("name:", name)
print("age next year:", age + 1)
print("price:", price)

# ----- Reassignment: a variable can change -----
score = 0
print("start score:", score)
score = score + 10   # right side computed first (0 + 10), then stored back
print("after +10:", score)

# ----- Dynamic typing: a variable can even change TYPE -----
x = 10
print("x is now:", x, "(", type(x).__name__, ")")
x = "ten"
print("x is now:", x, "(", type(x).__name__, ")")

# ----- Multiple assignment -----
a, b = 1, 2
print("a, b =", a, b)

a, b = b, a          # swap without a temp variable
print("after swap, a, b =", a, b)

p , q , r = 0 , 0 , 0       # set several at once
print("p, q, r =", p, q, r)