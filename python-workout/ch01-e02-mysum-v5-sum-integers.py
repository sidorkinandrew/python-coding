#!/usr/bin/env python3
"""Solution to chapter 1, exercise 2, beyond 4: sum of integers from a list of objects"""

def get_integer(item):
    try:
        return int(item)
    except ValueError:
        return 0

def mysum(*numbers):
    result = 0
    for anumber in numbers:
        result += anumber
    return result

def sum_integers(items):
    return mysum(*[get_integer(item) for item in items])
