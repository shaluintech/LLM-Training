age = 20
has_ticket = True

if age >= 18:
    print("You are old enought to enter")
    if has_ticket:
        print("You can enter")
    else:
        print("You do not have ticket")
else:
    print("You are not old ")
