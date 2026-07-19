"""
Break - Quit the loop
Continue - Skip the round
"""
orders = [100,299,499,1299,80]
for amount in orders:
    if amount > 1000:
        print(f"We have a BIG order :Rs {amount} -stopping")
        break 
    print(f" Checked Rs {amount}: Small Order")

transactions = [310,343,800,343,-300,-199,400]
income = 0
for t in transactions:
    if t < 0:
        print(f"Skipping Refund : {t}")
        continue 
    income += t 
print(f"Total Income : {income}")


CORRECT_PIN = 1234
attempt_left = 3

while attempt_left > 0:
    entered_pin = int(input(f"Enter pin . {attempt_left} attempts left :" ).strip())
    if entered_pin == CORRECT_PIN:
        print("Access Granted!!")
        break
    attempt_left -= 1
    print("Wrong PIN")
else:
    print("Card Blocked !!!")