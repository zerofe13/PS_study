def solution(prices):
    answer = []
    for i in range(len(prices)):
        flag = False
        for j in range(i,len(prices)):
            if prices[i] > prices[j]:
                answer.append(j-i)
                flag = True
                break
        if flag:
            continue
        else:
            answer.append(j-i)
    return answer