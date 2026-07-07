### Classes and Objects - blueprint(class), instance(onject)



class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
        
Shalu = Dog("Shalu","Retriver")
kallu = Dog("Kallu","Desi")

kallu.name = " Dogesh"
print(Shalu.name, Shalu.breed)

#create a class student - name, roll number, email

class Student:
    def __init__(self, name, rollno, email):
        self.name = name
        self.rollno = rollno
        self.email = email
        
tanya = Student("tanya", 48, "tanyatiwari066@gmail.com")
tushar = Student("tushar", 51, "tushar11@gmail.com")
print(tanya.name, tanya.rollno, tanya.email)
print(tushar.name, tushar.rollno, tushar.email)


## instance attribute & methods
class BankAccount:
    bank_name = "SBI"
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        self.balance+= amount
        return self.balance

    
    
tom = BankAccount("tom", 1000)
tanya = BankAccount("tanya", 1000000)
tom.deposit(5000)
tanya.deposit(6000)
print(tom.balance)
print(tanya.balance)
print(vars(tom))
BankAccount.bank_name="HDFC"
