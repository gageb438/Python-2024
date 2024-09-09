def example1():
    # exmaple1 accepts no arguments
    # it takes input from the user
    # and outputs a response based on the input
    
    choice = int(input("Enter 1 to continue..."))
    
    if choice == 1:
        # then this code will run
        print("Continuing...")
        # and this will run
        print("Continuing...")
        # and this
        print("and... continuing...")
    # this will run no matter what happens
    print("The program has completed")
    

def test_average():
    # test_average accepts no arguments
    # asks the user for test scores and averages them
    # outputs the average score and a congratulations if it is over 95.
    
    # assigns all 3 scores
    firstScore = float(input("Enter the first score: "))
    secondScore = float(input("Enter the second score: "))
    thirdScore = float(input("Enter the third score: "))
    highScore = 95.00
    # finds the average score
    averageScore = ((firstScore + secondScore + thirdScore) / 3)
    
    # prints the average score
    print("The average score is: %", format(averageScore, '.2f'), sep = '')
    
    # if the average score is greater than or equal to 95.00 it prints "Congratulations!" "Thats a high score!"
    if averageScore > highScore:
        print("Congratulations!")
        print("Thats a high score!")