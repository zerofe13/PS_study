#용액
import sys
input = sys.stdin.readline

n = int(input())
num_list= list(map(int,input().split()))
result =[1e11,0]
left,right = 0, n-1
while True:
    if left >= right:
        break
    sum_num = num_list[left] + num_list[right]
    if abs(sum_num) < abs(sum(result)):
        result = [num_list[left],num_list[right]]
    if sum_num > 0:
        right -= 1
    elif sum_num < 0 :
        left += 1
    else:
        break

print(*sorted(result))