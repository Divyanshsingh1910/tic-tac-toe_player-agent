"""
Tic Tac Toe Player
"""

import math
import copy

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
    countX = 0
    countO = 0

    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == X:
                countX += 1
            elif board[row][col] == O:
                countO += 1
    
    if countX > countO:
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleActions = set()
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == EMPTY:
                possibleActions.add((row, col))

    return possibleActions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid action")
    else:
        board_copy = copy.deepcopy(board)
        board_copy[action[0]][action[1]] = player(board)
        return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in range(len(board[0])):
        if board[row][0] == board[row][1] and board[row][1] == board[row][2] and board[row][0] != None:
            return board[row][0]
    
    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] and  board[1][col] == board[2][col] and board[0][col] != None:
            return board[0][col]
    
    # Check diagonals
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != None:
        return board[0][0]
    
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != None:
        return board[0][2]

    # No winner
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == EMPTY:
                return False
    
    return True
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    currentWinner = winner(board)
    if currentWinner == X:
        return 1
    elif currentWinner == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            value, move = max_value(board)
            return move
        else:
            value, move = min_value(board)
            return move
        
def max_value(board):
    if terminal(board):
        return utility(board), None

    v = float('-inf')
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        aux, act = min_value(result(board, action))
        if aux > v:
            v = aux
            move = action
            if v == 1:
                return v, move

    return v, move


def min_value(board):
    if terminal(board):
        return utility(board), None

    v = float('inf')
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        aux, act = max_value(result(board, action))
        if aux < v:
            v = aux
            move = action
            if v == -1:
                return v, move

    return v, move