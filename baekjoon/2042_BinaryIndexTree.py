#펜윅트리 ,바이너리 인덱스 트리 
#백준 2042 구간 합 구하기
import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())

arr = [0] * (n+1)
tree = [0] * (n+1)

def prefix_sum(i):
    result = 0 
    while i>0:
        result += tree[i]
        i -= (i&-i)
    return result

def update(i,dif):
    while i<= n:
        tree[i] += dif
        i +=(i&-i)

def interval_sum(start,end):
    return prefix_sum(end)-prefix_sum(start-1)

for i in range(1,n+1):
    num = int(input())
    arr[i] = num
    update(i,num)

for i in range(m+k):
    a,b,c = map(int,input().split())
    if a == 1:
        update(b,c-arr[b])
        arr[b] =c
    else:
       print(interval_sum(b,c))