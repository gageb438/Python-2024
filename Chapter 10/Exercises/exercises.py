import pet
import car
import pickle
import os
import random
import question

def pet_driver():
    # pet driver recieves noa rguments
    # it drives the pet class
    # it outputs a menu
    # and does what the option was
    
    def menu():
        # menu recieves no arguments
        # it prints the menu, returns the choice
        
        # initialize choices
        choices = [1,2,3,4,5]
        choice = -1
        
        print("1) Add a pet\n2) Modify a pet\n3) Display a pet\n4) Display all pets\n5) Quit")
        while choice not in choices:
            try:
                choice = int(input("Enter a choice: "))
            except:
                pass
        
        if choice == 1:
            add_pet()
        elif choice == 2:
            modify_pet()
        elif choice == 3:
            display_pet()
        elif choice == 4:
            display_all()
        else:
            print("Goodbye.")
        
        return choice
    
    def add_pet():
        # add a pet recieves no arguments
        # it adds a pet to the pet list
        
        # initialize data
        data = []
        
        # get info
        print()
        name = input("Enter the pets name: ")
        typee = input("Enter the pets type: ")
        age = input("Enter the pets age: ")
        print()
        
        if os.path.exists("pets_data.dat"):
            file = open("pets_data.dat", "rb")
            
            # account for empty file
            try:
                data = pickle.load(file)
            except:
                data = []
            
            # close
            file.close()
        else:
            # create and close
            file = open("pets_data.dat", "wb")
            file.close()
            
        pet_obj = pet.Pets(name, typee, age)
        data.append(pet_obj)
        
        file = open("pets_data.dat", "wb")
        pickle.dump(data, file)
        file.close()
        
        return
    
    def modify_pet():
        # modify pet modifies a pet
        # and re-writes the file
        
        if not os.path.exists("pets_data.dat"):
            print("No pets stored, returning to menu! Add some before trying to find.")
            return
        
        file = open("pets_data.dat", "rb")
        data = pickle.load(file)
        
        # get the pets name to find
        name = input("Enter the name of the pet you want to modify(CASE SENSITIVE): ")
        
        for item in data:
            if item.get_name() == name:
                typee = input("Enter the pets type: ")
                age = input("Enter the pets age: ")
                
                item.set_animal_type(typee)
                item.set_age(typee)
            else:
                print("Pet not found.")
                
        file.close()
        
    def display_pet():
        # display pet recieves no arguments
        # it displays the requested pet
        # and outputs it
        
        if os.path.exists("pets_data.dat"):
            file = open("pets_data.dat", "rb")
            
            pet_name = input("What is the name of the pet? (CASE SENSITIVE): ")
            data = pickle.load(file)
            for item in data:
                if item.get_name() == pet_name:
                    print()
                    print(item)
                    print()
                    printed = True
            if printed != True:
                print("Pet not found.")
        else:
            print("\nNo pets stored, returning to menu! Add some before trying to find.\n")
            return
        file.close()
    
    def display_all():
        # display all receieves no argument
        # it reads the whole fiel
        # and displays everything
        if os.path.exists("pets_data.dat"):
            file = open("pets_data.dat", "rb")
        else:
            print("\nNo pets stored, returning to menu! Add some before trying to find.\n")
            return
        
        data = pickle.load(file)
        for item in data:
            print()
            
        file.close()
    
    choice = 1
    
    while choice != 5:
        choice = menu()

def car_driver():
    # car driver recieves no arguments
    # it speeds the car up by 5
    # and slows it by 5
    # while printing the speed

    # get the make and model
    make = input("What is the make of the car?\n:> ")
    model = input("What is the model of the car?\n:> ")

    # make the object
    myCar = car.Cars(model, make)

    # make it accelerate 5 times
    for num in range(5):
        myCar.accelerate()
        print("Accelerating.")

        print(myCar)

    # make it deccalerate 5 times
    for num in range(5):
        myCar.brake()
        print("Braking")

        print(myCar)

