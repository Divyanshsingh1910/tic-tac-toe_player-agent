#importing library
import numpy as np
from tictactoe.tictactoe import actions,result,winner,player,minimax
import random

"""
Functions:
     player:
            Arguments: 
                * Array: The image array of the input snap-shot ( can convert this to .png file)

            Action: This is the user algorithm which when given the snap-shot image as 
            array ( or .png), it should analyze the image and based on that it can return 
            following values

            - index: An integer value depicting the next turn the player wants to play on
            - Giveup: [-1] to giveup 
            - possibility_3: I am thinking on this ( you guys also think )
"""
"""
            modification : returns the tuple and the character which must be placed
            else returns None if the player decides to giveup    
"""

def player_main(Array):
    """
    recieve the image
    """
    board = np.array(Array)
    #board = np.reshape(board, (3,3))
    """
    decode the pattern
    """
    #predict is a function that when given an image predicts if it is zero, cross or None
    #returns None , "X" or "O"
    char_array = np.array([predict(img) for img in board])
    char_array = char_array.reshape(3,3)
    """
    find the next turn 
    """
    """
    return the next turn/giveup
    """
    acts = actions(char_array)

    for act in acts:
        copy = char_array.copy()
        copy = result(copy,act)
        win = winner(copy)
        if win is not None :
            return act,win
        else:
            continue

    # #if for loop ends without returning no one is winning.
    # #choose a random action and play!
    
    # turn = player(char_array)
    # random_action = random.choice(list(acts))
    # return random_action , turn
    turn = player(board)
    #other option is to play the optimum action
    opt = minimax(char_array)
    return opt,turn
    #note that the function returns None if no action is available.



