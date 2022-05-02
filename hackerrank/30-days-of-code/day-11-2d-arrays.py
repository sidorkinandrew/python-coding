#!/bin/python3

# https://www.hackerrank.com/challenges/30-2d-arrays/problem?isFullScreen=true

import math
import os
import random
import re
import sys



def get_hourglass(arr, i, j):
    res = [arr[i][j], arr[i][j+1], arr[i][j+2], arr[i+1][j+1],
           arr[i+2][j], arr[i+2][j+1], arr[i+2][j+2]]
    return res

if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    mx, my, max_hourglass = len(arr), len(arr[0]), float('-inf')
    for i in range(mx-2):
        for j in range(my-2):
            _ = sum(get_hourglass(arr, i, j))
            if _ > max_hourglass:
                max_hourglass = _
    print(max_hourglass)
