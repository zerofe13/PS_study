def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]
def union(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b
def solution(n, wires):
    answer = (1e9)
    for i in range(len(wires)):
        parent = [x for x in range(n+1)]
        for j in range(len(wires)):
            if i == j:
                continue
            if find_parent(parent,wires[j][0]) != find_parent(parent,wires[j][1]):
                union(parent,wires[j][0],wires[j][1])
        a,b = 0,0
        for i in range(1,n+1):
            if find_parent(parent,parent[i]) ==1:
                a += 1
            else:
                b +=1
        answer=min(answer,abs(a-b))   
    return answer

print(solution(6,[[1, 4], [6, 3], [2, 5], [5, 1], [5, 3]]))