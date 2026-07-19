"""
Logical Operators - and / or / not 
Combine boolean into one
"""
age = 25
salary = 40000
print(age >= 18 and salary >=25000)
print(age >= 18 and salary >=50000)

is_weekend = False
is_holiday = True

print(is_weekend or is_holiday)
print(False or False)

print(not True)
print(not age>=18)

print("-----and------")
print(True and True , True and False, False and False)
print("-----or------")
print(True or True , True or False, False or False)

#Precedence 
#not > and > or
print(True or False and False)
print((True or False) and False)