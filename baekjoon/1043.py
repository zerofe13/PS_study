import sys
from typing import Tuple
input = sys.stdin.readline

N,M = map(int,input().split())
true_list = list(map(int,input().split())) # [0] 은 사람수
party_list = [[] for _ in range(M)]
visited = [0]*(M)
count = 0
for i in range(M):
    party_list[i] = list(map(int,input().split()))

true_set = set(true_list[1:])
party_set = [{} for _ in range(M)]
for i in range(len(party_list)):
    party_set[i] = set(party_list[i][1:])

def solution(flag):
    global true_set , count 
    for i in range(len(party_set)):
        if party_set[i] & true_set:
            if party_set[i] - true_set:
                true_set |= party_set[i] - true_set
                count = 0
                solution(flag)
                return
            elif visited[i] == 0:
                count += 1
    return
solution(True)
print(M- count)