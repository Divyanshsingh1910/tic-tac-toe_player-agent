#importing library
import numpy as np

from Player import player_main
from Helper_functions import get_pattern,generate_image,tester

"""
Functions:
     player_agent:
            Arguments:
            Action: This is the main agent which will play with the user.
                    Use all the helper function for all the required funtionalities.

"""


def player_agent():
    """
    Maintain a count --> #winning_turns
    """
    wins = 0
    """
    using helper function --> generate querry pattern
    """
    #generate a ranom querry pattern 
    #None implies pattern is to be generated
    querry = get_pattern(None,0)
    """
    pattern_img <-- querry stored
    """
    img = generate_image(querry)
    """
    user_response = player(pattern_img)
    """
    response = player_main(img)
    """
    result = tester(user_response,querry)
    """
    result = tester(response,querry)
    """"
    while result is not decidable:
        call player again

        if result decidable:
            break
    """
    #assuming that testor returns None if no one is winning
    new_querry = np.array(querry)
    new_querry = new_querry.reshape(3,3)
    while result is None :
        board = result(new_querry,response[0])
        new_querry = board.reshape(-1)
        img = generate_image(new_querry)
        response = player_main(img)
        result = tester(response,new_querry)
    
    if result == 1 :# 1 for winning
        wins += 1
