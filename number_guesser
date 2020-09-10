import random, sys

number_to_guess = random.randint(1, 100)

print("Guess the number! 1-100")


def guesser():
    user_guess = int(input("> "))
    if user_guess == number_to_guess:
        print("Congrats, you got it!")
        sys.exit()
    elif user_guess > number_to_guess:
        print("Too high. Guess lower!")
        guesser()
    elif user_guess < number_to_guess:
        print("Too low. Guess higher!")
        guesser()


guesser()
