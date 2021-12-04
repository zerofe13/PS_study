# 2018 kakao blind 뉴스 클러스터링
import re
import math
def solution(str1, str2):
    answer = 0
    p = re.compile('[A-Z]{2}')
    def split_str(str):
        result= []
        for i in range(len(str)-1):
            temp = str[i] + str[i+1]
            temp = temp.upper()
            if p.match(temp):
                result.append(temp)
        return result

    def multiset_union(A,B):
        temp = A.copy()
        result = A.copy()
        
        for i in B:
            if i not in result:
                temp.append(i)
            else:
                result.remove(i)
        return B+result
    def multiset_inter(A,B):
        A_temp = A.copy()
        B_temp = B.copy()
        result = []
        for i in B_temp:
            if i in A_temp:
                A_temp.remove(i)
                result.append(i)
        return result
    
    A = split_str(str1)
    B = split_str(str2)    
    
    union_set = multiset_union(A,B)
    inter_set = multiset_inter(A,B)
    
    if len(union_set) == 0 and len(inter_set) == 0:
        answer = 65536
    else:
        answer = math.trunc((len(inter_set)/len(union_set)) * 65536)
    return answer