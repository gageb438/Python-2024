import coin

def main():
  # coin main accepts no arguments
  # it uses the Coin class to create an object

  # Create an object from the coin class
  my_coin = coin.Coin()

  # display the side of the coin that is facing up
  print(f"This side is up: {my_coin.get_sideup())}.")

  # toss the coin
  print("Tossing the coin...")
  my_coin.toss()

  # display the side of the coin that is facing up
  print(f"This side is up: {my_coin.get_sideup())}.")

# call the main funciton to flip the coin
main()
