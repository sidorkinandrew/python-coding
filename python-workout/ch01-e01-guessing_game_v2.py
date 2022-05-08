#!/usr/bin/env python3
"""Modify this program, such that it gives the user only three chances to guess the
correct number. If they try three times without success, the program tells them
that they didn’t guess in time and then exits"""
"""Solution to chapter 1, exercise 1, beyond 1: Guessing game, only 3 chances"""

import random


def guessing_game():
    answer = random.randint(0, 100)
    remaining_guesses = 2

    while remaining_guesses >= 0:
        remaining_guesses -= 1
        user_guess = int(input('What is your guess? '))

        if user_guess == answer:
            print(f'Right!  The answer is {user_guess}')
            break

        if user_guess < answer:
            print(f'Your guess of {user_guess} is too low!')

        else:
            print(f'Your guess of {user_guess} is too high!')

    else:
        print('Your three chances are up!')
