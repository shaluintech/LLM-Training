# PROBLEM-4. Password Strength Checker

while True:

    password = input("Enter password: ")

    score = 0

    if len(password) >= 8:
        score += 1

    if any(ch.isupper() for ch in password):
        score += 1

    if any(ch.islower() for ch in password):
        score += 1

    if any(ch.isdigit() for ch in password):
        score += 1

    special = "!@#$%^&*"

    if any(ch in special for ch in password):
        score += 1

    print("Score:", score)

    if score == 5:
        print("Strong")
    elif score >= 3:
        print("Medium")
    else:
        print("Weak")

    again = input("Again? y/n: ")

    if again == "n":
        break