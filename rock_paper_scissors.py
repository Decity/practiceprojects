import random, sys


def menu():
    while True:
        print("1. Fight")
        print("2. Quit")
        playerChoice = input()
        if playerChoice == "2":
            sys.exit()
        elif playerChoice == "1":
            combat()


def combat():
    wins = 0
    losses = 0
    ties = 0
    print('ROCK, PAPER, SCISSORS')
    while True: # The main game loop.
        while True:
            print("Pick r, p, or s to play! Or q to quit.")
            print("Wins: {}".format(wins))
            print("Losses: {}".format(losses))
            print("Ties: {}".format(ties))
            playerChoice = input("> ").lower()
            if playerChoice == "q":
                menu()
            elif playerChoice =="r" or playerChoice == "p" or playerChoice == "s":
                break

        # Display what the player chose:
        if playerChoice == "r":
            print("It's ROCK versus..")
        elif playerChoice == "p":
            print("It's PAPER versus..")
        elif playerChoice == "s":
            print("It's SCISSORS versus..")

        # Display what the computer chose:
        computerChoice = random.randint(1,3)
        if computerChoice == 1:
            computerChoice = "r"
            print("ROCK!")
        elif computerChoice == 2:
            computerChoice = "p"
            print("PAPER!")
        elif computerChoice == 3:
            computerChoice = "s"
            print("SCISSORS!")

        # Display and record the win/loss/tie:
        if computerChoice == playerChoice:
            print("It's a tie!")
            ties += 1
        elif playerChoice == "r" and computerChoice == "p":
            print("You lose!")
            losses += 1
        elif playerChoice == "r" and computerChoice == "s":
            print("You win!")
            wins += 1
        elif playerChoice == "p" and computerChoice == "s":
            print("You lose!")
            losses += 1
        elif playerChoice == "p" and computerChoice == "r":
            print("You win!")
            wins += 1
        elif playerChoice == "s" and computerChoice == "r":
            print("You lose!")
            losses += 1
        elif playerChoice == "s" and computerChoice == "p":
            print("You win!")
            wins += 1


menu()
