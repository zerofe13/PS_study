def solution(plans):
    answer = []
    stack = []
    plans.sort(key = lambda x:x[1])
    
    h,m = plans[1][1].split(":")
    for name,start,playtime in plans:
        h,m = map(int,start.split(":"))
        time = h*60+m
        playtime = int(playtime)
        if stack:
            prev_name,prev_time,prev_playtime= stack.pop()
            # 다음 일이 오기전에 끝남
            spare_time =  time - (prev_time + prev_playtime)
            if spare_time ==0 :
                answer.append(prev_name)
            
            elif spare_time <0:
                stack.append([prev_name,-1,-spare_time])
            else:
                answer.append(prev_name)
                while spare_time:
                    if len(stack) ==0:
                        break
                    if spare_time == stack[-1][2]:
                        a,b,c=stack.pop()
                        spare_time = 0
                        answer.append(a)
                    elif spare_time > stack[-1][2]:
                        a,b,c=stack.pop()
                        spare_time-=c
                        answer.append(a)
                    else:
                        stack[-1][2] -= spare_time
                        spare_time = 0 
        
        stack.append([name,time,playtime])
    while stack:
        answer.append(stack.pop()[0])
    return answer
