#falsy values
print(bool(0))
print(bool(0.0))
print(bool(""))
print(bool(None))
print(bool([]))
print(bool({}))

print(bool(1))
print(bool(-5))
print(bool("hi"))
print(bool("0"))
print(bool(" "))

name = input("Enter your name (or just press ENTER)")
if name:
    print(f"Hello {name}!")
else:
    print("you didn't enter name")


# in 
print("a" in "cat")
print("a" not in "cat")