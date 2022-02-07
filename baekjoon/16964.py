N = int(input())
graph = [[] for _ in range(N+1)]
check = [0]*(N+1)

for _ in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

order_path = list(map(int,input().split()))
path = []
def dfs(x):
    if(check[x] == 1):
        return
    check[x] = 1
    path.append(x)
    for i in graph[x]:
        dfs(i)

my_priority= dict()
for i,v in enumerate(order_path):
    my_priority[v]=i
for i in range(N+1):
    graph[i] = sorted(graph[i],key= lambda x:my_priority[x])
dfs(1)

if order_path == path:
    print(1)
else:
    print(0)