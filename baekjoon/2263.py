# import sys
# input = sys.stdin.readline

# n = int(input())

# in_order = list(map(int,input().split()))
# post_order = list(map(int,input().split()))

# graph =[[] for _ in range(n+1)]

# def pre_order(root):
#     print(root,end=" ")
#     if len(graph[root])==0:
#         return
#     elif len(graph[root])==1:  
#         pre_order(graph[root][0])
#     else:
#         pre_order(graph[root][0])
#         pre_order(graph[root][1])
# def search_graph(root,in_order,post_order):
#     right = post_order[-2]
#     if len(in_order) == 2:
#         graph[root].append(right)
#         return
#     for i,v in enumerate(in_order):
#         if v == root:
#             if i == len(in_order)-1:
#                 flag = in_order[i]
#                 graph[root].append(right)
#                 search_graph(right,in_order[:-1],post_order[:-1])
#                 return
#             elif i == 0:
#                 graph[root].append(right)
#                 search_graph(right,in_order[1:],post_order[:-1])
#                 return
#             else:   
#                 flag= in_order[i+1]
#                 in_order_index =i 
#                 break
#     for i,v in enumerate(post_order):
#         if v == flag:
#                 left = post_order[i-1]
#                 post_order_index =i
#                 break
    
#     graph[root].append(left)
#     graph[root].append(right)
    
#     if len(in_order[:in_order_index]) >= 2 and len(post_order[:post_order_index]) >= 2:
#         search_graph(left,in_order[:in_order_index],post_order[:post_order_index])
        
#     if len(in_order[in_order_index+1:]) >= 2 and len(post_order[post_order_index:-1]) >= 2:
#         search_graph(right,in_order[in_order_index+1:],post_order[post_order_index:-1])
        
# search_graph(post_order[-1],in_order,post_order)
# pre_order(post_order[-1])

# 7 3 8 1 9 4 10 0 11 5 2 6
# 7 8 3 9 10 4 1 11 5 6 2 0


import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find_pre_order(l_in,r_in,l_post,r_post):
    if l_in>r_in or l_post>r_post:
        return
    parent = post_order[r_post]
    print(parent,end=' ')
    
    split_idx = idx[parent]
    left = split_idx-l_in
    
    find_pre_order(l_in,split_idx-1,l_post,(l_post+left)-1)
    find_pre_order(split_idx+1,r_in,l_post+left,r_post-1)

n= int(input())
in_order = list(map(int,input().split()))
post_order =list(map(int,input().split()))

idx = [0]*(n+1)
for i in range(n):
    idx[in_order[i]]=i

find_pre_order(0,n-1,0,n-1)