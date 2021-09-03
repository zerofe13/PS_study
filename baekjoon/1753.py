#최단경로
import sys
import heapq
input = sys.stdin.readline
INF = (1e9)

v,e = map(int,input().split())
start = int(input())
graph = [[] for _ in range(v+1)]
distList = [INF] *(v+1)

for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distList[start] = 0
    while q:
        dist, a = heapq.heappop(q)
        if distList[a]<dist:
            continue
        for i,d in graph[a]:
            if d+dist<distList[i]:
                heapq.heappush(q,(d+dist,i))
                distList[i] = d+dist
dijkstra(start)
for i in range(1,len(distList)):
    if distList[i] == INF:
        print("INF")
    else:
        print(distList[i])