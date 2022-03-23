#별자리 만들기
import sys
from collections import deque
input = sys.stdin.readline
INF = 1e9 

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
graph = []
star_info = []
parent = [0]*(n+1)
result = 0
for i in range(1,n+1):
    parent[i] = i
    
for i in range(n):
    a,b = map(float,input().split())
    star_info.append((a,b))
for a in range(n):
    for b in range(a,n):
        if a==b:
            continue
        c = round((abs(star_info[a][0]-star_info[b][0])**2 +abs(star_info[a][1]-star_info[b][1])**2)**0.5,2)
        graph.append((c,a+1,b+1))

graph.sort()
for c,a,b in graph:
    if find_parent(parent,a) != find_parent(parent,b):
        result += c
        union_parent(parent,a,b)
print(result)