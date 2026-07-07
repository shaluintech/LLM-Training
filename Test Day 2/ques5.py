#PROBLEM-5. Wallet / UPI Simulator

balance = 0

while True:

    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Exit")

    choice = input("Choice: ")

    if choice == "1":

        amount = float(input("Amount: "))

        balance = balance + amount

        print("Balance =", balance)

    elif choice == "2":

        amount = float(input("Amount: "))

        if amount > balance:
            print("Insufficient balance")
        else:
            balance = balance - amount
            print("Balance =", balance)

    elif choice == "3":
        break