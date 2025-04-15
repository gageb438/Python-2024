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
        if float(amount) >= float(self.__balance):
            print("Error: Insufficent funds")
        else:
            self.__balance -= float(amount)
            print("Withdrawl successful")
    
    # the get_balance method returns the account balance
    def get_balance(self):
        return self.__balance
    
    def __str__(self):
        return f"The balance is ${self.__balance:,.2f}"