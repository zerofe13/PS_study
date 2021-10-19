from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    graph = [[0 for _ in range(102)]for _ in range(102)]
    visit = [[0 for _ in range(102)]for _ in range(102)]
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    answer = (1e9)
    for x,y,x1,y1 in rectangle:
        for i in range(2*y,(2*y1)+1):
            for j in range(2*x,(2*x1)+1):
                graph[i][j] = 1
    for x,y,x1,y1 in rectangle:
        for i in range((2*y)+1,(2*y1)):
            for j in range((2*x)+1,(2*x1)):
                graph[i][j] = 0
    q = deque()
    q.append((characterX*2,characterY*2))
    visit[characterY*2][characterX*2] = 1
    while q:
        x,y = q.popleft()
        if x == itemX*2 and y == itemY*2:
            break
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<= 102 and 0<= ny <= 102 and graph[ny][nx] == 1 and visit[ny][nx] == 0:
                visit[ny][nx] = visit[y][x]+1
                q.append((nx,ny))
    
    
    return (visit[itemY*2][itemX*2]-1)//2