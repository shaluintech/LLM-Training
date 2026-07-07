"""
Defining Function - a block of code that can be reused
"""
def greet():
    """Print a friendly greeting""" #docstring - one line description
    print("Hello , welcome to your course!!!")

greet()
greet()


# print(greet())
print(greet.__doc__)

def say_bye():
    """Sign off"""
    print("See you tomorrow")

say_bye()