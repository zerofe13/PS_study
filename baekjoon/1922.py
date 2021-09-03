#네트워크 연결
import sys
input= sys.stdin.readline

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

N = int(input())
M = int(input())
computers = []
parent = [0] * (N+1)
result = 0

for i in range(M):
    a,b,cost= map(int,input().split())
    computers.append((cost,a,b))

for i in range(1,N+1):
    parent[i] = i

computers.sort()

for computer in computers:
    cost,a,b = computer
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost

print(result)

