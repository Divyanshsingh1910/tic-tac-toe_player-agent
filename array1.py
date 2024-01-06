from tictactoe.tictactoe import terminal, utility, minimax, winner
import numpy as np

data = []


arr = {0 : "X", 1 : "O", 2 : None}

for i_0 in range(3):
    for i_1 in range(3):
        for i_2 in range(3):
            for i_3 in range(3):
                for i_4 in range(3):
                    for i_5 in range(3):
                        for i_6 in range(3):
                            for i_7 in range(3):
                                for i_8 in range(3):

                                    board = np.array([i_0, i_1, i_2, i_3, i_4, i_5, i_6, i_7, i_8])
                                    board_2 = np.array([arr[i] for i in board])

                                    if terminal(board_2.reshape(3,3)):
                                        continue

                                    count_0 = 0
                                    count_X = 0
                                    for i in range(9):
                                        if board[i] == 0:
                                            count_X += 1
                                        elif board[i] == 1:
                                            count_0 += 1

                                    if count_X == count_0:
                                        data.append((board, 'X'))
                                    elif count_X == count_0 + 1:
                                        data.append((board, 'O'))

print(len(data))

# 0 is X and 1 is O
# if both count are equal then X will be the one to move first