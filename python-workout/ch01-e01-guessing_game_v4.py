#!/usr/bin/env python3
"""Try the same thing, but have the program choose a random word from the dic-
tionary, and then ask the user to guess the word. (You might want to limit your-
self to words containing two to five letters, to avoid making it too horribly
difficult.) Instead of telling the user that they should guess a smaller or larger
number, have them choose an earlier or later word in the dict"""

"""Solution to chapter 1, exercise 1, beyond 3: Guessing game, words"""
import random

WORD_DICT = [aword.strip() for aword in open(input("Please enter dictionary filename:"))]


def guessing_game():

    answer = random.choice(WORD_DICT)

    while True:
        user_guess = int(input('What is your guess? '))

        if user_guess == answer:
            print(f'Right!  The answer is {user_guess}')
            break

        if user_guess < answer:
            print(f'Your guess of {user_guess} is too low!')

        else:
            print(f'Your guess of {user_guess} is too high!')
