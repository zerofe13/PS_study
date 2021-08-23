def solution(arr):
    # max arr size 1000
    # max num size 255
    answer = -1
    a =0 
    b =0
    for i in range(255):
        for num in arr:
            if num <i:
                b= b+1
            elif num > i :
                a = a+1
    answer = midNum

    return answer

print(solution([100,50,100,200]))