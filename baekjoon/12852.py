import sys

input = sys.stdin.readline

n = int(input())
INF = 1e9
dp = [0]*(n+1)
for i in range(n+1):
    dp[i] =INF
dp[n] = 0
for i in range(n,1,-1):
    if i%3 == 0:
        dp[i//3] = min(dp[i//3],dp[i]+1)
    if i%2 == 0:
        dp[i//2] = min(dp[i//2],dp[i]+1)
    dp[i-1] = min(dp[i]+1,dp[i-1])
print(dp[1])
count = dp[1]
num = 1
temp = [1]
for i in range(2,n+1):
    if count == 0:
        break
    if num*3 == i and dp[i] == count -1:
        temp.append(i)
        num = i
        count -=1
    elif num *2 == i and dp[i] == count -1 :
        temp.append(i)
        num = i
        count -=1
    elif num +1 == i and dp[i] == count -1 :
        temp.append(i)
        num = i
        count -= 1
for i in reversed(temp):
    print(i, end=" ")