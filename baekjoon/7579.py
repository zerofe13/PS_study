#앱
import sys
from unittest import result
input =sys.stdin.readline

N,M = map(int,input().split())

mem_list =[0] + list(map(int,input().split()))
cost_list =[0] + list(map(int,input().split()))

sum_cost = sum(cost_list)
result = 1e9
dp = [[0]*(sum_cost+1) for _ in range(N+1)]

for i in range(N+1):
    for j in range(sum_cost+1):
        if cost_list[i]<=j:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-cost_list[i]]+mem_list[i])
        else:
            dp[i][j]=dp[i-1][j]
        if dp[i][j] >= M:
           result = min(j,result) 
print(result)
for i in dp:
    print(i)