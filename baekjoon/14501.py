# 퇴사
N = int(input())
arr = [list(map(int,input().split()))for _ in range(N)]
dp = [0]*N
money = 0
for i in range(N):
    money = max(money,dp[i])
    if arr[i][0]+i-1 <= N:
        dp[arr[i][0]+i-1] = max(money+arr[i][1],dp[arr[i][0]+i-1])
print(dp[N])