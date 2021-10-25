def solution(k, dungeons):
    answer = -1
    visit = [0 for _ in range(len(dungeons))]
    
    def dfs(k,depth):
        nonlocal answer
        answer = max(depth,answer)
        for i in range(len(visit)):
            if visit[i] == 0 and k >= dungeons[i][0]:
                k -= dungeons[i][1]
                visit[i] = 1
                dfs(k,depth+1)
                visit[i] = 0 
                k += dungeons[i][1]
    dfs(k,0)
    return answer