import random
import game_classes

def tutorial():
    # tutorial recieves no arguments
    # it creates the player, and prompts for a tutorial of the game
    # it also introduces the systems for people new to the game
    
    # describe the scene
    print("You awake in a dark room, staring at the ceiling, not remembering anything.")
    
    # ask if they want to do the tutorial
    print("Would you like to recover your memory? (TUTORIAL, yes/no)")
    choice = input(":>")
    
    while choice.lower() != "yes" and choice.lower() != "no" and choice.lower() != "y" and choice.lower() != "n":
        choice = input(":>")
    
    # return if they didnt choose to do the tutorial
    if choice != "yes" and choice != "y":
        return
    
    # delete variables for optimization
    del choice

    # print the tutorial scene
    print("You are laying in bed, staring at a loudspeaker on the ceiling.")
    print("You need to see whats near, but your visions clouded, you can only see so much at one time.")
    print("[LOUDSPEAKER] Hints will appear throughout the game, recently someone has been messing with our systems, keep in mind, they are only real if they start with [HINT].")
    print("[LOUDSPEAKER] In the event you find a hint, contact our team, they'll figure it out.")
    print("[HINT] Type Look in the console to see your surroundings.")

    # get console input
    console = input(":>")
    
    if console.lower() == "look":
        # print scene
        print("You look around to see your surroundings.")
        print("You see a table, with a computer.")
        print("You see a loudspeaker on the ceiling.")
        print("You see a bed.")
        print("You see a metal door.")
        print("[HINT] Type the name of an item to interact with it, some actions are not undo-able once you make it, be careful.")
        
        # get console input again
        console = input(":>")

        # set the valid inputs
        valid_inputs = ["table", "computer", "loudspeaker", "speaker", "bed", "sleep", "door"]

        # validate the choice
        while console.lower() not in valid_inputs:
            print(f"{console} is not recognized as a valid command.")
            console = input(":>")
        
        # get users choice and print action
        if console.lower() == "table" or console.lower() == "computer":
            print("You move to the computer.")

            # since they chose the computer, print computers scene
            print("You open the computer on the table.")
            print("It appears to be a company computer.")
            print("Theres a few programs.")
            print("(HINT) Open the program called survey.exe")

            # get input again and set the valid inputs
            console = input(":>")
            valid_inputs = ["virus.exe", "look", "shutdown", "close"]
            
            # validate for the input
            while console.lower() not in valid_inputs:
                print(f"{console} not recognized as a valid command.")
                console = input(":>")
            
            console = console.lower()

            if console == "virus.exe":
                # this was the setup.
                print("[LOUDSPEAKER] Well we detected you opened virus.exe, that was one of the decoy hints, watch out for those, they are more dangerous than a simple announcement.")
                print("You close the program.")
            elif console == "look":
                print("You look at the programs on the computer.")
                print("You see a program called survey.")
                print("You see a program called contact.")
                print("You see a program called shutdown.")
                print("The virus.exe program deleted itself.")
                

        elif console.lower() == "loudspeaker" or console.lower() == "speaker":
            print("Its a loudspeaker. Used to send you messages from command.")
        elif console.lower() == "bed" or console.lower() == "sleep":
            print("Its a bed, no use going back to sleep.")
        elif console.lower() == "door":
            print("Its a locked door, no way for you to open it.")