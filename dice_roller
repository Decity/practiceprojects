import random, sys


def dice_thrower(amount, sides):
    for times in range(amount):
        print(random.randint(1, sides))


while True:
    print("Let's roll some dice!")
    print("How many dice do you want to roll?")
    roll_amount = int(input("> "))
    print("How many sides to the die/dice?")
    roll_sides = int(input("> "))
    dice_thrower(roll_amount, roll_sides)
    print("Would you like to play again? y/n")
    play_again = input("> ")
    if play_again == "n":
        sys.exit()
