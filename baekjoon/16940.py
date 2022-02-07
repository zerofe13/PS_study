from collections import deque
from sys import path_hooks

n = int(input())
graph = [[] for _ in range(n+1)]
check = [0]*(n+1)


for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

order_path = list(map(int,input().split()))

my_priority = dict()

for i,v in enumerate(order_path):
    my_priority[v] = i
for i in range(len(graph)):
    graph[i] = sorted(graph[i], key=lambda x:my_priority[x])
path = []
q = deque()
q.append(1)
path.append(1)
check[1] = 1
while q:
    now = q.popleft()
    for a in graph[now]:
        if check[a] == 0:
            q.append(a)
            path.append(a)
            check[a] = 1
print(path)
if path == order_path:
    print(1)
else:
    print(0)