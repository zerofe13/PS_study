#acm craft
import sys
from collections import deque
input =sys.stdin.readline
reulst = []
T = int(input())
for _ in range(T):
    N,K = map(int,input().split())
    time_list= list(map(int,input().split()))   
    graph = [[] for _ in range(N+1)]
    indegree= [0]*(N+1)
    dp = [0]*(N+1)

    for _ in range(K):
        x,y= map(int,input().split())
        graph[x].append(y)
        indegree[y] += 1
    w = int(input())

    def solution():
        q = deque()
        for i in range(1,len(indegree)):
            if indegree[i] == 0:
                q.append(i)
                dp[i] = time_list[i-1]
        
        while q:
            now = q.popleft()
            for i in graph[now]:
                dp[i] = max(dp[now]+time_list[i-1],dp[i])
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
    solution()
    reulst.append(dp[w])
for r in reulst:
    print(r)