#greedy
import sys
input = sys.stdin.readline

N = int(input())
dice = list(map(int,input().split()))
min_side = [min(dice[0],dice[5]),min(dice[1],dice[4]),min(dice[2],dice[3])]
min_side.sort()
three_side,two_side,one_sied= 4,4*(N-1)+4*(N-2),4*(N-1)*(N-2)+(N-2)**2
result = one_sied*min_side[0]+two_side*(min_side[0]+min_side[1])+three_side*sum(min_side)
if N == 1:
    result = sum(dice)-max(dice)
print(result)