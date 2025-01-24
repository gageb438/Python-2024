global game_number
global roll_number
game_number = 0
roll_number = 0

import random
import time
import os

def main():
    # main recieves no arguments
    # main handles everything in the program
    
    # check that the highscore file exists
    if os.path.exists("high_score.txt"):
        highscore = open("high_score.txt","r")
        highscor = highscore.readline()
        print(f"High score found of {highscor}")
        highscore.close()
    else:
        print("Highscore not found. Generating high score.")
        highscore = open("high_score.txt", "w")
        highscore.write("9" * 99)
        highscore.close()
    
    try:
        games = int(input("How many games would you like to play? : "))
        while games < 0:
            games = int(input(":> "))
    except: 
        print("Please enter a valid number.")

    for game in range(games):
        # reset the game number
        global game_number
        global roll_number
        game_number += 1
        roll_number = 0
        # get the first dice list
        dice_list = first_roll()

        # wipe indexes and index variables
        indexes = [0]

        while indexes != []:
            # output the dice
            display_rolls(dice_list)

            # find the mode
            mode = find_mode(dice_list)

            # find which dice need to be rerolled
            indexes = list_unmatched(dice_list, mode)

            # remake the dice list
            dice_list = reroll_many(dice_list, indexes)

        # check if they got the highscore
        try:
            highscore_file = open("high_score.txt", "r")
            highscore = int(highscore_file.readline())
            highscore_file.close()
            if roll_number < highscore:
                print(f"New highscore of {roll_number} rolls!")
                # request and input to continue
                input("Press enter to continue.")

                # write the highscore to the file
                highscore_file = open("high_score.txt", "w")
                highscore_file.write(str(roll_number))
                highscore_file.close()
        except Exception as err:
            print(err)
        input("Press enter to continue...")

def first_roll():
    # first_roll recieves no arguments
    # it creates a list with 12 random die.
    # uses roll_die to roll each dice one at a time
  
    DIE_AMOUNT = 12
    dice_list = []
    
    for die in range(DIE_AMOUNT):
        dice_rolled = roll_die()
        dice_list.append(dice_rolled)
  
    return dice_list
  
def roll_die():
    # roll die recieves no arguments
    # it rolls a dice and returns the value
  
    die = random.randint(1,6)
    return die
    
def count_frequency(dice_list, number):
    # count frequency recieves an argument for a number 
    # and the dice list.
    # it counts the time that the number occurs in dice_list
    
    frequency = dice_list.count(number)
    
    return frequency
    
def find_mode(dice_list):
    # find mode accepts an argument for the dice list
    # it uses count_frequency to return the mode.
    
    NUMBERS = [1,2,3,4,5,6]
    frequency_list = []
    counter = 0
    
    for number in range(6):
        counter += 1
        frequency = count_frequency(dice_list, counter)
        frequency_list.append(frequency)
    
    # find the max on that list
    mode_number = max(frequency_list)
    mode_index = frequency_list.index(mode_number)
    mode = NUMBERS[mode_index]
    
    return mode
    
def list_unmatched(dice_list, mode):
    # list_unmatched recieves an argument for the dice list and the mode
    # it checks which numbers on the dice list are not equal to the mode
    # it returns a list of indexes that need to be rerolled
    
    indexes = []
    index = -1
    
    for number in dice_list:
        index += 1
        if number != mode:
           indexes.append(index)
    
    return indexes

def reroll_many(dice_list, indexes):
    # reroll many accepts a list for the indexes of the dice
    # and a list of the dice
    # it rerolls every index on that list
    
    for index in indexes:
        dice_list = reroll_one(dice_list, index)
    
    return dice_list

def reroll_one(dice_list, index):
    # reroll one recieves an argument for the dice list
    # it also recieves an argument for the index on the list that needs
    # rerolled.
    # it uses roll_die to reroll that dice.
    
    new_die = roll_die()
    
    dice_list[index] = new_die
    
    return dice_list

def display_rolls(dice_list,):
    # display_rolls accepts an argument for the list of dice
    # it prints the dice and the roll number for each one
    
    # access global variables
    global roll_number
    
    # add onto the roll number
    roll_number += 1
    
    # print the header
    print(f"\n---Roll Number {roll_number}---")
    
    # begin to read the list and initalize a counter
    counter = 0
    
    for die in dice_list:
        # add onto the counter
        counter += 1
        print(f"Dice #{counter}:\t{die}")
    time.sleep(.5)
main()
