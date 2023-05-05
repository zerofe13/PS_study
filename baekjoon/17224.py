import sys
    
input = sys.stdin.readline
# 문제의 수 , 역량, 풀수 있는 최대 개수
n,l,k = map(int,input().split()) 
result = 0
sub_list = []
for i in range(n):
    sub1,sub2 = map(int, input().split())
    sub_list.append((sub1,sub2))
sub_list.sort(key = lambda x:(x[1] ,x[0]))
    
for sub1,sub2 in sub_list:
    if k ==0:
        break
    if sub2 <= l :
        result += 140
        k -= 1
    elif sub1 <=l:
        result += 100
        k -= 1

print(result)

