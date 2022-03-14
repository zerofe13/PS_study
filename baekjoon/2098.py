#TSP
import sys
input = sys.stdin.readline

N = int(input())
city_map = [list(map(int,input().split())) for _ in range(N)]
dp = [[0] * (1 << N) for _ in range(N)]
inf = 1e9

def TSP(now,trace):
    if dp[now][trace]:
        return dp[now][trace]
    if trace == (1<<N)-1:
        return city_map[now][0] if city_map[now][0]>0 else inf
    cost = inf
    for i in range(1,N):
        if not trace & (i<<i) and city_map[now][i]:
            val = TSP(i,trace| (1<<i))
            cost = min(cost,val+city_map[now][i])
        dp[now][trace] = cost
        return dp[now][trace]