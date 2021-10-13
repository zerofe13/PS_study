def solution(lines):
    star = []
    max_y,max_x =-(1e15),-(1e15)
    min_x,min_y = (1e15),(1e15)
    for i in range(len(lines)):
        for j in range(i,len(lines)):
            a,b,e = lines[i]
            c,d,f = lines[j]
            if a*d - b*c != 0:
                x = (b*f-e*d)/(a*d-b*c)
                y = (e*c-a*f)/(a*d-b*c)
                if x % 1 == 0:
                    x= int(x)
                if y % 1 == 0:
                    y=int(y)
                if type(x) == int and type(y) == int:
                    max_y,max_x = max(max_y,y),max(max_x,x)
                    min_y,min_x = min(min_y,y),min(min_x,x)
                    star.append([y,x])
    for i in range(len(star)):
        star[i][0] = max_y-star[i][0]
    for i in range(len(star)):
        star[i][1] = star[i][1]-min_x
    temp = [["." for _ in range(max_x-min_x+1)]for _ in range(max_y-min_y+1)]
    for pos in star:
        y,x = pos
        temp[y][x] ='*'
    answer=[]
    for i in range(len(temp)):
        t =''
        for j in range(len(temp[i])):
            t +=temp[i][j]
        answer.append(t)
    return answer