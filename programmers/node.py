from collections import deque
# def solution(n, edge):
#     map = [[0 for _ in range(n)] for _ in range(n)]
#     distList = [0]*n
#     maxDist = 0
#     visited = [False]*n
#     visitedCount= 0
#     for e in edge:
#         map[e[0]-1][e[1]-1] = 1
#         map[e[1]-1][e[0]-1] = 1
#     q = deque()
#     #1번 노드 
#     visited[0]= True
#     for i in range(n):
#         if map[0][i] == 1:
#             q.append(i)
#             visited[i] = True
#             visitedCount = visitedCount +1 
#             distList[i] = 1
#     while q:
#         if visitedCount == 6:
#             break
#         n_node = q.popleft()
#         for i in range(n):
#             if map[n_node][i] == 1 and visited[i] == False:
#                 q.append(i)
#                 visited[i] = True
#                 visitedCount = visitedCount +1 
#                 distList[i] = distList[n_node]+1
#                 maxDist = max(maxDist,distList[i])
#     answer = 0
#     for dist in distList:
#         if dist == maxDist :
#             answer = answer +1 
#     return answer
# 인접행렬방식 7,8,9 case 시간초과
def solution(n,edge):
    distList = [0]*(n+1)
    maxDist = 0
    visited = [False]*(n+1)
    visitedCount= 0

    v_dic = {i:[] for i in range(n+1)}
    for e in edge:
        v_dic[e[0]].append(e[1])
        v_dic[e[1]].append(e[0])
    
    q = deque()
    # 1 번 노드
    visited[1]= True
    for i in v_dic[1]:
        q.append(i)
        visited[i] = True
        visitedCount = visitedCount +1 
        distList[i] = 1     

    while q:
        if visitedCount == n-1:
            break
        n_node = q.popleft()
        for i in v_dic[n_node]:
            if visited[i] == False:
                q.append(i)
                visited[i] = True
                visitedCount = visitedCount +1 
                distList[i] = distList[n_node]+1
                maxDist = max(maxDist,distList[i])
    answer = 0
    for dist in distList:
        if dist == maxDist :
            answer = answer +1 
    return answer

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n,edge))