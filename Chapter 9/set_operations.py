def set_main():
    # set_main recieves no arguments
    # it is a function to output all outputs
    # listed in 9-3
    
    # initalize default sets
    softball = set(["Jodi", "Carmen", "Aida", "Alicia"])
    basketball = set(["Eva", "Carmen", "Alicia", "Sarah"])
    
    # print the people on the softball team
    print("The following people are on the softball team:")
    for person in softball:
        print(person)
    
    print()
    
    # print the people on the basketball team
    print("The following people are in the basketball team:")
    for person in basketball:
        print(person)
    
    print()
    
    # get the people in both teams
    both = softball | basketball
    
    # print the people in both
    print("The folowing students play both softball AND basketball:")
    for person in both:
        print(person)
        
    print()
    
    # get the people in only one sport
    only_one = softball ^ basketball
    
    print("The following students play either softball OR basketball:")
    for person in only_one:
        print(person)
        
    print()
    
set_main()