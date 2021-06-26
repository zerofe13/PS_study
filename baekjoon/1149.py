N = int(input())
red = []
green=[]
blue = []
dp = [[0]*(N+1) for _ in range(3)]
for i in range(N):
    r,g,b = map(int,input().split())
    red.append(r)
    green.append(g)
    blue.append(b)
dp[0][1] = red[0]
dp[1][1] = green[0]
dp[2][1] = blue[0]

for i in range(2,N+1):
    dp[0][i] = min(dp[1][i-1],dp[2][i-1]) + red[i-1]
    dp[1][i] = min(dp[0][i-1],dp[2][i-1]) + green[i-1]
    dp[2][i] = min(dp[0][i-1],dp[1][i-1],) + blue[i-1]

print(min(dp[0][N],dp[1][N],dp[2][N]))