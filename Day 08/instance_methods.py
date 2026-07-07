class BankAccount:
    bank_name = "SBI"
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance 

    def deposit(self,amount):
        self.balance += amount
        return self.balance 
    
tom = BankAccount("tom",1000)
ketan = BankAccount("ketan")
tom.deposit(5000)
print(tom.balance)
print(vars(tom))
BankAccount,bank_name = "HDFC"
