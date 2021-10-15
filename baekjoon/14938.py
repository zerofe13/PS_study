import sys
input =sys.stdin.readline

n,m,r = map(int,input().split())
item = list(map(int,input().split()))
INF = (1e9)
ground= [[INF for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i==j: ground[i][j]=0
for i in range(r):
    a,b,c = map(int,input().split())
    ground[a-1][b-1] = c
    ground[b-1][a-1] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            ground[i][j] = min(ground[i][j],ground[i][k]+ground[k][j])
result = 0
for i in range(n):
    sum_item = 0
    for j in range(n):
        if ground[i][j] <=m:
            sum_item += item[j]
    result = max(result,sum_item)

print(result)