#!/usr/bin/env python3
"""Solution to chapter 1, exercise 2, beyond 3: words list summary"""

def mean(numbers):
    result = 0
    for anumber in numbers:
        result += anumber    
    return result / len(numbers)

def summarize(words):
    word_lengths = [len(aword) for aword in words]
    return min(word_lengths), max(word_lengths), mean(word_lengths)
