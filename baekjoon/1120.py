#문자열
import sys
input= sys.stdin.readline

str_a,str_b = map(str,input().split())
result = (1e9)
for i in range(len(str_b) - len(str_a)+1):
    temp = 0
    for j in range(len(str_a)):
        if str_a[j] != str_b[i+j]:
            temp += 1
    result = min(temp,result)
print(result)