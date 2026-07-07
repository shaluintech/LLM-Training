"""
String Method - Built in tools for cleaning and transforming

"""

text = "Arjit Verma"
print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())
# print(text)

messy = "     hello world         "
print(f"{messy.strip()}")

print(messy.strip().upper())