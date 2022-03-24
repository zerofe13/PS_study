import sys
import math
input = sys.stdin.readline

n,m = map(int,input().split())

n_f =math.factorial(n)
m_f =math.factorial(m)
n_m_f=math.factorial(n-m)

print(n_f//(m_f*n_m_f))