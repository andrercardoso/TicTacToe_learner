import numpy as np
import pandas as pd


class TicTacToe:
    def __init__(self, pl1, pl2):
        self.board = np.zeros((3, 3))
        self.pl1 = pl1
        self.pl2 = pl2
        self.isEnd = False
        self.boardReshaped = None
        self.whoStarted = None
        self.playerSymbol = None

    def who_starts(self):
        """
        Function which decide which player goes first
        """
        turn = np.random.randint(0, 2, size=1)
        if turn:
            self.playerSymbol = 1
            self.whoStarted = 1
        else:
            self.playerSymbol = -1
            self.whoStarted = -1
        return self.playerSymbol

    def winner(self):
        """
        Function that checks which player won
        """
        # row
        for i in range(3):
            self.pontuation = sum(self.board[i, :])
            if abs(self.pontuation) == 3:
                self.isEnd = True
                return 1 if self.pontuation == 3 else -1
        # col
        for i in range(3):
            self.pontuation = sum(self.board[:, i])
            if abs(self.pontuation) == 3:
                self.isEnd = True
                return 1 if self.pontuation == 3 else -1

        # diagonal
        diag_sum1 = sum(self.board[i, i] for i in range(3))
        diag_sum2 = sum(self.board[i, 2 - i] for i in range(3))
        diag_sum = max(abs(diag_sum1), abs(diag_sum2))
        if diag_sum == 3:
            self.isEnd = True
            return 1 if diag_sum1 == 3 or diag_sum2 == 3 else -1
        # tie
        if len(self.available_positions()) == 0:
            self.isEnd = True
            return 0
        
        # not end
        return None

    def available_positions(self):
        """
        Check available Positions on board
        """
        positions = []
        for i in range(3):
            for j in range(3):
                if self.board[i, j] == 0:
                    positions.append((i, j))
        return positions

    def update_state(self, position):
        self.board[position] = self.playerSymbol
        # switch player
        self.playerSymbol = -1 if self.playerSymbol == 1 else 1

    def give_reward(self):
        """
        Give Reward when game ends
        """
        result = self.winner()

        if result == 1:
            self.pl1.feed_reward(1)
            self.pl2.feed_reward(-1)
        elif result == -1:
            self.pl1.feed_reward(-1)
            self.pl2.feed_reward(1)
        else:
            if self.whoStarted == 1:
                self.pl1.feed_reward(-0.2)
                self.pl2.feed_reward(0.2)
            else:
                self.pl1.feed_reward(0.2)
                self.pl2.feed_reward(-0.2)

    def reset(self):
        """
        Board Reset
        """
        self.board = np.zeros((3, 3))
        self.boardReshaped = None
        self.isEnd = False
        self.whoStarted = None

    def play(self, rounds=1, verbose=False):
        """
        Function which play and train computer players during n rounds

        """
        n_win = 0
        n_loses = 0
        n_tie = 0
        graph_data = pd.DataFrame()
        out = ''

        for i in range(rounds):
            self.who_starts()
            n_move = 1
            if i % 1000 == 0 and i != 0:
                print(f'Games  {i}')

            while not self.isEnd:
                if self.playerSymbol == 1:  # Player 1
                    positions = self.available_positions()
                    pl1_action = self.pl1.choose_action(positions, self.board, self.playerSymbol)
                    self.pl1.state_action.append(f'{str(self.board.reshape(9))} {str(pl1_action)}')
                    self.update_state(pl1_action)
                else:
                    # Player 2
                    positions = self.available_positions()
                    pl2_action = self.pl2.choose_action(positions, self.board, self.playerSymbol)
                    self.pl2.state_action.append(f'{str(self.board.reshape(9))} {str(pl2_action)}')
                    self.update_state(pl2_action)

                win = self.winner()
                n_move += 1
                if verbose:
                    if n_move % 2 == 0:
                        print(f'Round {n_move // 2}')
                    self.show_board()

                if win is not None:
                    new_df = pd.DataFrame({"n_games": i, "result": win}, index=[0])
                    graph_data = pd.concat([graph_data, new_df])
                    if win == -1:
                        n_loses += 1
                        out = self.pl2.name + " wins!"
                    elif win == 0:
                        n_tie += 1
                        out = "It's a draw!"
                    elif win == 1:
                        n_win += 1
                        out = self.pl1.name + " wins!"
                    if verbose:
                        print(out)
                    self.give_reward()
                    self.pl1.reset()
                    self.pl2.reset()
                    self.reset()
                    break

        return n_win, n_loses, n_tie, graph_data

    def show_board(self):
        # pl1: x ------ pl2: o
        token = ''
        for i in range(3):
            print('-------------')
            out = '| '
            for j in range(3):
                if self.board[i, j] == 1:
                    token = 'x'
                if self.board[i, j] == -1:
                    token = 'o'
                if self.board[i, j] == 0:
                    token = ' '
                out += token + ' | '
            print(out)
        print('-------------\n')
