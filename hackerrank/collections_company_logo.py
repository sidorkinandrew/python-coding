#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    counts = {}
    for asymbol in set(s):
        counts[s.count(asymbol)] = counts[s.count(asymbol)] + asymbol if s.count(asymbol) in counts else asymbol
    result = [asymbol+" "+ str(count) for count in sorted(counts, reverse=True) for asymbol in sorted(list(counts[count]))][:3]
    print("\n".join(result))
