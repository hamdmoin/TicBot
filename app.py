from flask import Flask, render_template, url_for, request
from tictactoe import check_win, empty_cells, minimax
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
current_player = -1  # Human starts
human_wins = 0
computer_wins = 0

@app.route('/')
def index():
    global human_wins, computer_wins
    return render_template('index.html', board=board, current_player=current_player,
                           human_wins=human_wins, computer_wins=computer_wins)

@app.route('/move/<int:x>/<int:y>', methods=['POST'])
def move(x, y):
    global board, current_player, human_wins, computer_wins
    logging.debug(f"Human move at ({x}, {y})")
    if board[x][y] == 0:
        board[x][y] = current_player
        if check_win(current_player, board):
            if current_player == -1:
                human_wins += 1
                logging.debug("Human wins!")
                return render_template('index.html', board=board, current_player=current_player,
                                       human_wins=human_wins, computer_wins=computer_wins, message="Human wins!")
            current_player = -current_player

        # Computer's move
        if current_player == 1:
            logging.debug("Computer's turn")
            best_move = minimax(board, current_player, len(empty_cells(board)))
            logging.debug(f"Computer move at {best_move}")
            if best_move:
                board[best_move[0]][best_move[1]] = current_player
                if check_win(current_player, board):
                    computer_wins += 1
                    logging.debug("Computer wins!")
                    return render_template('index.html', board=board, current_player=current_player,
                                           human_wins=human_wins, computer_wins=computer_wins, message="Computer wins!")
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
    app.run(debug=True)