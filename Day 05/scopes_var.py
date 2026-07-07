#Global Scope
app_name = "My First App"

#Local Scope
def show_total():
    total = 999
    print("Welcome to :", app_name)
    print("Inside : ", total)
show_total()
# print(total)

def make_multiplier(factor):
    """Return a function that multiplies its input by factor"""
    def multiply(n):
        return n * factor
    return multiply
triple = make_multiplier(3)
print(triple(10))
tenfold = make_multiplier(10)
print(tenfold(90))