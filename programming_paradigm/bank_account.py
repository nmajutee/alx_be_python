# 
class BankAccount:
    def __init__(self, account_balance = 0):
        self.account_balance = account_balance
    
    def deposit(self, amount):
       if amount > 0:
           self.account_balance += amount
           return f"Deposited {amount}. New balance: {self.account_balance}"
       else:
           return f"Invalid deposit amount"
           
    def withdraw(self, amount):
        if amount > 0 and amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False
    def display_balance(self):
        balance = self.account_balance
        print(f"Current Balance: ${balance:.2f}")
