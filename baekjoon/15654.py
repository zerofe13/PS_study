import sys
from itertools import permutations
input =sys.stdin.readline

n,m = map(int,input().split())
n_list = list(map(int,input().split()))

result =permutations(n_list,m)
result = sorted(result)
for temp in result:
    for i in temp:
        print(i,end=' ')
    print()