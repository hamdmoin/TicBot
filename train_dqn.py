import gym
import numpy as np
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from collections import deque
import random
from tictactoe_env import TicTacToeEnv

# Hyperparameters
episodes = 10000
gamma = 0.95
epsilon = 1.0
epsilon_min = 0.01
epsilon_decay = 0.995
learning_rate = 0.001
batch_size = 32
memory = deque(maxlen=2000)

# GPU setup
physical_devices = tf.config.list_physical_devices('GPU')
if physical_devices:
    tf.config.experimental.set_memory_growth(physical_devices[0], True)

env = TicTacToeEnv()
state_size = env.observation_space.shape[0] * env.observation_space.shape[1]
action_size = env.action_space.n

# Build the model
model = Sequential([
    Dense(24, input_dim=state_size, activation='relu'),
    Dense(24, activation='relu'),
    Dense(action_size, activation='linear')
])
model.compile(loss='mse', optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate))

# Training function with tf.function
@tf.function
def train_step(states, targets):
    model.fit(states, targets, epochs=1, verbose=0)

# Training
for e in range(episodes):
    state = env.reset()
    state = np.reshape(state, [1, state_size])
    done = False
    for time in range(5):
        if np.random.rand() <= epsilon:
            action = random.randrange(action_size)
        else:
            action = np.argmax(model.predict_on_batch(state)[0])

        next_state, reward, done, _ = env.step(action)
        next_state = np.reshape(next_state, [1, state_size])

        memory.append((state, action, reward, next_state, done))
        state = next_state

        if done:
            print(f"episode: {e}/{episodes}, score: {time}, e: {epsilon:.2}")
            break

        if len(memory) > batch_size:
            minibatch = random.sample(memory, batch_size)
            states = np.zeros((batch_size, state_size))
            targets = np.zeros((batch_size, action_size))

            for i, (s, a, r, ns, d) in enumerate(minibatch):
                target = r
                if not d:
                    target += gamma * np.amax(model.predict_on_batch(ns)[0])
                target_f = model.predict_on_batch(s)
                target_f[0][a] = target

                states[i] = s
                targets[i] = target_f

            # Train the model on the entire batch at once
            train_step(states, targets)

    if epsilon > epsilon_min:
        epsilon *= epsilon_decay

# Save the trained model
model.save('tictactoe_dqn_model.h5')
