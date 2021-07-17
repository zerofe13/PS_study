from collections import deque

dx= [-1,-1,0,1,1,1,0,-1]
dy= [0,1,1,1,0,-1,-1,-1]

N,M = map(int,input().split())
array = [list(map(int,input().split())) for _ in range(N)]
infoArr =[list(map(int,input().split()))for _ in range(M)]

def move(d,s):
    for _ in range(s):
        nx = 0 + dx[d]
        ny = N + ny[d]
        if nx == -1 : nx = N
        if ny == -1 : ny = N
        