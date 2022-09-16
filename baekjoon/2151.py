#거울설치

import sys
from collections import deque
input = sys.stdin.readline

dx = [0,1,0,-1]
dy = [1,0,-1,0] #아,오,위,왼
door_pos=[]
arr = []
result = 1e9
n = int(input())

for i in range(n):
    arr.append(list(input()))
    for j in range(n):
        if arr[i][j] == '#':
            door_pos.append((i,j))

def sol(door_pos):
    global result
    fir_door = door_pos[0]
    sec_door = door_pos[1]
    visited = [[0]*n for _ in range(n)] 
    d = 0
    q = deque()
    for i in range(4):
        q.append((fir_door[0],fir_door[1],i,0))
            
    while q:
        y,x,d,cnt=q.popleft()
        nx = x + dx[d]
        ny = y + dy[d]
        while 0<=nx< n and 0<=ny<n and arr[ny][nx] != "*":
            if arr[ny][nx] == "!":
                if d == 0 or  d ==2:
                    q.append((ny,nx,1,cnt+1))
                    q.append((ny,nx,3,cnt+1))
                else:
                    q.append((ny,nx,0,cnt+1))
                    q.append((ny,nx,2,cnt+1))
            if ny == sec_door[0] and nx == sec_door[1]:
                return cnt
            nx += dx[d]
            ny += dy[d]
print(sol(door_pos))