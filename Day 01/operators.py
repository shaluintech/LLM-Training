# ----- The familiar four -----
print("3 + 2 =", 3 + 2)
print("3 - 2 =", 3 - 2)
print("3 * 2 =", 3 * 2)
print("7 / 2 =", 7 / 2)     # 3.5  (true division -> float)


# ----- Floor division: divide and round DOWN to a whole number -----
print("7 // 2 =", 7 // 2)   # 3
print("17 // 5 =", 17 // 5)  # 3


# ----- Modulo: the REMAINDER after division -----
print("7 % 2 =", 7 % 2)     # 1
print("17 % 5 =", 17 % 5)   # 2


# A classic use of modulo: is a number even?  (even numbers have remainder 0)
print("Is 10 even? ->", 10 % 2 == 0)   # True
print("Is 7 even?  ->", 7 % 2 == 0)    # False


# ----- Exponent (power) -----
print("3 ** 2 =", 3 ** 2)   # 9
print("2 ** 10 =", 2 ** 10)  # 1024

# ----- Precedence: Python does ** , then * / // % , then + - -----
print("2 + 3 * 4 =", 2 + 3 * 4)      # 14 (not 20)
print("(2 + 3) * 4 =", (2 + 3) * 4)  # 20 (parentheses win)