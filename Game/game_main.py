import random
import game_classes

def intro():
    # intro recieves no arguments
    # it teaches the user the options they have
    # and creates the player
    # and how to interact
    def clearing():
        # start off by creating the player
        print("You wake up in a foggy clearing. You look around, theres a paper, you decide to go to it and read.")
    
        # get players name
        first_name = input("[Paper] : Please write your first name : ")
        last_name = input(f"[Paper] : Please write your last name : ")
    
        # get rid of paper
        print("The paper is quickly whisked away by a gust of wind.")
    
        # get their object
        player = game_classes.Hero(first_name, last_name, "fists")
        weapon = player.get_weapon()
        
        # print the location
        print("You now have a few options, the area to your north is clear, seemingly empty.")
        print("The area to your west is hard to see through, but you're still able to go there.")
        print("The area to your south and your east are covered in vines, too hard to pass through.")
        print("Hint: Type the direction alone to move.")
    
        # prime movement loop
        moving = False
        while moving == False:
            choices = ["north", "west", "hit", "dig", "fly", "jump"]
            choice = input("What would you like to do?\n:>")
        
            while choice.lower() not in choices:
                print(f"{choice} not recognized as a command.")
                choice = input("What would you like to do?\n:>")
    
            if choice == "hit":
                print(f"You swing with your {weapon}, hitting nothing.")
            elif choice == "dig":
                print(f"You try to dig with your {weapon}, making it no-where.")
            elif choice == "fly":
                print("Your not a bird!")
            elif choice == "jump":
                print("You jump.")
            elif choice == "north":
                slime_area()
            elif choice == "west":
                overly_strong_boss()
            else:
                print(f"Uh oh! We've encountered an error proccessing {choice} please restart the game!")   
                
    def overly_strong_boss():
        # overly strong boss recieves no arguments
        # its a boss in the training area meant to kill the player.
        # basically a way to skip the tutorial.

        
