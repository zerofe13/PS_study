from collections import deque
N,M,K = map(int,input().split())
arr = [list(map(int,input().split()))for _ in range(N)]
array = [[5]*N for _ in range(N)] 
treeArr = [[deque()for _ in range(N)]for _ in range(N)]
count = 0
for _ in range(M):
    x,y,z = map(int,input().split())
    treeArr[x-1][y-1].append(z)
    count += 1

dx = [1,1,1,0,0,-1,-1,-1]
dy = [1,0,-1,1,-1,1,0,-1]

def solution ():
    global count
    for i in range(N):
        for j in range(N):
            if treeArr[i][j]:
                for z in range(len(treeArr[i][j])):
                    if array[i][j] >= treeArr[i][j][z]:
                        array[i][j] -= treeArr[i][j][z]
                        treeArr[i][j][z] += 1
                    else:
                        for _ in range(z,len(treeArr[i][j])):
                            array[i][j] += treeArr[i][j].pop()//2
                            count -= 1
                        break
    for i in range(N):
        for j in range(N):
            if treeArr[i][j]:
                for tree in treeArr[i][j]:
                    if tree% 5 ==0:
                        for d in range(8):
                            nx = j +dx[d]
                            ny = i +dy[d]
                            if nx >= 0 and nx <N and ny >= 0 and ny<N:
                                treeArr[ny][nx].appendleft(1)
                                count += 1
            array[i][j] += arr[i][j]
    
for i in range(K): 
    solution()

print(count)