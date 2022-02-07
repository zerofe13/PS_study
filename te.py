def check(stones):
    lenth = len(stones)
    count = 0
    result = 0
    for stone in stones:
        if stone != 0:
            result = stone
        else:
            count += 1
    if lenth - count == 1:
        return result
    else:
        return False
def solution(stones, k):
    answer = ''
    temp = []
    def dfs(stones,k,result):
        nonlocal temp
        if check(stones) ==k:
            temp.append(result)
        for i in range(len(stones)-1,-1,-1):
            copy_stones = stones.copy()
            for j in range(len(stones)):
                if i == j:
                    copy_stones[j] += 1
                else:
                    copy_stones[j] -=1
            if -1 not in copy_stones:
                stones = copy_stones.copy()
                result.append(i)
                next_result = result.copy()
                dfs(stones,k,next_result)
    dfs(stones,k,[])
    answer = temp
    return answer

print(solution([1,3,2],3))