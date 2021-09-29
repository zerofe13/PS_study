#구간 합 구하기 5
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
sum_arr = [[0]*(N+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,N+1):
        if i == 1:
            sum_arr[i][j] = sum_arr[i][j-1] +arr[i-1][j-1]
            continue
        if j == 1:
            sum_arr[i][j] = sum_arr[i-1][j] +arr[i-1][j-1]
            continue
        sum_arr[i][j]=sum_arr[i-1][j]+sum_arr[i][j-1]-sum_arr[i-1][j-1]+arr[i-1][j-1]

def interval_sum(sum_arr,x1,y1,x2,y2):
    result = sum_arr[x2][y2] + sum_arr[x1-1][y1-1]-sum_arr[x1-1][y2]-sum_arr[x2][y1-1]
    return result
for i in range(M):
    x1,y1,x2,y2 = map(int,input().split())
    print(interval_sum(sum_arr,x1,y1,x2,y2))