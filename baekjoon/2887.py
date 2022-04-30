import sys
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]
    
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b
        
n = int(input())
parent = [0] *(n+1)
for i in range(n+1):
    parent[i]=i

planet = []
edges = []
for i in range(n):
    a,b,c = map(int,input().split())
    planet.append((a,b,c,i))
for i in range(3):
    planet.sort(key = lambda x:x[i])
    for j in range(1,n):
        edges.append((abs(planet[j-1][i] - planet[j][i]),planet[j-1][3],planet[j][3]))
edges.sort()
result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost

print(result)
