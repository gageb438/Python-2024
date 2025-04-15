class CellPhone():
    # CellPhone recieves no arguments
    # it makes a cell phone object
    # and gives it a model, manufacturer, and price
    
    # initializes phone
    def __init__(self, manufacturer, model, price):
        self.__manufacturer = manufacturer
        self.__model = model
        self.__price = price
    
    # sets the manufacutrer
    def set_manufact(self, manufacturer):
        self.__manufacturer = manufacturer
    
    # sets the model
    def set_model(self, model):
        self.__model = model
    
    # sets the price
    def set_retail_price(self, price):
        self.__price = price
    
    def get_manufact(self):
        return self.__manufacturer
    
    def get_model(self):
        return self.__model
    
    def get_retail_price(self):
        return self.__price