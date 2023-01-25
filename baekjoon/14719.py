import sys

input = sys.stdin.readline

h,w = map(int,input().split())
block_list = list(map(int,input().split()))
sum_num = 0
for i in range(1,w-1):
    l_m = max(block_list[:i])
    r_m = max(block_list[i+1:])
    
    num = min(l_m,r_m)
    
    if num> block_list[i]:
        sum_num += num-block_list[i]
print(sum_num)
