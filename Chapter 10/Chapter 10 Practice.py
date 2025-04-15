import coin

def main():
    # main accepts no arguments
    # it uses an obect my_coin using the Coin class in coin.py
    # it uses the get_sideup() method in the Coin to dispaly the starting state
    # it loops 10 times, tossing the coin with the toss() method
    # and displaying the side again with the get_sideup() method
    
    my_coin = coin.Coin()
    print(f"This side is up {my_coin.get_sideup()}")
    print("Tossing the coin ten times...\n")
    
    for num in range(1,10 + 1):
        my_coin.toss()
        print(f"Toss {num}: {my_coin.get_sideup()}")
        