import game_classes
weapon = input("Enter a weapon: ")
player = game_classes.Hero(100, 100, weapon)

player.lose_hp(10)
print(player.get_hp())
player.gain_hp(10)
print(player.get_hp())

living = player.lose_hp(99)

print(player.get_hp())
if living == True:
    print("Living")
else:
    print("Dead")

print(player.get_weapon())
player.s_weapon("Sword")
print(player.get_weapon())
bump
