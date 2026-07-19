"""
Conditionals - if / elif / else - Decisions
"""

temp = 38
if temp > 35:
    print("Its Hot!")

print("THis will always be printed")
age = 16
if age >=18:
    print("You can vote")
else:
    print("Too young to vote")


marks = 72
if marks > 90:
    grade = "A"
elif marks >=75:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >=40:
    grade = "D"
else:
    grade = "E" 

print(f"Your Marks {marks} : Your Grade {grade}")