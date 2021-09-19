#구간 합 구하기2
import sys
from math import ceil,log
input = sys.stdin.readline
n,m,k = map(int,input().split())

arr= [0]*(n+1)
tree = [0]*(2**ceil(log(n,2)+1))
lazy = [0]*(2**ceil(log(n,2)+1))
def init(node,start,end):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    else:
        tree[node] = init(node*2,start,(start+end)//2)+init(node*2+1,(start+end)//2+1,end)
        return tree[node]
def lazy_propagate(node,start,end): #나중에 업데이트할 정보를 레이지 배열에 저장
    if lazy[node] != 0:
        tree[node] += (end-start+1)*lazy[node]
        if start != end:
            lazy[2*node] += lazy[node]
            lazy[2*node+1] += lazy[node]
    lazy[node] = 0
def update(node,start,end,left,right,diff):
    lazy_propagate(node,start,end) # 레이지 업데이트 후 업데이트
    if start>right or end<left:
        return
    if left<=start and end <= right:
        tree[node] +=(end-start+1)*diff 
        if start != end:
            lazy[2*node] += diff
            lazy[2*node+1] += diff #레이지에 정보를 저장후 리턴 레이지 정보는 나중에 방문할 일이 있을때 업데이트 된다
        return
    update(node*2,start,(start+end)//2,left,right,diff)
    update(node*2+1,(start+end)//2+1,end,left,right,diff)
    tree[node] = tree[node*2]+tree[node*2+1] # 부모 노드의 값을 업데이트 해준다.
def interval_sum(node,start,end,left,right):
    lazy_propagate(node,start,end) # 구간 합을 구하기전 레이지 업데이트 
    if start>right or end<left:
        return 0 
    if left<=start and end <= right:
        return tree[node]
    return interval_sum(node*2,start,(start+end)//2,left,right)+interval_sum(node*2+1,(start+end)//2+1,end,left,right)
for i in range(1,n+1):
    num = int(input())
    arr[i] = num
init(1,1,n)

for i in range(m+k):
    a = list(map(int,input().split()))
    if a[0] == 1:
        update(1,1,n,a[1],a[2],a[3])
    else:
        print(interval_sum(1,1,n,a[1],a[2]))