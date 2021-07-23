import copy

N,M = map(int,input().split())
array= [list(map(int,input().split())) for _ in range(N)]
# 오,위,왼,아
dx=[1,0,-1,0]
dy=[0,1,0,-1] 
cctvArr = []
tempArr = copy.deepcopy(array)
result =1e9

for i in range(N):
        for j in range(M):
            if array[i][j] not in [0,6,-1]:
                cctvArr.append((i,j))

dirArr = [0]*len(cctvArr)

def search(i,j,d):

    if array[i][j] ==1:
        x = j
        y = i
        while True:
            nx = x+ dx[d]
            ny = y+ dy[d]
            if 0<=ny<N and 0<=nx<M:
                if array[ny][nx] == 0:
                    array[ny][nx] = -1
                elif  array[ny][nx] == 6:
                    break
                else:
                    x = nx
                    y = ny
            else:
                break
    if array[i][j] == 2:
        x = j
        y = i
        for di in range(0,3,2):
            while True:
                nx = x+ dx[(d+di)%4]
                ny = y+ dy[(d+di)%4]
                if 0<=ny<N and 0<=nx<M:
                    if array[ny][nx] == 0:
                        array[ny][nx] = -1
                        x = nx
                        y = ny
                    elif  array[ny][nx] == 6:
                        x = j
                        y = i
                        break
                    else:
                        x = nx
                        y = ny
                else:
                    x=j
                    y=i
                    break
    if array[i][j] == 3:
        x = j
        y = i
        for di in range(2):
            while True:
                nx = x+ dx[(d+di)%4]
                ny = y+ dy[(d+di)%4]
                if 0<=ny<N and 0<=nx<M:
                    if array[ny][nx] == 0:
                        array[ny][nx] = -1
                        x = nx
                        y = ny
                    elif  array[ny][nx] == 6:
                        x = j
                        y = i
                        break
                    else:
                        x = nx
                        y = ny
                else:
                    x=j
                    y=i
                    break
    if array[i][j] == 4:
        x = j
        y = i
        for di in range(3):
            while True:
                nx = x+ dx[(d+di)%4]
                ny = y+ dy[(d+di)%4]
                if 0<=ny<N and 0<=nx<M:
                    if array[ny][nx] == 0:
                        array[ny][nx] = -1
                        x = nx
                        y = ny
                    elif  array[ny][nx] == 6:
                        x = j
                        y = i
                        break
                    else:
                        x = nx
                        y = ny
                else:
                    x=j
                    y=i
                    break
    if array[i][j] == 5:
        x = j
        y = i
        for di in range(4):
            while True:
                nx = x+ dx[(d+di)%4]
                ny = y+ dy[(d+di)%4]
                if 0<=ny<N and 0<=nx<M:
                    if array[ny][nx] == 0:
                        array[ny][nx] = -1
                        x = nx
                        y = ny
                    elif  array[ny][nx] == 6:
                        x = j
                        y = i
                        break
                    else:
                        x = nx
                        y = ny
                else:
                    x=j
                    y=i
                    break

def count(arr):
    count = 0
    for ar in arr:
        for a in ar:
            if a == 0:
                count +=1
    return count

def dfs(depth):
    global result
    global array
    if depth == len(cctvArr)-1 :
        for i in range(len(cctvArr)):
            search(cctvArr[i][0],cctvArr[i][1],dirArr[i])
        # for i in range(len(array)):
        #     print(array[i])
        # print(" ");
        result = min(result,count(array))
        array = copy.deepcopy(tempArr)
        return
    for i in range(4):
        dirArr[depth+1] = i
        dfs(depth+1)
    
if dirArr:
    for i in range(4):
        dirArr[0] = i
        dfs(0)
else: #cctv없는경우 
    result = count(array)

print(result)