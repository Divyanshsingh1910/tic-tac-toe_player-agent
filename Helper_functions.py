#importing library
import numpy as np

import os
import random
import pandas as pd 
from PIL import Image
import matplotlib.pyplot as plt

"""
Functions:
    get_pattern:
            Arguments:
                * querry_array: The status of game after user's input
                * Flag: values - [0, 1, 2]

            Action: The functionality varies with the Flag
                * Flag = 0: Generate the start pattern ( game will start with this 
                            first turn of the agent)
                * Flag = 1: Generate the start pattern ( But it can be any random 
                            state of starting, not necessarily the first)
                * Flag = 2: Generate next pattern based on the user's input querry
                            array( i.e. next turn after the user)

            Return val: This should return the a 9-length array for output pattern 
    -------------------------------------------------------------------
    generate_image:
            Arguments:
                * Array: A 9-length array

            Action: Generate a 2D image for the input pattern ( array )

            Return val: A 2D array for the image generated for the querry 
                array passed as input
    --------------------------------------------------------------------
    tester:     
            Arguments:
                * querry_array: A 9-length array ( sent as querry to user )
                * user_input: An index denoting user's next turn
            Action:  
                This is something on which I have think upon, like based on the 
                complexity that we want, iske functionality change ho skti hai but
                basic idea is to evaluate the user's input based on the querry input
            Return val: 
                This will also change accordingly         
            #modification : user_input will be a pair of indices on where to play and the character to play
"""
def choose_image_0():
        folder_0 = r'C:\Users\Trijal Srivastava\OneDrive\Desktop\VS CODE\ICG_competition\tic-tac-toe_player-agent\Data\Images\zeros'
        files_0 = os.listdir(r'C:\Users\Trijal Srivastava\OneDrive\Desktop\VS CODE\ICG_competition\tic-tac-toe_player-agent\Data\Images\zeros')
        image_files_0 = [f for f in files_0 if f.endswith(('.png'))]
        random_image_0 = random.choice(image_files_0)
        image_path_0 = os.path.join(folder_0, random_image_0)
        return image_path_0
    
def choose_image_1():
        folder_1 = r'C:\Users\Trijal Srivastava\OneDrive\Desktop\VS CODE\ICG_competition\tic-tac-toe_player-agent\Data\Images\crosses'
        files_1 = os.listdir(r'C:\Users\Trijal Srivastava\OneDrive\Desktop\VS CODE\ICG_competition\tic-tac-toe_player-agent\Data\Images\crosses')
        image_files_1 = [f for f in files_1 if f.endswith( ('.png'))]
        random_image_1 = random.choice(image_files_1)
        image_path_1 = os.path.join(folder_1, random_image_1)
        return image_path_1


def png_to_array(file_path):
     
        image = Image.open(file_path).convert('L')   

        image_array = np.array(image)

        return image_array

def generate_image(Array):
    m = len(Array)
    big_matrix = np.zeros((84, 84))
    small_matrix = []

    for i in range(m):

            if Array[i] == 1:
                x = choose_image_1()
                x_np = png_to_array(x)
                small_matrix.append(x_np)
        
    
            elif Array[i] == 0:
                x = choose_image_0()
                x_np = png_to_array(x)
                small_matrix.append(x_np)



            elif Array[i] ==2:
                x = np.zeros((28,28))
                small_matrix.append(x)


    positions = [(0, 0), (0, 28), (0, 56), (28, 0), (28, 28), (28, 56), (56, 0), (56, 28), (56, 56)]

    for i, (row, col) in enumerate(positions):
            big_matrix[row:row+28, col:col+28] = small_matrix[i]

    return big_matrix


    

def get_pattern(querry_array,Flag, user):

    """
    Flag := Ineractive mode -> Iss case mein machine ka turn --> tackle ho jayega
    When flag := Generative mode -> Pull pattern from the dataset


    Flag = 0 -> Start pattern
    Flag = 1 -> Intermediate pattern
    """

    board = np.reshape(np.array(querry_array), (3,3))

    if Flag == 0:
        board = np.zeros((3,3))
    
    else:
        board = np.reshape(np.array(querry_array), (3,3))

    while not tt.terminal(board):

        player = tt.player(board)
        if user != player :
            move = tt.minimax(board)

        else:
            print("Enter the index of the next turn")
            index = int(input())
            move = (index//3, index%3)

        if(move not in tt.actions(board)):
            print("Invalid move")
            continue
            
        board = tt.result(board, move)


    tester(board, index)
    return np.reshape(np.array(board), (1,9))
    pass

def tester(querry_array, user):
    """
    Either user won/lost
    error

    Returns 1 if user has won the game, -1 if AI has won, 0 otherwise.
    """
    board = np.reshape(np.array(querry_array), (3,3))

    currentWinner = tt.winner(board)
    if currentWinner == user:
        return 1
    elif currentWinner == None: # case of tie
        return 0
    else:
        return -1


"""
>>>>>> dataset: patterns --> 2 category - (a) start
                                          (b) Intermediate

                                          100 patterns

"""