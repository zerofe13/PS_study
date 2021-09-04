#기차표 검사
import sys
input = sys.stdin.readline

N,K = map(int,input().split())
check_num =0
nucheck_num = 0
station = []
total = 0
for i in range(N):
    a,b =map(int,input().split())
    station.append((a,b))

for i in range(len(station)):
    if i == N-1:
        total += nucheck_num
        break
    
    if check_num - station[i][0]>0:
        check_num -= station[i][0]
    else:
        nucheck_num -= (station[i][0] -check_num)
        total += (station[i][0] -check_num)
        check_num = 0
    nucheck_num += station[i][1]
    if i%K == 0: #검사
        check_num += nucheck_num
        nucheck_num = 0
print(total,end=" ")
check_num,nucheck_num,total = 0,0,0
for i in range(len(station)):
    if i == N-1:
        total += nucheck_num
        break
    
    if nucheck_num - station[i][0]>0:
        nucheck_num -= station[i][0]
        total += station[i][0]
    else:
        check_num -= (station[i][0] -nucheck_num)
        total += nucheck_num
        nucheck_num = 0
    nucheck_num += station[i][1]
    if i%K == 0: #검사
        check_num += nucheck_num
        nucheck_num = 0
print(total)