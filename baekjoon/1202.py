#보석도둑 
import sys
import heapq
input = sys.stdin.readline

n,k = map(int,input().split())
gem =[]
for _ in range(n):
    m,v = map(int,input().split())
    heapq.heappush(gem,(m,v))
bag_size = [int(input()) for _ in range(k)]

bag_size.sort()

q= []
result = 0
for w in bag_size:
    while gem and w>=gem[0][0]:
        m,v = heapq.heappop(gem)
        heapq.heappush(q,-v)
    if q:
        result -= heapq.heappop(q)

print(result)
