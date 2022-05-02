# https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input().strip())
phonebook = {}
for i in range(n):
    k, v = input().strip().split()
    phonebook[k]=v
while(True):
    try:
        k = input().strip()
        v = phonebook.get(k, "Not found")
        print(f"{v}" if v=="Not found" else f"{k}={v}")
    except:
        break
