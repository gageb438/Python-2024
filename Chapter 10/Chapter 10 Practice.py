class Dog:
    species = "Canis familaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # getter methods for the Dog class   
    def speak(self, sound):
        return f"{self.name} says {sound}."
    
    def __str__(self):
        return f"{self.name} is {self.age} years old."
    
    def breed(self, name, breed):
        return f"{self.name} is a {self.breed}"
    