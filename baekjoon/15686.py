from itertools import combinations

N,M = map(int,input().split())
array = [list(map(int,input().split()))for _ in range(N)]

house_pos = []
chicken_pos =  []
result = 1e9

for i in range(N):
    for j in range(N):
        if array[i][j] == 1:
            house_pos.append((j,i))
        elif array[i][j] == 2:
            chicken_pos.append((j,i))

def calc_dist(house_pos,chicken_pos):
    return abs(house_pos[0]-chicken_pos[0]) + abs(house_pos[1]-chicken_pos[1])

def sum_dist():
    global result
    sum = 0
    min_dist = 1e9
    select_chicken = list(combinations(chicken_pos,M))
    
    for i in range(len(select_chicken)):
        for house in house_pos:
            for chicken in select_chicken[i]:
                min_dist= min(calc_dist(house,chicken),min_dist)
            sum += min_dist
            min_dist = 1e9
        result = min(sum,result)
        sum = 0
    
sum_dist()
print(result)