#!/usr/bin/env python3

"""Solution to chapter 1, exercise 2: mysum"""


def mysum(*numbers):
    result = 0
    for anumber in numbers:
        result += anumber
    return result
