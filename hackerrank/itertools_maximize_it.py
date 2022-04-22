# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/maximize-it/problem?isFullScreen=true

from functools import reduce

k, m = map(int,input().strip().split(" "))

def f(x):
    return x*x

def s(m, arr):
    return int(sum([f(i) for i in arr])%m)

data = []
for i in range(k):
    data.append(list(map(int, input().split()))[1:])

current = [0 for i in range(k)]
max_len = [len(data[i]) for i in range(k)]
results = []
for i in range(reduce(lambda x, y: x*y, max_len)):
  carry, pos = 0, -1
  combi = [data[l][current[l]] for l in range(k)]
  results.append(s(m,combi))
  current[pos], carry = (current[pos]+1)%max_len[pos], (current[pos]+1)//max_len[pos]
  while carry > 0 and pos > -k:
    pos -= 1
    current[pos], carry = (current[pos]+1)%max_len[pos], (current[pos]+1)//max_len[pos]

print(max(results))
