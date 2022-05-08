#!/usr/bin/env python3

"""Solution to chapter 1, exercise 2: mysum"""


def mysum(*numbers):
    output = 0
    for number in numbers:
        output += number
    return output
