#MST
import sys
input = sys.stdin.readline
def find_parent(parent,x):
    if parent[x] !=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b
result = 0
N = int(input())
wells=[]
for i in range(1,N+1):
    cost = int(input())
    wells.append((cost,0,i))
array = [list(map(int,input().split())) for _ in range(N)]
parent = [i for i in range(N+1)]

for i in range(N):
    for j in range(i+1,N):
        wells.append((array[i][j],i+1,j+1))

wells.sort()
for well in wells:
    c,a,b = well
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += c

print(result)
