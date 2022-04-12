#미세먼지 안녕!
import sys
from collections import deque

input = sys.stdin.readline
dx = [1,0,-1,0]
dy =[0,1,0,-1]

R,C,T = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(R)]
air_filter = []

for i in range(R):
    for j in range(C):
        if graph[i][j] == -1:
            air_filter.append((j,i))

for t in range(T):
    # 미세먼지 확산
    q= deque()
    for i in range(R):
        for j in range(C):
            if graph[i][j] != 0 and graph[i][j] != -1:
                q.append((j,i,graph[i][j]))
    while q:
        x,y,v = q.popleft()
        count = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx <C and 0<=ny<R and graph[ny][nx]!=-1:
                graph[ny][nx] += v//5
                count += 1
        if count > 0:
            graph[y][x] -= (v//5) *count
    # 공기 청정기 작동
    x,y = air_filter[0]
    for i in range(y-1,0,-1):
        graph[i][0] = graph[i-1][0]
    for i in range(C-1):
        graph[0][i] = graph[0][i+1]
    for i in range(y):
        graph[i][C-1]= graph[i+1][C-1]
    for i in range(C-1,0,-1):
        if i == x+1:
            graph[y][i] = 0
        else:
            graph[y][i]=graph[y][i-1]
    x,y = air_filter[1]
    for i in range(y+1,R-1):
        graph[i][0] = graph[i+1][0]
    for i in range(C-1):
        graph[R-1][i] = graph[R-1][i+1]
    for i in range(R-1,y,-1):
        graph[i][C-1]= graph[i-1][C-1]
    for i in range(C-1,0,-1):
        if i == x+1:
            graph[y][i] = 0
        else:
            graph[y][i]=graph[y][i-1]

answer = 0
for i in range(R):
    for j in range(C):
        answer +=graph[i][j]

print(answer+2)
