import sys

input = sys.stdin.readline

def divide (a,b,n):
    if n == 1:
        return array[a][b] 
    else:
        temp = [divide(a,b,n//2),divide(a+n//2,b,n//2),divide(a,b+n//2,n//2),divide(a+n//2,b+n//2,n//2)]
        temp.sort()
        return temp[1]
    
n = int(input())
array = [list(map(int,input().split())) for i in range(n)]
print(divide(0,0,n))