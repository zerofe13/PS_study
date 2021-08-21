# def solution(m,n,puddles):
    
#     answer = 0
#     dp=[[0]*m for _ in range(n)]
#     for i in range (n):
#         dp[i][0] = 1
#     for i in range(m):
#         dp[0][i] = 1
#     # puddles  가 1행 이거나 1열 일경우 
#     for x,y in puddles:
#         dp[y-1][x-1] = 0
#     for i in range(1,n):
#         for j in range(1,m):
#             if [j+1,i+1] in puddles:
#                 dp[i][j] = 0
#             else :
#                 dp[i][j] = dp[i][j-1] + dp[i-1][j]
#     answer = dp[n-1][m-1]%1000000007
#     return answer
#  초기값 세팅 1 로 하면 오류남

def solution(m,n,puddles):
    
    answer = 0
    dp=[[0]*(m+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if [j,i] == [1,1]:
                dp[1][1] = 1
                continue
            if [j,i] in puddles:
                dp[i][j] = 0
            else :
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
    answer = dp[n][m]%1000000007
    return answer

print(solution(4,3,[[2,2]]))