# import sys
# import heapq
# from collections import deque
# input= sys.stdin.readline

# dx = [0,1,0,-1]
# dy = [1,0,-1,0]

# N,M,K = map(int,input().split())
# graph = [list(map(int,input().rstrip())) for _ in range(N)]


# def bfs ():
#     q= []
#     heapq.heappush(q,(K,0,0))
#     visited =[[[0]*(K+1) for _ in range(M)] for _ in range(N)]
#     visited[0][0][K] = 1

#     while q:
#         z,x,y = heapq.heappop(q)
        
#         if x == M-1 and y == N-1:
#            return visited[N-1][M-1][z]
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx >= 0 and ny >= 0 and nx < M and ny <N:
#                 if graph[ny][nx] ==0 and visited[ny][nx][z] == 0:
#                     visited[ny][nx][z] = visited[y][x][z] + 1
#                     heapq.heappush(q,(z,nx,ny))
#                 elif graph[ny][nx]== 1 and  z >=1 and z<=K and visited[ny][nx][z-1] ==0:
#                     visited[ny][nx][z-1] =visited[y][x][z] + 1
#                     heapq.heappush(q,(z-1,nx,ny))
#     return -1
# print(bfs())

import sys
from collections import deque
input= sys.stdin.readline

dx = [0,1,0,-1]
dy = [1,0,-1,0]

N,M,K = map(int,input().split())
graph = [list(map(int,input().rstrip())) for _ in range(N)]


def bfs ():
    q= deque()
    q.append((0,0,K))
    visited =[[[0]*(K+1) for _ in range(M)] for _ in range(N)]
    visited[0][0][K] = 1

    while q:
        x,y,z = q.popleft()
        if x == M-1 and y == N-1:
           return visited[N-1][M-1][z]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < M and ny <N:
                if graph[ny][nx] ==0 and visited[ny][nx][z] == 0:
                    visited[ny][nx][z] = visited[y][x][z] + 1
                    q.append((nx,ny,z))
                elif graph[ny][nx]== 1 and z >=1 and z<=K and visited[ny][nx][z-1] ==0:
                    visited[ny][nx][z-1] =visited[y][x][z] + 1
                    q.append((nx,ny,z-1))
    return -1
print(bfs())