from flask import Flask, render_template, url_for, request
from tictactoe import check_win, empty_cells, minimax

app = Flask(__name__)

board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
current_player = -1  # Human starts

@app.route('/')
def index():
    return render_template('index.html', board=board, current_player=current_player)

@app.route('/move/<int:x>/<int:y>', methods=['POST'])
def move(x, y):
    global board, current_player
    if board[x][y] == 0:
        board[x][y] = current_player
        if check_win(current_player, board):
            return render_template('index.html', board=board, current_player=current_player, message="Human wins!")
        current_player = -current_player

        # Computer's move
        if current_player == 1:
            best_move = minimax(board, current_player, len(empty_cells(board)))
            board[best_move[0]][best_move[1]] = current_player
            if check_win(current_player, board):
                return render_template('index.html', board=board, current_player=current_player, message="Computer wins!")
            current_player = -current_player

    return render_template('index.html', board=board, current_player=current_player)

@app.route('/reset', methods=['POST'])
def reset():
    global board, current_player
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    current_player = -1
    return render_template('index.html', board=board, current_player=current_player)

if __name__ == '__main__':
    app.run(debug=True)