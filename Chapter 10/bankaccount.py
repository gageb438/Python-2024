# bank account class makes a bank account

class BankAccount(): #10-7
    
    # init makes the balance
    def __init__(self, balance):
        self.__balance = balance
    
    # deposit lets them deposit
    def deposit(self, amount):
        self.__balance += amount
    
    # withdraw lets them witdhraw
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Error: Insufficent funds")
        elif:
            self.__balance -= amount
    
    # the get_balance method returns the account balance
    def get_balance(self):
        return self.__balance
    
