#2019 kakao blind recuitment실패율
def solution(N, stages):
    answer = []
    num_people= len(stages)
    fail= [0 for _ in range(N+2)]
    stages.sort()
    stages.append(-1)
    count = 1
    for i in range(len(stages)-1):
        if stages[i] != stages[i+1]:
            fail[stages[i]-1] = count/num_people
            num_people -= count
            count = 1
        else:
            count += 1
    temp = []
    for i in range(N):
        temp.append([fail[i],i+1])
    temp.sort(key = lambda x:(-x[0],x[1]))
    for a,b in temp:
        answer.append(b)
    return answer