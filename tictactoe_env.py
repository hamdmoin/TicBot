import gym
from gym import spaces
import numpy as np
from tictactoe import check_win, empty_cells

class TicTacToeEnv(gym.Env):
    def __init__(self):
        super(TicTacToeEnv, self).__init__()
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.current_player = -1  # Human
        self.action_space = spaces.Discrete(9)  # 9 possible moves
        self.observation_space = spaces.Box(low=-1, high=1, shape=(3, 3), dtype=np.int8)

    def reset(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.current_player = -1
        return np.array(self.board)

    def step(self, action):
        x, y = divmod(action, 3)
        if self.board[x][y] != 0:
            return np.array(self.board), -10, True, {}  # Invalid move

        self.board[x][y] = self.current_player
        if check_win(self.current_player, self.board):
            reward = 1 if self.current_player == 1 else -1
            return np.array(self.board), reward, True, {}

        if not empty_cells(self.board):
            return np.array(self.board), 0, True, {}  # Draw

        self.current_player = -self.current_player  # Switch player
        return np.array(self.board), 0, False, {}

    def render(self, mode='human'):
        for row in self.board:
            print(row)
        print()

    def close(self):
        pass
