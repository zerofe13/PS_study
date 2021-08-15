import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())

start = int(input())
graph = [[]for i in range(n+1)]
visited = [False] *(n+1)
distance = [INF] *(n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i]<min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1] ## 시작 노드 에서의 각 노드에 대한 거리 입력
    for i in range(n-1):
        now= get_smallest_node() ## 다음 노드(거리가 가장 짧은노드)로 이동 
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1] ## 현재 노드를 거쳐 가는 경로가 더 짧다면
            if cost < distance[j[0]]:
                distance[j[0]] = cost ## 갱신 

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

    
