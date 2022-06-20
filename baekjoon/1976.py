#여행가자
import sys

input = sys.stdin.readline

def find_parent(x,parent):
    if parent[x] != x:
        parent[x] = find_parent(parent[x],parent)
    return parent[x]
def union_parent(a,b,parent):
    a = find_parent(a,parent)
    b = find_parent(b,parent)
    if a>b:
        parent[a]=b
    else:
        parent[b]=a

n = int(input())
m = int(input())

graph = [list(map(int,input().split())) for _ in range(n)]
parent = [0] * (n+1)
order = list(map(int,input().split()))

for i in range(1,n+1):
    parent[i] =i
    
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union_parent(i+1,j+1,parent)
        
result = "YES";
for i in range(1,len(order)):
    if(parent[order[i]] !=parent[order[i-1]]):
        result="NO"
        break
print(result)