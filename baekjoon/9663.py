n = int(input())
result =0
col=[0]*n

def check(x):
    for i in range(x):
        if col[x] == col[i] or abs(col[i]-col[x])== x-i:
            return False
    return True

def dfs(x):
    global result
    if x == n:
        result += 1
        return
    for i in range(n):
        col[x] = i
        if check(x):
            dfs(x+1)
            
dfs(0)
print(result)