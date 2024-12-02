# import area
import random
import math

#==========================

def fileWrite(): # program6-1
    # fileWrite recieves no arguments
    # it opens file lotr.txt
    # and writes the names of three lotr characters.
    
    # opens the file
    outfile = open("lotr.txt", "w")
    
    # writes three lotr character names
    outfile.write("Sauron\n")
    outfile.write("Galadriel\n")
    outfile.write("Frodo Baggins\n")
    
    # closes the file
    outfile.close()
    
#==========================
    
def fileRead(): # program6-2
    # fileRead recieves no arguments
    # it opens the file lotr.txt
    # and reads the names of three lotr characters
    # prints them
    
    # opens the file
    infile = open("lotr.txt", "r")
    
    # reads the lotr character names
    fileNames = infile.read()
    
    # close the file
    infile.close()
    
    # print the names
    print(fileNames)
    
#==========================
    
def lineRead(): # program6-3
    # lineRead accepts no arguments
    # it opens the file lotr.txt
    # and reads the content of the file one line at a time
    # it then outputs the contents of the file
    
    # opens the file
    infile = open("lotr.txt", "r")
    
    # read the character names one line at a time
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    
    # closes the file
    infile.close()
    
    # prints the names
    print(line1)
    print(line2)
    print(line3)
    
#==========================
    
def writeNames(): # program6-4
    # writeNames accepts no arguments
    # it prompts the user for the names of three friends
    # and assigns each name to a unique variable
    # it opens friends.txt and writes each name to the file
    # on it's own line in the file
    
    print("Please enter the names of three friends.")
    
    # asks for the names
    friend1 = input("Friend 1: ")
    friend2 = input("Friend 2: ")
    friend3 = input("Friend 3: ")
    
    # opens the file
    friendsFile = open('friends.txt', 'w')
    
    # writes the names
    friendsFile.write(friend1 + '\n')
    friendsFile.write(friend2 + '\n')
    friendsFile.write(friend3 + '\n')
    
    # closes the file
    friendsFile.close()
    
    print("Names successfully written to 'friends.txt'")
    
#==========================
    
def strip_newline(): #program6-5
    # strip newline accepts no arguments
    # it opens the file lotr.txt and reads each line
    # it strips the newline '\n' characters from each line
    # and prints the lines
    
    # opens the file
    infile = open('lotr.txt', 'r')
    
    # reads the lines
    line1 = infile.readline().rstrip('\n')
    line2 = infile.readline().rstrip('\n')
    line3 = infile.readline().rstrip('\n')
    
    # prints them
    print(line1)
    print(line2)
    print(line3)

#==========================
    
def writeNamesMod(): # program6-5 md
    # writeNames accepts no arguments
    # it prompts the user for the names of three friends
    # and assigns each name to a unique variable
    # it opens friends.txt and writes each name to the file
    # on it's own line in the file
    
    print("Please enter the names of three friends.")
    
    # asks for the names
    friend1 = input("Friend 1: ")
    friend2 = input("Friend 2: ")
    friend3 = input("Friend 3: ")
    
    # opens the file
    friendsFile = open('friends.txt', 'a')
    
    # writes the names
    friendsFile.write(friend1 + '\n')
    friendsFile.write(friend2 + '\n')
    friendsFile.write(friend3 + '\n')
    
    # closes the file
    friendsFile.close()
    
    print("Names successfully written to 'friends.txt'")
    
#==========================

def writeNumbers(): # program 6-6
    # write numbers accepts no arguments
    # it takes input from the user in the form of three integers
    # it opens the file numbers.txt
    # and writes the three numbers to the file as strings
    
    # asks for the numbers
    num1 = int(input("Please enter a number: "))
    num2 = int(input("Please enter a number: "))
    num3 = int(input("Please enter a number: "))
    
    # opens the file
    numbersFile = open('numbers.txt', 'w')
    
    numbersFile.write(str(num1) + '\n')
    numbersFile.write(str(num2) + '\n')
    numbersFile.write(str(num3) + '\n')
    
    # closes the file
    numbersFile.close()
    
    print("Your numbers have been written to numbers.txt")
    
#==========================
    
def readNumbers(): # program6-7
    # read numbers accepts no arguments
    # it opens the file numbers.txt and reads in each line
    # converting each from a string to an integer
    # it totals and outputs the three numbers and their total
    
    # open the file
    infile = open("numbers.txt", 'r')
    
    # read in the numbers and convert to an int
    num1 = int(infile.readline())
    num2 = int(infile.readline())
    num3 = int(infile.readline())
    
    # close the file
    infile.close()
    
    # perform calculations and output the result
    total = num1 + num2 + num3
    
    print(f"Here is your problem: {num1} + {num2} + {num3} = {total}")
    
#==========================
    
