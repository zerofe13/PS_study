# 2018 kakao blind 프렌즈4블록
def check(y,x,board):
    if board[y][x] == 'x':
        return False
    if board[y][x]==board[y+1][x] and board[y][x]==board[y][x+1]and board[y][x] == board[y+1][x+1]:
        return (y,x),(y+1,x),(y,x+1),(y+1,x+1)
    else:
        return False
def move(m,n,board):
    for i in range(n):
        for j in range(m-1,0,-1):
            if board[j][i] == 'x':
                for k in range(j,-1,-1):
                    if board[k][i] != 'x':   
                        board[j][i],board[k][i]=board[k][i],board[j][i]
                        break
def solution(m, n, board):
    answer = 0
    temp_board = []
    for i in range(m):
        temp_board.append(list(board[i]))
    while True:
        pos = set()
        for i in range(m-1):
            for j in range(n-1):
                if check(i,j,temp_board):
                    pos.update(check(i,j,temp_board))  
        if len(pos) == 0:
            break
        else:
            print(pos)
            for y,x in pos:
                temp_board[y][x] ='x'
                answer += 1
        move(m,n,temp_board)
        
    return answer

print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))