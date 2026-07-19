"""
Dict - key:value pairs , Look things by name
not position
"""
student = {
    "name":"Rohan",
    "age":21,
    "marks":[88,43,23]
}

print("Name:      ",student["name"])
print("How many items in dict:", len(student))
print("'age' in student", "age" in student)
# print("Missing values" , student["college"])
print("Missing values" , student.get("college","n/a"))



student["email"] ="abc@gmail.com"
student["age"] = 35
print("Student After Update", student)

removed_item = student.pop("marks")
print(removed_item)

del student["email"]
#Task - Create the total bill
prices = {
    "coffee":120,
    "juice":100,
    "sandwich":150
}
order = ["coffee" , "juice"]

total_bill = 0
for item in order:
    total_bill +=prices.get(item)

print("Your total bill is:" ,total_bill)