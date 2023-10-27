
#necessary libraries 
import numpy as np 
import os
import random
import pandas as pd 
from PIL import Image
import matplotlib.pyplot as plt

 
# Here i have downloaded dataset images locally and then used them to call whenever needed
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
    # Basically this is where the matrix is created, first i have created an empty big matrix of 84*48 and then i have filled it with small matrix 
    # Here, i have assumed a fixed pattern of filling the matrix according to array by assigning positions 
def generate_image(arr):

        m = len(arr)
        big_matrix = np.zeros((84, 84))
        small_matrix = []

        for i in range(m):

            if arr[i] == 1:
                x = choose_image_1()
                x_np = png_to_array(x)
                small_matrix.append(x_np)
        
    
            elif arr[i] == 0:
                x = choose_image_0()
                x_np = png_to_array(x)
                small_matrix.append(x_np)



            elif arr[i] ==2:
                x = np.zeros((28,28))
                small_matrix.append(x)


        positions = [(0, 0), (0, 28), (0, 56), (28, 0), (28, 28), (28, 56), (56, 0), (56, 28), (56, 56)]

        for i, (row, col) in enumerate(positions):
            big_matrix[row:row+28, col:col+28] = small_matrix[i]

        return big_matrix

 
 

 

 

# %%



