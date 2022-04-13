#행렬 곱셈 순서
import sys
input = sys.stdin.readline


N = int(input())
matrix_list = [list(map(int,input().split())) for _ in range(N)]
dp = [[0] *(N) for _ in range(N)]

for i in range(1,N):
    for j in range(N-i):
        dp[j][j+i]=2**31
        for k in range(j,j+i):
            dp[j][j+i] = min(dp[j][j+i],dp[j][k]+dp[k+1][j+i]+matrix_list[j][0]*matrix_list[k][1]*matrix_list[j+i][1])
    

print(dp[0][N-1])