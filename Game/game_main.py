import random
import game_classes

def intro():
    # intro recieves no arguments
    # it teaches the user the options they have
    # and creates the player
    # and how to interact

    # start off by creating the player
    print("You wake up in a grimy, messy, and stuffy dark room. You look around, theres a paper, you decide to go to it and read.")
    
    first_name = input("[Paper] : Please write your first name : ")
    last_name = input(f"[Paper] : Please write your last name : ")

    print("The moment you write your first and last name, text in red appears on the paper.")
    
