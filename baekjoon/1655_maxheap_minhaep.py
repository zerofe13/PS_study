#가운데를 말요 (min heap, max heap)
import sys
import heapq

input = sys.stdin.readline
maxheap = []
minheap = []

n = int(input())

for i in range(n):
    num = int(input())
    if len(maxheap) <= len(minheap):
        heapq.heappush(maxheap,(-num,num))
    else:
        heapq.heappush(minheap,(num,num))
    if i>0 and maxheap[0][1] > minheap[0][1]:
        maxnum = heapq.heappop(maxheap)[1]
        minnum = heapq.heappop(minheap)[1]
        
        heapq.heappush(maxheap,(-minnum,minnum))
        heapq.heappush(minheap,(maxnum,maxnum))
    print(maxheap[0][1])
    