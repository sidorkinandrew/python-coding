# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true

import math
a = int(input().strip())
b = int(input().strip())
print(str(int(round(math.degrees(math.atan2(a,b)))))+chr(176))
