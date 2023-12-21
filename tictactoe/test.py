from tictactoe import minimax, result, actions, player, terminal, winner, X, O, EMPTY
import numpy as np


Array = [2,1 ,0, 2, 1, 0, 2, 2, 0]
arr = ["X", "O", None]
char_array = [arr[i] for i in Array]
char_array = np.array(char_array)  # for now consider this as the char array
board = char_array.reshape(3,3)

for col in range(len(board[0])):
        if board[0][col] == board[1][col] and  board[1][col] == board[2][col]:
            print(board[0][col])