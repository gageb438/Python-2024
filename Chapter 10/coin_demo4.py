# program 10-6 in coin_demo4.py
# import the coin module
import coin

def main(): #program 10-6
    # main accepts no arguments
    # it creates an object my_coin using the coin class in coin.py
    # it uses the get_sideup() method in the coin class to display the starting state
    # it loops 10 times, tossing the coin with the toss() method
    # and displaying the side again with the get_sideup() method

    # initialize the coin and the counter
    my_coin = coin.Coin()
    counter = 0

    # print the side up
    print(f"This side is up: {my_coin.get_sideup()}\nTossing the coin 10 times...")

    # loop for while the counter isnt 10
    while counter != 10:
        counter += 1

        # toss the coin
        my_coin.toss()

        # print the side that is up
        print(f"Toss {counter}: {my_coin.get_sideup()}")
main()
