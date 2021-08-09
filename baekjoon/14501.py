# 퇴사
N = int(input())
arr = [list(map(int,input().split()))for _ in range(N)]
result = 0

def dfs(t,p):
    global result
    if t>N:
        return
    if t==N:
        result = max (result,p)
        return
    dfs(t+arr[t][0],p+arr[t][1])
    dfs(t+1,p)
dfs(0,0)
print(result)