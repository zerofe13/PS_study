import sys
import heapq

input = sys.stdin.readline
INF = (1e9)

v,e = map(int,input().split())
graph= [[] for _ in range(v+3)]

macTerminal = v+1
starTerminal = v+2

for i in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

M,x = map(int,input().split())
mac_pos = list(map(int,input().split()))

S,y = map(int,input().split())
star_pos = list(map(int,input().split()))

for m in mac_pos:
    graph[macTerminal].append((m,0))
    graph[m].append((macTerminal,0))
for s in star_pos:
    graph[s].append((starTerminal,0))
    graph[starTerminal].append((s,0))
    
def dijkstra(start):
    dist = [INF] * (v+3)
    q= []
    heapq.heappush(q,(0,start))
    dist[start] = 0
    while q:
        d,now = heapq.heappop(q)
        if dist[now]<d:
            continue
        for nn,n_d in graph[now]:
            if nn == v+1 or nn == v+2:
                continue
            sum_d = n_d + d
            if dist[nn] >sum_d:
                dist[nn] = sum_d
                heapq.heappush(q,(sum_d,nn))
    return dist

mac_dist = dijkstra(v+1)
star_dist = dijkstra(v+2)

result = INF

for i in range(1,v+1):
    if (i in mac_pos) or (i in star_pos):
        continue
    if mac_dist[i]<=x and star_dist[i]<=y:
        if mac_dist[i]+star_dist[i]<result:
            result = mac_dist[i]+star_dist[i]

# if result ==INF:
#     print(-1)
# else:
#     print(result)