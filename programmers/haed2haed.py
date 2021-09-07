def solution(weights, head2head):
    answer = []
    boxer_list = [] #승률, 무거운 복서이긴 횟수,몸무게, index
    for i in range(len(head2head)):
        w,l,over_weights= 0,0,0
        for j in range(len(head2head[i])):
            if head2head[i][j] == 'W':
                w += 1
                if weights[i] < weights[j]:
                    over_weights += 1
            elif head2head[i][j] =="L":
                l +=1 
        if w+l == 0:
            rate = 0
        else:
            rate = (w/(w+l))*100
        boxer_list.append((rate,over_weights,weights[i],i+1))
    temp=sorted(boxer_list, key = lambda x :(-x[0],-x[1],-x[2],x[3]))
    for t in temp:
        answer.append(t[3])
    return answer
weights = [50,82,75,120]
head2head = ["NLWL","WNLL","LWNW","WWLN"]
print(solution(weights,head2head))