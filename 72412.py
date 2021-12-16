# 2021 kakao blind 순위검색 (이진탐색)
from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    answer = []
    info_dict = {}
    for i in range(len(info)):
        temp = info[i].split()
        v = temp[-1]
        k = temp[:-1]
        for j in range(5):
            for combi in combinations(k,j):
                k_temp = ''.join(combi)
                if k_temp in info_dict:
                    info_dict[k_temp].append(int(v))
                else:
                    info_dict[k_temp] = [int(v)]
    for k in info_dict:
        info_dict[k].sort()
    for i in range(len(query)):
        temp = query[i].split()
        q_v = temp[-1]
        q_k = temp[:-1]
        while 'and' in q_k:
            q_k.remove('and')
        while '-' in q_k:
            q_k.remove('-')
        q_k = ''.join(q_k)
        if  q_k in info_dict:
            answer.append(len(info_dict[q_k])-bisect_left(info_dict[q_k],int(q_v)))
        else:
            answer.append(0)
    return answer