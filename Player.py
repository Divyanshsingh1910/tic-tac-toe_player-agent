#importing library
import numpy as np
from tictactoe import tictactoe
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

def player(Array):
    board = np.array(Array)
    board = np.reshape(board, (3,3))
    pass

