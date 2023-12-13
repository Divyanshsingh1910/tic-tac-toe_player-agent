#importing library
import numpy as np
from tictactoe.tictactoe import actions,result,winner,player,minimax, terminal
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


# dummy definition 
def predict(image):
    choice_arr = [0,1,2]

    return random.choice(choice_arr)

# define 2 boards one is the original board and the other is the predicted by user
def player_main(Array, user):
    # we should return the final array after move and the score alongside

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
    
    # char_array = np.array([predict(img) for img in board])
    arr = ["X", "O", None]
    char_array = [arr[i] for i in Array]
    char_array = np.array(char_array)  # for now consider this as the char array
    char_array = char_array.reshape(3,3)
    """
    find the next turn
    """
    next_turn = player(char_array)
    """
    return the next turn/giveup
    """
    # computer turn
    if next_turn != user:

        move = minimax(char_array)
        if move is not None:
            char_array = result(char_array, move)

        if terminal(char_array):        # computer wins
            return None, None

    # user turn
    else:
        acts = actions(board.reshape(3,3))
        if len(acts) == 0:          # tie
            return None, None
        else:
            mov = int(input("Enter the move: "))
            move = (mov//3, mov%3)

            if move not in acts:
                print("Invalid move")
                # we can make the user lose if he makes a wrong move
                return None, None

            else:
                char_array = result(char_array, move)
    
            if terminal(char_array):        # user wins
                return None, None

            return None, None
    # for act in acts:
    #     copy = char_array.copy()
    #     copy = result(copy,act)
    #     win = winner(copy)
    #     if win is not None :
    #         return act,win
    #     else:
    #         continue

    # #if for loop ends without returning no one is winning.
    # #choose a random action and play!
    
    # turn = player(char_array)
    # random_action = random.choice(list(acts))
    # return random_action , turn
    turn = player(char_array)
    # #other option is to play the optimum action
    opt = minimax(char_array)
    return opt,turn
    #note that the function returns None if no action is available.



