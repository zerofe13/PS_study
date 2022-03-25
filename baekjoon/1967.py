#트리의 지름
import sys
import heapq
input =  sys.stdin.readline
INF = 1e9

n = int(input())
graph = [[] for _ in range(n+1)]
dist = [INF]*(n+1)

for i in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))
def search(start):
    q = []
    heapq.heappush(q,(0,start))
    while q:
        now_d, now = heapq.heappop(q)
        if dist[now]<now_d:
            continue
        for next_d, next_n in graph[now]:
            sum_dist = now_d+next_d
            if dist[next_n] > sum_dist:
                dist[next_n] = sum_dist
                heapq.heappush(q,(sum_dist,next_n))
            
dist[1] = 0
search(1)
end_node = 1
for i in range(1,n+1):
    if dist[end_node]<dist[i]:
        end_node = i
dist= [INF] *(n+1)
dist[end_node]=0
search(end_node)
dist[0] = 0
print(max(dist))
