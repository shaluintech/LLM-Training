#PROBLEM-2. OTP Engine

import random
otp = ""
attempts = 3

while True:
    print("\n1. send otp")
    print("2.enter otp")
    print("3.exit")
    
    choice = input("Enter choice:")
    
    if choice == "1":

        otp = str(random.randint(100000, 999999))
        attempts = 3
        print("OTP Sent:", otp)

    elif choice == "2":

        if otp == "":
            print("No OTP sent yet.")
            continue

        entered = input("Enter OTP: ")
        
        if len(entered) != 6 or entered.isdigit() == False:
            print("Enter valid OTP.")
            continue

        if entered == otp:
            print("Verified!")
            otp = ""
        else:
            attempts -= 1

            if attempts == 0:
                print("OTP expired.")
                otp = ""
            else:
                print("Wrong OTP.")
                print("Attempts left:", attempts)

    elif choice == "3":
        break

    else:
        print("Invalid choice.")
