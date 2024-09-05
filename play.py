import numpy as np
import tensorflow as tf
from tictactoe_env import TicTacToeEnv

# Load the trained model
model = tf.keras.models.load_model("tictactoe_dqn_model.h5")
env = TicTacToeEnv()

def play_game():
    state = env.reset()
    done = False
    while not done:
        env.render()
        state = np.reshape(state, [1, 9])
        action = np.argmax(model.predict(state)[0])
        next_state, reward, done, _ = env.step(action)
        state = next_state
        if done:
            env.render()
            print(f"Game Over! Reward: {reward}")
            break

play_game()
