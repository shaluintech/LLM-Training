"""
Booleans - the True/ False data type that powers decision
"""

is_raining = True
is_sunny = False
print(is_raining)
print(is_sunny)
print("Type ==>", type(is_raining))

real_bool = True
fake_bool = "True"
print(type(real_bool))
print(type(fake_bool))

# Boolean usually comes from questions
age = 20
is_adult = age >= 21
print("Is adult?", is_adult)

#Task : Take user age input and tell if they
# can vote or not


# Under the hood True is 1 , False is 0 
print(True + True)
print(False + 10)
print(int(True), int(False))

#Typecast To Bool - for truthiness
print(bool(1))
print(bool(0))
print(bool("Hi"))
print(bool(""))



