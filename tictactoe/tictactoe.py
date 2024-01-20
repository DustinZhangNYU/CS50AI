"""
Tic Tac Toe Player
"""

import math
import random

X = "X"
O = "O"
EMPTY = None

MAXPLAYER = True

moves = set((i,j) for i in range(3) for j in range(3))

def initial_state():
    """
    Returns starting state of the board.
    """
    global MAXPLAYER,moves
    MAXPLAYER = True

    moves = set((i, j) for i in range(3) for j in range(3))
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if MAXPLAYER:
        return X

    return O


def actions(board):

    return actions
    """
    Returns set of all possible actions (i, j) available on the board.
    """



def result(board, action):
    global MAXPLAYER
    curPlayer = O
    if MAXPLAYER:
        curPlayer = X
    """
    Returns the board that results from making move (i, j) on the board."""
    board[action[0]][action[1]] = curPlayer

    moves.remove(action)
    MAXPLAYER = not MAXPLAYER
    return board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for i in range(3):
        if (board[i][0] == board[i][1] and board[i][1] == board[i][2]):
            return board[i][0];
    for i in range(3):
        if (board[0][i] == board[1][i] and board[1][i] == board[2][i]):
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
    if len(moves) == 0:
        return True
    return False


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
    if(terminal(board)):
        return None
    """
    Returns the optimal action for the current player on the board.
    """
    result = minmaxHelper(board, MAXPLAYER)[1]
    return result
def minmaxHelper(board, Maxing):
    if (terminal(board)):
        return (utility(board),None)
    if(Maxing):
        bestScore = -100
        bestAction = None
        for (i, j) in moves:
            board[i][j] = X
            moves.remove((i,j))
            score,Action = minmaxHelper(board, not Maxing)
            # if (score == bestScore):
            #     k = random.randint(0, 1)
            #     if(k == 0):
            #         bestScore = score
            #         bestAction = (i, j)
            if(score > bestScore):
                bestScore = score
                bestAction = (i,j)
            moves.add((i,j))
            board[i][j] = EMPTY
        return (bestScore, bestAction)
    else:
        bestScore = 100
        bestAction = None
        for (i, j) in moves:
            board[i][j] = O
            moves.remove((i, j))
            score, Action = minmaxHelper(board, not Maxing)
            # if (score == bestScore):
            #     k = random.randint(0, 1)
            #     if(k == 0):
            #         bestScore = score
            #         bestAction = (i, j)
            if (score < bestScore):
                bestScore = score
                bestAction = (i, j)
            moves.add((i, j))
            board[i][j] = EMPTY
        return (bestScore, bestAction)


board = initial_state()

