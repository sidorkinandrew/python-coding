# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/30-review-loop/problem?isFullScreen=true

n = int(input().strip())
for i in range(n):
    s = input().strip()
    print(s[::2],s[1::2])

