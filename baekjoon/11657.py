import sys
import heapq
INF = (1e9)
input= sys.stdin.readline

N,M = map(int,input().split());
dist = [INF] *(N+1)

# graph = [[] for _ in range(N+1)]
graph = []
for i in range(M):
    a,b,c, = map(int,input().split())
    # graph[a].append((b,c)) 다익스트라
    graph.append((a,b,c))
    
# def dijkstra(start):
#     q = []
#     heapq.heappush(q,(0,start))
#     dist[start] = 0
#     while q:
#         now_d,now_n = heapq.heappop(q)
#         if dist[now_n] <now_d:
#             continue
#         for next_n,next_d in graph[now_n]:
#             sum_d = now_d + next_d
#             if dist[next_n] >sum_d:
#                 heapq.heappush(q,(sum_d,next_n))

def bellman(start):
    dist[start] = 0
    for i in range(N):
        for j in range(M):
            now_n = graph[j][0]
            next_n = graph[j][1]
            cost = graph[j][2]
            if dist[now_n]+cost < dist[next_n] and dist[now_n] != INF:
                dist[next_n] = dist[now_n]+cost
                if i == N-1:
                    return False
    return True
            
if bellman(1):
    for i,v in enumerate(dist):
        if i == 0 or i == 1:
            continue
        if v == INF:
            print(-1)
        else:
            print(v)
else:
    print(-1)