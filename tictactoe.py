from math import inf as infinity

board = [[0,0,0],
         [0,0,0],
         [0,0,0]]

def check_win(player, state):
    """
    Checks if a player (Human: -1 or Computer: +1) has won.
    """
    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]]
    ]

    return [player, player, player] in win_state

def empty_cells(state):
    """
    Returns a list of empty cells in the board.
    """
    return [[x, y] for x, row in enumerate(state) for y, cell in enumerate(row) if cell == 0]

def gameover(state):
    """
    Returns True if the game is over (win or draw).
    """
    return check_win(+1, state) or check_win(-1, state) or not empty_cells(state)

def minimax(state, player, depth):
    """
    Minimax algorithm for finding the best move for the computer.
    """
    if gameover(state) or depth == 0:
        if check_win(+1, state):
            return [-1, -1, +1]
        elif check_win(-1, state):
            return [-1, -1, -1]
        else:
            return [-1, -1, 0]

    if player == +1:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    for cell in empty_cells(state):
        x, y = cell
        state[x][y] = player
        score = minimax(state, -player, depth - 1)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == +1:
            if score[2] > best[2]:
                best = score
        else:
            if score[2] < best[2]:
                best = score

    return best
