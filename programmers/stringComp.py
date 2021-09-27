# 문자열 압축
def compStr(s,size):
    l,r = 0,size-1
    target = s[:size]
    count = 1
    result =''
    while True:
        l += size
        r += size
        if r > len(s):
            if count >1 :
                result += str(count)
            result += target
            result +=s[l:]
            break
        if target == s[l:r+1]:
            count += 1
        else:
            if count >1 :
                result += str(count)
            result += target
            count = 1
        target = s[l:r+1]
    return len(result)
def solution(s):
    answer = compStr(s,1)
    for i in range(1,len(s)//2+1):
        answer=min(answer,compStr(s,i))
    return answer
print(solution('a'))
