#2018 kakao blind 비밀지도
def decToBin(n,num):
    bi = []
    result = [0]*n
    while True:
        if num <= 1:
            bi.append(num)
            break
        bi.append(num%2)
        num=num//2
    for i in range(len(bi)):
        if i>=n:
            break
        result[i] = bi[i]
    result = result[-1::-1]
    return result

def solution(n, arr1, arr2):
    answer = []
    bin_arr1 =[]
    bin_arr2 =[]
    for num in arr1:
        bin_arr1.append(decToBin(n,num))
    for num in arr2:
        bin_arr2.append(decToBin(n,num))
    for i in range(n):
        temp = ""
        for j in range(n):
            if bin_arr1[i][j] == 0 and bin_arr2[i][j] == 0:
                temp += " "
            else:
                temp += "#"
        answer.append(temp)
    return answer