# 우주신과의 교감
import sys
import math
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

def calc_dist(a,b,c,d):
    return ((abs(a-c)**2)+(abs(b-d)**2))**(1/2)

n,m = map(int,input().split())
parent = [i for i in range(n+1)]
pos_dict = dict()
edges = []
result = 0

for i in range(n):
    x,y = map(int,input().split())
    pos_dict[i+1] = (x,y)

for i in range(m):
    a,b = map(int,input().split())
    union_parent(parent,a,b)
    #result += calc_dist(pos_dict[a][0],pos_dict[a][1],pos_dict[b][0],pos_dict[b][1])

for i in range(1,n+1):
    for j in range(i,n+1):
        edges.append((calc_dist(pos_dict[i][0],pos_dict[i][1],pos_dict[j][0],pos_dict[j][1]),i,j))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost
print("{0:.2f}".format(result))