def writeSales(): # program 6-8
    # write sales accepts no arguments
    # it prompts the user for the number of days for to input sales
    # for each iteration it writes the sale to the file sales.txt
    # after all days have been processed
    # it closes the file and outputs a message
    
    days = int(input("How many days do you want to enter the sales for? :> "))
    
    # open the file
    salesFile = open('sales.txt', 'w')
    
    for dayCounter in range(1, days + 1):
        daySale = input(f"Enter the sales for day #{dayCounter} :> ")
        salesFile.write(daySale + '\n')
        
    # close the file
    salesFile.close()
    
    print("All data has been saved to sales.txt.")
    
#==========================
    
def readSales(): # program 6-9
    # readSales accepts no argument
    # it opens and reads from sales.txt
    # it loops until it reaches the end of the file
    # each iteration of the loop will output the amount
    # and read the next line
    
    # open the file
    salesFile = open("sales.txt", 'r')
    
    # read the first line
    line = salesFile.readline()
    
    # loop while the line isnt blank
    while line != '':
        amount = float(line)
        
        # print the amount
        print(f"${amount:,.2f}")
        
        line = salesFile.readline()
        
    # close the file
    salesFile.close()
    
#==========================
    
def readSales2(): # program 6-10
    # read sales accepts no arguments
    # it opens and reads from sales.txt
    # it loops for each line in the file
    # and outputs the line
    
    # open the file
    salesFile = open("sales.txt", 'r')
    
    for line in salesFile:
        # make it a float
        amount = float(line)
        
        # output the amount
        print(f"${amount:,.2f}")
    
    # close the file
    salesFile.close()
    
#==========================
    
def writeVideoTimes(): # program 6-11
    # writevideoTimes accepts no arguments
    # it asks the user for how many videos are in the project and how long the video is
    # it loops for the total videos
    # writes the length to a file
    # writes all to video_times
    
    videos = int(input("How many videos are in the project? :> "))
    
    # opens the file videoTimes
    videoTimes = open("videoTimes.txt", 'w')
    
    for video in range(1, videos + 1):
        time = input(f"Enter the time for video #{video}: ")
        
        # write the time
        videoTimes.write(time + '\n')
        
    # close the file
    videoTimes.close()
    
    # prints closing statement
    print("All times have been written to videoTimes.txt.")

#==========================
    
def readVideoTimes(): # progrma 6-12
    # readVideoTimes accpets no arguments
    # it reads each line from videoTimes.txt
    # it outputs the times of the videos and the total running time of all seconds
    
    # initialize variable
    total = 0
    lineNumber = 0
    
    # open the file
    videoTimes = open("videoTimes.txt", 'r')
    
    for line in videoTimes:
        # makes the number a float
        time = float(line)
        
        lineNumber = lineNumber + 1
        # adds to the total
        total = total + time
        
        print(f"Video #{lineNumber} time: {time} seconds")
        
    print(f"Total running time of all videos is {total} seconds.")
    
#==========================
    
def crash():
    # crash accepts no arugments
    # it tries to perform division by 0
    
    numerator = int("12a")
    denominator = 0
    
    # perform division
    total = numerator / denominator
    
    print(total)
    
#==========================

def gross_pay1(): # progrma 6-22
    # gross pay 1 accepts no arguments
    # it prompts the user for hours worked and hourly pay
    # it calculates the gross pay = hours * rate and outputs the result
    
    try:
        # get input from the user
        hours = int(input("Enter the number of hours worked: "))
        rate = float(input("Enter the pay rate: "))
        
        pay = hours * rate
        
        print(f"Gross pay: ${pay:,.2f}")
    except ValueError as err:
        print(f"Error: {err}")
        print("ERROR: Hours worked and hourly rate must be vaid integers. ")
        
#==========================
        
def display_file1(): #program 6-24
    # display file 1 accepts no arguments
    # takes input from the user for a filename to open
    # and reads the contents of the file
    
    # get input from the user
    filename = input("Enter the filename to open: ")
    
    try:
        # opens the file and read the contents
        infile = open(filename, 'r')
        contents = infile.read()
        
        # output and close the file
        print(contents)
        infile.close()
    except IOError:
        print("File does not exist.")

#==========================
        
def sales_report1():
    # sales report 1 accepts no arguments
    # it opens a file sales_data.txt to read
    # it accumulates the total for each line in the file
    
    # initialize the total
    total = 0
    
    try:
        # open the file
        sales_data = open("sales_data.txt", "r")
        
        # loop for each line and accumulate the valu
        for line in sales_data:
            amount = float(line)
            total += amount
        
        # close thew file
        sales_data.close()
        
        # output the data
        print(format(total, ",.2f"))
        
    except IOError:
        print("ERROR: An error occured trying to read the file.")
    except ValueError:
        print("ERROR: Non-numeric data found, calculations haulted.")
    # catch final exceptions
    except:
        print("ERROR: A problem was encountered")