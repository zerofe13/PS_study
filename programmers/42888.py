# 2019 kakao blind 오픈채팅방
def solution(records):
    answer = []
    state = []
    user = {}
    for record in records:
        temp =[]
        temp = list(map(str,record.split()))
        state.append((temp[1],temp[0]))
        if temp[0] != "Leave":
            user[temp[1]] = temp[2]
    for s in state:
        if s[1] == "Enter":
            answer.append(user[s[0]]+"님이 들어왔습니다.")
        elif s[1] == "Leave":
            answer.append(user[s[0]]+"님이 나갔습니다.")
    return answer