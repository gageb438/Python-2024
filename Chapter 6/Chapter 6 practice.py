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
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    
    # strips them of their '\n'
    line1 = line1.rstrip('\n')
    line2 = line2.rstrip('\n')
    line3 = line3.rstrip('\n')
    
    # prints them
    print(line1)
    print(line2)
    print(line3)