""" A program that implements a “Guess the Number” game.

    author: Fatih IZGI
    date: 20-Feb-2020
    version: python 3.8.1
"""

import random

def compare(number: int, guess: int) -> int:
    """ Compares two parameters, the number to be guessed and the number that was guessed
        and returns a result (0, -1 or 1) as a result of that compare.
    """
    if number == guess:
        return 0
    elif number < guess:
        return -1
    else:
        return 1

name: str = input("Hello! What is your name? ")  # Greetings
print(f"Well, {name}, I am thinking of a number between 1 and 20.")

number: int = random.randint(1, 20)  # The number to be guessed
count: int = 0  # try counter

while True:  # each loop means a new try to guess the number
    count += 1
    if count > 6:  # maximum try count reached
        print(f"\nSorry, {name}, you couldn't guessed the number in < 6 tries")
        print(f"The number I was thinking of was {number}")
        break  # end game

    while True:  # make sure to get a valid input from the user
        try:
            guess: int = int(input("Take a guess: "))
            if 1 <= guess <= 20:  # if the input is a number in the range we want
                break  # stop asking an input
            else:
                print("Your number should be between 1 and 20!")
        except ValueError:  # will be raised if the input is not a number
            print("Please enter a number!")

    result = compare(number, guess)  # compare the number and the guess of the user

    if result == -1:
        print("Your guess is too high")  # loop again
    elif result == 1:
        print("Your guess is too low")  # loop again
    else:
        print(f"Good job, {name}! You guessed my number in {count} guess(es)!")
        break  # end game

