class Pets():
    # the pet class creates a pet object with a name,
    # animal type, and age
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
      
    # setter methods
    def set_name(self, name):
        self.__name = name
    
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type
    
    def set_age(self, age):
        self.__age = age
        
    # getter methods
    def get_name(self):
        return self.__name
    
    def get_animal_type(self):
        return self.__animal_type
    
    def get_age(self):
        return self.__age
    
    def __str__(self):
        return f"{self.__name} is a {self.__animal_type} and is {self.__age} years old."
