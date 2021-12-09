# 2021 dev-matching 행렬 테두리 회전하기
def solution(rows, columns, queries):
    answer = []
    graph = [[0]*columns for _ in range(rows)]
    num = 1
    for i in range(rows):
        for j in range(columns):
            graph[i][j] = num
            num += 1
    for query in queries:
        min_num = 99999
        x1,y1,x2,y2 = query
        temp1,temp2,temp3 = graph[x1-1][y2-1],graph[x2-1][y2-1],graph[x2-1][y1-1]
        graph[x1-1][y1:y2] = graph[x1-1][y1-1:y2-1]
        for i in range(x2-2,x1-2,-1):
            graph[i+1][y2-1] = graph[i][y2-1]
        graph[x2-1][y1-1:y2-1] = graph[x2-1][y1:y2]
        for i in range(x1,x2):
            graph[i-1][y1-1] = graph[i][y1-1]
        graph[x1][y2-1],graph[x2-1][y2-2],graph[x2-2][y1-1] = temp1,temp2,temp3
        min_num = min(min(graph[x1-1][y1-1:y2]),min(graph[x2-1][y1-1:y2]),min_num)
        for i in range(x1,x2):
            min_num  = min(graph[i][y1-1],graph[i][y2-1],min_num)
        answer.append(min_num)
    return answer

print(solution(3,3,[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))