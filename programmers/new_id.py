
def solution(new_id):
    answer =""
    new_id= new_id.lower()
    for i in new_id:
        if (ord(i) >= ord('a') and ord(i) <= ord('z')) or (ord(i) >= ord('0') and ord(i) <= ord('9')) or i in '-_.':
            answer += i
    while '..' in answer:
        answer = answer.replace('..','.')
    if answer != '':
        if answer[0] == '.' :
            answer = answer[1:]
    if answer != '':
        if answer[-1] == '.':
            answer = answer[:-1]
    if answer == '':
        answer = 'a'
    if len(answer) >= 16:

        answer =answer[:15]
        if answer[-1] == '.':
            answer =answer[:-1]
    if len(answer) <=2:
        answer += answer[-1]*(3-len(answer))
    return answer


new_id = "=.="
print(solution(new_id))