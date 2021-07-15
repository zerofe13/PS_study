def solution(numbers, target):
    answer = 0

    def DFS(compare,depth):
        nonlocal answer
        if depth == len(numbers):
            if compare == target:
                answer += 1
            return
        DFS(compare + numbers[depth],depth+1)
        DFS(compare - numbers[depth],depth+1)
        
    DFS(0,0)
    return answer

print(solution([1,1,1,1,1],3))