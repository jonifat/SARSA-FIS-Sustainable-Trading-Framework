import numpy as np
import pandas as pd

import csv
import os

"""
Action: Wait, Reward: Negative (-10)
Action: Next, Reward: Positive (15)
Action: Next, Reward: Negative (-10)
Action: Jump, Reward: Positive (15)
"""

class Environment:
    def __init__(self):
        self.num_states = 3
        self.num_actions = 3
    def reset(self):
        return 0  # Mulai dari state 0

    def step(self, state, action):
        if state == 0:
            if action == 0:  # Wait
                next_state = 0
                reward = -10
            elif action == 1:  # Next
                next_state = 1
                reward = -10
            else:  # Jump
                next_state = 2
                reward = 15
        elif state == 1:
            if action == 0:  # Wait
                next_state = 1
                reward = -10
            elif action == 1:  # Next
                next_state = 2
                reward = 15
            else:  # Jump
                next_state = 0
                reward = 15
        else:  # state == 2
            if action == 0:  # Wait
                next_state = 2
                reward = -10
            elif action == 1:  # Next
                next_state = 0
                reward = 15
            else:  # Jump
                next_state = 1
                reward = -10
        
        return next_state, reward

def ema(data, window):
    weights = np.exp(np.linspace(-1., 0., window))
    weights /= weights.sum()
    ema_values = np.convolve(data, weights, mode='full')[:len(data)]
    ema_values[:window] = ema_values[window]
    return ema_values

def transform_to_state(close_price, ema50):
    if close_price <= ema50 - 100:
        return 0
    elif ema50 - 100 < close_price <= ema50 + 100:
        return 1
    else:
        return 2

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df['Close'].values

def train(env, episodes=1000, alpha=0.1, gamma=0.99, epsilon=0.8, convergence_threshold=0.001):
    Q = np.zeros((env.num_states, env.num_actions))
    prev_Q = np.copy(Q)
    for _ in range(episodes):
        #print("episode : ",_)
        state = env.reset()
        while True:
            if np.random.uniform(0, 1) < epsilon:
                action = np.random.randint(0, env.num_actions)
            else:
                action = np.argmax(Q[state])
            next_state, reward = env.step(state, action)
            Q[state, action] += alpha * (reward + gamma * np.max(Q[next_state]) - Q[state, action])
            state = next_state
            if state == 2:  # State akhir
                break
        if np.all(np.abs(Q - prev_Q) < convergence_threshold):
            print("episode : ",_)
            #episode = "episode : " + _
            break
        prev_Q = np.copy(Q)
    train_result = {
        "Q_table": Q,
        "episode": _
        }
    return train_result

if __name__ == "__main__":
    for filename in os.listdir('history'):
        print(filename)
        if filename.endswith('.csv'):
            with open(os.path.join('history', filename)) as f:
                ##content = f.read()
                # Load data
                #file_path = 'data.csv'  # Ubah sesuai dengan path file data.csv
                #close_prices = load_data(file_path)
                close_prices = load_data(f)
                pair = filename.split('.csv')[0]
                

                # Hitung EMA50
                ema50 = ema(close_prices, 50)
                print(ema50)
                print("panjang ema", len(ema50))

                # Transformasi harga penutupan ke State
                states = [transform_to_state(price, ema50[i]) for i, price in enumerate(close_prices)]

                # Inisialisasi Environment
                env = Environment()

                # Latih SARSA
                #Q_table = train(env)
                train_result = train(env)

                # Tampilkan Q-table
                print("Q-table:")
                print(train_result['Q_table'])

                with open(os.path.join(os.getcwd(), "results", f"Q_result_{pair}.csv"), "w", encoding="UTF8", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(train_result['Q_table'])
                    writer.writerow("episode : " + str(train_result['episode']))
