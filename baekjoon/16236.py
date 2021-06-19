from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]
n_x,n_y = 0,0
baby_size, size_count,count= 2, 0 ,0
possibilty_pos= []

N = int(input())
array =[list(map(int,input().split()))for _ in range(N)]

def BFS (x,y):
    check = [[0] * N for _ in range(N)]
    queue = deque()
    queue.append((x,y))
    check[y][x] = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx <N and ny<N and  check[ny][nx] == 0 and array[ny][nx]<=baby_size:
                if array[ny][nx] != 0 and array[ny][nx]<baby_size:
                    check[ny][nx]=check[y][x] +1 
                    possibilty_pos.append((check[ny][nx],ny,nx))
                elif possibilty_pos: #이동가능한 위치 있을경우 큐 추가 x
                    continue
                else:
                    check[ny][nx]=check[y][x] +1  
                    queue.append((nx,ny))
    if possibilty_pos:
        possibilty_pos.sort() # 거리 , y축,x,축 순으로 정렬
        dist,r_y,r_x = possibilty_pos[0]
        return r_y,r_x,dist-1
    else: # 엄마상어
        return N+1,N+1,0
while True:
    if n_x == N+1:
        break
    for i in range(N):
        for j in range(N):
            if array[i][j] == 9:
                n_y, n_x,dist = BFS(j,i)
                if n_x != N+1 and n_y != N+1:
                    array[n_y][n_x] = 9 # 아기상어 위치이동
                    array[i][j]=0
                    possibilty_pos=[] #초기화
                    size_count += 1#먹이 
                    if size_count == baby_size:
                        baby_size += 1 #아기사이즈 
                        size_count = 0
                    count += dist 
                else:
                    break
print(count)

                    





