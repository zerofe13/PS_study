def solution(brown, yellow):
    answer = []
    
    
    for x in range(brown//2):
        for y in range(x+1):
    
            if 2*(x+y)-4 == brown and (x-2)*(y-2) == yellow and x*y == brown+yellow:
                answer.append((x,y))
                break
        
    return answer[0]