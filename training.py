from TicTacToe import TicTacToe
from computerPlayer import ComputerPlayer
from staticPlayer import StaticPlayer
import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    # Train our agent in 50,000 games against the static Player
    pl1 = ComputerPlayer('pl1')
    pl2 = StaticPlayer('pl2')
    game = TicTacToe(pl1, pl2)
    print("training...")
    n_games = 50000
    win, lose, tie, data = game.play(n_games, verbose=False)
    print("Completed!")
    print(f'Player 1 won {win} out of {n_games} games (win rate = {round((win / n_games) * 100, 2)}%)')
    print(f'Player 1 lose {lose} out of {n_games} games (lose rate = {round((lose / n_games) * 100, 2)}%)')
    print(f'Player 1 drew {tie} out of {n_games} games (tie rate = {round((tie / n_games) * 100, 2)}%)')

    # Graphic the agent evolution against staticPlayer
    bins = np.arange(1, n_games / 5000) * 5000
    data['game_counter_bins'] = np.digitize(data["n_games"], bins, right=True)
    counts = data.groupby(['game_counter_bins', 'result']).n_games.count().unstack()
    ax = counts.plot(kind='bar', stacked=True, figsize=(17, 5))
    ax.set_xlabel("Count of Games in Bins of 5,000")
    ax.set_ylabel("Counts of Draws/Losses/Wins")
    ax.legend(labels=['Loses', 'Draws', 'Wins'], loc='center left', bbox_to_anchor=(1.0, 0.5))
    ax.set_title('Results Distribution Vs Games Played')
    plt.show()

    # Save agent policy
    pl1.save_knowledge('50,000_games_against_computer_player')
