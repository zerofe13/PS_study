import sys
input = sys.stdin.readline
INF = 1000000000
def solution(n, s, a, b, fares):
    answer =INF
    graph = [[INF]*(n+1) for _ in range(n+1)]
    for c in range(1,n+1):
        for d in range(1,n+1):
            if c== d:
                graph[c][d] = 0
    for c,d,f in fares:
        graph[c][d] = f
        graph[d][c] = f

    for k in range(1,n+1):
        for c in range(1,n+1):
            for d in range(1,n+1):
                graph[c][d] = min(graph[c][d],graph[c][k]+graph[k][d])
    
    for i in range(1,n+1):
        answer = min(answer,graph[s][i]+graph[i][a]+graph[i][b])
    return answer


fares=[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(6,4,6,2,fares))
