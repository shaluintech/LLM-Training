"""
Tuples - ordered but UNCHANGEABLE - A frozen
list
"""

point = (3,4)
print("Point    ", point)
print("Point    ", point[0])
print("Point    ", len(point))

# point[0] = 9 - will not work

#Unpacking a tuple
person = ("Arjit",34,"AI Consultant")
name , age, job = person
print(f"Name : {name}, Age: {age}, Job:{job}")