def trivia_game():
    # trivia game recieves no arguments
    # it asks players between science, math, and history
    # it outputs a qustion, with a set of possible answers
    
    # create the questions
    science = [
        question.Question("What does DNA stand for?", ["Deoxy-ribose nucleic acid", "Ribose nucleic acid", "Nucleic acid", "Deoxy-ribose acid"], "Deoxy-ribose nucleic acid"),
        question.Question("How many bones are in the human body?", ["201", "212", "206", "200"], "206"),
        question.Question("Who discovered gravity?", ["Albert Einstein" ,"Isaac Newton", "Galileo Galilei", "Nikola Tesla"], "Isaac Newton"),
        question.Question("What is the hardest natural substance on earth?", ["Carbon", "Iron", "Steel", "Diamond"], "Diamond"),
        question.Question("What is the main gas that takes up Earth's Atmosphere?", ["Nitrogen", "Oxygen", "Carbon-Dioxide", "Hydrogen"], "Nitrogen"),
        question.Question("Humans and chimpanzees share roughly how much DNA?", ["95 per cent", "98 per cent", "96 per cent", "93 per cent"], "98 per cent"),
        question.Question("At what temperature are Clesius and Fahrenheit equal?", ["0 degrees", "-40 degrees", "80 degrees", "-80 degrees"], "-40 degrees"),
        question.Question("What is the only metal that is liquid at room teperature?", ["Steel", "Nickel", "Iron", "Mercury"], "Mercury"),
        question.Question("What does a Geiger counter measure?", ["Radiation", "Temperature", "Distance", "Place"], "Radiation"),
        question.Question("What is the largest desert on Earth?", ["Sahara", "Arabian", "Gobi", "Antarctic"], "Antarctic") 
    ]

    math = [
        question.Question("What famous Greek mathmatician, who wrote The Elements, is known as the Father of Geometry", ["Isaac Newton", "Albert Einstein", "Galileo", "Oppenheimer"], "Isaac Newton"),
        question.Question("What famous German mathmatician is best known for his contributions in the field of statistics and Gaussian distribution, which we know as today as the normal distribution curve?", ["Carl Gauss", "Jane Gauss", "David guass", "Max Gauss"], "Carl Gauss"),
        question.Question("What famous mathmatician and philosopher developed the Cartesian coordinate system in the 17th-century", ["Robert Hook", "Margaret Avendish", "Rene Descartes", "Gottfried Leibniz"], "Rene Descartes"),
        question.Question("What famous Greek mathmetician is known for having accurately calculated the circumference of the planet Earth using only shadows and simple geometry?", ["Eratosthenes", "Aristotle", "Socrates", "Alan"], "Eratosthenes"),
        question.Question("True or false: 51 is a prime number", ["True", "False"], "False"),
        question.Question("True or false: 64 is both a Perfect Square", ["True", "False"], "True"),
        question.Question("What is the smallest positive integer that is divisible by both 6 and 8?", ["24", "21", "28", "32"], "24"),
        question.Question("In the famous Netflix show Stranger Things, the young characters frequently refer to this branch of mathematics as it relates to an alternate dimensions, which they call the upside down", ["Quantum Physics", "Quantum Mechanics"], "Quantum Mechanics"),
        question.Question("This fraction represents the odds of flipping a coin four times in a row and each time it landing on heads.", ["1/16", "1/8", "1/4", "1/2"], "1/16"),
        question.Question("This statistical measure of central tendency represents the middle value in a data set when the numbers are arranged from smallest to largest.", ["Mean", "Median", "Mode", "Outlier"], "Median")
    ]

    history = [
        question.Question("How many wives did Henry VIII have?", ["4", "5", "6", "7"], "6"),
        question.Question("Francisco Franco ruled which European country from 1939 to 1975?", ["Russia", "Spain", "Portugal", "Germany"], "Spain"),
        question.Question("What type of boats did the Vikings use when exploring and raiding?", ["Longship", "Paddleboat", "Pirate Ship", "Canoes"], "Longship"),
        question.Question("In what year was the Concorde's first flight?", ["1969", "1950", "1942", "1977"], "1969"),
        question.Question("Which country did Germany invade to kickstart World War II?", ["Ukraine", "United States", "Poland", "Canada"], "Poland"),
        question.Question("What language was spoken in Ancient Rome?", ["English", "Latin", "Spanish", "Roman"], "Latin"),
        question.Question("Who discovered penicillin?", ["Alexander Fleming", "Marie Curie", "Albert Einstein", "Charles Darwin"], "Alexander Fleming"),
        question.Question("In what year did Pakistan gain independence from the UK?", ["1958", "1947", "1969", "1957"], "1947"),
        question.Question("In what year did the French Revolution start?", ["1753", "1794", "1789", "1723"], "1789"),
        question.Question("Who is said to be so beautiful that her face launched a thousand ships?", ["Helen of Troy", "Priam of Troy", "Hector of Troy", "Matthew of Troy"], "Helen of Troy")
    ]

    # get the player names
    player1 = input("Player 1, enter your name: ")
    player2 = input("Player 2, enter your name: ")

    # initialize score
    p1_score = 0
    p2_score = 0
    
    # initalize categories and choice
    categories = ["history", "math", "science"]
    p1_cata = " "
    p2_cata = " "

    # validate choice
    while p1_cata.lower() not in categories:
        print(f"{player1}, pick a category between history, math, and science.")
        p1_cata = input(":> ")
        
    while p2_cata.lower() not in categories:
        print(f"{player2}, pick a category between history, math, and science.")
        p2_cata = input(":> ")

    # set category and ask questions
    if p1_cata.lower() == "history":
        p1_cata = history
    elif p1_cata.lower() == "math":
        p1_cata = math
    else:
        p1_cata = science
    
    if p2_cata.lower() == "history":
        pw_cata = history
    elif p2_cata.lower() == "math":
        p2_cata = math
    else:
        p2_cata = science
    
    # ask questions
    print(f"{player1} these are your questions:")
    for count in range(5):
        q = random.choice(p1_cata)
        p1_cata.remove(q)

        q.question()
        correct = q.answer()
    
        if correct == True:
            p1_score += 1

    print(f"{player2} these are your questions:")
    for count in range(5):
        q = random.choice(p2_cata)
        p2_cata.remove(q)

        q.question()
        correct = q.answer()

        if correct == True:
            p2_score += 1
    
    if p1_score > p2_score:
        print(f"{player1} wins with {p1_score} points while {player2} had {p2_score} points.")
    elif p2_score > p1_score:
        print(f"{player2} wins with {p2_score} points while {player1} had {p1_score} points.")
    else:
        print(f"It was a tie! Both players had {p1_score} points.")
