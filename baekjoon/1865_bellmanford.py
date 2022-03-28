import sys
input = sys.stdin.readline
INF = 1e9
t= int(input())
for _ in range(t):
    # n 지점 m 도로 w 웜홀
    n,m,w = map(int,input().split())
    
    graph = []
    dist =[INF] *(n+1)
    for i in range(m):
        s,e,t = map(int,input().split())
        graph.append((s,e,t))
        graph.append((e,s,t))
    for i in range(w):
        s,e,t = map(int,input().split())
        graph.append((s,e,-t))

    def bf(start):
        dist[start] = 0
        for i in range(n):
            for j in range(m*2+w):
                now = graph[j][0]
                next_node = graph[j][1]
                cost = graph[j][2]
                if dist[next_node]>dist[now] + cost:
                    dist[next_node] = dist[now]+cost
                    if i == n-1: #마지막 노드에서 한번더 갱신된다면 음수 루틴 존재 = 시간이 줄어듬
                        return True
        return False
    
    cycle_check = bf(1)
    if cycle_check:
        print("YES")
    else:
        print("NO")