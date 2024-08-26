from flask import Flask, render_template, request
from tictactoe import check_win, empty_cells, minimax,check_draw

app = Flask(__name__)

board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
current_player = -1  # Human starts
human_wins = 0
computer_wins = 0

@app.route('/')
def index():
    return render_template('index.html', board=board, current_player=current_player, 
                           human_wins=human_wins, computer_wins=computer_wins)

@app.route('/move/<int:x>/<int:y>', methods=['POST'])
def move(x, y):
    global board, current_player, human_wins, computer_wins
    if board[x][y] == 0:
        board[x][y] = current_player
        if check_win(current_player, board):
            if current_player == -1:
                human_wins += 1
                message = "Human wins!"
            else:
                computer_wins += 1
                message = "Computer wins!"
            return render_template('index.html', board=board, current_player=current_player,
                                   human_wins=human_wins, computer_wins=computer_wins, message=message)

        else:
            if check_draw(len(empty_cells(board)),board):
                message = "Draw"

        current_player = -current_player

        if current_player == 1:
            best_move = minimax(board, current_player, len(empty_cells(board)))
            board[best_move[0]][best_move[1]] = current_player
            if check_win(current_player, board):
                computer_wins += 1
                message = "Computer wins!"
                return render_template('index.html', board=board, current_player=current_player,
                                       human_wins=human_wins, computer_wins=computer_wins, message=message)
            current_player = -current_player

    return render_template('index.html', board=board, current_player=current_player,
                           human_wins=human_wins, computer_wins=computer_wins)

@app.route('/reset', methods=['POST'])
def reset():
    global board, current_player
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    current_player = -1
    return render_template('index.html', board=board, current_player=current_player,
                           human_wins=human_wins, computer_wins=computer_wins)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)
