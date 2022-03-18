#RGB 거리2
import sys
from unittest import result
input = sys.stdin.readline
INF = 1e9
N = int(input())


rgb = []
result = INF
for _ in range(N):
    rgb.append(list(map(int,input().split())))
for j in range(3):
    dp=[[INF]*N for _ in range(3)]
    dp[j][0] = rgb[0][j]
    for i in range(1,N):
        dp[0][i] = min(dp[1][i-1],dp[2][i-1])+rgb[i][0]
        dp[1][i] = min(dp[0][i-1],dp[2][i-1])+rgb[i][1]
        dp[2][i] = min(dp[1][i-1],dp[0][i-1])+rgb[i][2]
    for i in range(3):
        if i !=j:
            result = min(result,dp[i][-1])

print(result)