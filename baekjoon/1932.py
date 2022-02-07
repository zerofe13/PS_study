n=int(input())
tri = []

for i in range(n):
    tri.append(list(map(int,input().split())))

for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            left = 0
        else:
            left = tri[i-1][j-1]
        if i == j:
            right = 0
        else:
            right = tri[i-1][j]
        tri[i][j] = tri[i][j] + max(left,right)
print(max(tri[n-1]))