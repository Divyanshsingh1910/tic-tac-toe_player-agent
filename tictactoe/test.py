from tictactoe import minimax, result, actions, player, terminal, winner, X, O, EMPTY
import numpy as np


Array = [0, 1, 2, 0, 1, 2, 2, 2, 2]
arr = ["X", "O", None]
char_array = [arr[i] for i in Array]
char_array = np.array(char_array)  # for now consider this as the char array
char_array = char_array.reshape(3,3)