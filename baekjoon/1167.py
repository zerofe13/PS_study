#트리의  지름
import sys
import heapq
input = sys.stdin.readline
INF = 1e9

n = int(input())
graph = [[] for _ in range(n+1)]
temp = []

for _ in range(n):
    temp = list(map(int,input().split()))
    a,b,c = 0,0,0
    for i,v in enumerate(temp):
        if v == -1:
            break
        if i == 0:
            a = v
            continue
        if i % 2== 0:
           c = v
           graph[a].append((c,b))
        else:
            b=v

dist = [INF]*(n+1)

def search(start):
    q = []
    heapq.heappush(q,(0,start))
    while q:
        now_dist,now_index = heapq.heappop(q)
        if dist[now_index]<now_dist:
            continue
        for next_d,next_i in graph[now_index]:
            sum_dist = now_dist+next_d
            if dist[next_i] > sum_dist:
                dist[next_i] = sum_dist
                heapq.heappush(q,(sum_dist,next_i))

dist[1] = 0
search(1)
edge = 0
max_num =0
for i in range(1,n+1):
    if max_num < dist[i]:
        max_num = dist[i]
        edge = i
dist = [INF] *(n+1)
dist[0],dist[edge] = 0,0
search(edge)
print(max(dist))