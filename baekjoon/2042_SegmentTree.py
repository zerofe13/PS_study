import sys
from math import ceil,log 
input = sys.stdin.readline
n,m,k =map(int,input().split())
arr = [0]*(n+1)
tree = [0]*(2**(ceil(log(n,2))+1))
def init(node,start,end): #트리생성 노드,인덱스 범위 (start,end ) ex) (1,1,n) 1노드에 arr[1]~arr[n] 까지 합 
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    else:
        tree[node]= init(node*2,start,(start+end)//2)+init(node*2+1,(start+end)//2+1,end)
        return tree[node]
def interval_sum(node,start,end,left,right): #노드 인덱스 범위 , 구간합 구간
    if start>right or end<left:
        return 0
    if start >= left and end <=right:
        return tree[node]
    return interval_sum(node*2,start,(start+end)//2,left,right) +interval_sum(node*2+1,(start+end)//2+1,end,left,right)
def update(node,start,end,index,diff):
    if index<start or index>end:
        return
    tree[node] += diff
    if start != end:
        update(node*2,start,(start+end)//2,index,diff)
        update(node*2+1,(start+end)//2+1,end,index,diff)
for i in range(1,n+1):
    num = int(input())
    arr[i] = num
init(1,1,n)
for i in range(m+k):
    a,b,c = map(int,input().split())
    if a == 1:
        update(1,1,n,b,c-arr[b])
        arr[b] =c
    else:
       print(interval_sum(1,1,n,b,c))