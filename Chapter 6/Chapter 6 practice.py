def overWriteAll():
    # overWriteAll overwrites all files
    outfile = open('lotr.txt', 'w')
    outfile = open('friends.txt', 'w')
    
    outfile.close()

def fileWrite():
    #file write recieves no arguments
    #it opens a file named lotr.txt
    # and writes 3 lotr characters to the file
    
    # open file
    outfile = open("lotr.txt", "w")
    
    # write three lotr names.
    outfile.write("Frodo Baggins\n")
    outfile.write("Gandalf\n")
    outfile.write("Aragorn\n")
    
    # close the file
    outfile.close

def fileRead():
    # file read recieves no arguments
    # it opens a file named lotr.txt and reads the txt file to an object.
    # it then prints the file contents
    
    # open the file
    infile = open("lotr.txt", "r")
    
    # read the contents
    file_contents = infile.read()
    
    # close the file
    infile.close()
    
    # print the contents
    print(file_contents)

def readLine():
    # readl ine recieves no arguments
    # it reads each line one by one
    # prints each line
    
    #open the file
    infile = open("lotr.txt", "r")
    
    # read the lines
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    
    # close the file
    infile.close()
    
    # print the lines
    print(line1)
    print(line2)
    print(line3)

def writeNames():
  # write names receives no arguments
  # it prompts the user to enter 3 names
  # and assigns them each to a unique variable
  # it openes friends.txt and writes the names to the file
  # on it's own line in the file
  
  print("Please enter the names of three friends.")
  friend1 = input("Friend 1: ")
  friend2 = input("Friend 2: ")
  friend3 = input("Friend 3: ")
  
  # open the file
  outfile = open("friends.txt", "a")
  
  outfile.write(friend1 + '\n')
  outfile.write(friend2 + '\n')
  outfile.write(friend3 + '\n')
  
  # closes the file
  outfile.close()

def strip_newline():
    # strip new line recieves no arguments
    # it opens the file lotr.txt
    # it strens the newline \n characters from each line
    # and prints the lines
    
    # opens the file
    infile = open("lotr.txt", "r")
    
    # read the lines
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    
    # strip the \n characters
    line1 = line1.rstrip('\n')
    line2 = line2.rstrip('\n')
    line3 = line3.rstrip('\n')
    
    # closes the file
    infile.close()
    
    # prints the lines
    print(line1)
    print(line2)
    print(line3)
  
def writeNumbers():
    # write numbers accepts no arguments
    # it takes input from the user in the form of three integers
    # it opens the file numbers.txt
    # and writes three numbers to the file as strings
    
    number1 = int(input("Please enter a number: "))
    number2 = int(input("Please enter a number: "))
    number3 = int(input("Please enter a number: "))
    
    outfile = open("numbers.txt", "w")
    
    outfile.write(str(number1) + '\n')
    outfile.write(str(number2) + '\n')
    outfile.write(str(number3) + '\n')
    
    outfile.close()
    
    print()
    print("Your numbers have been written to numbers.txt")

fileWrite()
fileRead()
readLine()
writeNames()
strip_newline()
writeNumbers()
