"""
Variable naming — rules, conventions, and the keyword list.

Run:
    python variable_naming.py
"""

# ----- Valid names (snake_case is the Python convention) -----
first_name = "Arjit"
total_price = 199.99
is_active = True
_internal = 0
age2 = 30


print(first_name, total_price, is_active, age2)

# Case matters: these are THREE different variables
age = 1
Age = 2
AGE = 3
print("age, Age, AGE =", age, Age, AGE)

# ----- The reserved keywords you may NOT use as names -----
import keyword
print("\nPython keywords (cannot be variable names):")
print(keyword.kwlist)

# The following lines would each be a SyntaxError if uncommented:
# 2age = 30          # can't start with a digit
# user-name = "x"    # '-' is not allowed in names
# class = "CS"       # 'class' is a reserved keyword