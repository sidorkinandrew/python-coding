#!/bin/python3
# https://www.hackerrank.com/challenges/30-scope/problem?isFullScreen=true
class Difference:
    def __init__(self, a):
        self.__elements = a
    def computeDifference(self):
        _ = list(map(int, self.__elements))
        self.maximumDifference = abs(max(_) - min(_))
    

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
