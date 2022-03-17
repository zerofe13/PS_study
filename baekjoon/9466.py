#텀프로젝트
import sys
from collections import deque
input= sys.stdin.readline
sys.setrecursionlimit(10**5)
T = int(input())
for t in range(T):
    n = int(input())
    num_list = [0]
    visited = [0] * (n+1)
    temp_list = list(map(int,input().split()))
    num_list = num_list + temp_list
    result =[]
    def dfs(i):
        global result
        visited[i] = 1
        path.append(i)
        if visited[num_list[i]] == 0:
            dfs(num_list[i])
        elif num_list[i] in path:
            result += path[path.index(num_list[i]):]
        return
    for i in range(1,n+1):
        if visited[i] == 0:
            path = []    
            dfs(i)
    
    print(n-len(result))
