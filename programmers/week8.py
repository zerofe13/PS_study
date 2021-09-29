#최소직사각형
def solution(sizes):
    answer = 0
    w,h= 0,0
    for size in sizes:
        if size[0] < size[1]:
            size[0],size[1] = size[1],size[0]
        w= max(w,size[0])
        h= max(h,size[1])
    answer = w*h
    return answer