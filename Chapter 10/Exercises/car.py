class Cars():
    def __init__(self, model, make):
        self.__model = model
        self.__make = make
        self.__speed = 0
    
    def accelerate(self):
        self.__speed += 5
    
    def brake(self):
        self.__speed -= 5
    
    def get_speed(self):
        return self.__speed
    def get_model(self):
        return self.__model
    def get_make(self):
        return self.__make

    def __str__(self):
        return f"The {self.__make} {self.__model} is going {self.__speed} mph."
