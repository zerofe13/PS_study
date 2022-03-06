# 1987 알파벳
import sys

input = sys.stdin.readline
dx = [0,1,0,-1]
dy = [1,0,-1,0]

r,c = map(int,input().split())
graph = []

for i in range(r):
    alpa_list = input().rstrip()
    graph.append(alpa_list)

check_alpa = [0]*26
visited = [[0]*c for _ in range(r)]
result = 0
def dfs (x,y,depth,check):
    global result
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >=0 and ny >= 0 and nx<c and ny<r:
            if check[ord(graph[ny][nx]) -ord("A")] == 0 and visited[ny][nx] == 0:
                check[ord(graph[ny][nx]) -ord("A")] = 1
                visited[ny][nx] =1
                dfs (nx,ny,depth+1,check)
                check[ord(graph[ny][nx]) -ord("A")] = 0
                visited[ny][nx] = 0
    result = max(result,depth)
check_alpa[ord(graph[0][0])-ord("A")] = 1
visited[0][0] = 1 
dfs(0,0,1,check_alpa)
print(result)