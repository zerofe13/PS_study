from collections import deque

N,M = map(int,input().split())
array = [list(map(int,input().split())) for _ in range(N)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
result = 0
def BFS():
    global result
    check = [[0]*M for _ in range (N)]
    queue = deque()
    for i in range(N):
        for j in range(M):
            if array[i][j] == 2:
                check[i][j] = 1
                queue.append((j,i))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >=0 and ny >= 0 and nx <M and ny <N and check[ny][nx] == 0 and array[ny][nx] != 1:
                check[ny][nx] = 1
                queue.append((nx,ny))
    count = 0
    for i in range(N):
        for j in range(M):
            if check[i][j] == 0 and array[i][j] == 0:
                count += 1
    result = max(count , result)

def create_wall(cnt):
    if cnt == 3:
        BFS()
    else:
        for i in range(N):
            for j in range(M):
                if array[i][j] == 0 :
                    array[i][j] = 1
                    create_wall(cnt + 1)
                    array[i][j] = 0

create_wall(0)
print(result)