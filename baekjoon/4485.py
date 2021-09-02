#녹색 옷 입은 애가 젤다지?
import heapq
import sys
input = sys.stdin.readline
INF = (1e9)
dx = [0,1,0,-1]
dy = [1,0,-1,0]
ts = 1
while True:
    n = int(input())
    if n == 0:
        break
    graph = [list(map(int,input().split())) for _ in range(n)]
    cost_map = [[INF]*n for _ in range(n)]
    q = []
    heapq.heappush(q,(graph[0][0],0,0)) #cost,y,x
    cost_map[0][0] = graph[0][0]
    while q:
        cost,y,x = heapq.heappop(q)
        for i in range(4):
            n_x = x + dx[i]
            n_y = y + dy[i]
            if 0<=n_x<n and 0<=n_y<n :
                n_cost = cost+graph[n_y][n_x]
                if n_cost < cost_map[n_y][n_x]:
                    heapq.heappush(q,(n_cost,n_y,n_x))
                    cost_map[n_y][n_x] = n_cost
    print("Problem %d: %d"%(ts,cost_map[n-1][n-1]),end="\n")
    ts = ts+1 