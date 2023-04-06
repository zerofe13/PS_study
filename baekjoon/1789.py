import sys

input = sys.stdin.readline

s = int(input())
i = 1
n = 0
while True:
    if s < i:
        break
    s = s - i
    i += 1
    n+=1 

print(n)