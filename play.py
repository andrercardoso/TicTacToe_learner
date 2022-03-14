from TicTacToe import TicTacToe
from computerPlayer import ComputerPlayer
from humanPlayer import HumanPlayer

# Computer player Vs Human player
pl1 = ComputerPlayer("computer", e_greedy_rate=0)
pl1.load_knowledge('Policy_100,000_games_against_computer_player')
pl3 = HumanPlayer("Human")
game = TicTacToe(pl1, pl3)
game.play(verbose=True)
