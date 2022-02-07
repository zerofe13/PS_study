from collections import deque
n = int(input())

tree= [[] for _ in range(n)]
check = [0] *(n)
order = list(map(int,input().split())) 
q = deque()
root = 0
for i,a in enumerate(order):
    if a == -1:
        root = i
        continue
    tree[a].append(i)

b =int(input())
tree[b] = []
count =0
q.append(root)
check[root] = 1
if b != root:
    while q:
        now = q.popleft()
        if len(tree[now]) == 0:
            count += 1
        for i in tree[now]:
            if check[i] == 0 and i != b:
                check[i] = 1
                q.append(i)
            elif i==b and len(tree[now]) == 1:
                count += 1
    print(count)
else:
    print(0)
