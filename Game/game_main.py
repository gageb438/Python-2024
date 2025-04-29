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
        player = game_classes.Hero(first_name, last_name, "fists", 5)
        weapon = player.get_weapon()
        
        # print the location
        print("\nYou now have a few options, the area to your north is clear, seemingly empty.")
        print("The area to your west is hard to see through, but you're still able to go there.")
        print("The area to your south and your east are covered in vines, too hard to pass through.")
        print("\nHint: Type the direction alone to move.")
    
        # prime movement loop
        moving = False
        while moving == False:
            choices = ["north", "west", "south", "east", "hit", "dig", "fly", "jump"]
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
                moving = True
                slime_area()
            elif choice == "west":
                overly_strong_boss(player)
                moving = True
            elif choice == "south" or choice == "east":
                print("You try to move through the vines, but find yourself back where you started.")
            else:
                print(f"Uh oh! We've encountered an error proccessing {choice} please restart the game!")   
                
    def overly_strong_boss(player):
        # overly strong boss recieves an argument for the playter
        # its a boss in the training area meant to kill the player.
        # basically a way to skip the tutorial.
  
        # create the boss
        user_moves = ["attack", "hit", "swing", "fight", "run", "hide"]
        boss = game_classes.Enemy("Zummie, the Guardian of the Forest", 1000, 1000, {"swings":50, "pokes":25, "kicks":200}, "tree branch")
  
        print(f"You've stepped into a dangerous area, {boss.get_name()} has arrived, beware he is very strong.")
        print("Hint: You have a few moves here, not every one of them is the right one.")
        while True:
            choice = input("What would you like to do?\n:>")
            
            # validate move
            while choice.lower() not in user_moves:
                print(f"{choice} not recognized as a command.")
                choice = input("What would you like to do?\n:>")
            
            # set the choice to lower
            choice = choice.lower()
            
            # if they attacked
            if choice == "attack" or choice == "swing" or choice == "hit" or choice == "fight":
                # attempt to figth
                print(f"You attempt to attack {boss.get_name()}...")
      
                # win/lose
                if random.randint(1,2) == 1:
                    # win condition, deal damage to boss
                    boss.lose_hp(player.get_dmg())
                    print(f"You land your hit on {boss.get_name()} dealing {player.get_dmg()}, leaving {boss.get_name()} at {boss.get_hp()}hp.")
                else:
                    # lose condition, nothing happens
                    print("You attack, but miss.")
            
                # have rick my boy make a move
                damage = boss.make_a_move()
                
                # make the player lose health
                player.lose_hp(damage)
                
                # check if they died
                if player.get_hp() == False:
                    print(f"You have died to {boss.get_name()}.")
                    # call dead function
                    dead()
                else:
                    print(f"Your health is now at {player.get_hp()}")
            
            if choice == "hide":
                print("You attempt to hide, but there is no cover near you.")
                # have the boss make a move in return
                damage = boss.make_a_move()
                
                # make the player lose health
                player.lose_hp(damage)
                
                # check if they died
                if player.get_hp() == False:
                    print(f"You have died to {boss.get_name()}.")
                    # call dead function
                    dead()
                else:
                    print(f"Your health is now at {player.get_hp()}")
            
            if choice == "run":
                print("You attempt to run, however the vines block your path, it appears {boss.get_name()} has blocked the way with some kind of magic.")
                
    clearing()
intro()
