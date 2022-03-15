#팰린드롬 
import sys
input = sys.stdin.readline

N = int(input())
num_list=list(map(int,input().split()))
M = int(input())
dp = [[0]*(N) for _ in range(N)]

#dp 
for i in range(N):
    for j in range(N-i):
        x,y = i+j,j
        if x == y:
            dp[y][x] =1
        elif x == y+1 and num_list[x] == num_list[y]:
            dp[y][x] = 1
        elif num_list[x] == num_list[y] and dp[y+1][x-1] == 1:
            dp[y][x] = 1

for _ in range(M):
    s,e = map(int,input().split())
    if dp[s-1][e-1] == 1:
        print(1)
    else:
        print(0)

