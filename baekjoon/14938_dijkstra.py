# import sys
# import heapq
# input =sys.stdin.readline
# INF = (1e9)
# n,m,r = map(int,input().split())
# item_list = list(map(int,input().split()))
# graph = [[] for _ in range(n+1)]

# for i in range(r):
#     a,b,c = map(int,input().split())
#     graph[a].append((b,c))
#     graph[b].append((a,c))

# def dijkstra(start):
#     dist = [INF]*(n+1)
#     q = []
#     heapq.heappush(q,(0,start))
#     dist[start] = 0
#     while q:
#         cost,now = heapq.heappop(q)
#         if dist[now] < cost:
#             continue
#         for node,d in graph[now]:
#             if dist[node] > d + cost:
#                 heapq.heappush(q,(d+cost,node))
#                 dist[node] = d+cost
#     return dist

# result = 0
# for i in range(1,n+1):
#     item = dijkstra(i)
#     sum_item = 0
#     for i in range(1,len(item)):
#         if item[i] <=m:
#             sum_item += item_list[i-1]
#     result = max(result,sum_item)
# print(result)
import heapq

INF = (1e9)

n,m,r = map(int,input().split()) #지역,수색범위,길의 개수
item_list = list(map(int,input().split()))
graph = [[] for _ in range(n+1)]

for i in range(r):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(start):
    q= []
    distance= [INF] * (n+1)
    distance[start] = 0
    heapq.heappush(q,(0,start))
    while q:
        dist,now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    return distance

result = 0
for i in range(1,n+1):
    item = dijkstra(i)
    sum_item = 0
    for i in range(1,len(item)):
        if item[i] <=m:
            sum_item += item_list[i-1]
    result = max(result,sum_item)
print(result)