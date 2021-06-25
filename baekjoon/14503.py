from collections import deque

N,M = map(int,input().split())
r,c,d = map(int,input().split())
array = [list(map(int,input().split())) for _ in range(N)]
dx = [0,1,0,-1]
dy = [-1,0,1,0]
check = [[0]* M for _ in range(N)]
result = 1

def search():
    queue =deque()
    queue.append((r,c,d))

    while queue:
        y,x,f_d = queue.popleft()
        nd = f_d
        flag = False
        global result
        for i in range(4):
            nd = (nd+3)%4
            nx = x + dx[nd]
            ny = y + dy[nd]
            if nx >= 0 and ny >= 0 and nx <M and ny < N and array[ny][nx] ==0 and check[ny][nx] == 0:
                check[ny][nx] = 1
                result += 1
                queue.append((ny,nx,nd))
                flag = True
                break
        if not flag:
            nd = (f_d+2)%4
            nx = x +dx[nd]
            ny = y +dy[nd]

            if nx >=0 and ny >=0 and nx <M and ny<N and array[ny][nx] == 0:
                queue.append((ny,nx,f_d))
check[r][c] = 1
search()
print(result)