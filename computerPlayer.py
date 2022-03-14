import numpy as np
import pickle


class ComputerPlayer:
    def __init__(self, name, e_greedy_rate=0.1, learn_rate=0.2, discount_factor=0.9):
        self.name = name
        self.lr = learn_rate
        self.df = discount_factor
        self.e_greedy_rate = e_greedy_rate  # tradeoff between exploration-exploitation
        self.state_action = []  # record all positions taken
        self.Q_value = {}  # state -> score of state

    def choose_action(self, positions, current_board, symbol):
        value_max = -1
        if np.random.uniform(0, 1) <= self.e_greedy_rate:
            # take random action - exploration
            idx = np.random.choice(len(positions))
            action = positions[idx]
        else:
            for p in positions:
                # choose option which seems the best - exploitation
                if self.Q_value.get(str(current_board.reshape(9)) + ' ' + str(p)) is None:
                    value = 0
                else:
                    value = self.Q_value.get(str(current_board.reshape(9)) + ' ' + str(p))
                if value >= value_max:
                    value_max = value
                    action = p
        return action

    def feed_reward(self, reward):
        """
        At the end of game, it backpropagates Q value and updates states value
        """
        next_q_value = 0
        for st in reversed(self.state_action):
            if self.Q_value.get(st) is None:
                self.Q_value[st] = 0
            self.Q_value[st] = (1 - self.lr) * self.Q_value[st] + self.lr * (reward + self.df * next_q_value)
            reward = 0
            next_q_value = self.Q_value[st]

    def reset(self):
        self.state_action = []

    def save_knowledge(self, extension=''):
        fw = open('Policy_' + extension, 'wb')
        pickle.dump(self.Q_value, fw)
        fw.close()

    def load_knowledge(self, file):
        fr = open(file, 'rb')
        self.Q_value = pickle.load(fr)
        fr.close()
