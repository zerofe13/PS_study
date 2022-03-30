#피보나치 수 6
import sys
from unittest import result
input = sys.stdin.readline

n = int(input())
a = [[1,1],[1,0]]
mod = 1000000007

def matrix_multi(A,B):
    result = [[0]*len(A[0]) for _ in range(len(A))]
    for row in range(len(A)):
        for col in range(len(A[0])):
            temp = 0
            for i in range(len(B[0])):
                temp += A[row][i] * B[i][col]
            result[row][col] = temp%mod
    return result

def search(A,depth):
    if depth == 1:
        return A
    temp = search(A,depth//2) 
    if depth % 2 == 0 : #2
        return matrix_multi(temp,temp)
    else: #3
        return matrix_multi(matrix_multi(temp,temp),A) 
    
result = search(a,n)
print(result[0][1])