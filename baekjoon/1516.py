from collections import deque

n = int(input())
b_time = [0]* (n+1)
graph = [[] for i in range(n+1)]
indegree =[0]*(n+1)
result = [0]*(n+1)

for i in range(1,n+1):
    temp = list(map(int,input().split()))
    for temp_i,a in enumerate(temp):
        if a == -1:
            break
        if temp_i == 0:
            b_time[i] = a
        else:
            graph[a].append(i)
            indegree[i] += 1

def topology_sort():
    q = deque()
    
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        result[now] += b_time[now]
        for i in graph[now]:
            indegree[i] -= 1
            result[i] = max(result[i],result[now])

            if indegree[i] == 0:
                q.append(i)
                
topology_sort()
for i in range(1,n+1):
    print(result[i])
