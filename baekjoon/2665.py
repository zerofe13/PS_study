
import heapq


INF = (1e9)
dx =[1,0,-1,0]
dy =[0,1,0,-1]

n = int(input())
graph = []
distance = [[INF] *n for _ in range(n)]

for i in range(n):
    graph.append(list(map(int,str(input()))))
for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            graph[i][j] = 1
        else:
            graph[i][j] = 0
x,y =0,0
q = [(graph[x][y],x,y)]
distance[x][y] = 0
while q:
    dist,x,y = heapq.heappop(q)
    if dist > distance[x][y]:
        continue
    for i in range(4):
        nx = x +dx[i]
        ny = y +dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        cost = dist + graph[nx][ny]
        if cost < distance[nx][ny]:
            distance[nx][ny] = cost
            heapq.heappush(q,(cost,nx,ny))
print(distance[n-1][n-1])