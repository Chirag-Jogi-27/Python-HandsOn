
class BankAccount:
    def __init__(self, account_holder, initial_balance = 0.0):
        self.account_holder = account_holder
        self.balance = float(initial_balance)

    def deposit(self,amount):
        if amount > 0 :
            self.balance += amount
            print (f"[{self.account_holder}] Deposited : {amount:.2f} | New Balance : {self.balance:.2f}") 


    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print (f"[{self.account_holder}] Withdraw : {amount:.2f} | New Balance : {self.balance:.2f}")  

        else:
            print(f"[{self.account_holder}] Transaction Failed: Insufficient funds!")


    def chekc_balance(self):
        print(f"Holder : [{self.account_holder}] | Current Balance : {self.balance}") 



a1 =  BankAccount("Chirag Jogi", 10000)
a2 = BankAccount("Rohit Sharma" , 15000)

a1.chekc_balance()
a2.chekc_balance()

# Deposit 
a1.deposit(5000)
a2.deposit(7000) 

# withdraw

a1.withdraw(10000)
a2.withdraw(12000)