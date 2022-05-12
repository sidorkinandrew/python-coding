#!/bin/python3
# https://www.hackerrank.com/challenges/30-sorting/problem?isFullScreen=true

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    numberOfSwaps = 0
    for i in range (n):
        for j in range(n - 1):
            if (a[j] > a[j + 1]):
                a[j], a[j+1] = a[j+1], a[j]
                numberOfSwaps+=1
    
    print(f"Array is sorted in {numberOfSwaps} swaps.\nFirst Element: {a[0]}\nLast Element: {a[n-1]}")
