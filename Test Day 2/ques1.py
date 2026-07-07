# PROBLEM-1. Fake Login System

users = {
    "tanya": "pass123",
    "siya": "hunter2"
    }

attempts = {
    "tanya": 0,
    "siya": 0
}
locked = []

while True:
    username = input ("Enter username:").strip()
    
    if username == "":
        print("username cannot be empty")
        continue
    password = input ("enter password:").strip()
    if password == "":
        print("password cannot be empty")
        continue
    if username in locked:
        print("Account locked!")
        break
    if username not in users:
        print("No such user.")
        continue
    if password == users[username]:
        print("Login successful!")
        break
    else:
        attempts[username] +=1
        
        if attempts[username] ==3:
            locked.append(username)
            print("account locked")
            break
        
        else:
            print("Wrong password.")
            print("Tries left:", 3 - attempts[username])
            
