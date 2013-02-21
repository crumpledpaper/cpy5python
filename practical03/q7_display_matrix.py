#Filename: q7_display_matrix.py
#Author: Bryan Ong
#Created: 2013/02/19
#Modified: 2013/02/19
#Description: Displaying matrix of 0s and 1s

from random import randint

def print_matrix(n):
    for j in range(n):
        for i in range(n):
            print(randint(0,1),end=" ")
        print()
