#1644 소수의 연속합
#에라토스테네스의 체, 투포이터
import sys

input = sys.stdin.readline
N = int(input())
def is_prime_num(n):
    arr =[True] *(n+1)
    arr[0] = False
    arr[1] = False

    for i in range(2,int(n**0.5)+1):
        if arr[i] == True:
            j = 2
            while (i*j)<=n:
                arr[i*j] = False
                j += 1

    return arr
def solution():
    arr = is_prime_num(N)
    prime_list = []
    for i,v in enumerate(arr):
        if v == True:
            prime_list.append(i)

    L,R  = 0,0
    sum_num = prime_list[0]
    result = 0
    while L<= len(prime_list):
        if L == len(prime_list)-1:
            if sum_num == N:
                result += 1
            break
        if sum_num >= N:
            if sum_num == N:
                result += 1
            sum_num -= prime_list[L]
            L += 1
        else:
            R += 1
            sum_num += prime_list[R]
    return result
if N == 1 or N == 0:
    print(0)
else:
    print(solution())