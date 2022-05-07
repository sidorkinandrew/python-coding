#!/bin/python3
#https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/problem?isFullScreen=true

import math
import os
import random
import re
import sys


S = input()

try:
    print(int(S))
except ValueError:
    print("Bad String")
