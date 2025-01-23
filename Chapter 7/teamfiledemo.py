import random

def main():
  # main recieves no arguments
  # main handles everything in the program
  try:
    games = int(input("How many games would you like to play? : "))
    while games < 0:
      games = int(input(":> "))
      
  except:
    print("Please enter a valid number.")
  
  for game in range(games):
      # get the first dice list
      dice_list = first_roll()
      
      # find the mode
      mode = find_mode(dice_list)
      
      # find which dice need to be rerolled
      indexes = list_unmatched(dice_list, mode)
      print(dice_list)
      print(mode)
      print(indexes)
      
      dice_list = reroll_many(dice_list, indexes)

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
    
    print(dice_list)
    return dice_list

def reroll_one(dice_list, index):
    # reroll one recieves an argument for the dice list
    # it also recieves an argument for the index on the list that needs
    # rerolled.
    # it uses roll_die to reroll that dice.
    
    new_die = roll_die()
    
    dice_list[index] = new_die
    
    return dice_list
main()
