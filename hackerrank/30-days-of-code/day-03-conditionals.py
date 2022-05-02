#!/bin/python3
# https://www.hackerrank.com/challenges/30-conditional-statements/problem?isFullScreen=true
import math
import os
import random
import re
import sys


def check_weirdness(anumber):
    is_odd = anumber % 2
    if is_odd:
        return "Weird"
    elif 2<= anumber <= 5:
        return "Not Weird"
    elif 6<= anumber <= 20:
        return "Weird"
    else:
        return "Not Weird"

if __name__ == '__main__':
    N = int(input().strip())
    print(check_weirdness(N))
