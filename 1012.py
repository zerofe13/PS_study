t = int(input())
dx = [1,0,-1,0]
dy = [0,1,0,-1]


for test_case in range(t):
    m,n,k = map(int,input().split())
    counter = 0
    array = [[0]*m for _ in range(n)]
    check = [[0]*m for _ in range(n)]
    for i in range(k):
        x,y = map(int,input().split())
        array[y][x] = 1
    def DFS(x,y):
        check[y][x] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >=0 and ny >= 0 and nx < m and ny <n and check[ny][nx] == 0 and array[ny][nx] == 1:
                DFS(nx,ny)
    for i in range(n):
        for j in range(m):
            if array[i][j] == 1 and check[i][j] == 0:
                DFS(j,i)
                counter += 1
    print(counter)