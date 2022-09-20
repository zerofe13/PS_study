import sys
from collections import deque

input = sys.stdin.readline

a,b,c, = map(int,input().split())

def sol(a,b,c):
    sum_num = a+b+c
    if sum_num % 3 != 0:
        return 0
    
    visited = [[0]*(sum_num+1) for _ in range((sum_num+1))]
    visited[a][b] = 1
    q = deque() 
    q.append((a,b))
    
    while q:
        a,b = q.popleft()
        c = sum_num - a - b
        if a == b == c:
            return 1
        for x,y in (a,b),(a,c),(b,c):
            if x <y:
                y -= x
                x += x
            elif x>y:
                x -= y
                y += y
            else:
                continue
            z = sum_num - x - y
            min_num = min(x,y,z)
            max_num = max(x,y,z)
            if not visited[min_num][max_num]:
                q.append((min_num,max_num))
                visited[min_num][max_num] = 1
    return 0

print(sol(a,b,c))