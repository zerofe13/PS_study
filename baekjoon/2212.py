#백준 2212 센서
import sys
input = sys.stdin.readline

#n 센서 , k 집중국
n = int(input())
k = int(input())
sen_list = list(map(int,input().split()))
sen_list.sort()
dist=[]

for i in range(1,len(sen_list)):
    dist.append(abs(sen_list[i-1]-sen_list[i]))

dist.sort(key = lambda x: -x)
print(sum(dist[k-1:]))