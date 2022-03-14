import numpy as np
from staticRules import winning_move_check, block_move_check, second_move_check


class StaticPlayer:
    # players who knows some rules, but no evolve
    def __init__(self, name):
        self.name = name
        self.state_action = []

    def choose_action(self, positions, current_board, symbol):
        if winning_move_check(current_board, positions, symbol) is not None:
            action = winning_move_check(current_board, positions, symbol)
        elif block_move_check(current_board, positions, symbol) is not None:
            action = block_move_check(current_board, positions, symbol)
        elif second_move_check(current_board, positions, symbol) is not None:
            action = second_move_check(current_board, positions, symbol)
        else:
            idx = np.random.choice(len(positions))
            action = positions[idx]
        return action

    def feed_reward(self, reward):
        pass

    def reset(self):
        pass
