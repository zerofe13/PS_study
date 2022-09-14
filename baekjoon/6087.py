#레이저 통신
import sys
from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0] 

w,h = map(int,input().split())
arr =[]
target = []
result = 1e9
for i in range(h):
    arr.append(list(input()))
for i in range(h):
    for j in range(w):
        if arr[i][j] == 'C':
            target.append((i,j))
            
def sol(target):
    global result
    dep = target[0]
    arv = target[1]
    
    visited = [[0] * w for _ in range(h)]
    visited[dep[0]][dep[1]] = 0
    q= deque()
    q.append((dep[0],dep[1],-1,0))
    
    while q:
        y,x,d,cnt = q.popleft()
        if y == arv[0] and x == arv[1]:
            result = min(result,cnt)
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<w and 0<=ny<h and arr[ny][nx] != '*':
                if cnt == visited[y][x]:
                    if not visited[ny][nx]:
                        if d == -1 or d == i :
                            q.append((ny,nx,i,cnt))
                            visited[ny][nx] = cnt
                        elif d != i:
                            q.append((ny,nx,i,cnt+1))
                            visited[ny][nx] = cnt+1
                    else:
                        if d == i and visited[ny][nx] >= cnt:
                            visited[ny][nx] = cnt
                            q.append((ny,nx,i,cnt))
                        elif d != i and visited[ny][nx] >= cnt+1:
                            visited[ny][nx] = cnt+1
                            q.append((ny,nx,i,cnt+1))

sol(target)
print(result)