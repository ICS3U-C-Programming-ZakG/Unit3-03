#!/usr/bin/env python3
# Created by: Zak Goneau
# Created on: Oct. 16, 2023
# This program makes the user guess a number from 0-9
# Then it will generate a random number and tell the user if they're right or wrong.

import random


def main():
    # Introduce the program to user then get user guess
    print("This is a guessing game and you must guess a random number between 0-9!\n")
    user_guess = int(input("Please guess a number from 0-9: "))

    # Generate random answer and check if guess is correct
    correct_answer = random.randint(1, 9)
    if correct_answer == user_guess:
        print("\nYou guessed correctly!")
    else:
        print("\nYou guessed incorrectly, the number was {}".format(correct_answer))


if __name__ == "__main__":
    main()
