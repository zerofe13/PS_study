import sys

input = sys.stdin.readline
INF = (1e9)

v,e = map(int,input().split());
graph = [[INF]*(v) for _ in range(v)]
for i in range (v):
    graph[i][i] =0
for i in range(e):
    a,b,c = map(int,input().split())
    graph[a-1][b-1] = c
    
for k in range(v):
    for i in range(v):
        for j in range(v):
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])

result = INF
for i in range(v):
    for j in range(i+1,v):
        if graph[i][j] != INF and graph[j][i] != INF:
            result = min(result,graph[i][j] + graph[j][i])

if result == INF:
    print(-1)
else:
    print(result)