def solution(enter, leave):
    answer = [0]*len(enter)
    temp = []
    enterIndex=0
    temp.append(enter[0])
    enterIndex += 1
    for i in range(len(leave)):
        while True:
            if leave[i] in temp:
                temp.remove(leave[i])
                break
            else:
                if enterIndex < len(enter):
                    for j in temp:
                        answer[j-1] += 1 
                    temp.append(enter[enterIndex])
                    answer[enter[enterIndex]-1] = len(temp)-1
                    enterIndex += 1
    return answer

enter = [1,4,2,3]
leave = [2,1,3,4]

solution(enter,leave)