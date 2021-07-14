from collections import deque
from typing import get_origin

N,L,R = map(int,input().split())
dx = [0,1,0,-1]
dy = [1,0,-1,0]
array =[list(map(int,input().split()))for _ in range(N)]
check = [[0] * N for _ in range(N)]
mem_q = deque()
sum_num = 0
flag = 0
count = 0

#인구이동 함수
def swap():
    global sum_num
    global flag
    po_num = sum_num//len(mem_q)
    while mem_q:
        x,y = mem_q.pop()
        array[y][x] = po_num    
    sum_num = 0
    flag = 1

# 국경 bfs
def bfs(x,y):
    global sum_num
    queue = deque()
    queue.append((x,y))
    mem_q.append((x,y))
    sum_num += array[y][x]
    check[y][x] = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx <N and ny >= 0 and ny <N and check[ny][nx]== 0 and abs(array[ny][nx] - array[y][x]) >= L and abs(array[ny][nx] - array[y][x]) <= R :
                check[ny][nx] = 1
                queue.append((nx,ny))
                mem_q.append((nx,ny))
                sum_num += array[ny][nx]
    if len(mem_q)> 1:
        swap()
    else:
        mem_q.clear()
        sum_num = 0

while True:
    for i in range(N):
        for j in range(N):
            if check[i][j] == 0:
                bfs(j,i)
    if flag == 1:
        check = [[0] * N for _ in range(N)]
        count += 1
        flag = 0
        for i in range(N):
            print(array[i])
        print("\n")
    else:
        break
print(count)
        