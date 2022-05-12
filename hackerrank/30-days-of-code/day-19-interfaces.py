#!/bin/python3
# https://www.hackerrank.com/challenges/30-interfaces/problem?isFullScreen=true

class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

from itertools import chain
from math import sqrt
       
class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        return sum(set(chain.from_iterable((i,n//i) for i in range(1,int(sqrt(n))+1) if n%i == 0)))


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
