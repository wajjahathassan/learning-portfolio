"""Module providing a function printing python version."""

import random

secret_number = random.randint(1, 10)

player_guess = int(input("Guess the number (between 1 and 10): "))

guesses = {"Player Choice": player_guess, "Secret Number": secret_number}


def check_guess(player_guess, secret_number):
    print(f"You chose {player_guess}!")

    if player_guess == secret_number:
        return "You got it!"
    elif player_guess < secret_number:
        return "Too low!"
    else:
        return "Too high!"


result = check_guess(guesses["Player Choice"], guesses["Secret Number"])

print(result)

if result != "You got it!":
    print(f"The correct answer is {secret_number}.")
