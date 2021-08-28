
import sys
import heapq
input = sys.stdin.readline
INF = (1e9)

N,M,X = map(int,input().split()) # N = 학생수 M = 마을수 X = target

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    distList = [INF]*(N+1)
    q = []
    heapq.heappush(q,(0,start))
    distList[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distList[now]<dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if cost <distList[i[0]]:
                distList[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    return distList

stdList = dijkstra(X)

for i in range(1,N+1):
    if i ==0 and i == X:
        continue
    temp = dijkstra(i)
    stdList[i]= temp[X]+stdList[i]
stdList[0] = 0
print(max(stdList))