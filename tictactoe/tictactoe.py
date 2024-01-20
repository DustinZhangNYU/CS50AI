"""
Tic Tac Toe Player
"""

import math
import random

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if count_for_X(board) <= count_for_O(board):
        return X
    return O


def actions(board):
    moves = set()
    for i in range(3):
        for j in range(3):
            if(board[i][j] == EMPTY):
                moves.add((i,j))
    return moves
    """
    Returns set of all possible actions (i, j) available on the board.
    """



def result(board, action):
    if action[0] < 0 or action[0] >= 3 or action[1] < 0 or action[1] >=3 or board[action[0]][action[1]] != EMPTY:
        raise Exception("illegal move")
    p = player(board)
    """
    Returns the board that results from making move (i, j) on the board."""
    board[action[0]][action[1]] = p
    return board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for i in range(3):
        if (board[i][0] != EMPTY and board[i][0] == board[i][1] and board[i][1] == board[i][2] ):
            return board[i][0];
    for i in range(3):
        if (board[0][i] != EMPTY and board[0][i] == board[1][i] and board[1][i] == board[2][i]):
            return board[0][i];
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2]):
        return board[1][1];
    if (board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        return board[1][1];
    return None;



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    if count_for_X(board) + count_for_O(board) == 9:
        return True
    return False

def count_for_X(board):
    count = 0
    for row in board:
        for e in row:
            if(e == X):
                count += 1
    return count

def count_for_O(board):
    count = 0
    for row in board:
        for e in row:
            if(e == O):
                count += 1
    return count
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.

    """

    if(winner(board) == "X"):
        return 1
    if (winner(board) == "O"):
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    res = minimaxHelper(board)[1]
    return res
def minimaxHelper(board):
    if (terminal(board)):
        return (utility(board),None)
    if(player(board) == 'X'):
        bestScore = -100
        bestAction = None
        for (i, j) in actions(board):
            board[i][j] = X
            score, action = minimaxHelper(board)
            # if (score == bestScore):
            #     k = random.randint(0, 1)
            #     if(k == 0):
            #         bestScore = score
            #         bestAction = (i, j)
            if(score > bestScore):
                bestScore = score
                bestAction = (i,j)
            board[i][j] = EMPTY
        return (bestScore, bestAction)
    else:
        bestScore = 100
        bestAction = None
        for (i, j) in actions(board):
            board[i][j] = O
            score, Action = minimaxHelper(board)
            # if (score == bestScore):
            #     k = random.randint(0, 1)
            #     if(k == 0):
            #         bestScore = score
            #         bestAction = (i, j)
            if (score < bestScore):
                bestScore = score
                bestAction = (i,j)
            board[i][j] = EMPTY
        return (bestScore, bestAction)



board = [[EMPTY, X, EMPTY],
            [EMPTY, X, O],
            [EMPTY, EMPTY, EMPTY]]

