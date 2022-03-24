#트리순회
import sys
input = sys.stdin.readline

graph= [[] for _ in range(26)]

n=int(input())
for i in range(n):
    a,b,c = input().split()
    graph[ord(a) - ord("A")].append(ord(b)-ord("A"))
    graph[ord(a) - ord("A")].append(ord(c)-ord("A"))
    
def pre_order(n):
    print(chr(n+ord('A')),end="")
    if graph[n][0] > 0:
        pre_order(graph[n][0])
    if graph[n][1]>0:
        pre_order(graph[n][1])
def in_order(n):
    if graph[n][0] > 0:
        in_order(graph[n][0])
    print(chr(n+ord('A')),end="")
    if graph[n][1]>0:
        in_order(graph[n][1])
def post_order(n):
    if graph[n][0] > 0:
        post_order(graph[n][0])
    if graph[n][1]>0:
        post_order(graph[n][1])
    print(chr(n+ord('A')),end="")
pre_order(0)
print()
in_order(0)
print()
post_order(0)
print()