#importing library
import numpy as np

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

def generate_image(Array):
    pass

def get_pattern(querry_array,Flag):

    """
    Flag := Ineractive mode -> Iss case mein machine ka turn --> tackle ho jayega
    When flag := Generative mode -> Pull pattern from the dataset


    """

    pass

def tester(querry_array, user_input):
    """
    Either user won/lost
    error
    
    """
    pass


"""
>>>>>> dataset: patterns --> 2 category - (a) start
                                          (b) Intermediate

                                          100 patterns

"""