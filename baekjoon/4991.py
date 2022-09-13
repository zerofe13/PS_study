#로봇청소기
import sys
from collections import deque

input = sys.stdin.readline
dx = [0,1,0,-1]
dy = [1,0,-1,0]
w = h = 0

def sol(dust,robot_pos):
    visited = [[[0]*2**10 for _ in range(w)] for _ in range(h)]
    q = deque()
    q.append((robot_pos[0],robot_pos[1],0))
    while q:
        y,x,bit = q.popleft()
        if bit == (1<<len(dust))-1:
            return visited[y][x][bit]
        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]
            if 0<=nx<w and 0<=ny<h and arr[y][x] !='x':
                if arr[ny][nx] == '*':
                    nbit = bit | (1<<dust.index((ny,nx)))
                    if not visited[ny][nx][nbit]:
                        q.append((ny,nx,nbit))
                        visited[ny][nx][nbit] = visited[y][x][bit] +1
                else:
                    if not visited[ny][nx][bit]:
                        q.append((ny,nx,bit))
                        visited[ny][nx][bit] = visited[y][x][bit]+1
    return -1
while True:
    w,h = map(int,input().split())
    if w == 0 and h == 0:
        break
    arr = []
    dust = []
    for i in range(h):
        arr.append(list(input()))
    for i in range(h):
        for j in range(w):
            if arr[i][j] == '*':
                dust.append((i,j))
            elif arr[i][j] == 'o':
                robot_pos = (i,j)
    print(sol(dust,robot_pos))