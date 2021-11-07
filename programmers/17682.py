#2018 kakao blind 다트게임
def solution(dartResult):
    answer = 0
    sum_num  = []
    i = 0
    while True:
        if i >=len(dartResult):
            break
        temp =0
        if "0"<=dartResult[i] <="9":
            if dartResult[i]== "1" and dartResult[i+1]=="0":
                temp = 10
                if dartResult[i+2] == "S":
                    temp = temp**1
                elif dartResult[i+2]== "D":
                    temp =temp **2
                elif dartResult[i+2] == "T":
                    temp = temp **3
                sum_num.append(temp)   
                i = i+3
            else:
                temp = int(dartResult[i])
                if dartResult[i+1] == "S":
                    temp = temp**1
                elif dartResult[i+1]== "D":
                    temp =temp **2
                elif dartResult[i+1] == "T":
                    temp = temp **3
                sum_num.append(temp)
                i = i+2
        elif dartResult[i] == "*":
            sum_num[-1] = sum_num[-1]*2
            if len(sum_num)>=2:
                sum_num[-2] = sum_num[-2]*2
            i = i+1
        elif dartResult[i] == "#":
            sum_num[-1] = sum_num[-1]*(-1)
            i = i+1
    answer = sum(sum_num)
    return answer