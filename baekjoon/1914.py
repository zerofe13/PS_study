#하노이 탑
import sys

input = sys.stdin.readline

k = int(input())
def hanoi(n,fr,to,via):
    if n == 1:
        print(fr,to)
        return
    hanoi(n-1,fr,via,to)
    print(fr,to)
    hanoi(n-1,via,to,fr)
    
print(2**k-1)
if(k<=20):
    hanoi(k,1,3,2)