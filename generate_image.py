
#necessary libraries 
import numpy as np 
import os
import random
import pandas as pd 
from PIL import Image
import matplotlib.pyplot as plt

# The class takes the input from user and outputs a 2D matrix 
# For making it more visually appealing i have outputed the image as well but we can remove that code and just return the 2D array
# The code outside the class can be removed without any issues i have added that just for my help and debugging ease
class  generate_image():

    def __init__(self, arr ):

        self.arr = arr
# Here i have downloaded dataset images locally and then used them to call whenever needed
    def choose_image_0(self):
        folder_0 = r'C:\Users\Trijal Srivastava\OneDrive\Desktop\VS CODE\ICG_competition\zeros'
        files_0 = os.listdir(r'C:\Users\Trijal Srivastava\OneDrive\Desktop\VS CODE\ICG_competition\zeros')
        image_files_0 = [f for f in files_0 if f.endswith(('.png'))]
        random_image_0 = random.choice(image_files_0)
        image_path_0 = os.path.join(folder_0, random_image_0)
        return image_path_0
    
    def choose_image_1(self):
        folder_1 = r'C:\Users\Trijal Srivastava\OneDrive\Desktop\VS CODE\ICG_competition\ones'
        files_1 = os.listdir(r'C:\Users\Trijal Srivastava\OneDrive\Desktop\VS CODE\ICG_competition\ones')
        image_files_1 = [f for f in files_1 if f.endswith( ('.png'))]
        random_image_1 = random.choice(image_files_1)
        image_path_1 = os.path.join(folder_1, random_image_1)
        return image_path_1
    
    def png_to_array(self,file_path):
     
        image = Image.open(file_path).convert('L')   

        image_array = np.array(image)

        return image_array
    # Basically this is where the matrix is created, first i have created an empty big matrix of 84*48 and then i have filled it with small matrix 
    # Here, i have assumed a fixed pattern of filling the matrix according to array by assigning positions 
    def matrix_create(self):

        m = len(self.arr)
        self.big_matrix = np.zeros((84, 84))
        self.small_matrix = []

        for i in range(m):

            if self.arr[i] == 1:
                x = self.choose_image_1()
                x_np = self.png_to_array(x)
                self.small_matrix.append(x_np)
        
    
            elif self.arr[i] == 0:
                x = self.choose_image_0()
                x_np = self.png_to_array(x)
                self.small_matrix.append(x_np)



            elif self.arr[i] ==2:
                x = np.zeros((28,28))
                self.small_matrix.append(x)


        positions = [(0, 0), (0, 28), (0, 56), (28, 0), (28, 28), (28, 56), (56, 0), (56, 28), (56, 56)]

        for i, (row, col) in enumerate(positions):
            self.big_matrix[row:row+28, col:col+28] = self.small_matrix[i]

        return self.big_matrix

 
def get_input():

    arr = []
    num = input()
    input_list = num.split()
    for i in range(9):
        arr.append(int(input_list[i]))
    return arr

arr = get_input()

output = generate_image(arr)

final_matrix = output.matrix_create()
print(arr)

plt.imshow(final_matrix, cmap='gray')

plt.show

    

# %%



