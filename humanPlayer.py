class HumanPlayer:
    def __init__(self, name):
        self.name = name
        self.state_action = []

    def choose_action(self, positions, board, symbol):
        while True:
            row = int(input("Choose a row: "))
            col = int(input("Choose a column: "))
            action = (row, col)
            if action in positions:
                return action

    def feed_reward(self, reward):
        pass

    def reset(self):
        self.state_action = []