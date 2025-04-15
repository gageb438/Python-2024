import bankaccount

def main():#10-8
    # main accepts no arguments
    # it accepts input for a starting balance
    # it lets them deposit money and withdraw
    
    balance = 0
    go = True
    
    # get their starting balanace
    while go == True:
        try:
            balance = float(input("Enter a starting balance: "))
            go = False
        except:
            print("Must be a number.")
            
    account = bankaccount.BankAccount(balance)
    
    go = True
    while go == True:
        try:
            paycheck = float(input("Enter the amount of your paycheck to deposit: "))
            go = False
        except:
            print("Must be a number.")
    
    account.deposit(paycheck)
    
    print(account.__str__())
    
    #print(f"\nThe balance is ${account.get_balance():,.2f}")
    
    withdraw = input("How much would you like to withdraw: ")
    account.withdraw(withdraw)
    
    #print(f"\nThe balance is {account.get_balance():,.2f}")
    
    print(account.__str__())