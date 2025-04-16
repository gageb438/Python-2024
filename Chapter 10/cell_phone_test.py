import cellphone

def main():
    # main recieves no arguments
    # it asks the user for a phone
    # and it creates an object with all the attributes
    
    # print the header
    print("Welcome to the Galactic Phone Database.")
    
    # get info
    manufacturer = input("Enter the phone manufacturer: ")
    model_number = input("Enter the phone model number: ")
    price = input(f"Enter the retail price for your {manufacturer}, model {model_number}: ")
    
    # make an object
    my_phone = cellphone.CellPhone(manufacturer, model_number, price)
    
    # set the info to the objects info
    manufacturer = my_phone.get_manufact()
    model_number = my_phone.get_model()
    price = my_phone.get_retail_price()
    
    # output the object
    print("\nHere is the data you entered: ")
    print(f"Manufacturer {manufacturer}")
    print(f"Model: {model_number}")
    print(f"Retail Price: ${float(price):.2f}")

main()