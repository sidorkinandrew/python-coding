#!/usr/bin/env python3

"""Not only should you choose a random number, but you should also choose a
random number base, from 2 to 16, in which the user should submit their
input. If the user inputs “10” as their guess, you’ll need to interpret it in the 
correct number base; “10” might mean 10 (decimal), or 2 (binary), or 16 (hexadecimal)."""

"""Solution to chapter 1, exercise 1, beyond 2: Guessing game, number bases"""
import random


def guessing_game():

    answer = random.randint(0, 100)
    required_base = random.choice([2, 8, 10, 16])

    while True:
        user_guess = int(input('What is your guess? '), required_base)

        if user_guess == answer:
            print(f'Right!  The answer is {user_guess}')
            break

        if user_guess < answer:
            print(f'Your guess of {user_guess} is too low!')

        else:
            print(f'Your guess of {user_guess} is too high!')
