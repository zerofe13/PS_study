#가장 긴 증가하는 부분수열
import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int,input().split()))
dp = [-1e9-1]

for num in num_list:
    if dp[-1] <num :
        dp.append(num)
    else:
        l,r = 0,len(dp)
        while l<r:
            mid = (l+r)//2
            if dp[mid]<num:
                l =mid+1
            else:
                r = mid
        dp[r] = num
print(len(dp)-1)