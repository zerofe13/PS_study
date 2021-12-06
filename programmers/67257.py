# 2020 카카오 인턴쉽 수식 최대화
from itertools import permutations
def solution(expression):
    answer = 0
    operator = ['*','-','+']
    per_oper = list(permutations(operator))
    def exp_split(exp):
        result = []
        start = 0
        for i in range(len(exp)):
            if i == len(exp)-1:
                result.append(exp[start:])
            if exp [i] in ('*','-','+'):
                result.append(exp[start:i])
                result.append(exp[i])
                start = i+1
        return result
    exp = exp_split(expression)
    for per in per_oper:
        temp = exp.copy()
        for p in per:
            i = 0 
            while True:
                if len(temp) == 1:
                    answer =max(abs(int(temp[0])),answer)
                    break
                if i == len(temp)-1:
                    break
                if temp[i] == p:
                    temp[i-1] = str(eval(temp[i-1]+temp[i]+temp[i+1]))
                    del temp[i]
                    del temp[i]
                    i = i-1
                else:
                    i =i+1
    return answer

expression = "100-200*300-500+20"


print(solution(expression))