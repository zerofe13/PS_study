# 통나무 옮기기
from collections import deque

N = int(input())
arr = [list(str,input()) for _ in range(N)]
dx=[1,0,-1,0,1,-1,1,-1]
dy=[0,1,0,-1,1,1,-1,-1]
state = 0 # 0 수평 1 수직 
e_state = 0 # 도착지점 상태 도착지점의 중심값과 형태가 통나무와 일치해야한다.
b_pos = [] #통나무의 위치
e_pos = [] # 도착지점 위치 
check=[[[0 for col in range(N)] for row in range(N)] for depth in range(N)] #상태에 따른 방문 체크 

def searchPos(arr): #위치 초기화함수
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'B':
                b_pos.append([i,j])
            elif arr[i][j] == 'E':
                e_pos.append([i,j])

def checkState(posList): # 상태체크 
    if posList[0][0]==posList[1][0]-1: # y ==y-1 수직
        return 1
    elif posList[0][1]==posList[1][1]-1: #x == x-1 수평
        return 0 

def veriticalMovePossible(y,x):  #수직 상태일때 이동가능
    if arr[y+1][x] == "0" and arr[y-1][x] == "0":
        return True
    return False

def horizonMovePossible(y,x): #수평상태일때 이동가능 
    if arr[y][x+1] == "0" and arr[y][x-1] == "0":
        return True
    return False

def turnPossible(y,x): #회전가능 
    for i in range(8):
        nx = x + dx[i]
        ny = y + dx[i]
        if arr[nx][ny] != '0':
            return False
    return True

searchPos(arr)
# tree == target 가 되는 최단거리 (bfs로 구현)
tree = [b_pos[1][0],b_pos[1][1],checkState(b_pos)] #[통나무 중심 y, 통나무 중심 x , 통나무 상태]
target = [e_pos[1][0],e_pos[1][1],checkState(e_pos)] #[목표 중심 y, x, 상태]  
