import sys

input = sys.stdin.readline

n, k = map(int, input().split())
term = []
if n == 1:
    print(1)
    exit()
temp = int(input())
first = temp
last = 0
for i in range(n-1):
    time = int(input())
    if i == n-2:
        last = time
    term.append(time - temp)
    temp = time
    
term.sort(key = lambda x: -x);
result = last - first +1
# 첫번째 난로 고려해서 k-1
for i in range(k-1):
    result -= (term[i]-1)
print(result)