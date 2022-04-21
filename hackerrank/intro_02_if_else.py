#!/bin/python3

import math
import os
import random
import re
import sys

def check_weirdness(anumber):
    is_odd = anumber % 2
    if is_odd:
        return "Weird"
    elif 2<= n <= 5:
        return "Not Weird"
    elif 6<= n <= 20:
        return "Weird"
    else:
        return "Not Weird"

if __name__ == '__main__':
    n = int(input().strip())
    print(check_weirdness(n))
