from abc import ABC,abstractmethod


class BankAccount:
    def deposit(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass
    def checkbalance(self):
        print("You can check out your balance")
    def viewtransaction(self):
        print("You can see your transaction history")
        
class CurrentAccount(BankAccount):
    def deposit(self):
        print("Any time u can deposit")
    def withdraw(self):
        print("Unlimited withdraw")

class SavingAccount(BankAccount):
    def deposit(self):
        print("Any time u can deposit")
    def withdraw(self):
        print("Limited withdraw per month")

class FixedDeposit(BankAccount):
    def deposit(self):
        print("Only one time u can deposit")
    def withdraw(self):
        print("limited withdraw according to the time")

class SalaryAccount(BankAccount):
    def deposit(self):
        print("Only salary u can deposit")
    def withdraw(self):
        print("limted withdraw per month")

class JoinAccount(BankAccount):
    def deposit(self):
        print("u can do shared deposit")
    def withdraw(self):
        print("withdraw depends on base type")

class PensionAccount(BankAccount):
    def deposit(self):
        print("only pension deposit")
    def withdraw(self):
        print("limited withdraw per month")


print("Jyothsna Current Account")
jyothsna=CurrentAccount()
jyothsna.deposit()
jyothsna.withdraw()
jyothsna.checkbalance()
jyothsna.viewtransaction()


print("\nSandhya Saving Account")
sandhya=CurrentAccount()
sandhya.deposit()
sandhya.withdraw()
sandhya.checkbalance()
sandhya.viewtransaction()


print("\nShravani Fixed Deposit")
shravani=CurrentAccount()
shravani.deposit()
shravani.withdraw()
shravani.checkbalance()
shravani.viewtransaction()

print("\nHarini Salary Account")
harini=CurrentAccount()
harini.deposit()
harini.withdraw()
harini.checkbalance()
harini.viewtransaction()

print("\nSneha and Shashi Join Account")
ss=CurrentAccount()
ss.deposit()
ss.withdraw()
ss.checkbalance()
ss.viewtransaction()

print("\nJyothi Pension Account")
jyothi=CurrentAccount()
jyothi.deposit()
jyothi.withdraw()
jyothi.checkbalance()
jyothi.viewtransaction()

    
#Output:
'''
Jyothsna Current Account
Any time u can deposit
Unlimited withdraw
You can check out your balance
You can see your transaction history

Sandhya Saving Account
Any time u can deposit
Unlimited withdraw
You can check out your balance
You can see your transaction history

Shravani Fixed Deposit
Any time u can deposit
Unlimited withdraw
You can check out your balance
You can see your transaction history

Harini Salary Account
Any time u can deposit
Unlimited withdraw
You can check out your balance
You can see your transaction history

Sneha and Shashi Join Account
Any time u can deposit
Unlimited withdraw
You can check out your balance
You can see your transaction history

Jyothi Pension Account
Any time u can deposit
Unlimited withdraw
You can check out your balance
You can see your transaction history

'''