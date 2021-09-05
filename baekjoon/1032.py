#명령 프롬프트
import sys
input = sys.stdin.readline

N = int(input())
str_list = []
result = ""
for _ in range(N):
    temp = input()
    str_list.append(temp)

result = list(str_list[0])
for i in range(1,N):
    for j in range(len(str_list[i])):
        if result[j] == str_list[i][j]:
            result[j]=str_list[i][j]
        else:
            result[j] = "?"
print("".join(result))
