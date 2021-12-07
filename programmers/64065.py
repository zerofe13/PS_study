#2019 겨울 인턴십 튜플 

def solution(s):
    answer = []
    s_list = s[2:-2].split('},{')
    s_list.sort(key = lambda x:len(x))
    for temp in s_list:
        t_list = list(map(int,temp.split(',')))
        for i in t_list:
            if i not in answer:
                answer.append(i)
    return answer