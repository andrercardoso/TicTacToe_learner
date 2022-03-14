import numpy as np


# Rules
def winning_move_check(current_board, positions, symbol):
    """
    Function to identify coordinates that will result in a winning board state
    """
    for position in positions:
        current_board_copy = current_board.copy()
        current_board_copy[position] = symbol
        # check for a win along rows
        for i in range(current_board_copy.shape[0]):
            if 0 not in current_board_copy[i, :] and len(set(current_board_copy[i, :])) == 1:
                return position
        # check for a win along columns
        for j in range(current_board_copy.shape[1]):
            if 0 not in current_board_copy[:, j] and len(set(current_board_copy[:, j])) == 1:
                return position
        # check for a win in the diagonals
        if 0 not in np.diag(current_board_copy) and len(set(np.diag(current_board_copy))) == 1:
            return position
        if 0 not in np.diag(np.fliplr(current_board_copy)) and len(set(np.diag(np.fliplr(current_board_copy)))) == 1:
            return position


def block_move_check(current_board, positions, symbol):
    """
    Function to  identify coordinates that will prevent the player 1 from winning
    """
    for position in positions:
        current_board_copy = current_board.copy()
        current_board_copy[position] = symbol
        # check for a win along rows
        for i in range(current_board_copy.shape[0]):
            if 0 not in current_board_copy[i, :] and (current_board_copy[i, :] == 1).sum() == 2:
                if not (0 not in current_board[i, :] and (current_board[i, :] == 1).sum() == 2):
                    return position
        # check for a win along cols
        for j in range(current_board_copy.shape[1]):
            if 0 not in current_board_copy[:, j] and (current_board_copy[:, j] == 1).sum() == 2:
                if not (0 not in current_board[:, j] and (current_board[:, j] == 1).sum() == 2):
                    return position
        # check for a win in the diagonals
        if 0 not in np.diag(current_board_copy) and (np.diag(current_board_copy) == 1).sum() == 2:
            if not (0 not in np.diag(current_board) and (np.diag(current_board) == 1).sum() == 2):
                return position
        if 0 not in np.diag(np.fliplr(current_board_copy)) and (
                np.diag(np.fliplr(current_board_copy)) == 1).sum() == 2:
            if not (0 not in np.diag(np.fliplr(current_board)) and (
                    np.diag(np.fliplr(current_board)) == 1).sum() == 2):
                return position


def second_move_check(current_board, positions, symbol):
    """
    Function which identify coordinates that will result in a row having two 0's and no 1's
    """
    for position in positions:
        current_board_copy = current_board.copy()
        current_board_copy[position] = symbol
        for i in range(current_board_copy.shape[0]):
            if 1 not in current_board_copy[i, :] and (current_board_copy[i, :] == -1).sum() == 2:
                if not (1 not in current_board[i, :] and (current_board[i, :] == -1).sum() == 2):
                    return position
        for j in range(current_board_copy.shape[1]):
            if 1 not in current_board_copy[:, j] and (current_board_copy[:, j] == -1).sum() == 2:
                if not (1 not in current_board[:, j] and (current_board[:, j] == -1).sum() == 2):
                    return position
        if 1 not in np.diag(current_board_copy) and (np.diag(current_board_copy) == -1).sum() == 2:
            if not (1 not in np.diag(current_board) and (np.diag(current_board) == -1).sum() == 2):
                return position
        if 1 not in np.diag(np.fliplr(current_board_copy)) and (
                np.diag(np.fliplr(current_board_copy)) == -1).sum() == 2:
            if not (1 not in np.diag(np.fliplr(current_board)) and (
                    np.diag(np.fliplr(current_board)) == -1).sum() == 2):
                return position
