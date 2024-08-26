from math import inf as infinity

board = [[0,0,0],
         [0,0,0],
         [0,0,0]]

def check_win(player, state):
    '''
    this function checks if a player whether Human (-1) or Computer (+1) has won 
    parameters:
        player = Computer Or Human
        state = state of current board
    win_state:
        all of the conditions in which a player can win
    '''
    win_state = [[state[0][0], state[0][1], state[0][2]],
                 [state[1][0], state[1][1], state[1][2]],
                 [state[2][0], state[2][1], state[2][2]],
                 [state[0][0], state[1][0], state[2][0]],
                 [state[1][0], state[1][1], state[1][2]],
                 [state[2][0], state[2][1], state[2][2]],
                 [state[0][0], state[1][1], state[2][2]],
                 [state[2][0], state[1][1], state[0][2]]]
    
    if [player, player, player] in win_state:
        return True
    else:
        return False
    
def empty_cells(state):
    '''
    this functions adds empty cells to a set 
    parameters:
        state = current state of the board
    empty_cells:
        all of the available cells in the board 
    '''
    empty_cells = []
    for x, i in enumerate(state):
        for y, j in enumerate(i):
            if j == 0:
                empty_cells = empty_cells + [[x, y]]
    return empty_cells

def gameover(depth, state):
    '''
    checks if the game has finished 
    parameters
    '''
    if depth == 0 or check_win(+1, state) or check_win(-1, state):
        return True
    else:
        return False

def minimax(state, player, depth):
    if gameover(depth=depth, state=state):
        if check_win(+1, state):
            return [-1, -1, +1]
        elif check_win(-1, state):
            return [-1, -1, -1]
        else:
            return [-1, -1, 0]

    if player == +1:
        best = [-1, -1, -float('inf')]
    else:
        best = [-1, -1, +float('inf')]
    
    for i in empty_cells(state):
        state[i[0]][i[1]] = player
        score = minimax(state, -player, depth - 1)
        state[i[0]][i[1]] = 0
        score[0], score[1] = i[0], i[1]
        
        if player == +1:
            if score[2] > best[2]:
                best = score
        else:
            if score[2] < best[2]:
                best = score

    return best

