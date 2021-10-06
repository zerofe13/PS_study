import sys
import heapq

input = sys.stdin.readline
INF = (1e9)

n,e = map(int,input().split())
grape = [[] for _ in range(n+1)]
for _ in range(e):
    a,b,c= map(int,input().split())
    grape[a].append((b,c))
    grape[b].append((a,c))
v1,v2 = map(int,input().split())

def dijkstra(start):
    q = []
    distance = [INF] *(n+1)
    heapq.heappush(q,(0,start)) #(거리, 노드) 거리를 기준으로 우선수위 큐
    distance[start]= 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now]<dist:
            continue
        for n_node,n_dist in grape[now]:
            cost = distance[now] + n_dist
            if distance[n_node] >cost:
                distance[n_node] = cost
                heapq.heappush(q,(cost,n_node))
    return distance

v1_dist = dijkstra(v1)
v2_dist = dijkstra(v2)

result = min(v1_dist[1]+v1_dist[v2]+v2_dist[n],v2_dist[1]+v2_dist[v1]+v1_dist[n])
if result >= INF:
    print(-1)
else: 
    print(result)