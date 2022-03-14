#낙시왕
import sys
input = sys.stdin.readline

R,C,M = map(int,input().split())
graph = [[(0,0,0)]*C for _ in range(R)]
king = -1
result = 0
for _ in range(M):
    # s 속력, d 방향 , z크기
    r,c,s,d,z = map(int,input().split()) 
    graph[r-1][c-1] = (s,d,z)

def shark_move_eat():
    new_graph=[[(0,0,0)]*C for _ in range(R)]
    shark_list = []
    #1 위 ,2 아래, 3 오른쪽, 4왼쪽 
    dx = [0,0,0,1,-1]
    dy = [0,-1,1,0,0]
    for i in range(R):
        for j in range(C):
            if graph[i][j] !=(0,0,0):
                nx,ny = j,i
                s,d,z = graph[i][j]
                for K in range(s):
                    nx = nx + dx[d]
                    ny = ny + dy[d]
                    if 0<=nx<C and 0<=ny<R:
                        continue
                    else:
                        if d % 2 == 0:
                            d -= 1
                        else:
                            d += 1
                        nx = nx + (2*dx[d])
                        ny = ny + (2*dy[d])
                shark_list.append((ny,nx,s,d,z))
    for shark in shark_list:
        r,c,s,d,z = shark
        if new_graph[r][c] != (0,0,0):
            if new_graph[r][c][2] >z:
                continue
            else:
                new_graph[r][c] = (s,d,z)
        else:
            new_graph[r][c] = (s,d,z)
    return new_graph
for time in range(C):
    #낙씨왕이 오른쪽으로 한 칸 이동한다.
    king +=1
    #낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다. 
    # 상어를 잡으면 격자판에서 잡은 상어가 사라진다.
    for i in range(R):
        if graph[i][king] != (0,0,0):
            result += graph[i][king][2]
            graph[i][king] = (0,0,0)
            break
    graph = shark_move_eat()
print(result)
