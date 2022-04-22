#!/bin/python3

# https://www.hackerrank.com/challenges/matrix-script/problem?isFullScreen=true

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

matrix = "".join(["".join(i) for i in zip(*matrix)])

print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", matrix))
