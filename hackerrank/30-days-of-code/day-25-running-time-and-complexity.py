#!/bin/python3
# https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
def check_prime(n):
    if(n > 1):
        for i in range(2, int(n**0.5) + 1):
            if (n % i == 0):
                return False
        return True
    else:
        return False

for i in range(int(input())):
    print("Prime" if check_prime(int(input())) else "Not prime")
    
