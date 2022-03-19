#문제집
import sys
import heapq

m,n = map(int,input().split())
graph = [[] for _ in range(m+1)]
indegree = [0] *(m+1)
for _ in range(n):
    a,b = map(int,input().split())
    indegree[b] += 1
    graph[a].append(b)

def tp_sort():
    result = [] 
    q = []
    for i in range(1,m+1):
        if indegree[i] == 0:
            heapq.heappush(q,i)
    while q:
        now = heapq.heappop(q)
        result.append(now)
        for node in graph[now]:
            indegree[node] -= 1
            if indegree[node] == 0:
                heapq.heappush(q,node)

    return result

result = tp_sort()

for r in result:
    print(r,end= " ")