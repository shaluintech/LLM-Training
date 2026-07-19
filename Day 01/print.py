"""
print() — separators, line endings, and mixing values.

Run:
    python print_basics.py
"""

# Multiple values: print() puts a space between them by default
print("Score:", 42, "points")

# sep=... changes what goes BETWEEN the values
print("2024", "06", "10", sep="-")    # 2024-06-10
print("a", "b", "c", sep="")           # abc

# end=... changes what goes AFTER the line (default is a newline "\n")
print("Loading", end="")
print("...", end="")
print(" done")                          # all on one line: Loading... done

# Mixing text and numbers is fine — commas convert each value to text
age = 25
print("I am", age, "years old")

# An empty print() just prints a blank line
print()
print("(there was a blank line above)")