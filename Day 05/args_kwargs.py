"""
*args (extra positionals -> tuple)
**kwargs (extra keywords)
"""

def total(*args):
    print(" args is a tuple", args)
    return sum(args)

print("Total (15,20,40) =", total(15,20,40))
print("Total (10,250) =", total(10,250))
print("Total () =", total())



def make_user(**kwargs):
    print(" kwargs is a dict", kwargs)
    return kwargs

make_user(name="Tushar", age=34,city="Lucknow")
make_user(name="Ben")
