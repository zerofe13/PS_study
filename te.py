def solution(arr):
    answer = -1
    sortedList = sorted(arr)
    myList =[]
    midNum = 0
    for n in sortedList:
        if n not in myList:
            myList.append(n)
    
    if len(myList)%2 == 1:
        midNum = myList[len(myList)//2]-1
    else:
        midNum = myList[len(myList)//2-1]+1
    answer = midNum

    return answer

print(solution([100,50,100,200]))