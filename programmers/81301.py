## 숫자 문자열과 영단어
def solution(s):
    answer = ""
    result = []
    str_num = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    i = 0
    while True:
        if i >= len(s):
            break
        if "0"<=s[i]<="9":
            result.append(int(s[i]))
            i += 1
        elif "a"<= s[i]<="z":
            for j in range(len(str_num)):
                temp = s[i:i+len(str_num[j])]
                if temp == str_num[j]:
                    result.append(j)
                    i += len(str_num[j])
                    break
    answer = "".join(map(str,result))

    return int(answer)


# num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

# def solution(s):
#     answer = s
#     for key, value in num_dic.items():
#         answer = answer.replace(key, value)
#     return int(answer)