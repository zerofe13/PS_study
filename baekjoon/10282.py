#해킹
import sys
import heapq
INF = 1e9

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n,d,c = map(int,input().split())
    dist = [INF] * (n+1)
    graph= [[] for _ in range(n+1)]

    for i in range(d):
        a,b,s = map(int,input().split())
        graph[b].append((a,s))

    def dijkstra(start):
        q= []
        heapq.heappush(q,(0,start))
        dist[start] = 0
        while q:
            cost,now = heapq.heappop(q)
            if dist[now] < cost:
                continue
            for n,c in graph[now]:
                nc = cost + c
                if nc < dist[n]:
                    heapq.heappush(q,(nc,n))
                    dist[n] = nc
    dijkstra(c)
    result = []
    for i,v in enumerate(dist):
        if v != INF:
            result.append(v)
    print(len(result),max(result))