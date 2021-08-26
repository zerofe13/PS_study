# 숨바꼭질3
# x -> 걷기 1초후 x-1, x+1 순간이동 2*x
import sys
import heapq
input = sys.stdin.readline
INF = (1e9)

start, target = map(int,input().split())
distList = [INF] * 200001
def dikstar(start): # graph 대신 각 노드에 걷기와 순간이동시 노드와 코스트를 사용, 루프는 target 노드에 도착시 종료
    q= []
    heapq.heappush(q,(0,start))
    distList[start] = 0
    while q :
        dist,now = heapq.heappop(q)
        if distList[now] < dist:
            continue
        cost = 1 + dist # x+1 
        if cost < distList[now+1] and now+1<= target:
            heapq.heappush(q,(cost,now+1))
            distList[now+1] = cost
        cost = 1 + dist # x+1 
        if cost < distList[now-1] and now-1 >=0:
            heapq.heappush(q,(cost,now-1))
            distList[now-1] = cost
        cost = 0 + dist # x+1 
        if (2*now)<=2*target and cost < distList[2*now] :
            heapq.heappush(q,(cost,2*now))
            distList[2*now] = cost

        if now == target:
            break

dikstar(start)
print(distList[target])