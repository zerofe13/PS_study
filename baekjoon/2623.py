import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int,input().split())
indegree = [0]*(N+1)
graph = [[] for _ in range(N+1)]
result = []
for _ in range(M):
    temp= list(map(int,input().split()))
    size,singer = temp[0],temp[1:]
    for i in range(1,size):
        graph[singer[i-1]].append(singer[i])
        indegree[singer[i]] += 1

q=deque()
for i in range(1,N+1):
    if indegree[i] == 0:
        q.append(i)
while q:
    now = q.popleft()
    result.append(now)
    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] <= 0:
            q.append(i)
if len(result) == N:
    for i in result:
        print(i)
else:
    print(0)