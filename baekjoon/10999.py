#구간 합 구하기2
import sys
input = sys.stdin.readline
n,m,k = map(int,input().split())

arr= [0]*(n+1)
tree = [0]*(n+1)

def prefix_sum(i):
    result = 0
    while i>0:
        result+=tree[i]
        i -=(i&-i)
    return result

def update(i,dif):
    while i<=n:
        tree[i] += dif
        i += (i&-i)
def interval_snm(start,end):
    return(prefix_sum(end)-prefix_sum(start-1))

for i in range(1,n+1):
    num = int(input())
    arr[i] = num
    update(i,num)

for i in range(m+k):
    a = list(map(int,input().split()))
    if a[0] == 1:
        for i in range(a[1],a[2]+1):
            arr[i] += a[3]
            update(i,a[3])
    else:
        print(interval_snm(a[1],a[2]))