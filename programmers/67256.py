#2020 카카오 인턴쉽 키패드 누르기
def solution(numbers, hand):
    answer = ''
    pos = [[3,1],[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    left = [3,0]
    right = [3,2]
    def clac(i,hand_pos,pos):
        return abs(pos[i][0]-hand_pos[0])+abs(pos[i][1]-hand_pos[1])
    for i in numbers:
        if i ==1 or i ==4 or i ==7:
            answer += 'L'
            left=pos[i]
        elif i ==3 or i ==6 or i ==9:
            answer += 'R'
            right = pos[i]
        else:
            if clac(i,right,pos)>clac(i,left,pos):
                answer += 'L'
                left = pos[i]
            elif clac(i,right,pos)<clac(i,left,pos):
                answer += 'R'
                right = pos[i]
            elif clac(i,right,pos)==clac(i,left,pos):
                if hand == "right":
                    answer += 'R'
                    right = pos[i]
                else:
                    answer += 'L'
                    left = pos[i]
    return answer