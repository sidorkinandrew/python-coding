#!/bin/python3
# https://www.hackerrank.com/challenges/30-nested-logic/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
import datetime as dt
date_returned = dt.date(*list(map(int,input().split()[::-1])))
date_due = dt.date(*list(map(int,input().split()[::-1])))

if date_returned<date_due:
    print(0)
elif date_returned.year != date_due.year:
    print(10000)
elif date_returned.month > date_due.month:
    print(500*(date_returned.month - date_due.month))
else:
    print(15*(date_returned.day - date_due.day))
