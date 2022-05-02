#!/bin/python3

# https://www.hackerrank.com/challenges/30-binary-numbers/problem?isFullScreen=true

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    print(max([len(i) for i in bin(n)[2:].split('0')]))
