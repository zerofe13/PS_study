def solution(v):
    x,y = 0,0
    x_sort = sorted(v,key=lambda x:x[0])
    if x_sort[1][0] == x_sort[2][0]:
        x= x_sort[0][0]
    else:
        x = x_sort[2][0]
        
    y_sort = sorted(v,key=lambda x:x[1])
    if y_sort[1][1] == y_sort[2][1]:
        y= y_sort[0][1]
    else:
        y = y_sort[2][1]
    answer = [x,y]

    return answer