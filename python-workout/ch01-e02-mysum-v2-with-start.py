#!/usr/bin/env python3
"""Solution to chapter 1, exercise 2, beyond 1: mysum with an additional `start` parameter"""

def mysum(numbers, start=0):
    result = start
    for anumber in numbers:
        result += anumber
    return result
