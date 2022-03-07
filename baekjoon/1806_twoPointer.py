#1806 부분합 
# 완전탐색 시간초과 O(N^2)나옴
import sys

input =sys.stdin.readline

N,S = map(int,input().split())
num_list = list(map(int,input().split()))

left,right = 0,0
result = 1e9
num_sum  =num_list[left]

while True:
    if num_sum >= S:
        num_sum -= num_list[left]
        result =min((right-left+1),result)
        left += 1 
    elif right <= len(num_list): 
        right += 1
        if right == len(num_list):
            break
        num_sum += num_list[right]

if result == 1e9:
    print(0)
else:
    print(result)