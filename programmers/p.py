# 괄호변환
from collections import deque
def find_uv(p):
    l,r = 0,0
    for i in range(len(p)):
        if p[i] == '(':
            l +=1
        elif p[i] == ')':
            r +=1
        if l == r:
            u=p[:i+1]
            v=p[i+1:] if i+1 < len(p) else ""
            break
    return u,v
def isValid(v):
    stack = deque()
    for c in v:
        if c == '(':
            stack.append(c)
        else:
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False
    else:
        return True
def recursive(p):
    temp =""
    if p == "":
        return ""
    u,v = find_uv(p)
    if isValid(u):
        return u+recursive(v)
    else:
        temp +="("
        temp += recursive(v)
        temp +=")"
        u = u[1:-1]
        for c in u:
            if c=='(':
                temp+=')'
            else:
                temp+='('
    return temp
def solution(p):
    answer = ''
    if isValid(p):
        return p
    else:
        answer=recursive(p)
    return answer

p="()))((()"
print(solution(p))