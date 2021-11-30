# 2021 kakao blind 메뉴 리뉴얼
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course:
        menu_list = []
        for order in orders:
            combi = list(combinations(sorted(order),c))
            menu_list += combi
        counter = Counter(menu_list) 
        for i in range(len(counter)):
            if list(counter.values())[i] >= 2and list(counter.values())[i] == max(counter.values()):
                answer += [''.join(list(counter)[i])]
        answer.sort()
    return answer