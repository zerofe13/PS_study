# 2021 카카오 인턴 거리두기 확인하기
from collections import deque
def solution(places):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    answer = []
    
    for place in places:
        queue = deque()
        flag = 0
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    check = [[0] * 5 for _ in range(5)]
                    queue.append((j,i))
                    check[i][j] = 1
                    while queue:
                        x,y = queue.popleft()
                        for k in range(4):
                            nx = x + dx[k]
                            ny = y + dy[k]
                            if 0<=nx<5 and 0<=ny<5 and check[ny][nx] == 0 and abs(i-ny)+abs(j-nx)<3 and place[ny][nx] != 'X':
                                if place[ny][nx] == 'P':
                                    flag = 1
                                check[ny][nx] = check[y][x]+1
                                queue.append((nx,ny))
                            
        if flag == 1:
            answer.append(0)
        else:
            answer.append(1)
    return answer
