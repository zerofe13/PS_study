# 통나무 옮기기
N = int(input())
arr = [list(str,input()) for _ in range(N)]
state = 0 # 0 수평 1 수직 
def searchPos(arr):
    pos = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'B':
                pos.append([i,j])
    return pos[1]

def up(state): #x,y 통나무 중심 위치
    y,x = searchPos(arr)
    if state == 0:    
        if y-1 >=0 and arr[y-1][x-1]=='0' and arr[y-1][x]=='0' and arr[y-1][x+1]=='0':
            for x in (x-1,x,x+1):
                arr[y][x] = '0'
                arr[y-1][x] = 'B'
    else:
        if y-2 >=0 and arr[y-2][x]=='0':
            arr[y+1][x] ='0'
            arr[y-2][x] ="B"
def down(state): #x,y 통나무 중심 위치
    y,x = searchPos(arr)
    if state == 0:    
        if y+1 <N and arr[y+1][x-1]=='0' and arr[y+1][x]=='0' and arr[y+1][x+1]=='0':
            for x in (x-1,x,x+1):
                arr[y][x] = '0'
                arr[y+1][x] = 'B'
    else:
        if y+2 <0 and arr[y+2][x]=='0':
            arr[y-1][x] ='0'
            arr[y+2][x] ="B"
def left(state): #x,y 통나무 중심 위치
    x,y = searchPos(arr)
    if state == 1:    
        if x-1 >=0 and arr[x-1][y-1]=='0' and arr[x-1][y]=='0' and arr[x-1][y+1]=='0':
            for x in (y-1,y,y+1):
                arr[x][y] = '0'
                arr[x-1][y] = 'B'
    else:
        if x-2 >=0 and arr[x-2][y]=='0':
            arr[x+1][y] ='0'
            arr[x-2][y] ="B"
def right(state):
    x,y = searchPos(arr)
    if state == 1:    
        if x+1 <N and arr[x+1][y-1]=='0' and arr[x+1][y]=='0' and arr[x+1][y+1]=='0':
            for x in (y-1,y,y+1):
                arr[x][y] = '0'
                arr[x+1][y] = 'B'
    else:
        if x+2 <0 and arr[x+2][y]=='0':
            arr[x][y-1] ='0'
            arr[x][y+2] ="B"