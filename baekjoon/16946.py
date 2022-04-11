#벽 부수고 이동하기 4
import sys
from collections import deque

input = sys.stdin.readline
dx = [0,1,0,-1]
dy = [1,0,-1,0]

n,m = map(int,input().split())
graph = [list(map(int,input().rstrip())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
flood = [[0] * m for _ in range(n)]
flood_dict = dict()
def flood_fill(x,y,num):
    q = deque()
    q.append((y,x))
    visited[y][x] = 1
    flood[y][x] = num
    count = 1
    while q:
        y,x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<=ny<n and visited[ny][nx] == 0 and graph[ny][nx] == 0:
                if visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    q.append((ny,nx))
                    flood[ny][nx] = num
                    count += 1       
    return count        
num = 1
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and visited[i][j] == 0:
            count = flood_fill(j,i,num)
            flood_dict[num] = count
            num += 1
            
def check(x,y):
    count = 1
    f_visited = set()
    for i in range(4):
        nx = x +dx[i]
        ny = y +dy[i]
        if 0<=nx<m and 0<=ny<n and graph[ny][nx] == 0 and flood[ny][nx] != 0:
            f_visited.add(flood[ny][nx])
    for k in f_visited:
        count += flood_dict[k]
    return count % 10

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            temp = check(j,i)
            graph[i][j] = temp

for g in graph:
    print("".join(map(str, g)))

# print(flood)
# print(flood_dict)