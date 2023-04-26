#14621 크루스칼 (union find)
import sys
input = sys.stdin.readline

def find_parent(x,parent):
    if x != parent[x]:
        parent[x] = find_parent(parent[x],parent)
    return parent[x]

def union_find(a,b,parent):
    a = find_parent(a,parent)
    b = find_parent(b,parent)
    
    if a<b:
        parent[b] = a

    else:
        parent[a] = b

n,m = map(int,input().split())
gen = list(map(int,input().split()))

edges = []
for i in range(m):
    u,v,d = map(int,input().split())
    if gen[u-1] != gen[v-1]:
        edges.append((d,u,v))
        
edges.sort()
parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i
result  = 0
count = 0
for edge in edges:
    d,u,v = edge
    if find_parent(u,parent)!= find_parent(v,parent):
        union_find(u,v,parent)
        result += d
        count += 1
if count != n-1:
    result = -1
print(result)
