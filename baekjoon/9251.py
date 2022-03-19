#LSC
import sys
input = sys.stdin.readline

arr = list(input().strip())
arr2 = list(input().strip())

dp = [[0]*(len(arr)+1) for _ in range(len(arr2)+1)]
for i in range(1,len(arr2)+1):
    for j in range(1,len(arr)+1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        if arr[j-1] == arr2[i-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

print(dp[len(arr2)][len(arr)])