def solution(triangle):
    dp = [[0]*(len(triangle[-1])+1) for _ in range(len(triangle[-1]))]
    dp[0][0] = triangle[0][0]
    for  i in range(1,len(triangle)):
        for j in range(0,len(triangle[i])):
            if j == 0:
                dp[i][j] = dp[i-1][j]+triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j]+triangle[i][j],dp[i-1][j-1]+triangle[i][j])
    return max(dp[-1])
    
triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))