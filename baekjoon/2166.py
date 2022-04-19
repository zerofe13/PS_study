#다각형의 면적
import sys

input = sys.stdin.readline

n = int(input())
pos = []
for i in range(n):
    x,y = map(int,input().split())
    pos.append((x,y))
pos.append(pos[0])
a,b =0,0

for i in range(n):
    a += pos[i][1]*pos[i+1][0]
    b += pos[i][0]*pos[i+1][1]
    
result = abs(a-b) / 2

print(round(result,2))
