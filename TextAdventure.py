# imports
import random

def maps():
    # maps recieves an argument for a list of points of interest in the map
    # it draws it out based off of that.
    
    map_design = ["O O O O O O O O O O",
                  "O O O O O O O O O O",
                  "O O O O O O O O O O",
                  "O O O O O O O O O O",
                  "O O O O O O O O O O",
                  "O O O O O O O O O O",
                  "O O O O O O O O O O",
                  "O O O O O O O O O O",
                  "O O O O O O O O O O",
                  "O O O O O O O O O O",
                  "O O O O O O O O O O",
                  "O O O O O O O O O O",
                  "O O O O O O O O O O"]
    for row in map_design:
        print(row)