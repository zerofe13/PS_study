#후위 표기식
import sys
input = sys.stdin.readline

order = list(input())
answer = ""
stack = []
for o in order:
    if o == '+' or o == '-':
        while stack and stack[-1] != '(':
            answer += stack.pop()
        stack.append(o)
    elif o == '*' or o =='/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            answer += stack.pop()
        stack.append(o)
    elif o == '(':
        stack.append(o)
    elif o == ')':
        while stack and stack[-1] != '(':
            answer += stack.pop()
        stack.pop()
    else:
        answer+=o
while stack:
    answer += stack.pop()

print(answer)