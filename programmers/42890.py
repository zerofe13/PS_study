# 2019 kakao blind 후보키
from itertools import combinations

def check_key(c_i,rel):
    result = []
    for i in range(len(rel)):
        temp = []
        for j in range(len(c_i)):
            temp.append(rel[i][c_i[j]])
        if temp in result:
            return False
        else:
            result.append(temp)
    return True
        
def solution(relation):
    answer = 0
    col_i = [i for i in range(len(relation[0]))]
    rel = relation.copy()
    key = []
    for i in range(1,len(col_i)+1):
        combi = list(combinations(col_i,i))
        for c_i in combi:
            if check_key(c_i,rel) == True: 
                key.append(set(c_i))
    for i in reversed(range(len(key))):
        flag = True
        for j in range(i):
            if key[j].issubset(key[i]):
                flag = False
                break
        if flag:
            answer += 1
    return answer

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))