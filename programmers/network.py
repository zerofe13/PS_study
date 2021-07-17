from collections import deque
def solution(n, computers):
    answer = 0
    r,c = 0,0
    check= [0] *len(computers)


    def bfs(comN):
        nonlocal answer
        queue =deque()
        queue.append(comN)
        check[comN] = 1
        while queue:
            computerNum = queue.popleft()
            for i in range(n):
                if computers[computerNum][i] ==1 and computers[i][computerNum] ==1 and i != computerNum and check[i] == 0:
                    queue.append(i)
                    check[i] = 1 
        answer +=1    

    for i in range(n):
        if check[i] == 0:
            bfs(i)
    return answer

computers = [[1,1,0],[1,1,0],[0,0,1]]
n = 3
print(solution(n,computers))