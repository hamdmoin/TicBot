board = [[0,0,0],
         [0,0,0],
         [0,0,0]]
def check_win(player,state):
    '''
    this funtion checks if a player whether Human (-1) or Computer (+1) has won 
    parameters:
        player = Computer Or Human
        state = state of current board
    win_state:
        all of the conditions in which a player can win
    '''
    win_state = [[state[0][0],state[0][1],state[0][2]],
                 [state[1][0],state[1][1],state[1][2]],
                 [state[2][0],state[2][1],state[2][1]],
                 [state[0][0],state[1][0],state[2][0]],
                 [state[1][0],state[1][1],state[1][2]],
                 [state[2][0],state[2][1],state[2][2]],
                 [state[0][0],state[1][1],state[2][2]],
                 [state[2][0],state[1][1],state[0][2]]]
    
    if [player , player , player] in win_state:
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
    for x,i in enumerate(state):
        for y,j in enumerate(i):
            if j == 0:
                empty_cells = empty_cells + [state[x][y]]
    return empty_cells

    
