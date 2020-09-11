import random

word_list = ["Bee", "Fuzzy", "Existentialism"]


# Picks a random word from the list and returns it in uppercase.
def get_word():
    word = random.choice(word_list)
    return word.upper()


# The game engine
def play(word):
    hint = "_" * len(word)
    lives = 6
    word_guessed = False
    right_guessed_letters = []
    wrong_guessed_letters = []
    guessed_words = []
    print("Welcome to hangman.")
    print("You have {} lives.".format(lives))
    print(hint)
    while word_guessed == False and lives > 0:
        guess = input("> ").upper()
        if guess == word:
            print("you got it!")
            word_guessed = True
        elif guess in word and len(guess) == 1:
            print("You guessed the letter right!")
            right_guessed_letters.append(guess)
            print("Letters guessed wrong:{}".format(wrong_guessed_letters))
        elif len(guess) > 1 or not guess.isalpha():
            print("You can only guess one letter")
        elif len(guess) == 1 and guess.isalpha():
            print("Wrong guess.")
            wrong_guessed_letters.append(guess)
            print("Letters guessed wrong:{}".format(wrong_guessed_letters))
            lives -= 1
            print("You've got {} lives left!".format(lives))
        else:
            print("You can guess only one letter")


# The main loop to keep the game running
def main():
    word = get_word()
    play(word)
    while input("Play Again? y/n \n> ").upper() == "Y":
        word = get_word()
        play(word)


main()
