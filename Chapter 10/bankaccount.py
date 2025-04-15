# the bank account class simulates a bank account

class BankAccount(): #10-7

    # the __init__ method accepts an argument for the account's balance.
    # it is assigned to the __ balance attribute

    def __init__(self, bal):
        self.__balance = bal
    
    # the deposit method makes a deposit into the account

    def deposit(self, amount):
        self.__balance += amount
    
    # the withdraw method makes a withdrawl from the account

    def withdraw(self, amount):
        if self.__balance > amount:
            self.__balance -= amount
        else:
            print("Error: Insufficenet funds")
    
    # the get balance method returns the account balance

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"The blaance is ${eslf.__balance:",.2f"}"
