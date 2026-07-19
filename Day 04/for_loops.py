"""
for loops - run the body once for Each item in a collection
"""

for ch in "Python":
    print("Letter: ",ch)

students = ["Asha","Rohan","Chetan","Diya"]

for student in students:
    print("Welcome ", student)

#Task: total cart value calculator
cart_prices = [300,499,88,2000]
total = 0
for price in cart_prices:
    total += price
print(f"Total cart amount : {total}")

leaderboard = ["Asha","Ben","Chetan"]
for rank,name in enumerate(leaderboard, start=1):
    print(f"# {rank} : {name}")

#Task : For a given List of Price print new prices 
# with 10% discount
cart_prices = [300,499,88,2000]
