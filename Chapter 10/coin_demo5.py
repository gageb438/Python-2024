import coin

def main():
    # main accepts no arguments
    # it flips 3 coins
    # it outputs each of their faces
    
    coin1 = coin.Coin()
    coin2 = coin.Coin()
    coin3 = coin.Coin()
    
    print("Your three coins are facing...")
    
    print(f"Coin 1 is: {coin1.get_sideup()}\nCoin 2 is: {coin2.get_sideup()}\nCoin 3 is: {coin3.get_sideup()}")
    print("I am tossing your three coins...")
    
    # toss the coin
    coin1.toss()
    coin2.toss()
    coin3.toss()
    
    print("\nHere are your coins again after tossing them...")
    print(f"Coin 1 is: {coin1.get_sideup()}\nCoin 2 is: {coin2.get_sideup()}\nCoin 3 is: {coin3.get_sideup()}")