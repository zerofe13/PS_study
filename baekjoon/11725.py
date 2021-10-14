import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[]for _ in range(n+1)]
parent = [0]*(n+1)
check = [0]*(n+1)
for i in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
q = deque()
q.append(1)
parent[1]= 1
while q:
    now = q.popleft()
    for n_node in graph[now]:
        if parent[n_node] == 0:
            q.append(n_node)
            parent[n_node] = now
for i in range(2,n+1):
    print(parent[i])