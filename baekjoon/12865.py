import sys
input =sys.stdin.readline

n,k = map(int,input().split())
w,v = [0],[0]
dp=[[0 for _ in range(k+1)]for _ in range(n+1)]
for i in range(n):
    a,b= map(int,input().split())
    w.append(a)
    v.append(b)
for i in range(n+1):
    for j in range(k+1):
        if w[i] <= j :
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-w[i]]+v[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][k])
