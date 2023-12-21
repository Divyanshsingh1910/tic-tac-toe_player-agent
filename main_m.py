import numpy as np
import matplotlib.pyplot as plt

from Player import player_main, turn
from Helper_functions import get_pattern,generate_image,tester


# function to return the predictions
def predict(img_arr):
    return img_arr


# user algorithm to play
def player_turn():
    return None

# arr is the starting array
def player_agent(arr):

    user = turn(arr)

    img = generate_image(arr)
    plt.imshow(img)
    
    while tester(arr, user) is None:
        arr = player_main(arr, user)[0]
        img = generate_image(arr)
        plt.imshow(img)
        plt.show()

    if tester(arr, user) == 1:
        print("You won!")
    elif tester(arr, user) == -1:
        print("You lost!")
    else:
        print("Tie!")