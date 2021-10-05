
def turn_puzzle(puzzle):
    result = []
    max_y = max(map(lambda p_y: p_y[1],puzzle))
    for i in range(len(puzzle)):
            result.append([puzzle[i][1],max_y-puzzle[i][0]])
    return result

def compare(hole,puzzle):
    sort_hole = sorted(hole)
    com_hole = []
    for i in range(1,len(sort_hole)):
        com_hole.append([sort_hole[i][0]-sort_hole[i-1][0],sort_hole[i][1]-sort_hole[i-1][1]])
    t_p = puzzle[:]
    for i in range(4):
        t_p = turn_puzzle(t_p)
        sort_puzzle = sorted(t_p)
        com_puzzle=[]
        for i in range(1,len(sort_puzzle)):
            com_puzzle.append([sort_puzzle[i][0]-sort_puzzle[i-1][0],sort_puzzle[i][1]-sort_puzzle[i-1][1]])
        if com_puzzle == com_hole:
            return True
    return False

def solution(game_board, table):
    answer = -1
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    size = len(table)
    visit,board_visit = [[0]*size for _ in range(size)],[[0]*size for _ in range(size)]
    puzzles,holes =[],[]
    
    def dfs(x,y,mode):
        for i in range(4):
            n_x =x + dx[i]
            n_y = y + dy[i]
            if 0<=n_x<size and 0<=n_y<size:
                if mode ==0 and visit[n_y][n_x] != 1 and table[n_y][n_x] == 1:
                    temp.append([n_y,n_x])
                    visit[n_y][n_x] = 1
                    dfs(n_x,n_y,mode)
                elif mode == 1 and board_visit[n_y][n_x] != 1 and game_board[n_y][n_x] == 0:
                    temp.append([n_y,n_x])
                    board_visit[n_y][n_x] = 1
                    dfs(n_x,n_y,mode)

    for i in range(size):
        for j in range(size):
            if table[i][j] == 1 and visit[i][j] ==0:
                visit[i][j] = 1
                temp =[[i,j]]
                dfs(j,i,0)
                puzzles.append(temp)
            if game_board[i][j] == 0 and board_visit[i][j] == 0:
                board_visit[i][j] = 1
                temp = [[i,j]]
                dfs(j,i,1)
                holes.append(temp)
 
    check_puzzle = [0]*len(puzzles)
    for hole in holes:
        for i in range(len(puzzles)):  
            if check_puzzle[i] == 0:
               if compare(hole,puzzles[i]):
                   check_puzzle[i] =len(hole)
                   break
    answer = sum(check_puzzle)
    return  answer

game_board = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]

print(solution(game_board,table))