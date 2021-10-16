import sys
from itertools import combinations
input =sys.stdin.readline

n,m = map(int,input().split())
n_list = [i for i in range(1,n+1)]

result =combinations(n_list,m)
result = sorted(result)
for temp in result:
    for i in temp:
        print(i,end=' ')
    print()