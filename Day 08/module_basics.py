"""modules basics.py"""


import math
print(math.pi)
print(math.sqrt(144))
(print(math.ceil(4.1)))



import math
from random import randint, choice, seed
import datetime as dt
import json

print(math.pi)
print(math.sqrt(144))
(print(math.ceil(4.1)))

print(randint(1,6))
print(choice(['Rock','Paper','Scissors']))
print(seed(42))

today =dt.date.today()
print(type(today))
print(today.year)
print(today.month)
print(today.day) 

   
## new_year = dt.date(today.year,12,31)
my_bday = dt.date(2005,12,20)
print(my_bday)

user = {"name":"Arjit","skills":['py','ai']}
text = json.dumps(user)
print("User",user)
print("User Json",text)
back = json.loads(text)