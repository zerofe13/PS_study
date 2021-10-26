from collections import deque
def solution(board, moves):
    answer = 0
    stack = deque()
    for i in moves:
        for y in range(len(board)):
            if board[y][i-1] != 0:
                stack.append(board[y][i-1])
                board[y][i-1] = 0
                if len(stack)>=2 and stack[-2] == stack[-1]:
                    stack.pop()
                    stack.pop()
                    answer += 2
                break
    return answer

