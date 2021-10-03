def solution(scores):
    answer = ''
    new_scores = list(map(list,zip(*scores)))
    avg_scores = []
    for i in range(len(new_scores)):
        max_num,min_num = max(new_scores[i]),min(new_scores[i])
        if new_scores[i].index(max_num) == i and new_scores[i].count(max_num) ==1:
            avg_scores.append((sum(new_scores[i])-max_num)/(len(new_scores[i])-1))
            continue
        if new_scores[i].index(min_num) == i and new_scores[i].count(min_num) ==1:
            avg_scores.append((sum(new_scores[i])-min_num)/(len(new_scores[i])-1))
            continue
        avg_scores.append(sum(new_scores[i])/len(new_scores[i]))
    answer = "".join([ avg>=90 and "A" or avg>=80 and "B" or avg>=70 and "C" or avg>=50 and "D" or "F" for avg in avg_scores ])
    return answer
scores = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]

print(solution(scores))