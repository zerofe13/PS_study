# 최소비용 구하기
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

N = int(input())
M = int(input())
graph = [[] for i in range(N+1)] # graph[시작] = (도착, 거리)
distList = [INF] * (N+1)
#입력 
for _ in range(M):#
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
#다익스트라 
start,target = map(int,input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distList[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distList[now]<dist: #처리된적이 있는 노드 continue
            continue 
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distList[i[0]]:
                distList[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)
print(distList[target])