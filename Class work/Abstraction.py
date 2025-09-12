from abc import ABC, abstractmethod  

class BankAccount(ABC):  
    def __init__(self, account_holder, balance=0):  
        self.account_holder = account_holder  
        self.balance = balance  

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")

    @abstractmethod  
    def withdraw(self, amount):  
        pass  

class SavingsAccount(BankAccount):  
    def withdraw(self, amount):  
        if amount > self.balance:  
            print("Insufficient balance!")  
        else:  
            self.balance -= amount  
            print(f"{amount} withdrawn. New balance: {self.balance}")  

class CurrentAccount(BankAccount):  
    def withdraw(self, amount):  
        if amount > self.balance + 5000:  
            print("Overdraft limit exceeded!")  
        else:  
            self.balance -= amount  
            print(f"{amount} withdrawn. New balance: {self.balance}")  

savings = SavingsAccount("Alice", 10000)  
current = CurrentAccount("Bob", 2000)  

savings.deposit(2000)  # Alice deposits ₹2000  
savings.withdraw(5000)  # Alice withdraws ₹5000  
savings.withdraw(8000)  # Insufficient balance  

current.deposit(3000)  # Bob deposits ₹3000  
current.withdraw(6000)  # Allowed due to overdraft  
current.withdraw(8000)  # Overdraft limit exceeded!  
